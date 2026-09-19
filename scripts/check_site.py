#!/usr/bin/env python3
"""Check built Hugo output without a browser, network access, or third-party packages.

Usage: python3 scripts/check_site.py public --baseline /path/to/previous/public
This checks local structure and references; it cannot prove indexing or rich-result eligibility.
"""
import argparse
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.title = ''
        self.headings = []
        self.ids = []
        self.meta = {}
        self.canonicals = []
        self.references = []
        self.anchors = []
        self.images = []
        self.times = []
        self.schemas = []
        self.main_count = 0
        self.lang = None
        self.active = None
        self.anchor = None
        self.in_title = False
        self.schema = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.append(a['id'])
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'main':
            self.main_count += 1
        if tag == 'title':
            self.in_title = True
        if re.fullmatch(r'h[1-6]', tag):
            self.active = [int(tag[1]), '']
        if tag == 'meta':
            key = a.get('name') or a.get('property') or a.get('http-equiv')
            if key:
                self.meta.setdefault(key.lower(), []).append(a.get('content', ''))
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonicals.append(a.get('href', ''))
        if tag in ('a', 'link') and a.get('href'):
            self.references.append(a['href'])
        if tag == 'a':
            self.anchor = {'href': a.get('href'), 'label': a.get('aria-label', ''), 'text': ''}
        if tag in ('script', 'img') and a.get('src'):
            self.references.append(a['src'])
        if tag == 'img':
            self.images.append(a)
        if tag == 'time':
            self.times.append(a.get('datetime', ''))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.schema = ''

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.active is not None:
            self.active[1] += data
        if self.anchor is not None:
            self.anchor['text'] += data
        if self.schema is not None:
            self.schema += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if re.fullmatch(r'h[1-6]', tag) and self.active is not None:
            self.headings.append((self.active[0], ' '.join(self.active[1].split())))
            self.active = None
        if tag == 'a' and self.anchor is not None:
            self.anchors.append(self.anchor)
            self.anchor = None
        if tag == 'script' and self.schema is not None:
            self.schemas.append(self.schema)
            self.schema = None


def route(path):
    value = '/' + path.as_posix()
    return value[:-10] if value.endswith('index.html') else value


def resolve_file(root, url):
    path = root / unquote(urlsplit(url).path).lstrip('/')
    return path / 'index.html' if path.is_dir() else path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('public', type=Path)
    parser.add_argument('--base-url', default='https://huntersoftwareconsulting.com/')
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    root = args.public.resolve()
    errors = []
    pages = {p.relative_to(root): Page(p) for p in root.rglob('*.html')}
    if not pages:
        raise SystemExit('No built HTML found')
    origins = {urlsplit(args.base_url).netloc, 'huntersoftwareconsulting.com', 'www.huntersoftwareconsulting.com'}
    titles = {}
    aliases = 0
    schema_types = Counter()
    references_checked = 0

    def fail(path, message):
        errors.append(f'{path}: {message}')

    for relative, page in pages.items():
        page_url = urljoin(args.base_url, route(relative))
        if 'refresh' in page.meta:
            aliases += 1
            refresh = page.meta['refresh'][0]
            match = re.search(r'url=(.+)$', refresh, re.I)
            if not match or not resolve_file(root, match[1]).is_file():
                fail(relative, 'redirect target missing')
            if len(page.canonicals) != 1 or (match and page.canonicals[0] != match[1]):
                fail(relative, 'redirect and canonical disagree')
            continue
        if not page.lang or page.main_count != 1:
            fail(relative, 'requires a document language and one main landmark')
        h1 = [text for level, text in page.headings if level == 1]
        if len(h1) != 1 or not h1[0]:
            fail(relative, f'requires one non-empty H1, got {h1}')
        previous = 0
        for level, text in page.headings:
            if not text or level > previous + 1:
                fail(relative, f'heading hierarchy {previous} -> {level}: {text}')
            if 'Link to heading' in text:
                fail(relative, 'heading contains permalink label')
            previous = level
        if not page.title.strip() or page.title.strip().startswith(('·', '|')):
            fail(relative, 'empty page title')
        if page.title in titles:
            fail(relative, f'title duplicates {titles[page.title]}')
        titles[page.title] = str(relative)
        if len(page.canonicals) != 1 or page.canonicals[0] != page_url:
            fail(relative, f'canonical does not match {page_url}: {page.canonicals}')
        for name in ('description', 'og:title', 'og:description', 'og:url', 'og:image', 'og:image:alt', 'twitter:title', 'twitter:description', 'twitter:image', 'twitter:card'):
            values = page.meta.get(name, [])
            if len(values) != 1 or not values[0].strip():
                fail(relative, f'{name} missing or duplicated')
        description = page.meta.get('description', [''])[0]
        if len(description) > 200 or '\n' in description or 'Link to heading' in description or re.search(r'&(?:[a-z]+|#\d+);', description):
            fail(relative, f'unusable description: {description}')
        if page.meta.get('og:url') != page.canonicals:
            fail(relative, 'Open Graph URL and canonical disagree')
        if len(page.ids) != len(set(page.ids)):
            fail(relative, 'duplicate element IDs')
        for anchor in page.anchors:
            if not (anchor['label'] or anchor['text']).strip():
                fail(relative, f'unnamed link {anchor["href"]}')
        for img in page.images:
            decorative = img.get('aria-hidden') == 'true' or img.get('role') == 'presentation'
            if 'alt' not in img or (not (img.get('alt') or '').strip() and not decorative):
                fail(relative, f'image missing alternative text: {img.get("src")}')
        for ref in page.references + page.meta.get('og:image', []):
            resolved = urljoin(page_url, ref)
            parts = urlsplit(resolved)
            if parts.scheme in ('mailto', 'tel', 'data', 'javascript') or parts.netloc not in origins:
                continue
            target = resolve_file(root, resolved)
            references_checked += 1
            if not target.is_file():
                fail(relative, f'broken internal reference {ref}')
                continue
            if parts.fragment and target.suffix == '.html':
                target_page = pages.get(target.relative_to(root))
                if target_page and unquote(parts.fragment) not in target_page.ids:
                    fail(relative, f'missing fragment {ref}')
        if len(page.schemas) != 1:
            fail(relative, 'expected a single JSON-LD graph')
            continue
        try:
            schema = json.loads(page.schemas[0])
            graph = schema['@graph']
            assert schema['@context'] == 'https://schema.org'
            assert isinstance(graph, list)
            by_type = {node['@type']: node for node in graph}
            by_id = {node['@id']: node for node in graph}
            assert len(by_id) == len(graph)
            assert {'Organization', 'Person', 'WebPage'} <= by_type.keys()
            assert not ({'Review', 'AggregateRating', 'FAQPage'} & by_type.keys())
            assert by_type['WebPage']['url'] == page_url
            assert by_type['Organization']['founder']['@id'] == by_type['Person']['@id']
            if 'BlogPosting' in by_type:
                article = by_type['BlogPosting']
                assert article['headline'] == h1[0]
                assert article['author']['@id'] == by_type['Person']['@id']
                assert article['publisher']['@id'] == by_type['Organization']['@id']
                assert article['datePublished'][:10] in page.times
                datetime.fromisoformat(article['datePublished'].replace('Z', '+00:00'))
            schema_types.update(by_type.keys())
        except (ValueError, KeyError, AssertionError, TypeError) as error:
            fail(relative, f'invalid structured data contract: {error}')

    sitemap_path = root / 'sitemap.xml'
    sitemap_urls = []
    if sitemap_path.exists():
        doc = ET.parse(sitemap_path)
        sitemap_urls = [node.text for node in doc.iter() if node.tag.endswith('}loc')]
        for url in sitemap_urls:
            file = resolve_file(root, url)
            page = pages.get(file.relative_to(root))
            if not page or page.canonicals != [url] or 'refresh' in page.meta or any('noindex' in x for x in page.meta.get('robots', [])):
                fail('sitemap.xml', f'not an indexable canonical page: {url}')
        expected = {p.canonicals[0] for p in pages.values() if len(p.canonicals) == 1 and 'refresh' not in p.meta and not any('noindex' in x for x in p.meta.get('robots', [])) and '/page/' not in p.canonicals[0]}
        if set(sitemap_urls) != expected:
            fail('sitemap.xml', f'missing or extra canonical entries: {set(sitemap_urls) ^ expected}')
    else:
        fail('sitemap.xml', 'missing')
    robots = (root / 'robots.txt').read_text() if (root / 'robots.txt').exists() else ''
    if f'Sitemap: {urljoin(args.base_url, "sitemap.xml")}' not in robots or 'Allow: /' not in robots:
        fail('robots.txt', 'missing permissive policy or canonical sitemap')
    baseline_count = None
    if args.baseline:
        before = {p.relative_to(args.baseline) for p in args.baseline.rglob('*.html')}
        baseline_count = len(before)
        for missing in sorted(before - pages.keys()):
            fail(missing, 'previous HTML route removed')
    for target in ('pages/services/index.html', 'pages/about-me/index.html'):
        page = pages.get(Path(target))
        modified = None
        if page and page.schemas:
            try:
                modified = next(node.get('dateModified', '')[:10] for node in json.loads(page.schemas[0])['@graph'] if node['@type'] == 'WebPage')
            except (ValueError, KeyError, StopIteration):
                pass
        if not page or not modified or modified not in page.times:
            fail(target, 'missing visible revision date')
    services = pages[Path('pages/services/index.html')]
    if not any(ref.startswith('mailto:hunter@huntersoftwareconsulting.com') for ref in services.references):
        fail('services', 'email route missing')
    if not any(ref.startswith('https://calendly.com/rhunterharris/20-minute-consultation') for ref in services.references):
        fail('services', 'booking route missing')
    if not any('beehiiv.com/products/the-product-tech-scorecard' in ref for ref in services.references):
        fail('services', 'existing scorecard route missing')
    result = {'html_files': len(pages), 'content_pages': len(pages)-aliases, 'redirects': aliases,
              'sitemap_urls': len(sitemap_urls), 'internal_references_checked': references_checked,
              'schema_types': dict(schema_types), 'baseline_routes_checked': baseline_count,
              'errors': errors, 'passed': not errors}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
