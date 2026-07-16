#!/usr/bin/env python3
"""Expand teaching lessons Screen A/B → A/B/C/D and inject 15-min I can wins.
Works on HASS / Science (SLIDES.push) and English (array-style if needed).
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

WIN15_CSS = """
  /* 15-minute demonstrable win */
  .win15{
    background:linear-gradient(135deg, color-mix(in srgb, var(--mint, #3d9b8f) 18%, transparent), var(--panel2, var(--panel)));
    border:1px solid color-mix(in srgb, var(--mint, #3d9b8f) 45%, var(--line));
    border-radius:var(--radius); padding:12px 14px; margin-bottom:2px;
  }
  .win15 .lbl{
    font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;
    color:var(--mint, #2a9d8f); margin-bottom:6px;
  }
  .win15 .can{
    font-family:inherit; font-size:clamp(16px,1.9vmin,22px); font-weight:800;
    letter-spacing:-.02em; line-height:1.25; margin:0 0 8px;
  }
  .win15 .prove{
    font-size:13.5px; color:var(--ink-dim, #4a5a54); line-height:1.4; margin:0;
  }
  .win15 .prove b{ color:var(--ink); }
"""

WIN15_FN = """
function win15(b){
  return `<div class="win15"><div class="lbl">⏱ By 15 minutes · demonstrable win</div>
    <p class="can">I can ${b.can}</p>
    <p class="prove"><b>Prove it:</b> ${b.prove}</p></div>`;
}
"""

# Lesson-specific 15-min goals + C/D content seeds
SCIENCE = {
  1: dict(can="prove air is matter with one piece of evidence",
          prove="Name your evidence in one sentence (balloon mass, trapped air, bubbles…).",
          c_title="Air vs empty — dig deeper",
          c_focus="Use the two-part matter test on tricky cases.",
          d_title="Prove it to a partner",
          d_focus="Teach someone else why air counts as matter."),
  2: dict(can="name two properties that make a solid a solid",
          prove="Point to a solid nearby and say shape + volume in your own words.",
          c_title="Solid properties in action",
          c_focus="Test compressibility and shape with household solids.",
          d_title="Solid or not? Defend your call",
          d_focus="Sort edge cases (sand, jelly, sponge) with reasons."),
  3: dict(can="describe how liquid particles move differently from solids",
          prove="Act it out or sketch packed-but-sliding particles in 30 seconds.",
          c_title="Liquid behaviour lab talk",
          c_focus="Viscosity and pouring — same state, different flow.",
          d_title="Liquid checklist",
          d_focus="Write a 3-bullet 'how I know it's a liquid' card."),
  4: dict(can="explain why gases fill a container",
          prove="Use particle spacing in one clear sentence.",
          c_title="Gas evidence hunt",
          c_focus="Find three gas clues you can detect without seeing particles.",
          d_title="Gas vs liquid showdown",
          d_focus="Compare two examples side-by-side with particle language."),
  5: dict(can="sketch solid, liquid and gas particle arrangements",
          prove="Draw three quick boxes and label packing + movement.",
          c_title="Particle pictures upgraded",
          c_focus="Add arrows for movement and a caption for each state.",
          d_title="Spot the wrong diagram",
          d_focus="Fix one incorrect particle picture and explain why."),
  6: dict(can="use property language to classify one mystery sample",
          prove="Say solid/liquid/gas + one property that proves it.",
          c_title="Classification clinic",
          c_focus="Practice Part A style reasons with sentence starters.",
          d_title="Part A warm-up",
          d_focus="Self-check: mass, volume, particle talk — ready for assess?"),
  8: dict(can="name one fair-test idea for melting ice",
          prove="Say what you would change and what you would keep the same.",
          c_title="Variables workshop",
          c_focus="Independent / dependent / controlled — card sort practice.",
          d_title="Question into investigation",
          d_focus="Turn a curious question into a testable plan seed."),
  9: dict(can="write one measurable prediction",
          prove="Use 'I predict… because…' with a unit of time or size.",
          c_title="Prediction craft",
          c_focus="Upgrade weak predictions into scientific ones.",
          d_title="Prediction gallery",
          d_focus="Peer critique: is it measurable? Is it linked to a variable?"),
  10: dict(can="list equipment for a simple ice investigation",
          prove="Name 4 items and why each is needed.",
          c_title="Method builder",
          c_focus="Numbered steps that someone else could follow.",
          d_title="Risk & fairness check",
          d_focus="Spot one unfair step and fix it."),
  11: dict(can="record one observation with units",
          prove="Write time + what changed in a table-ready line.",
          c_title="Data habits",
          c_focus="Tables, repeats, and honest anomalies.",
          d_title="Observation vs inference",
          d_focus="Sort statements into see / think / conclude."),
  12: dict(can="choose a graph type for melting-time data",
          prove="Say bar or line and why in one sentence.",
          c_title="Graph clinic",
          c_focus="Axes labels, scales, and what the story of the graph is.",
          d_title="Read a graph aloud",
          d_focus="Say the pattern: as X increases, Y…"),
  15: dict(can="restate Part B success criteria in my own words",
          prove="Tick three things an excellent booklet must show.",
          c_title="Booklet quality control",
          c_focus="Improve a weak sample conclusion together.",
          d_title="Peer feedback protocol",
          d_focus="Give one glow and one grow using criteria language."),
  16: dict(can="name one improvement I would make next time",
          prove="Link the improvement to a Science Inquiry Skill.",
          c_title="Reflection that counts",
          c_focus="Turn 'it was fun' into evidence-based reflection.",
          d_title="Celebration & next steps",
          d_focus="Share one skill you grew this unit."),
}

HASS = {
  1: dict(can="sort one item as a need or a want with a reason",
          prove="Say the item + N/W + because… (context allowed).",
          c_title="Needs & wants edge cases",
          c_focus="Argue both sides for Wi‑Fi, uniforms, phones.",
          d_title="Scarcity in one minute",
          d_focus="Use scarcity correctly in a spoken sentence."),
  2: dict(can="give one example of how needs differ by community",
          prove="Name two people/places and one different need each.",
          c_title="Same planet, different lists — deeper",
          c_focus="Compare household spending patterns with evidence.",
          d_title="Perspective swap",
          d_focus="Rewrite a shopping list for someone else's life."),
  3: dict(can="label a resource as natural, human or capital",
          prove="Point to one classroom example for each type.",
          c_title="Resource hunt 2.0",
          c_focus="Find hidden capital resources in a service business.",
          d_title="Resource chain",
          d_focus="Trace a snack from natural → human → capital."),
  4: dict(can="tell a good from a service with an example of each",
          prove="Hold up or name one good + one service in 20 seconds.",
          c_title="Goods & services mash-up",
          c_focus="Split mixed purchases (Uber Eats, haircut + product).",
          d_title="Fete stall design",
          d_focus="Plan a stall that sells both a good and a service."),
  5: dict(can="name one factor that influences a consumer choice",
          prove="Link a real purchase to price, ads, peers, or values.",
          c_title="Factor detective",
          c_focus="Annotate an ad for hidden influence factors.",
          d_title="Factor ranking",
          d_focus="Rank 5 factors for a school fete purchase."),
  6: dict(can="state one trade-off in a land-use decision",
          prove="Say what is gained and what is given up.",
          c_title="Finite resources — decide",
          c_focus="Limes land options: justify with criteria.",
          d_title="Stakeholder voices",
          d_focus="Argue from a farmer / student / council view."),
  7: dict(can="read one value from a simple graph correctly",
          prove="Point to the bar/point and say the number aloud.",
          c_title="Graph literacy boost",
          c_focus="Axes, units, and 'what is this graph about?'",
          d_title="Tell the story",
          d_focus="Write a 2-sentence conclusion from the graph."),
  8: dict(can="connect The Lorax to a real consumer choice",
          prove="Name the choice + who is affected.",
          c_title="Lorax → real world",
          c_focus="Map Once-ler decisions onto school-fete packaging.",
          d_title="Responsibility pledge",
          d_focus="One personal consumer action you can actually do."),
  9: dict(can="define sustainable in one student-friendly sentence",
          prove="Include people, planet, or future generations.",
          c_title="Sustainable fete ideas",
          c_focus="Audit a stall for waste and redesign one item.",
          d_title="Pitch a greener option",
          d_focus="30-second pitch: cost vs impact."),
  10: dict(can="ask one inquiry question about consumer data",
          prove="Start with How/Why/What if and make it researchable.",
          c_title="Question clinic",
          c_focus="Upgrade closed questions into inquiry questions.",
          d_title="Data plan seed",
          d_focus="What evidence would answer your question?"),
  11: dict(can="use a decision matrix with two criteria",
          prove="Score two options and say which wins and why.",
          c_title="Matrix practice",
          c_focus="Fill a mini matrix for a fete spend decision.",
          d_title="Defend the winner",
          d_focus="Explain scores without just saying 'I like it'."),
  12: dict(can="cite one source type for a consumer decision",
          prove="Name primary/secondary or a specific reliable source.",
          c_title="Source quality check",
          c_focus="Trustworthy vs shaky: ads, ABS, blogs, interviews.",
          d_title="Source for the fete",
          d_focus="Pick the best source for your Part A claim."),
  13: dict(can="draft one Part A paragraph with a clear claim",
          prove="Claim + reason + evidence starter on screen.",
          c_title="Part A writing studio",
          c_focus="TEEL-ish structure for consumer decisions.",
          d_title="Peer edit pass",
          d_focus="Swap: does the evidence actually support the claim?"),
  14: dict(can="list what Part A must include from the marking guide",
          prove="Three must-haves in your own words.",
          c_title="Marking guide decoder",
          c_focus="Translate criteria into student checklist language.",
          d_title="Self-mark a sample",
          d_focus="Score a model paragraph honestly."),
  15: dict(can="state my Part B focus decision in one sentence",
          prove="Name the fete choice and the main factor.",
          c_title="Part B planning board",
          c_focus="Sources, factors, and justification outline.",
          d_title="Gap check",
          d_focus="What evidence am I still missing?"),
  16: dict(can="give peer feedback using criteria language",
          prove="One glow + one grow linked to the guide.",
          c_title="Feedback clinic",
          c_focus="Replace 'good job' with specific criteria talk.",
          d_title="Final polish plan",
          d_focus="Three edits before submit."),
}

ENGLISH = {
    n: dict(
        can="use today's key idea in one spoken or written sentence",
        prove="Say it aloud or write it in your workbook in under a minute.",
        c_title="Go deeper",
        c_focus="Stretch task: apply today's concept to a new renewable example.",
        d_title="Secure the learning",
        d_focus="Exit-ready practice + share one improved sentence.",
    )
    for n in range(1, 19)
}
ENGLISH[1].update(can="define energy in my own words", prove="Write a one-line definition without copying the slide.",
                   c_title="Energy all around us", c_focus="List 5 energy uses and sort them into heat / movement / light / other.",
                   d_title="Glossary lock-in", d_focus="Rewrite energy, resource, fuel in your own words — no copying.")
ENGLISH[2].update(can="name one renewable and one non-renewable source", prove="Say both aloud with an everyday example each.",
                   c_title="T-chart stretch", c_focus="Add a third column: Can it run out? Yes / No / Depends — with reasons.",
                   d_title="Sort under pressure", d_focus="Teacher calls items; you flash renewable or non-renewable.")
ENGLISH[3].update(can="explain why renewables matter in one sentence", prove="Include people or the environment in your reason.",
                   c_title="Climate link", c_focus="Connect emissions → climate → why communities switch.",
                   d_title="Report seed", d_focus="Write one general statement fit for an information report intro.")


def js_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def make_win15_block(meta: dict) -> str:
    return (
        "{k:'win15', can:'%s', prove:'%s'}"
        % (js_escape(meta["can"]), js_escape(meta["prove"]))
    )


def make_cd_pushes(lesson: int, week: int, title_base: str, meta: dict, exit_items: list[str], subject: str) -> str:
    """Return SLIDES.push for Screen C and D."""
    # Derive short title from A title if available
    clean = re.sub(r"<[^>]+>", "", title_base)
    clean = clean.replace("\\'", "'")
    c_nav = f"L{lesson}C — {meta['c_title']}"
    d_nav = f"L{lesson}D — {meta['d_title']}"
    exits = exit_items[:4] if exit_items else [
        "explain today's idea in my own words",
        "complete the stretch task",
        "use key vocabulary accurately",
        "share one improvement with a partner",
    ]
    exits_js = ",".join("'" + js_escape(x) + "'" for x in exits)

    if subject == "english":
        c_eyebrow = f"Week {week} · Lesson {lesson} · Explore"
        d_eyebrow = f"Week {week} · Lesson {lesson} · Secure"
        c_phase = "Explore / Stretch"
        d_phase = "Secure / Prove"
    else:
        c_eyebrow = f"Week {week} · Lesson {lesson} · Explore / Stretch / Share"
        d_eyebrow = f"Week {week} · Lesson {lesson} · Secure / Prove / Reflect"
        c_phase = "Explore / Stretch"
        d_phase = "Secure / Prove"

    c = f"""SLIDES.push({{ nav:'{js_escape(c_nav)}',
  eyebrow:'{js_escape(c_eyebrow)}', eyebrowR:'Lesson {lesson} · Screen C',
  title:'{js_escape(meta['c_title'])}',
  screenlbl:'Student screen 3 of 4', wideLeft:true,
  left:[{{k:'steps', label:'{c_phase}', rows:[
    {{t:'Revisit the win', d:'Re-state the 15-minute “I can…” from Screen A. Can you still do it cold?'}},
    {{t:'Stretch task', d:'{js_escape(meta["c_focus"])}'}},
    {{t:'Capture evidence', d:'Write, sketch, or record one artefact that proves the stretch.'}},
    {{t:'Share', d:'Teach a partner your best example in 40 seconds.'}}
  ]}}],
  right:[{{k:'html', html:`<div class="card cream"><span class="tag try">STRETCH</span>
    <h3 style="margin-top:8px">{js_escape(meta["c_title"])}</h3>
    <p style="margin-top:8px">{js_escape(meta["c_focus"])}</p>
    <p style="margin-top:10px;color:#4a5a54;font-size:14px">Link back to: <b>{js_escape(clean)}</b></p></div>`}},
    {{k:'brain', q:[
      'What was easy about the stretch — and what still feels sticky?',
      'Which vocabulary word unlocked the idea for you today?',
      'If you taught this to a Year 4 student, what example would you use?'
    ]}}],
  notes:`<h4>Screen C purpose</h4><p>Deepen beyond A/B. Keep the 15-minute win visible; stretch should feel doable in ~15–20 min.</p>
  <h4>Focus</h4><p>{js_escape(meta["c_focus"])}</p>` }});
"""

    d = f"""SLIDES.push({{ nav:'{js_escape(d_nav)}',
  eyebrow:'{js_escape(d_eyebrow)}', eyebrowR:'Lesson {lesson} · Screen D',
  title:'{js_escape(meta['d_title'])}',
  screenlbl:'Student screen 4 of 4',
  left:[{{k:'steps', label:'{d_phase}', rows:[
    {{t:'Independent prove-it', d:'{js_escape(meta["d_focus"])}'}},
    {{t:'Quality check', d:'Use today\\'s vocabulary in your answer — underline each word you used.'}},
    {{t:'Peer glow / grow', d:'Swap: one specific strength + one next step.'}},
    {{t:'Exit ready', d:'Complete the exit check. Be ready for a cold-call on the 15-minute win.'}}
  ]}}],
  right:[{{k:'html', html:`<div class="card dark"><span class="tag try">PROVE IT</span>
    <p style="margin-top:8px">{js_escape(meta["d_focus"])}</p>
    <p style="margin-top:10px;font-size:14px;opacity:.85">Remember the 15-minute goal: <b>I can {js_escape(meta["can"])}</b></p></div>`}},
    {{k:'exit', items:[{exits_js}]}}],
  notes:`<h4>Screen D purpose</h4><p>Consolidate and prove. Run exit check cold. Re-teach the 15-minute win if shaky.</p>
  <h4>Focus</h4><p>{js_escape(meta["d_focus"])}</p>` }});
"""
    return c + "\n" + d


def extract_exit_items(b_block: str) -> list[str]:
    m = re.search(r"\{k:'exit',\s*items:\[(.*?)\]\}", b_block, re.S)
    if not m:
        return []
    return re.findall(r"'((?:\\'|[^'])*)'", m.group(1))


def extract_title(block: str) -> str:
    m = re.search(r"title:'((?:\\'|[^'])*)'", block)
    return m.group(1) if m else "today's idea"


def extract_week(block: str, lesson: int) -> int:
    m = re.search(r"eyebrow:'Week\s+(\d+)", block)
    if m:
        return int(m.group(1))
    # fallback from lesson number (2 lessons/week)
    return (lesson + 1) // 2


def inject_win15(a_block: str, meta: dict) -> str:
    """Prepend win15 into right:[ array."""
    win = make_win15_block(meta)
    # Already has win15?
    if "k:'win15'" in a_block or 'k:"win15"' in a_block:
        return a_block
    # right:[{k:'hook'  or right:[
    def repl(m):
        return m.group(0) + win + ","

    new, n = re.subn(r"right:\[\s*", repl, a_block, count=1)
    if n:
        return new
    return a_block


def update_screen_labels(block: str, letter: str, lesson: int) -> str:
    block = re.sub(
        r"eyebrowR:'Lesson %d · Screen [ABCD]'" % lesson,
        f"eyebrowR:'Lesson {lesson} · Screen {letter}'",
        block,
        count=1,
    )
    mapping = {"A": "1", "B": "2", "C": "3", "D": "4"}
    block = re.sub(
        r"screenlbl:'Student screen \d of \d'",
        f"screenlbl:'Student screen {mapping[letter]} of 4'",
        block,
        count=1,
    )
    # also of 2 → of 4 variants already handled
    return block


def find_push_blocks(text: str) -> list[tuple[int, int, str]]:
    """Find SLIDES.push({...}); blocks with brace matching (strings aware)."""
    blocks = []
    for m in re.finditer(r"SLIDES\.push\(\{", text):
        start = m.start()
        i = m.end() - 1  # at {
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
                elif in_s == "`" and ch == "$" and j + 1 < len(text) and text[j + 1] == "{":
                    # template expression — still track braces roughly inside
                    pass
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
                    # expect }); 
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


def process_push_file(path: Path, goals: dict[int, dict], subject: str, skip_lessons: set[int] | None = None) -> None:
    skip_lessons = skip_lessons or set()
    text = path.read_text(encoding="utf-8")
    original = text

    # CSS
    if ".win15{" not in text:
        text = text.replace("  /* exit check */", WIN15_CSS + "\n  /* exit check */", 1)
        if ".win15{" not in text:
            # try alternate
            text = text.replace(".exit{", WIN15_CSS + "\n  .exit{", 1)

    # win15 function
    if "function win15(" not in text:
        text = text.replace(
            "function exitCheck(items){",
            WIN15_FN + "\nfunction exitCheck(items){",
            1,
        )

    # renderBlock case
    if "case 'win15'" not in text:
        text = text.replace(
            "case 'exit': return exitCheck(b.items);",
            "case 'win15': return win15(b);\n    case 'exit': return exitCheck(b.items);",
            1,
        )

    # Cover meta clarity for double lessons
    if subject in ("science", "hass"):
        text = text.replace(
            "8 weeks · 16 lessons",
            "8 weeks · 16 lessons · 2 per week",
        )
        text = text.replace(
            "8 teaching weeks · 16 lessons",
            "8 teaching weeks · 16 lessons · 2 per week",
        )

    blocks = find_push_blocks(text)
    # Map lesson -> (A block indices in blocks list)
    a_blocks = {}
    b_blocks = {}
    for idx, (start, end, body) in enumerate(blocks):
        m = re.search(r"nav:'L(\d+)([AB])\s*[—\-]", body)
        if not m:
            # try Screen in eyebrowR
            m2 = re.search(r"eyebrowR:'Lesson (\d+) · Screen ([AB])'", body)
            if not m2:
                continue
            lesson, letter = int(m2.group(1)), m2.group(2)
        else:
            lesson, letter = int(m.group(1)), m.group(2)
        if lesson in skip_lessons:
            continue
        if lesson not in goals:
            continue
        if letter == "A":
            a_blocks[lesson] = (idx, start, end, body)
        elif letter == "B":
            b_blocks[lesson] = (idx, start, end, body)

    # Skip if already expanded (has Screen C for lesson 1)
    if re.search(r"eyebrowR:'Lesson 1 · Screen C'", text):
        print(f"  already has Screen C — skipping structure expand for {path.name}")
        # still ensure CSS/renderer present
        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"  updated renderer/CSS only: {path}")
        return

    # Rebuild from end so offsets stay valid: collect replacements
    # Strategy: replace whole file sections lesson by lesson from high lesson # down
    lessons = sorted(set(a_blocks) & set(b_blocks), reverse=True)
    print(f"  expanding lessons: {sorted(lessons)}")

    for lesson in lessons:
        meta = goals[lesson]
        ai, a_start, a_end, a_body = a_blocks[lesson]
        bi, b_start, b_end, b_body = b_blocks[lesson]

        # Re-find in current text (offsets may have shifted — re-scan each time)
        blocks_now = find_push_blocks(text)
        a_body = b_body = None
        a_start = a_end = b_start = b_end = None
        for start, end, body in blocks_now:
            if re.search(rf"eyebrowR:'Lesson {lesson} · Screen A'", body) or re.search(
                rf"nav:'L{lesson}A\s*[—\-]", body
            ):
                a_start, a_end, a_body = start, end, body
            if re.search(rf"eyebrowR:'Lesson {lesson} · Screen B'", body) or re.search(
                rf"nav:'L{lesson}B\s*[—\-]", body
            ):
                b_start, b_end, b_body = start, end, body
        if not a_body or not b_body:
            print(f"  ! skip L{lesson} — could not re-find A/B")
            continue

        week = extract_week(a_body, lesson)
        title = extract_title(a_body)
        exits = extract_exit_items(b_body)

        new_a = update_screen_labels(inject_win15(a_body, meta), "A", lesson)
        new_b = update_screen_labels(b_body, "B", lesson)
        cd = make_cd_pushes(lesson, week, title, meta, exits, subject)

        # Replace B first (later in file), then A
        text = text[:b_start] + new_b + "\n\n" + cd + text[b_end:]
        # re-find A after B edit
        blocks_now = find_push_blocks(text)
        for start, end, body in blocks_now:
            if re.search(rf"eyebrowR:'Lesson {lesson} · Screen A'", body) or re.search(
                rf"nav:'L{lesson}A\s*[—\-]", body
            ):
                # rebuild new_a from current body in case
                body2 = update_screen_labels(inject_win15(body, meta), "A", lesson)
                text = text[:start] + body2 + text[end:]
                break

    path.write_text(text, encoding="utf-8")
    print(f"  wrote {path}")


def process_english_array(path: Path) -> None:
    """English unit uses SLIDES = [ {...}, ... ] style possibly — detect."""
    text = path.read_text(encoding="utf-8")
    if "SLIDES.push" in text:
        process_push_file(path, ENGLISH, "english", skip_lessons=set(range(19, 25)))
        return

    print("  English array mode not implemented in this pass — checking structure…")
    # If it's inline array, still add CSS/renderer and do a simpler regex pass
    if ".win15{" not in text:
        # insert CSS before </style>
        text = text.replace("</style>", WIN15_CSS + "\n</style>", 1)
    if "function win15(" not in text and "function exitCheck" in text:
        text = text.replace(
            "function exitCheck(items){",
            WIN15_FN + "\nfunction exitCheck(items){",
            1,
        )
    if "case 'win15'" not in text:
        text = text.replace(
            "case 'exit': return exitCheck(b.items);",
            "case 'win15': return win15(b);\n    case 'exit': return exitCheck(b.items);",
            1,
        )
    path.write_text(text, encoding="utf-8")
    print("  English: CSS/renderer updated; structure expand needs push-style — check file")


def main():
    root_sci = Path("/Users/niccomino/Desktop/sciencematter/states-of-matter-unit.html")
    root_hass = Path("/Users/niccomino/Desktop/hassconsumers/consumers-unit.html")
    root_eng = Path("/Users/niccomino/Desktop/renewableenergy/renewable-energy-unit.html")

    print("Science…")
    process_push_file(root_sci, SCIENCE, "science", skip_lessons={7, 13, 14})
    print("HASS…")
    process_push_file(root_hass, HASS, "hass")
    print("English…")
    process_english_array(root_eng)
    print("Done.")


if __name__ == "__main__":
    main()
