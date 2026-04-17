import json
import re


def _parse_inline(text: str) -> list[dict]:
    """Parse inline markdown (bold, italic, links) into Tiptap inline nodes."""
    nodes: list[dict] = []
    pattern = r"(\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\)|[^*\[]+)"
    for m in re.finditer(pattern, text):
        part = m.group(0)
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            nodes.append({"type": "text", "marks": [{"type": "bold"}], "text": part[2:-2]})
        elif part.startswith("*") and part.endswith("*"):
            nodes.append({"type": "text", "marks": [{"type": "italic"}], "text": part[1:-1]})
        else:
            link_m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part)
            if link_m:
                nodes.append({
                    "type": "text",
                    "marks": [{"type": "link", "attrs": {"href": link_m.group(2), "target": "_blank"}}],
                    "text": link_m.group(1),
                })
            elif part:
                nodes.append({"type": "text", "text": part})
    return nodes or [{"type": "text", "text": text}]


def markdown_to_tiptap(md: str) -> str:
    """Convert digest Markdown to Tiptap JSON string for Substack's draft_body field.

    Skips the ## title and *Issue #N* lines — Substack already renders those
    from draft_title and draft_subtitle.
    """
    content: list[dict] = []
    skip_next_hr = False

    for line in md.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue

        # Skip the ## heading (duplicate of draft_title)
        if stripped.startswith("## "):
            skip_next_hr = True
            continue

        # Skip *Issue #N* italic line
        if stripped.startswith("*Issue") and stripped.endswith("*"):
            continue

        # Skip the first --- after the header block
        if stripped == "---" and skip_next_hr:
            skip_next_hr = False
            continue

        if stripped.startswith("### "):
            content.append({
                "type": "heading",
                "attrs": {"level": 3},
                "content": _parse_inline(stripped[4:]),
            })
        elif stripped == "---":
            content.append({"type": "horizontalRule"})
        elif stripped.startswith("> "):
            # Blockquote — used for "Take" commentary
            content.append({
                "type": "blockquote",
                "content": [{"type": "paragraph", "content": _parse_inline(stripped[2:])}],
            })
        elif stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            content.append({
                "type": "paragraph",
                "content": [{"type": "text", "marks": [{"type": "italic"}], "text": stripped[1:-1]}],
            })
        else:
            content.append({"type": "paragraph", "content": _parse_inline(stripped)})

    return json.dumps({"type": "doc", "content": content})


# Aliases
markdown_to_substack_html = markdown_to_tiptap
markdown_to_simple_html = markdown_to_tiptap
