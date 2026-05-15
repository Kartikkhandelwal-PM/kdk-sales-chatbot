"""
KDK Software Knowledge Base Extractor
Uses the portal search API (no credentials required) to discover all articles
for Express-GST, Express-TDS, and Express-ITR, then fetches full content
via the articleByPermalink endpoint.

Output:
  Express-GST/    — Markdown files + _articles.json + _INDEX.md
  Express-TDS/    — same
  Express-ITR/    — same
  kb_all_articles.json  — combined training data
"""

import json
import re
import sys
import time
from pathlib import Path

import requests

# Force UTF-8 output on Windows console
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_URL = "https://support.kdksoftware.com"
PORTAL_ID = "edbsne55ba7deb431da433c4ac3f11d62c1ef5bef37105f67d6f01f43b9cda906bdf4"
LOCALE = "en"

# Each entry: (folder_name, search_keyword, root_category_id)
CATEGORIES = [
    ("Express-GST", "expressgst", "202722000155513689"),
    ("Express-TDS", "expresstds", "202722000233618629"),
    ("Express-ITR", "expressitr", "202722000387498539"),
]

OUTPUT_DIR = Path(__file__).parent

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Referer": BASE_URL,
})


# ─────────────────────────── API ──────────────────────────────────────────

def api_get(path: str, params: dict = None) -> dict | None:
    try:
        r = SESSION.get(f"{BASE_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"    [API ERR] {path} — {e}")
        return None


def search_articles(keyword: str) -> list[dict]:
    """Search for all articles matching keyword, handling pagination."""
    all_results: list[dict] = []
    from_idx = 0
    limit = 50

    while True:
        data = api_get("/portal/api/kbArticles/search", {
            "portalId": PORTAL_ID,
            "searchStr": keyword,
            "locale": LOCALE,
            "limit": limit,
            "from": from_idx,
        })
        if not data:
            break

        batch = data.get("data", [])
        if not batch:
            break

        all_results.extend(batch)
        print(f"    Search '{keyword}' page {from_idx//limit}: {len(batch)} results")

        if len(batch) < limit:
            break
        from_idx += limit
        time.sleep(0.3)

    return all_results


def fetch_article_detail(permalink: str) -> dict | None:
    """Fetch full article content by permalink."""
    return api_get("/portal/api/kbArticles/articleByPermalink", {
        "portalId": PORTAL_ID,
        "permalink": permalink,
        "locale": LOCALE,
    })


# ─────────────────────────── Content helpers ──────────────────────────────

def strip_html(html_text: str) -> str:
    if not html_text:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", html_text, flags=re.IGNORECASE)
    text = re.sub(r"</p>|</div>|</li>|</h[1-6]>|</tr>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<th[^>]*>|<td[^>]*>", " | ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    for ent, ch in [("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"),
                    ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'")]:
        text = text.replace(ent, ch)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def save_article(article: dict, folder: Path, index: int, category_name: str) -> dict:
    title = article.get("title", "") or f"article_{index}"
    slug = article.get("permalink", "")
    content_html = (
        article.get("answer", "")
        or article.get("content", "")
        or article.get("body", "")
        or ""
    )
    content_text = strip_html(content_html)
    summary = strip_html(article.get("summary", ""))

    # Section / sub-category info
    cat_info = article.get("category", {}) or {}
    section_name = cat_info.get("name", "") if isinstance(cat_info, dict) else ""
    if not section_name:
        section_name = article.get("sectionName", "")

    tags = article.get("tags", []) or []

    record = {
        "index": index,
        "category": category_name,
        "section": section_name,
        "title": title,
        "slug": slug,
        "url": f"{BASE_URL}/portal/en/kb/articles/{slug}",
        "id": article.get("id", ""),
        "views": article.get("viewCount", 0),
        "created_time": article.get("createdTime", ""),
        "modified_time": article.get("modifiedTime", ""),
        "tags": tags,
        "summary": summary,
        "content": content_text,
    }

    safe_title = re.sub(r'[<>:"/\\|?*]', "_", title)[:80].strip()
    md_path = folder / f"{index:04d}_{safe_title}.md"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        if section_name:
            f.write(f"**Section:** {section_name}\n\n")
        f.write(f"**Category:** {category_name}\n\n")
        f.write(f"**Source:** {record['url']}\n\n")
        if tags:
            f.write(f"**Tags:** {', '.join(tags)}\n\n")
        f.write("---\n\n")
        if content_text:
            f.write(content_text)
        elif summary:
            f.write(summary)

    return record


# ─────────────────────────── Main ─────────────────────────────────────────

def process_category(name: str, keyword: str, root_cat_id: str) -> list[dict]:
    folder = OUTPUT_DIR / name
    # Clear previous run so serial numbers are clean and consistent
    if folder.exists():
        for f in folder.glob("*.md"):
            f.unlink()
        for f in folder.glob("*.json"):
            f.unlink()
    folder.mkdir(exist_ok=True)

    print(f"\n{'='*65}")
    print(f"  {name}  (keyword: {keyword})")
    print(f"{'='*65}")

    # Step 1: discover all article slugs via search
    print("  Searching for articles...")
    search_results = search_articles(keyword)

    # Deduplicate by permalink
    seen_slugs: set[str] = set()
    unique_results: list[dict] = []
    for art in search_results:
        slug = art.get("permalink", "")
        if slug and slug not in seen_slugs:
            seen_slugs.add(slug)
            unique_results.append(art)

    total = len(unique_results)
    print(f"  Found {total} unique articles")

    if total == 0:
        print("  [WARN] No articles found")
        return []

    # Step 2: fetch full content for each article
    saved_records: list[dict] = []
    for i, meta in enumerate(unique_results, 1):
        slug = meta.get("permalink", "")
        title = meta.get("title", slug)
        print(f"  [{i:3d}/{total}] {title[:60]}", end="", flush=True)

        # Check if full content is already in the search result
        has_content = bool(
            meta.get("answer") or meta.get("content") or meta.get("body")
        )

        article_data = meta
        if not has_content and slug:
            detail = fetch_article_detail(slug)
            if detail:
                article_data = {**meta, **detail}
            time.sleep(0.3)

        record = save_article(article_data, folder, i, name)
        saved_records.append(record)
        print("  OK")

    # Save category JSON (full data for AI training)
    json_path = folder / "_articles.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(saved_records, f, ensure_ascii=False, indent=2)

    # Save index
    index_path = folder / "_INDEX.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(f"# {name} — Knowledge Base Index\n\n")
        f.write(f"**Total articles:** {len(saved_records)}\n\n")
        for rec in saved_records:
            sec = f" [{rec['section']}]" if rec["section"] else ""
            f.write(f"- {rec['index']:04d}.{sec} [{rec['title']}]({rec['url']})\n")

    print(f"\n  Saved {len(saved_records)} articles  =>  {folder.name}/")
    return saved_records


def main():
    print("\nKDK Software Knowledge Base Extractor")
    print("=" * 65)

    all_data: list[dict] = []

    for name, keyword, cat_id in CATEGORIES:
        records = process_category(name, keyword, cat_id)
        all_data.extend(records)

    # Master training JSON — clean fields only, no HTML
    master = OUTPUT_DIR / "kb_all_articles.json"
    training = [
        {
            "category": r["category"],
            "section": r["section"],
            "title": r["title"],
            "url": r["url"],
            "tags": r["tags"],
            "summary": r["summary"],
            "content": r["content"],
        }
        for r in all_data
    ]
    with open(master, "w", encoding="utf-8") as f:
        json.dump(training, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*65}")
    print(f"COMPLETE — {len(all_data)} total articles extracted")
    print(f"  Express-GST/   Express-TDS/   Express-ITR/")
    print(f"  kb_all_articles.json  ({len(all_data)} records for AI training)")
    print(f"{'='*65}\n")


if __name__ == "__main__":
    main()
