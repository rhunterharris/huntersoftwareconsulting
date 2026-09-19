#!/usr/bin/env python3
"""Serve a built site on loopback, including the custom GitHub Pages 404 page."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        not_found = Path(self.directory) / '404.html'
        if code != 404 or not not_found.is_file():
            return super().send_error(code, message, explain)
        body = not_found.read_bytes()
        self.send_response(404)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(body)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path('public'))
    parser.add_argument('--port', type=int, default=1318)
    args = parser.parse_args()
    if not (args.directory / 'index.html').is_file():
        parser.error('Build the site first; index.html is missing.')
    handler = partial(PreviewHandler, directory=str(args.directory.resolve()))
    server = ThreadingHTTPServer(('127.0.0.1', args.port), handler)
    print(f'Local preview: http://127.0.0.1:{args.port}/', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
