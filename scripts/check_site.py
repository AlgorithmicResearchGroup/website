#!/usr/bin/env python3
"""Check generated HTML, local links, assets, anchors, and imported content."""

import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.links = []
        self.ids = set()
        self.headings = 0
        self.main = 0
        self.structured_data = []
        self.in_json = False
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        self.headings += tag == "h1"
        self.main += tag == "main"
        for attribute in ["href", "src"]:
            if attrs.get(attribute):
                self.links.append(attrs[attribute])
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_json = True
            self.structured_data.append("")

    def handle_data(self, data):
        if self.in_json:
            self.structured_data[-1] += data

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_json = False


def main():
    pages = {path.resolve(): Page(path) for path in OUTPUT.rglob("*.html")}
    issues = []
    for path, page in pages.items():
        relative = path.relative_to(OUTPUT)
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = ((OUTPUT / unquote(url.path.lstrip("/"))) if url.path.startswith("/") else path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target /= "index.html"
            if not target.exists():
                issues.append(f"{relative}: missing file {link}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                issues.append(f"{relative}: missing anchor {link}")
        for data in page.structured_data:
            try:
                json.loads(data)
            except json.JSONDecodeError as error:
                issues.append(f"{relative}: invalid structured data: {error}")
        if page.main != 1 or page.headings != 1 or "main-content" not in page.ids:
            issues.append(f"{relative}: expected one main landmark, one h1, and a working skip link")
        if "{filename}" in path.read_text() or "{static}" in path.read_text():
            issues.append(f"{relative}: unresolved Pelican content reference")

    manifest = json.loads((ROOT / "docs/studio-content-import.json").read_text())
    groups = Counter(item["group"] for item in manifest["content"])
    for item in manifest["content"]:
        source = ROOT / "content" / item["destination"]
        if not source.is_file():
            issues.append(f"Missing imported Markdown: {source}")
            continue
        metadata = dict(line.split(":", 1) for line in source.read_text().split("\n\n", 1)[0].splitlines())
        route = metadata.get("Save_as", "").strip()
        if not route:
            route = metadata.get("Slug", "").strip() + ".html"
        if not (OUTPUT / route).is_file():
            issues.append(f"Imported Markdown has no rendered page: {item['destination']} ({route})")
    for asset in manifest["assets"]:
        if not (OUTPUT / asset).is_file():
            issues.append(f"Missing imported asset: {asset}")
    if (ROOT / "content/images/creative").exists() or (ROOT / "content/pages/work").exists():
        issues.append("Unexpected creative content directory")
    print(f"Checked {len(pages)} HTML pages, their local links/assets/anchors, and JSON-LD.")
    print("Imported content:", dict(groups))
    for issue in issues:
        print(issue)
    print(f"Issues: {len(issues)}")
    raise SystemExit(bool(issues))


if __name__ == "__main__":
    main()
