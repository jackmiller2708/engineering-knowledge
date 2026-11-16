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
**Objective · Problem · Prerequisites (with `Uses:` lines) · Techniques · What you need first · Practical challenge · Deliverable · Acceptance criteria · Verification · Mastery target · Next unlocks.**

Next unlocks lists each unlock this one enables and why. The checker confirms each really lists this unlock as a prerequisite.

## Rules for writing an unlock

1. It must exist for a reason in the engineering progression. State the reason under Problem.
2. Acceptance criteria are observable: a command, a test, a measurable behavior. No "understands X".
3. Keep it small enough for roughly 3–10 hours. Split anything bigger.
4. The deliverable should be reused later, or be explicitly marked an isolated experiment.
5. "What you need first" holds only what the learner needs *before* attempting. More arrives when a problem calls for it.
6. Give every unlock a class (E essential / O optional) and an hour estimate split build+study+verify+consolidate. An essential unlock may not require an optional one (checked).
7. In Prerequisites, name only the unlocks listed in the catalog as prerequisites. Add one `Uses:` line naming each artifact the challenge consumes or extends and the unlock that produces it, for example `Uses: the bits package (P0-BIT-01).` The checker confirms each named unlock is a (transitive) prerequisite. It cannot find an artifact you forgot to declare, so check this by reading the challenge: every package, service, document or tool it assumes must come from a prerequisite.
8. Do not include a full solution in the file. Hints go in a "Hints" subsection only if useful, staged from small to large.

## Status model

`locked` (prerequisite missing) → `available` → `in progress` → `completed`. Only the last two are stored. `completed` requires acceptance criteria met, mastery shown ≥ target, and an evidence record (`CLAUDE.md` section 5).

## Just-in-time authoring

The 14 unlocks authored so far were written before approval and are approved with the curriculum (D-007). The curriculum is approved, so Claude may author further unlocks as described next. Before approval no unlock was authored or edited. After approval (`CURRICULUM.md` status `APPROVED`), Claude may author a *planned* unlock without further approval, when it is the learner's likely next choice, if it stays inside these **frozen boundaries**, all taken from `CATALOG.md` and the phase files:

1. Identity and objective: the unlock ID and its catalog title.
2. Prerequisites (`Requires`).
3. Class (essential or optional).
4. Mastery target.
5. Estimated time (`Hours`).
6. Phase contribution: the completion criterion or milestone it serves (`COURSE_OBJECTIVE.md`, `PHASES/`, `project/PLAN.md`).

Claude may decide, within those limits: the explanations, exercises, practical challenge, deliverable details, acceptance criteria wording, verification procedure and implementation details. Authoring changes exactly one catalog cell, `Definition`: `planned` to `authored`.

If an unlock needs a change to any frozen boundary, Claude presents the change and its consequences and waits for the learner's approval, then logs it in `DECISION_LOG.md`. Examples: a new prerequisite, a different mastery target, 3 more hours, moving an unlock between essential and optional, a deliverable that no longer serves its criterion. Nothing here authorizes adding unlocks or widening scope.

`python3 tools/check_course.py` records the catalog's boundary columns as a fingerprint when the curriculum is approved and fails if they later change without an approved update.

## Authoring state

Fourteen unlocks are authored. The rest are planned in `CATALOG.md`. Do not author in bulk.

## Worked progression: bits → platform component

`P0-BIT-01` single bits → `-02` masks → `-05` binary encode/decode → `-06` framed protocol parser → `P0-INT-01` crash-safe record log, the model for the engine's durable history (`P2-DUR-01`). Optional side branches: `-03` permission flags, `-04` packed records, `-07` reusable library. Each step is a problem the previous step could not solve.
