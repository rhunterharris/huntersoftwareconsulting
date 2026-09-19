# Hunter Software Consulting website

Source for [huntersoftwareconsulting.com](https://huntersoftwareconsulting.com/). A static Hugo site: project-owned layouts and CSS provide the presentation; the vendored themes remain unchanged. Production uses GitHub Pages and Hugo Extended 0.154.4.

## Local development

```sh
git submodule update --init --recursive
hugo --gc --minify
python3 scripts/check_site.py public
python3 scripts/preview.py --directory public --port 1318
```

Open http://127.0.0.1:1318/. Rebuild and refresh after changing source. The preview binds only to loopback, disables browser caching, and returns the site's custom page with HTTP 404 for unknown paths.

For live development, `hugo server --disableFastRender --port 1318` also works. Restart it after frontmatter changes if content appears misaligned.

## Where things live

- Homepage copy: `content/_index.md`; composition: `layouts/home.html`.
- Services and experience: `content/pages/services.md`, `content/pages/about-me.md`.
- Homepage outcome examples: `data/experience.toml`.
- Engagement sequence: `data/engagement.toml` (feeds both the homepage and Services).
- Writing and recommendations: `content/posts/`, `content/testimonials/`.
- Navigation, contact destinations and organization metadata: `hugo.toml`.
- Layouts, structured data and metadata: `layouts/`; typography, palette and responsive behavior: `assets/css/site.css`.
- Images: `static/images/hunter-logo.png` (header) and `assets/images/hunter-harris.png` (headshot; Hugo generates responsive WebP copies).
- Typography: one self-hosted Archivo family. Shared role tokens are at the end of `assets/css/site.css`. The font license is `static/fonts/archivo-OFL.txt`.

Keep published URLs and original publication dates stable. Add `lastmod` when a page changes meaningfully. Give each page a specific description and one H1; body headings start at H2.

## Homepage content

Content changes appear on the next build; no template edits are needed.

- **Latest writing:** the three newest published posts by frontmatter `date`. Drafts and future-dated posts are excluded.
- **Newsletter/podcast:** `newsletterURL` in `hugo.toml` feeds the footer and Writing archive.
- **Featured recommendation:** add `homepageFeatured = true` to one testimonial's frontmatter. The homepage reads `excerpt`, `quoteAuthor`, `quoteRole` and `feedbackType`. If several are featured, the newest wins; with none, the newest recommendation is used.
- **Outcome examples:** edit `data/experience.toml`; each entry links to its fuller account on Experience.
- **Engagement:** edit the `action` and `outcome` fields in `data/engagement.toml`.

## Build checks and deployment

`scripts/check_site.py` checks generated links, anchors, metadata, heading structure, image alternative text, JSON-LD relationships, sitemap exclusions and contact destinations, using only Python's standard library. Compare against a previous build with `--baseline /path/to/previous/public`; write JSON with `--json /path/to/checks.json`.

`.github/workflows/hugo.yml` builds and validates on pushes to `main` and on manual dispatch, then deploys to GitHub Pages.
