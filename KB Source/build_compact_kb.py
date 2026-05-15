"""
build_compact_kb.py
Compresses large KB files into compact sales-friendly feature summaries.
No OpenAI needed — pure text processing.

How it works:
- Keeps article titles and first description paragraph
- Keeps feature bullet lists
- Skips all step-by-step instructions (Step 1, Click, Navigate, etc.)

Usage:
  python "KB Source/build_compact_kb.py"
"""

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

KB_DIR      = Path(__file__).parent.parent / "Sales Chatbot" / "Knowledge Base Files"
COMPACT_DIR = KB_DIR / "compact"
COMPACT_DIR.mkdir(exist_ok=True)

PRODUCTS = [
    {
        "input":  "Express-GST-KnowledgeBase.md",
        "output": "Express-GST-Compact.md",
        "name":   "Express GST",
    },
    {
        "input":  "Express-TDS-KnowledgeBase.md",
        "output": "Express-TDS-Compact.md",
        "name":   "Express TDS",
    },
    {
        "input":  "Express-ITR-KnowledgeBase.md",
        "output": "Express-ITR-Compact.md",
        "name":   "Express ITR",
    },
]

# Lines that indicate procedural/navigation content — skip these
SKIP_PATTERNS = re.compile(
    r'^(step\s*\d+|steps\s+(to|for)|procedure|how\s+to\s+(perform|use|access|create|add|delete|edit)|'
    r'navigate\s+to|click\s+(on\s+)?the|go\s+to|select\s+(the\s+)?|open\s+the\s+|'
    r'enter\s+(the\s+)?|choose\s+(the\s+)?|locate\s+the|upload\s+|download\s+|'
    r'browse\s+(and\s+)?select|press\s+(the\s+)?|type\s+in|fill\s+(in\s+|out\s+)?the|'
    r'check\s+(the\s+)?box|uncheck|enable\s+the|disable\s+the|'
    r'\*\*tags:\*\*|\*\*source:\*\*)',
    re.IGNORECASE
)

# Lines to always skip regardless
ALWAYS_SKIP = re.compile(
    r'^(\*\*tags:\*\*|\*\*source:\*\*|📌|>\s+\*\*product|>\s+\*\*description|>\s+\*\*total)',
    re.IGNORECASE
)


def is_heading(line: str) -> bool:
    return line.startswith('#')


def is_feature_bullet(line: str) -> bool:
    return line.startswith('- ') and len(line) > 10


def is_procedural(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    return bool(SKIP_PATTERNS.match(stripped)) or bool(ALWAYS_SKIP.match(stripped))


def compress_article_body(lines: list[str]) -> list[str]:
    """
    From an article's body lines, extract a brief summary.
    - Prefers description text (before steps) up to 3 lines
    - If no description found, includes first 2 step headings as a process hint
    - Always includes feature bullets if present
    """
    kept = []
    desc_lines = 0
    step_hints = []
    bullets = []
    found_procedural = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if desc_lines > 0 and not found_procedural:
                break
            continue

        if ALWAYS_SKIP.match(stripped):
            continue

        if is_feature_bullet(line):
            bullets.append(line)
            continue

        if is_procedural(line):
            found_procedural = True
            # Capture step headings (Step 1:, Step 2: etc.) as process hints
            step_match = re.match(r'^step\s*\d+\s*[:\-]?\s*(.+)', stripped, re.IGNORECASE)
            if step_match and len(step_hints) < 3:
                hint = step_match.group(1).strip()
                if len(hint) > 5:
                    step_hints.append(f"  - {hint}")
            continue

        if not found_procedural and not stripped.startswith('**') and len(stripped) > 20:
            kept.append(line)
            desc_lines += 1
            if desc_lines >= 3:
                break

    result = kept[:3]
    result.extend(bullets[:4])

    # If no description was found, use step hints as a process summary
    if not result and step_hints:
        result.append("Steps:")
        result.extend(step_hints)

    return result


def compress_file(input_path: Path, output_path: Path, product_name: str) -> None:
    print(f"\n[{product_name}]")
    text = input_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    print(f"  Source: {len(lines):,} lines, {len(text):,} chars")

    output_lines = []
    i = 0
    article_count = 0
    in_top_section = True  # Keep the "Key Features & Capabilities" section at the top

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Keep the top intro section (before "## Knowledge Base Articles")
        if in_top_section:
            if stripped.startswith('## Knowledge Base Articles'):
                in_top_section = False
                output_lines.append('')
                output_lines.append('---')
                output_lines.append('')
            else:
                # Skip the metadata block lines (> **Product:** etc.)
                if not ALWAYS_SKIP.match(stripped):
                    output_lines.append(line)
            i += 1
            continue

        # Article heading (#### N. Title)
        if stripped.startswith('####'):
            article_count += 1
            # Clean up the number prefix: "#### 1. Title" → "#### Title"
            title = re.sub(r'^#{1,6}\s+\d+\.\s*', '', stripped)
            output_lines.append(f'#### {title}')

            # Collect body lines until next article (next #### or ---)
            i += 1
            body = []
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                if next_stripped.startswith('####') or next_stripped == '---':
                    break
                body.append(next_line)
                i += 1

            # Extract description from body
            description = compress_article_body(body)
            if description:
                output_lines.extend(description)
            output_lines.append('')
            continue

        # Section headings (##, ###) — keep
        if stripped.startswith('##') or stripped.startswith('###'):
            output_lines.append(line)
            i += 1
            continue

        # Article separator --- skip (we add our own spacing)
        if stripped == '---':
            i += 1
            continue

        i += 1

    final_text = '\n'.join(output_lines)

    # Clean up excessive blank lines
    final_text = re.sub(r'\n{3,}', '\n\n', final_text)

    header = (
        f"# {product_name} — Compact Feature Reference\n"
        f"_Compressed from {len(lines):,} lines → {len(final_text.splitlines())} lines "
        f"({article_count} articles)_\n\n"
    )
    output_path.write_text(header + final_text, encoding="utf-8")

    out_size = len(header + final_text)
    reduction = round((1 - out_size / len(text)) * 100)
    print(f"  Output: {len(final_text.splitlines())} lines, {out_size:,} chars  ({reduction}% smaller)")
    print(f"  Saved → {output_path.name}")


if __name__ == "__main__":
    print("=" * 55)
    print("KDK KB Compressor — no API needed, pure text")
    print("=" * 55)

    for product in PRODUCTS:
        input_path  = KB_DIR / product["input"]
        output_path = COMPACT_DIR / product["output"]

        if not input_path.exists():
            print(f"\n[{product['name']}] SKIP — file not found: {input_path}")
            continue

        compress_file(input_path, output_path, product["name"])

    print("\n✅  Done! Compact files written to:")
    print(f"   {COMPACT_DIR}")
    print("\nRestart the chatbot server to load them.")
