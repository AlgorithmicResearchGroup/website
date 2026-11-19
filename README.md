# Algorithmic Research Group

The Algorithmic Research Group website, built with Pelican and hosted on GitHub Pages at `algorithmicresearchgroup.com`.

## Development

Install the pinned dependencies, build, and serve the site:

```sh
python3 -m pip install -r requirements.txt
make html
make serve PORT=8000
```

Open `http://localhost:8000`. `make devserver PORT=8000` serves the site with automatic rebuilding. Templates and styles live in `themes/custom`; Markdown and media live in `content`.

Build with production settings and validate the generated site:

```sh
make publish
python3 scripts/check_site.py
node --check themes/custom/static/js/site.js
```

`make publish` builds into `output/` locally. The existing GitHub Actions workflow deploys on pushes to `master`.

## Content imported from ARG Studio

The site includes 42 Markdown files from `ARG_Studio`: ten research articles, five app stories, thirteen open resources, seven posts, and seven general pages. The import preserves research findings, organization attribution, dates, app descriptions, feature lists, resource documentation, and external product/download links. Required app images and research figures are stored locally. The DeltaML-Bench paper links to its original ARG Studio copy, retaining the paper's original authorship.

The nine art and creative projects, their media, and the creative-archive paragraph in the studio biography are excluded. This site's theme, brand, domain, and deployment workflow are retained. New content templates use the existing design tokens; they do not import ARG Studio's theme.

- Research keeps the existing `/projects/` article URLs and `/projects.html` archive.
- Apps appear at `/work.html`, with details under `/work/`.
- Open resources have full detail pages under `/opensource/`, linked from `/opensource.html`.
- Writing appears at `/blog/`.
- The research-group background is at `/about.html`; the studio biography is at `/studio.html`; collaboration information is at `/services.html`.

The file-level inventory, original hashes, and imported assets are recorded in `docs/studio-content-import.json`. To refresh the selected content from the sibling checkout:

```sh
python3 scripts/import_studio_content.py ../ARG_Studio
make publish
python3 scripts/check_site.py
```

The importer updates the selected destination Markdown files and assets, maps internal Markdown links to their local destinations, and preserves this theme's featured-study metric. Personal names and university attribution are omitted from site content and metadata, including on later refreshes. It does not modify ARG Studio or copy its configuration, DNS files, analytics, design, or creative archive. Empty planning files in `content/projects` remain in the checkout and are excluded from publication.
