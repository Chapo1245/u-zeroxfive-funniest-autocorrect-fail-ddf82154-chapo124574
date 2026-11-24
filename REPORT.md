# REPORT — Funniest Autocorrect Fail

- **Competition:** `u-zeroxfive-funniest-autocorrect-fail-ddf82154` — Funniest Autocorrect Fail
- **Prize:** $2 total (1st $1, 2nd $0.35, 3rd $0.25, top 7 paid)
- **Deadline:** 28 Nov 2026 00:15 WIB (27 Nov 17:15 UTC)
- **Judge:** pairwise, z-ai/glm-5.3-flash. Criteria in order: (1) is a one-line
  autocorrect fail; (2) funny on first read, clear and surprising wrong word;
  (3) reads as a real autocorrect slip, not a written joke; (4) clear without
  explanation, fits in one line; (5) wrong word specific and original, not a
  generic typo.
- **Program:** `main.py` (Python, stdlib only) writes exactly one line to
  `/output/entry.txt`, deterministic, no trailing newline.

## Chosen entry (136 characters, 1 line)

> Hi Mr. Carter, confirming our 3pm meeting to discuss the merger. Sorry, autocorrect, I meant murder. MERGER. Please disregard that text.

## Candidates considered

### A — merger / murder (CHOSEN)

> Hi Mr. Carter, confirming our 3pm meeting to discuss the merger. Sorry, autocorrect, I meant murder. MERGER. Please disregard that text.

### B — damnation / salvation

> Pastor, thank you for the beautiful sermon on eternal damnation. I mean salvation. SALVATION. Sorry, my phone hates me.

### C — driver / killer

> Mom, I finally passed my driving test! The instructor said I was a natural born killer. I mean driver. DRIVER. Please stop crying.

## Pairwise reasoning

- **A vs B:** both use a formal context ruined by one word plus a panicked
  all-caps correction. A wins on surprise (criterion 2): a business meeting
  about a merger flipping to a meeting about a murder is a bigger, darker
  meaning-flip than a sermon flipping between two theological words, and
  "merger" → "murder" is a far more believable phone-keyboard slip
  (criterion 3) than "salvation" → "damnation", which no keyboard suggests.
  B's joke also leans on the church setting; A's joke lives entirely in the
  one wrong word.
- **A vs C:** C loses on criterion 3 — no autocorrect engine turns "driver"
  into "killer"; it reads as a written joke wearing an autocorrect costume.
  A's swap is plausible (same opening letters, similar length, a word the
  keyboard genuinely offers), and the correction-then-correction structure
  is exactly how a real panicked follow-up text reads.
- **B vs C:** B beats C for the same reason — "damnation" at least sits in
  the same word family as "salvation", while C's swap has no keyboard
  plausibility at all.

## Why A wins overall

- The original intent stays fully visible (confirming a 3pm meeting about a
  merger), so the fail lands without explanation (criterion 4).
- The wrong word is specific and original (criterion 5): not a generic typo,
  not the stock "duck"/"sperm bank" lines, and the double correction
  ("I meant murder. MERGER.") makes the slip unmistakable on first read.
- Short (136 chars) — helps the size tie-break, and the entry is submitted
  early, which helps the receipt tie-break.
- Deliberately avoided stock autocorrect lines (duck, sperm bank, milk/milf):
  the 3 fixed house texts play in every heat, and a byte-identical copy of
  one shares its rate and never enters the playoff.

## Local verification

- Ran `python3 main.py` twice; `/output/entry.txt` byte-identical both runs.
- Content: 136 characters, 136 bytes (ASCII), exactly 1 line, no trailing
  newline, not whitespace-only — inside the 1–199 character gate.
- No network, no secrets, no files read at runtime; the line is a constant
  in `main.py`.

## Loss-log lessons applied

- Fresh-written entry in this session; no starter read, no lines copied from
  any other entry or repo.
- Provisional/dev scores are never treated as results; this report records
  only the pick and its reasoning, not a score.
- Single best variant submitted (Force_Last): no weaker follow-up variant.
