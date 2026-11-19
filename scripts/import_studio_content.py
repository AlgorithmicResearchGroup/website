#!/usr/bin/env python3
"""Import ARG Studio's non-creative Markdown into this site's existing theme."""

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERSONAL_ATTRIBUTION = re.compile(r"\b(?:matt(?:hew)?\s+kenney|duke(?:\s+university)?)\b", re.I)
ORIGINAL_PAPER_URL = "https://arg.studio/papers/deltaml-bench.pdf"


def remove_personal_attribution(metadata, body):
    """Keep organization-level attribution without republishing personal details."""
    if PERSONAL_ATTRIBUTION.search(metadata.get("author", "")):
        metadata["author"] = "Algorithmic Research Group"
        metadata["author_type"] = "Organization"
    if PERSONAL_ATTRIBUTION.search(metadata.get("affiliation", "")):
        metadata.pop("affiliation")
    body = re.sub(
        r"The lab is run by \[[^\]]+\]\(https://x\.com/baykenney\) and a rotating cast of contractors\.",
        "The lab works with a rotating cast of contractors.", body,
    )
    body = re.sub(r"Introduced by matt(?:hew)?\s+kenney in the", "Introduced in the", body, flags=re.I)
    body = re.sub(r"The cards credit matt(?:hew)?\s+kenney, 2023, and retain", "The cards date to 2023 and retain", body, flags=re.I)
    body = re.sub(r"I teach AI at duke(?: university)?,", "I teach AI,", body, flags=re.I)
    if any(PERSONAL_ATTRIBUTION.search(value) for value in metadata.values()) or PERSONAL_ATTRIBUTION.search(body):
        raise ValueError("Unreviewed personal attribution remains in imported content")
    return body


def read_markdown(path):
    header, body = path.read_text(encoding="utf-8").split("\n\n", 1)
    metadata = {}
    for line in header.splitlines():
        key, value = line.split(":", 1)
        metadata[key.lower()] = value.strip()
    return metadata, body


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Path to the ARG_Studio checkout")
    args = parser.parse_args()
    source = args.source.resolve() / "content"
    destination = ROOT / "content"
    mappings = {}
    groups = {}
    for folder, target, group in [
        ("research", "projects", "research"),
        ("blog", "blog", "writing"),
        ("pages/apps", "pages/apps", "apps"),
        ("pages/resources", "pages/opensource", "resources"),
    ]:
        for path in sorted((source / folder).glob("*.md")):
            relative = path.relative_to(source).as_posix()
            mappings[relative] = f"{target}/{path.name}"
            groups[relative] = group
    general_pages = {
        "pages/about.md": "pages/studio.md",
        "pages/services.md": "pages/services.md",
        "pages/contact.md": "pages/contact.md",
        "pages/work.md": "pages/work.md",
        "pages/research/about.md": "pages/about.md",
        "pages/research/index.md": "pages/research/index.md",
        "pages/research/open-source.md": "pages/opensource.md",
    }
    mappings.update(general_pages)
    groups.update({path: "pages" for path in general_pages})
    for relative in mappings:
        if not (source / relative).is_file():
            raise FileNotFoundError(source / relative)

    records = []
    for relative, target in mappings.items():
        metadata, original_body = read_markdown(source / relative)
        body = original_body
        group = groups[relative]
        target_path = destination / target

        if group == "research":
            # Keep existing public project URLs and the current research layout.
            metadata.update(category="projects", template="project")
            metadata["url"] = f"projects/{metadata['slug']}.html"
            metadata["save_as"] = metadata["url"]
            if metadata.get("feature_image"):
                metadata["image"] = metadata["feature_image"].removeprefix("images/")
                for suffix in ["alt", "width", "height"]:
                    metadata[f"image_{suffix}"] = metadata[f"feature_image_{suffix}"]
                metadata["hide_hero"] = "true"
            if target_path.exists():
                previous, _ = read_markdown(target_path)
                for key in ["featured_value", "featured_unit", "featured_caption"]:
                    if key in previous:
                        metadata[key] = previous[key]
            if metadata.get("publication_status"):
                metadata["featured_label"] = metadata["publication_status"]
        elif group == "resources":
            metadata["template"] = "resource"
            metadata["url"] = "opensource/" + Path(metadata["url"]).name
            metadata["save_as"] = metadata["url"]
        elif group == "writing":
            metadata.setdefault("author", "ARG Studio")
            metadata["template"] = "article"
            metadata.setdefault("category", "blog")
            metadata["url"] = f"blog/{metadata['slug']}.html"
            metadata["save_as"] = metadata["url"]
        elif group == "apps":
            order = ["saylight", "harness", "presskeep", "elsewhere", "dropbeam"]
            metadata["app_order"] = f"{order.index(metadata['app_key']):02}"
            if metadata["app_key"] == "harness":
                metadata.update(
                    app_image="images/apps/harness/backlog1.png",
                    app_image_alt="Backlog's shared project board, with tasks in Backlog, Active, Review, and Done and visible dependencies.",
                    app_image_width="2934",
                    app_image_height="1904",
                )
        elif relative == "pages/about.md":
            metadata.update(slug="studio", url="studio.html", save_as="studio.html", template="page")
            # Keep the practice overview without the creative archive or biography.
            body = "\n\n".join(paragraph for paragraph in body.split("\n\n") if "[creative archive]" not in paragraph)
            body = re.sub(r"^## The person behind it\n.*?(?=^## |\Z)", "", body, flags=re.M | re.S)
            body = body.replace(
                "ARG Studio is where I make independent software, explore new ideas, and work with people on things worth building.",
                "ARG Studio develops independent software, practical tools, and open research.",
            )
            body = re.sub(r"^## Small on purpose\n.*?(?=^\[Work with the studio|\Z)", "", body, flags=re.M | re.S)
        elif relative == "pages/research/about.md":
            metadata.update(slug="about", url="about.html", save_as="about.html", template="about")
            body = re.sub(r"^## Small team, open output\n\n.*?\n\n", "## Open output\n\n", body, flags=re.M | re.S)
        elif relative == "pages/services.md":
            metadata["template"] = "page"
        elif relative == "pages/contact.md":
            metadata["template"] = "contact"
        elif relative == "pages/work.md":
            metadata.update(title="Apps & software", url="work.html", save_as="work.html")
            metadata["summary"] = "Private, local-first apps, tools for working with AI agents, and independent publishing."
            body = "Software that keeps data and control with the people using it. Explore five independent apps and the questions behind them.\n"
        elif relative == "pages/research/open-source.md":
            metadata.update(slug="opensource", url="opensource.html", save_as="opensource.html", template="opensource")

        def rewrite_link(match):
            link = match.group(1)
            link_path, separator, fragment = link.partition("#")
            resolved = (source / link_path.lstrip("/")) if link_path.startswith("/") else (source / relative).parent / link_path
            linked_source = resolved.resolve().relative_to(source).as_posix()
            if linked_source not in mappings:
                raise ValueError(f"Unmapped content link in {relative}: {link}")
            return "{filename}/" + mappings[linked_source] + (separator + fragment if separator else "")

        body = re.sub(r"\{filename\}([^\s)\"<>]+)", rewrite_link, body)
        body = body.replace("{static}/papers/deltaml-bench.pdf", ORIGINAL_PAPER_URL)
        body = body.replace("](papers/deltaml-bench.pdf)", "](" + ORIGINAL_PAPER_URL + ")")
        if metadata.get("paper") == "papers/deltaml-bench.pdf":
            metadata["paper"] = ORIGINAL_PAPER_URL
        body = remove_personal_attribution(metadata, body)
        header = "\n".join(f"{key.capitalize()}: {value}" for key, value in metadata.items())
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(header + "\n\n" + body, encoding="utf-8")
        records.append({
            "source": relative,
            "destination": target,
            "group": group,
            "source_sha256": hashlib.sha256((source / relative).read_bytes()).hexdigest(),
        })

    assets = []
    for folder in ["images/apps", "images/research"]:
        for asset in sorted((source / folder).rglob("*")):
            if not asset.is_file() or asset.name.startswith("."):
                continue
            target = destination / asset.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(asset, target)
            assets.append(asset.relative_to(source).as_posix())

    manifest = {
        "source_project": "ARG_Studio",
        "excluded_content": ["pages/work/*", "images/creative/*"],
        "adaptations": [
            "Research retains this site's /projects/ routes and templates.",
            "Resources use /opensource/ detail pages in the existing theme.",
            "Internal Markdown references resolve to imported local content.",
            "The practice overview omits creative projects, personal biography, and staffing details.",
            "The Work introduction lists software only.",
            "Personal names and university attribution are omitted from site content and metadata.",
            "The original research paper is linked externally with its authorship intact.",
        ],
        "content": records,
        "assets": assets,
    }
    manifest_path = ROOT / "docs/studio-content-import.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Imported {len(records)} Markdown files and {len(assets)} assets.")
    print("Excluded all nine creative projects and their assets.")


if __name__ == "__main__":
    main()
