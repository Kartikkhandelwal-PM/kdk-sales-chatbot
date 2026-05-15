"""
Builds three combined AI-training knowledge base files:
  Express-GST-KnowledgeBase.md
  Express-TDS-KnowledgeBase.md
  Express-ITR-KnowledgeBase.md

Each file merges all articles for that product into one clean document
that an AI sales agent can learn from.
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUTPUT_DIR = Path(__file__).parent

PRODUCTS = [
    {
        "folder": "Express-GST",
        "output": "Express-GST-KnowledgeBase.md",
        "full_name": "Express GST",
        "tagline": "Cloud-based GST compliance software for filing GST returns, reconciliation, e-invoicing, and e-way bill management.",
        "key_features": [
            "GSTR-1, GSTR-3B, GSTR-6, GSTR-9, GSTR-9C filing",
            "GSTR-2A / 2B reconciliation with books data",
            "E-Invoice generation and management",
            "E-Way Bill creation, cancellation, and update",
            "ITC Tracker and tax liability reports",
            "PAN-level multi-branch reconciliation",
            "Invoice Management System (IMS) dashboard",
            "Data import from Tally, Excel, and other sources",
            "Annual return preparation (GSTR-9 and GSTR-9C)",
        ],
    },
    {
        "folder": "Express-TDS",
        "output": "Express-TDS-KnowledgeBase.md",
        "full_name": "Express TDS",
        "tagline": "Cloud-based TDS/TCS return filing software for preparing and submitting 24Q, 26Q, 27Q, and 27EQ returns.",
        "key_features": [
            "Preparation and filing of 24Q, 26Q, 27Q, 27EQ TDS returns",
            "Challan creation, mapping, verification, and deletion",
            "Deductee and deductor master management",
            "FVU validation and error resolution",
            "TDS certificate (Form 16/16A) generation and email",
            "TRACES integration: consolidated file, justification report",
            "Online corrections and interest/late fee allocation",
            "Lower deduction certificate verification",
            "Bulk PAN verification",
            "Salary details (Annexure-II) feeding",
        ],
    },
    {
        "folder": "Express-ITR",
        "output": "Express-ITR-KnowledgeBase.md",
        "full_name": "Express ITR",
        "tagline": "Cloud-based income tax return preparation and filing software for individuals, firms, companies, and trusts.",
        "key_features": [
            "Filing of ITR-1 to ITR-7 (regular, belated, revised, updated ITR-U)",
            "Salary, house property, capital gains, and business income feeding",
            "Tax audit forms 3CA-3CB-3CD preparation",
            "Form 16 and AIS/TIS import",
            "Balance sheet, P&L, and financial statement preparation",
            "Depreciation chart (IT Act and Companies Act)",
            "Advance tax calculation and payment tracking",
            "Deductions under 80C, 80D, 80CCD(2), 80GG, 80P, 80PA, 80IAC, etc.",
            "Capital gain import via broker templates",
            "JSON file generation and e-filing on the income tax portal",
        ],
    },
]


def build_file(product: dict):
    folder = OUTPUT_DIR / product["folder"]
    json_path = folder / "_articles.json"

    if not json_path.exists():
        print(f"  [SKIP] {json_path} not found")
        return

    with open(json_path, encoding="utf-8") as f:
        articles: list[dict] = json.load(f)

    output_path = OUTPUT_DIR / product["output"]

    lines: list[str] = []

    # ── Header ────────────────────────────────────────────────────────────
    lines += [
        f"# {product['full_name']} — Complete Knowledge Base",
        "",
        f"> **Product:** {product['full_name']}",
        f"> **Description:** {product['tagline']}",
        f"> **Total Articles:** {len(articles)}",
        "",
        "---",
        "",
        "## Key Features & Capabilities",
        "",
    ]
    for feat in product["key_features"]:
        lines.append(f"- {feat}")
    lines += ["", "---", ""]

    # ── Articles ──────────────────────────────────────────────────────────
    lines.append("## Knowledge Base Articles")
    lines.append("")

    # Group by section for better readability
    sections: dict[str, list[dict]] = {}
    for art in articles:
        sec = art.get("section", "") or "General"
        sections.setdefault(sec, []).append(art)

    for sec_name, sec_articles in sections.items():
        if len(sections) > 1:
            lines += [f"### Section: {sec_name}", ""]

        for art in sec_articles:
            title = art.get("title", "").strip()
            content = (art.get("content", "") or "").strip()
            summary = (art.get("summary", "") or "").strip()
            url = art.get("url", "")
            tags = art.get("tags", [])
            idx = art.get("index", "")

            lines += [
                f"#### {idx}. {title}",
                "",
            ]

            if tags:
                lines.append(f"**Tags:** {', '.join(tags)}")
                lines.append("")

            if url:
                lines.append(f"**Source:** {url}")
                lines.append("")

            if content:
                lines.append(content)
            elif summary:
                lines.append(summary)
            else:
                lines.append("*(No content available)*")

            lines += ["", "---", ""]

    # ── Footer ────────────────────────────────────────────────────────────
    lines += [
        "",
        f"*End of {product['full_name']} Knowledge Base — {len(articles)} articles*",
    ]

    text = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    size_kb = output_path.stat().st_size / 1024
    print(f"  [{product['folder']}]  {len(articles)} articles  ->  {output_path.name}  ({size_kb:.0f} KB)")


def main():
    print("\nBuilding combined AI training knowledge base files...")
    print("=" * 60)
    for product in PRODUCTS:
        build_file(product)
    print("=" * 60)
    print("Done. Three files created in:", OUTPUT_DIR)
    print()


if __name__ == "__main__":
    main()
