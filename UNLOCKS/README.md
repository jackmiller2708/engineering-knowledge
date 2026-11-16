# Unlock System

An **unlock** is one practical challenge that gives the learner a capability, produces a reusable artifact, and is verified by evidence. Completing it makes later unlocks available.

## Identity

`P<phase>-<TRACK>-<NN>`, for example `P0-BIT-03`. Phase is `0`–`6` or `X` (stretch). IDs are stable: never renumber or reuse an ID. A retired unlock is marked `retired` in a `DECISION_LOG.md` entry; its ID stays reserved.

## Where each fact lives

| Fact | Location |
|---|---|
| Prerequisites, mastery target, class (essential/optional), hour estimate, authoring status | `CATALOG.md` (single source) |
| The 12 unlock fields | `UNLOCKS/<ID>.md` |
| Done / in progress | `LEARNER_STATE.md` |
| Proof | `EVIDENCE/<ID>/` |
| Available / blocked | **Derived**, never stored: run `python3 tools/check_course.py --status` |

## The 12 fields

Header (checked against catalog): `id`, `title`, `phase`, `requires`, `mastery`. Body sections, in this order:
**Objective · Problem · Prerequisites · Techniques · What you need first · Practical challenge · Deliverable · Acceptance criteria · Verification · Mastery target · Next unlocks.**

Next unlocks lists each unlock this one enables and why. The checker confirms each really lists this unlock as a prerequisite.

## Rules for writing an unlock

1. It must exist for a reason in the engineering progression. State the reason under Problem.
2. Acceptance criteria are observable: a command, a test, a measurable behavior. No "understands X".
3. Keep it small enough for roughly 3–10 hours. Split anything bigger.
4. The deliverable should be reused later, or be explicitly marked an isolated experiment.
5. "What you need first" holds only what the learner needs *before* attempting. More arrives when a problem calls for it.
6. Give every unlock a class (E essential / O optional) and an hour estimate split build+study+verify+consolidate. An essential unlock may not require an optional one (checked).
7. Do not include a full solution in the file. Hints go in a "Hints" subsection only if useful, staged from small to large.

## Status model

`locked` (prerequisite missing) → `available` → `in progress` → `completed`. Only the last two are stored. `completed` requires acceptance criteria met, mastery shown ≥ target, and an evidence record (`CLAUDE.md` section 5).

## Authoring state

Only 13 unlocks are authored, to show how a subject progresses and to test the architecture. The rest are planned in `CATALOG.md`. Author an unlock only when the learner is about to need it (or when the learner requests it), after the curriculum is approved. Authoring an unlock needs approval like any curriculum edit.

## Worked progression: bits → platform component

`P0-BIT-01` single bits → `-02` masks → `-05` binary encode/decode → `-06` framed protocol parser → `P0-INT-01` crash-safe record log, the model for the engine's durable history (`P2-DUR-01`). Optional side branches: `-03` permission flags, `-04` packed records, `-07` reusable library. Each step is a problem the previous step could not solve.
