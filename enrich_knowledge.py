#!/usr/bin/env python3
"""Enrich unit HTML slides with know/discuss content on Screens C/D (+ English Screen A).

Run: python3 enrich_knowledge.py

Content data lives in:
  - enrich_knowledge_content.py  (Science lessons 1,2,3,4,5,6,8,9,10,11,12,15,16 + HASS 1–16)
  - enrich_knowledge_english.py  (English lessons 1–18 C/D + Screen A read blocks)

Targets:
  - states-of-matter-unit.html
  - hassconsumers/consumers-unit.html
  - renewableenergy/renewable-energy-unit.html

If English file lacks Screen C/D, run expand_screens.py first.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

KNOW_CSS = """
  .know-card h3{font-size:17px;margin:8px 0 6px}
  .know-list{margin:8px 0 0;padding-left:18px;font-size:14px;line-height:1.45;color:var(--ink-dim)}
  .know-list li{margin-bottom:6px}
  .discuss-card h3{font-size:17px}
  .discuss-list{list-style:none;display:flex;flex-direction:column;gap:8px;margin-top:10px;padding:0;margin-left:0}
  .discuss-list li{display:flex;gap:10px;font-size:14px;line-height:1.35}
  .discuss-list .n{flex:none;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font-weight:800;font-size:11px;background:var(--chip-bg);border:1px solid var(--line)}
  .discuss-tip{margin-top:10px;font-size:13px;color:var(--ink-faint);font-style:italic}
  .sort-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
  .sort-col{background:var(--chip-bg);border:1px solid var(--line);border-radius:10px;padding:10px;font-size:13px}
  .sort-col b{display:block;margin-bottom:6px;color:var(--mint);font-size:12px;letter-spacing:.06em;text-transform:uppercase}
"""

KNOW_FN = """
function knowCard(k){
  const body=(k.body||[]).map(p=>`<p style="margin-bottom:8px;line-height:1.4">${p}</p>`).join('');
  const pts=(k.points||[]).map(p=>`<li>${p}</li>`).join('');
  return `<div class="card cream know-card"><span class="tag read">${k.label||'KNOWLEDGE'}</span>
    ${k.heading?`<h3>${k.heading}</h3>`:''}${body}
    ${pts?`<ul class="know-list">${pts}</ul>`:''}
    ${k.fact?`<div class="notice"><b>Key idea:</b> ${k.fact}</div>`:''}</div>`;
}
function discussCard(d){
  return `<div class="card dark discuss-card"><span class="tag try">${d.label||'DISCUSS'}</span>
    <h3>${d.title||'Talk it through'}</h3>
    <ul class="discuss-list">${(d.prompts||[]).map((p,i)=>`<li><span class="n">${i+1}</span><span>${p}</span></li>`).join('')}</ul>
    ${d.tip?`<p class="discuss-tip">${d.tip}</p>`:''}</div>`;
}
"""


def js_str(s: str) -> str:
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


def js_backtick(s: str) -> str:
    return "`" + s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${") + "`"


def find_push_blocks(text: str) -> list[tuple[int, int, str]]:
    blocks = []
    for m in re.finditer(r"SLIDES\.push\(\{", text):
        start = m.start()
        i = m.end() - 1
        depth = 0
        in_s = None
        esc = False
        j = i
        while j < len(text):
            ch = text[j]
            if in_s:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == in_s:
                    in_s = None
                j += 1
                continue
            if ch in ("'", '"', "`"):
                in_s = ch
                j += 1
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = j + 1
                    while end < len(text) and text[end] in " \t\r\n":
                        end += 1
                    if end < len(text) and text[end] == ")":
                        end += 1
                    if end < len(text) and text[end] == ";":
                        end += 1
                    blocks.append((start, end, text[start:end]))
                    break
            j += 1
    return blocks


def find_matching_bracket(text: str, open_pos: int) -> int:
    """Return index of matching ] for [ at open_pos."""
    depth = 0
    in_s = None
    esc = False
    j = open_pos
    while j < len(text):
        ch = text[j]
        if in_s:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == in_s:
                in_s = None
            j += 1
            continue
        if ch in ("'", '"', "`"):
            in_s = ch
            j += 1
            continue
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    raise ValueError("unmatched [")


def serialize_block(b: dict) -> str:
    k = b["k"]
    if k == "know":
        p = ["k:'know'"]
        for key in ("label", "heading", "fact"):
            if b.get(key):
                p.append(f"{key}:{js_str(b[key])}")
        if b.get("body"):
            p.append("body:[" + ",".join(js_str(x) for x in b["body"]) + "]")
        if b.get("points"):
            p.append("points:[" + ",".join(js_str(x) for x in b["points"]) + "]")
        return "{" + ",".join(p) + "}"
    if k == "discuss":
        p = ["k:'discuss'", f"title:{js_str(b.get('title', 'Talk it through'))}"]
        if b.get("label"):
            p.append(f"label:{js_str(b['label'])}")
        if b.get("tip"):
            p.append(f"tip:{js_str(b['tip'])}")
        p.append("prompts:[" + ",".join(js_str(x) for x in b["prompts"]) + "]")
        return "{" + ",".join(p) + "}"
    if k == "steps":
        rows = ",".join(
            f"{{t:{js_str(r['t'])},d:{js_str(r['d'])}}}" for r in b["rows"]
        )
        return f"{{k:'steps',label:{js_str(b.get('label', 'DO THIS'))},rows:[{rows}]}}"
    if k == "brain":
        qs = ",".join(js_str(q) for q in b["q"])
        return f"{{k:'brain',q:[{qs}]}}"
    if k == "read":
        p = ["k:'read'", f"heading:{js_str(b['heading'])}"]
        p.append("body:[" + ",".join(js_str(x) for x in b["body"]) + "]")
        if b.get("notice"):
            p.append(f"notice:{js_str(b['notice'])}")
        return "{" + ",".join(p) + "}"
    if k == "html":
        return f"{{k:'html',html:{js_backtick(b['html'])}}}"
    if k == "exit":
        items = ",".join(js_str(x) for x in b["items"])
        return f"{{k:'exit',items:[{items}]}}"
    raise ValueError(f"unknown block k={k}")


def serialize_array(blocks: list[dict]) -> str:
    return "[" + ",".join(serialize_block(b) for b in blocks) + "]"


def replace_key_array(block: str, key: str, blocks: list[dict]) -> str:
    m = re.search(rf"\b{key}:\s*\[", block)
    if not m:
        raise ValueError(f"{key}: not found")
    arr_start = m.end() - 1
    arr_end = find_matching_bracket(block, arr_start) + 1
    return block[:arr_start] + serialize_array(blocks) + block[arr_end:]


def replace_notes(block: str, notes_html: str) -> str:
    m = re.search(r"notes:`", block)
    if not m:
        return block + f",\n  notes:{js_backtick(notes_html)}"
    start = m.end()
    i = start
    while i < len(block):
        if block[i] == "\\":
            i += 2
            continue
        if block[i] == "`":
            return block[: m.start()] + f"notes:{js_backtick(notes_html)}" + block[i + 1 :]
        i += 1
    raise ValueError("unclosed notes backtick")


def extract_exit_block(block: str) -> dict | None:
    m = re.search(r"\{k:'exit',\s*items:\[", block)
    if not m:
        return None
    brace = m.start()
    depth = 0
    in_s = None
    esc = False
    j = brace
    while j < len(block):
        ch = block[j]
        if in_s:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == in_s:
                in_s = None
            j += 1
            continue
        if ch in ("'", '"', "`"):
            in_s = ch
            j += 1
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                raw = block[brace : j + 1]
                items = re.findall(r"'((?:\\'|[^'])*)'", raw.split("items:[", 1)[1])
                return {"k": "exit", "items": [x.replace("\\'", "'") for x in items]}
        j += 1
    return None


def parse_lesson_screen(body: str) -> tuple[int, str] | None:
    m = re.search(r"eyebrowR:'Lesson (\d+) · Screen ([ABCD])'", body)
    if m:
        return int(m.group(1)), m.group(2)
    return None


def left_needs_a_enrich(block: str) -> bool:
    m = re.search(r"left:\s*\[", block)
    if not m:
        return False
    arr_start = m.end() - 1
    arr_end = find_matching_bracket(block, arr_start) + 1
    left = block[arr_start:arr_end]
    if "k:'read'" in left or "k:'know'" in left:
        return False
    has_img = "k:'img'" in left
    has_hook = "k:'hook'" in left
    return has_img and has_hook


def inject_infra(text: str) -> str:
    if ".discuss-list{list-style:none" not in text:
        for anchor in (
            "  /* steps / report builder */",
            "  .steps{ background:var(--cream)",
            "  .steps{background:var(--cream)",
        ):
            if anchor in text:
                text = text.replace(anchor, KNOW_CSS + "\n" + anchor, 1)
                break
    if "function knowCard(" not in text:
        text = text.replace(
            "function exitCheck(items){",
            KNOW_FN + "\nfunction exitCheck(items){",
            1,
        )
    if "case 'know'" not in text:
        text = text.replace(
            "case 'exit': return exitCheck(b.items);",
            "case 'know': return knowCard(b);\n    case 'discuss': return discussCard(b);\n    case 'exit': return exitCheck(b.items);",
            1,
        )
    return text


def enrich_file(path: Path, cd_content: dict, a_content: dict | None = None) -> dict:
    text = path.read_text(encoding="utf-8")
    text = inject_infra(text)
    stats = {"C": 0, "D": 0, "A": 0, "skipped": []}

    blocks = find_push_blocks(text)
    replacements: list[tuple[int, int, str]] = []

    for start, end, body in blocks:
        ls = parse_lesson_screen(body)
        if not ls:
            continue
        lesson, screen = ls

        if screen in ("C", "D") and lesson in cd_content and screen in cd_content[lesson]:
            spec = cd_content[lesson][screen]
            new_body = body
            left = list(spec["left"])
            right = list(spec["right"])
            if screen == "D":
                exit_b = extract_exit_block(body)
                if exit_b:
                    right = [b for b in right if b.get("k") != "exit"] + [exit_b]
                else:
                    stats["skipped"].append(f"L{lesson}D no exit")
            new_body = replace_key_array(new_body, "left", left)
            new_body = replace_key_array(new_body, "right", right)
            new_body = replace_notes(new_body, spec["notes"])
            replacements.append((start, end, new_body))
            stats[screen] += 1

    for start, end, new_body in sorted(replacements, key=lambda x: x[0], reverse=True):
        text = text[:start] + new_body + text[end:]

    path.write_text(text, encoding="utf-8")
    return stats


def enrich_file_english_a(path: Path, a_content: dict) -> int:
    """Prepend know/read to Screen A without re-parsing full left arrays."""
    text = path.read_text(encoding="utf-8")
    count = 0
    while True:
        blocks = find_push_blocks(text)
        changed = False
        for start, end, body in blocks:
            ls = parse_lesson_screen(body)
            if not ls or ls[1] != "A" or ls[0] not in a_content:
                continue
            if not left_needs_a_enrich(body):
                continue
            prepend_js = serialize_block(a_content[ls[0]])
            m = re.search(r"left:\s*\[", body)
            if not m:
                continue
            insert_at = m.end()
            new_body = body[:insert_at] + prepend_js + "," + body[insert_at:]
            text = text[:start] + new_body + text[end:]
            count += 1
            changed = True
            break
        if not changed:
            break
    path.write_text(text, encoding="utf-8")
    return count


def validate_script(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"<script>(.*?)</script>", text, re.S)
    if not m:
        raise RuntimeError(f"No script in {path}")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(m.group(1))
        tmp = f.name
    r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"JS check failed for {path.name}:\n{r.stderr}")
    Path(tmp).unlink(missing_ok=True)
    print(f"  ✓ node --check {path.name}")


def main():
    from enrich_knowledge_content import HASS_CD, SCIENCE_CD
    from enrich_knowledge_english import ENGLISH_A, ENGLISH_CD

    files = [
        (Path("/Users/niccomino/Desktop/sciencematter/states-of-matter-unit.html"), SCIENCE_CD, None),
        (Path("/Users/niccomino/Desktop/hassconsumers/consumers-unit.html"), HASS_CD, None),
        (Path("/Users/niccomino/Desktop/renewableenergy/renewable-energy-unit.html"), ENGLISH_CD, ENGLISH_A),
    ]

    for path, cd, a in files:
        if not path.exists():
            print(f"SKIP missing {path}")
            continue
        print(f"Enriching {path.name}…")
        stats = enrich_file(path, cd, a)
        if a:
            stats["A"] = enrich_file_english_a(path, a)
        print(f"  screens C:{stats['C']} D:{stats['D']} A:{stats.get('A', 0)}")
        validate_script(path)
    print("Done.")


if __name__ == "__main__":
    main()
