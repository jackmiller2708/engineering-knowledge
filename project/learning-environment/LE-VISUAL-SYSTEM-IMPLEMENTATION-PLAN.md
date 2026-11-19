# ELE Visual System: Implementation Plan

Owner: learner approves; Claude proposes. Status: **proposal for review. Not approved.** This is a planning document. It authorizes no implementation.

Basis: [VISUAL_IDENTITY_SPECIFICATION.md](VISUAL_IDENTITY_SPECIFICATION.md) at commit `f3c162c`, referred to as "the spec". Rule IDs `VI-nn` are the spec's register rows (section 17 there). Related: [LE-PLAN.md](LE-PLAN.md), [LE-PRODUCT.md](LE-PRODUCT.md), [LE-DESIGN.md](LE-DESIGN.md), [LE-DECISIONS.md](LE-DECISIONS.md) (LE-nnn), [LE-FIRST-WORKBENCH-BRIEF.md](LE-FIRST-WORKBENCH-BRIEF.md) ("the brief"). This file edits none of them.

**Labels.** Findings use the Knowledge Standard section 6.1 labels. **Observation** means I read it in a file or ran a command in this task. **Interpretation** is my reasoning from observations. **Unknown** is not established. **Proposal** is a suggestion for the owner. **Decision** appears only for something already recorded by the owner, cited by ID.

**What this task did and did not do.** I read the spec, the five LE documents, and the application source named below. I ran `grep`, `wc`, `ls` and `git` commands. I did **not** build the application, run any test suite, run the application, take screenshots, or open the design-stage-4 or design-stage-5 screenshots. Nothing here is claimed as validated by execution. Stated test counts and results from earlier reports are quoted as earlier claims, not re-verified.

## 1. Objective and boundaries

### 1.1 Objective
Carry the approved visual grammar into the application in small, reviewable steps, using the **Place Value Bench** as the first real content, and learn from actual behaviour before building anything further. The aim is a maintainable result. A complete design system is not the aim.

### 1.2 Four layers, kept apart

| Layer | What it is | Status now |
|---|---|---|
| **Visual identity specification** | What the identity is: grammar, rules, decision statuses. Lives in this repository. | Approved as the canonical reference. Not changed by this plan. |
| **Design-system foundations** | The smallest set of semantic styling roles the first workbench needs (surface, border, text, state, selection). | Stage 1. Only what a Stage 3 rule uses. |
| **Workbench integration** | Applying the roles and any shared primitive to the Place Value Bench. | Stages 2 and 3. |
| **Later expansion** | Equipment plates, hybrid views, facility scenery, further primitives. | Conditional (section 4, "Later expansion"). |

### 1.3 What this plan does not authorize
- Any change to application code, styles, tests or assets. Each stage needs its own approval.
- A new package, a component library, a token catalogue, a theme switcher or a universal styling framework.
- Changing the place-value domain module, the manifest, persistence, routing, Rust, Tauri configuration or host permissions.
- Adding learner-facing words, concepts, ranges or curriculum. Copy beyond the approved set needs owner approval (brief tripwire 7).
- Promoting Signal Relay out of its isolated experiment.
- Reopening Direction D, Treatment B, or any Locked row of the spec.
- Changing LE-DECISIONS, LE-PLAN, LE-PRODUCT, LE-DESIGN, the brief or the spec.

## 2. Current-state audit

Paths are relative to `repositories/engineering-projects/projects/engineering-learning-environment/` (the application repository). Application branch at audit: `review/first-place-value-workbench-t1`, HEAD `cca267d`. The only uncommitted item there is the untracked `apps/desktop/design-stage-5/`. All findings below are **Observation** unless marked.

### 2.1 Styling and theme mechanism
- One shared stylesheet, `apps/desktop/src/styles.css` (222 lines), defines the custom properties on `:root`. Its header says "tokens and the few controls the screens use. No remote fonts or assets (strict CSP)".
- Themes use `color-scheme: light dark` with `light-dark(...)` on every colour token. There is no theme attribute, class or script. A search of `src/` for `data-theme` and `theme` found nothing. **Interpretation:** both themes are present and follow the system setting. That matches the LE-DESIGN recommendation. It is not a decision (VI-38 is Unresolved).
- Colours are `oklch()` values. Roles present: `--ground`, `--panel`, `--raised`, `--bench`, `--grid`, `--bar`, `--on-bar`, `--text`, `--muted`, `--rule`, `--edge`, `--accent`, `--on-accent`, `--focus`, `--danger`, `--danger-tint`, `--notice`, `--notice-tint`, `--new-tint`.
- Fonts: `--ui` is a system stack and `--mono` is a system mono stack. No font file is bundled. **Interpretation:** this already fits VI-45 and avoids VI-46 (fonts unresolved).
- Base size `0.875rem`, `font-variant-numeric: tabular-nums` set on `:root`. A global `:focus-visible` outline uses `--focus`. `prefers-reduced-motion` is respected in `styles.css` and in `place-value-bench.css`.
- Per-screen CSS lives beside each component, with Angular emulated encapsulation. CSS line counts: `place-value-bench.css` 533, `worlds-screen.css` 211, `lab-list.css` 170, `lab-frame.css` 140, `app.css` 134, `lab-create-form.css` 103, `signal-relay-experiment.css` 103.
- Hard-coded colours appear in the bench only in three `oklch(0 0 0 / …)` shadows (`place-value-bench.css`, `.bit`, `.thumb`, `.result`). Other colours use the tokens.

### 2.2 Components and shared UI responsibilities
- The Lab screen is `workspaces/lab-frame.{ts,html,css}`. Its template renders a `.labbar` (lab name, "Created"), a `section.benchwrap aria-label="Bench"` containing `<app-place-value-bench />`, then a `dl.facts` row (World, Lab, Created, ID) below the bench. This matches brief D5a.
- The shell is `app.{ts,html,css}`: skip link, a `header.bar` with brand and breadcrumb (Worlds / world / lab name plus short id), a `role="status"` line, and the routed content. The bar uses `--bar` and `--on-bar`, a solid dark-blue fill in both themes (`oklch(0.3 …)` light, `oklch(0.135 …)` dark). It has no scale, no gradient.
- There is **no shared component** for panel, pill, chip, frame or Inspector. Each screen styles its own panels with `background: var(--panel); border: 1px solid var(--edge); border-radius: 6px`. The same recipe is repeated in `.board`, `.inspector` and `.prediction` in `place-value-bench.css`. **Interpretation:** this is the one demonstrated duplication that could justify a shared rule. Whether it justifies a shared Angular component is Unknown.
- `.problem`, `.entries`, `button`, `button.primary`, `input` live in `styles.css` and are shared by the Worlds and Lab screens.
- The Signal Relay experiment is routed at `experiments/signal-relay` (`app.routes.ts`) with its own component folder `experiments/signal-relay/` and `signal-relay-experiment.css`. It uses the shared tokens (`--muted`, `--accent`, `--panel`, `--edge`). Its page title reads "Signal relay experiment". It is an isolated experiment and is not in the plan's scope.

### 2.3 The Place Value Bench today
Files: `apps/desktop/src/app/workspaces/place-value-bench.{ts,html,css,spec.ts}` (190, 78 template lines, 533, 604 lines). Domain: `packages/domain/src/place-value.ts`.
- **Domain.** Exports include `parsePattern`, `weightOf`, `contributions`, `total`, `flipBit`, `flipEffect`, `resizePattern`, `wouldDiscardActiveBits`, `clearedPattern`, `patternCount`, `maxTotal`, and the width limits 1 and 8. The component imports `contributions`, `flipBit`, `flipEffect`, `parsePattern`, `total`, `weightOf`. It does not import `patternCount` or `maxTotal`. All arithmetic is in the domain.
- **Behaviour.** Starts at `1011`, width 4, on every open. State is in component signals only (`selected`, `changed`, `lastPosition`, `skipped`, `draft`, `locked`, `revealed`, `announcement`). There is no width control, no Clear control, and a spec test asserts there are none (`place-value-bench.spec.ts`, "adds no width or Clear controls"). Brief tasks T5 (width and Clear) is therefore not implemented. **Interpretation:** the bench is a fixed four-bit instance today.
- **Structure.** An `.intro` with two approved copy lines and a "Starting example" label. A `.board` holding a four-row `table.places` (Position buttons, Weight, Bit switch buttons, Contribution with a `.meter` bar), then a `.result` block (Total and the sum line), then a polite live region `p.last`. A `.side` column holds the optional `section.prediction` and `section.inspector`.
- **Inspector.** `section.inspector aria-label="Inspector"`. With nothing selected it shows "Select a position to inspect it." With a selection it shows Position, Bit, Weight and Contribution and two sentences. A "Deselect" button appears while something is selected. It has no Hide/Show control and is always present. The Inspector sits in the same `.side` column as Prediction, not in a separate region.
- **Selection.** Selecting a Position (button `.pos`, `aria-pressed`) puts class `sel` on the four cells of that column. CSS draws a `2px` accent border on both inline sides and a `2px` accent border on the pressed button. Tests assert `aria-pressed` and `td.sel`, not colours.
- **State treatments.** The last-changed column (`.just`) gets `--new-tint` and an inset top accent line. A Bit switch shows its digit always; "on" is the accent colour with the thumb at the top. The Contribution meter fills with `--accent`. The locked Prediction is a dashed accent outline. A revealed actual change shows "▲" or "▼". Colour is never the only cue in these. **Interpretation:** the bench already follows "state needs a second cue" (VI-42).
- **Typography.** Mono for the table, digits, Total (`2.5rem`), sum line and Inspector values. `--ui` for labels. Small text uses `0.75rem` and `0.8125rem`. The smallest size in the bench CSS is `0.75rem`. `:root` sets `font-size: 0.875rem`, so by calculation `0.75rem` is about 10.5 px (assuming the default 16 px browser size; not measured in a render). **Observation:** no size below `0.75rem` in this file.
- **Layout.** The host is a wrapping flex row, `max-inline-size: 960px`. `.board` has `flex: 1 1 360px`. `.side` has `flex: 1 1 280px; max-inline-size: 320px`. There are no media queries in the bench CSS. The Inspector goes beside the board when there is room and below it when there is not. **Interpretation:** this matches the brief's "right column when wide, stacked at 720×480". The exact crossover width is Unknown without rendering.
- **Colour roles in use.** `--accent` carries at least six meanings in this bench: Bit on, Contribution meter, selection, last-changed cue, locked prediction outline, and (shared) buttons and links. **Interpretation:** the spec reserves teal for energised/high (VI-39) and makes selection neutral (VI-12). The current single accent does not separate those roles. In the dark theme the accent is `oklch(0.8 0.105 205)`, which looks teal-like. In light it is `oklch(0.44 0.12 238)`, which is blue. **Unknown:** how these render.
- **Keyboard and focus.** All controls are native buttons or an input. Focus is moved explicitly after Lock, Try another, Skip and Deselect (`focusAfterRender`, `deselect`). Tests cover focus staying on the Bit operated. A global `:focus-visible` ring exists. **Not observed:** actual Tab order in a running window for the bench (earlier reports cover the Worlds screen).
- **Tests.** `place-value-bench.spec.ts` has describe blocks for the example, flipping, the live region, the Inspector (nothing selected, selecting, staying in step), the copy scan and layout regions, and Prediction (optional, entering and locking, flipping). Test runner for the application is `@angular/build:unit-test` (`ng test`); the domain package uses `vitest run`. I did not run either.

### 2.4 Responsive behaviour
- Tauri window: height 720, `minWidth` 720, `minHeight` 480 (`src-tauri/tauri.conf.json`). This is LE-021.
- The shell is `grid-template-rows: 40px auto minmax(0, 1fr)` with `block-size: 100vh; overflow: hidden`, so `.content` is the one scroller. `.benchwrap` has `overflow: auto`.
- `app.css` hides the brand below 900 px. The Worlds screens have a `max-width: 899px` block. The bench has none.
- Earlier reports (design-stage-4 `STEP8_REPORT.md`) state that Worlds and the Lab screen were observed at 720×480 and other widths in the built app, in dark. A light-theme screenshot exists in `step8-evidence/closure/` by file name. **Unknown:** whether the Place Value Bench itself was observed at 720×480 in the built app after T4. Commit `16c3b79` is titled "fit the bench at 720x480 and keep focus after controls leave", which is evidence that someone checked it. I did not view that evidence.

### 2.5 Inconsistencies and gaps relevant to the first slice
1. **Lab name appears three times** on the Lab screen: breadcrumb (`app.html`), lab bar `h1` (`lab-frame.html`), and the facts row (`Lab`). Observation. The spec says do not duplicate a Lab name unnecessarily (VI-24). The brief requires the facts row (D5a). The spec leaves the facts row's relation to Treatment B Unresolved (VI-36). **Interpretation:** this is a real conflict between two non-locked sources. It is not in the first slice (section 5, D-04).
2. **No kind pill, tag or Model label** exists anywhere. The word "Model" is not in the approved learner copy list (brief section 10).
3. **Duplicated panel recipe** in three bench panels (2.2).
4. **One accent for many meanings** (2.3).
5. **Selection is a coloured box**, not the spec's brackets plus tint (VI-12).
6. **The Total, the "Starting example" label and the Contribution meter** are the bench's instrument-like parts. None is a decorative readout. No range string exists. The domain does have `patternCount` and `maxTotal`, which the brief lists as "always visible" (section 4.2: "the count of patterns and largest value for the width"). The current bench does not show them. **Unknown:** whether that omission was deliberate. The spec says a readout needs a meaningful domain-supplied property (VI-16).
7. **The shell bar** is a coloured solid, not the flat, scaled bar of Treatment B (VI-14). It is shared with the Worlds and Lab list screens.
8. **Page title of the relay experiment** reads "Signal relay experiment" (lowercase r). The spec locks the Lab name "Signal Relay" (VI-29). This is in an experiment outside scope. Recorded for later.

## 3. Implementation principles

Each rule says how the spec's statuses carry over. "Temporary" means a value used now that the spec does not lock.

1. **Model sheet versus equipment plate (VI-06, VI-09, VI-09a).** The Place Value Bench is a model-only workbench. It uses the model register: flat surface, thin lines, mono values. It gets **no** plate, screws, gradient or equipment pill. Equipment styling is not built in this phase (section 4, Later expansion).
2. **Three element roles (spec principle 6, VI-16).** Every added element must be an engineering indicator, a structural convention or environmental scenery. For the bench:
   - *Engineering indicator:* Bit digits, Weight, Contribution, Total, the sum line, the Inspector values, the "▲/▼" direction. Each is computed from the domain. They must stay true. The interface adds none.
   - *Structural convention:* a frame around the model sheet, selection brackets, crop marks if used. Restrained, identical wherever used, carrying no value, never shaped like a measurement.
   - *Environmental scenery:* none in the bench. The facility is out of scope for the first slice.
3. **No decorative readouts.** No range or measurement string is added to the bench unless the owner approves it as a meaningful property (D-05) and its text comes from `@ele/domain` (`patternCount`, `maxTotal`) with approved wording. The first slice adds none.
4. **Kind pills and tags (VI-06, VI-10, VI-11).** A kind pill is built only after the owner approves its learner-facing word (D-03). Tag chips (`S1`, `U1`) are **not** built in this phase: the Place Value Bench has one representation of each part, so no relationship exists to tag (VI-10).
5. **Selection (VI-12).** Selection becomes corner brackets plus a light tint in the neutral/ink family, replacing the accent-coloured box. Keep `aria-pressed`, the `sel` class and focus behaviour. Brackets must not rely on colour alone and must work in both themes. Cross-highlighting between views is not needed in a single-view bench.
6. **Inspector presentation (VI-30, VI-31, VI-32).** Keep it contextual, one consistent shell, never hiding the primary representation. It stays always visible in the first slice, so the Hide/Show control from the D3 mockup is **not** built (nothing hides, so nothing needs revealing; adding a control would be new navigation). Revisit when the Inspector must be collapsible (D-06). Its header may show the selected item as a chip (VI-15) only if the owner approves (D-03 applies to any new word; the chip would repeat an existing name such as "Position 2" and may need no new word).
7. **State communication (VI-42, VI-39).** Keep every existing second cue. Do not add a state without a non-colour cue. Do not claim colour-blind safety (VI-44).
8. **The high/energised role (VI-39, C9).** Whether an abstract stored Bit "1" takes the teal role is open. Until the owner decides (D-01), the bench keeps its current accent for Bit-on and the meter. No new teal value is introduced.
9. **Technical typography (VI-45, VI-46).** Keep the existing `--ui` and `--mono` stacks. Mono for values, identifiers and the Total. No new font, no bundled font, no new numeric type scale. Do not shrink text to fit a layout (VI-53). The bench's current smallest size (`0.75rem`) is the floor for this phase.
10. **Light and dark (VI-37, VI-38).** Every new colour rule must be written with `light-dark()` in the existing manner, so both themes ship together. No theme control, no stored preference, no primary theme. Values come from existing tokens, or from `color-mix()` of existing tokens, so no new palette value is invented. A new literal colour needs owner approval (D-02).
11. **Responsive (VI-50, VI-52, VI-53).** 720×480 and 1100×720 are the two checked sizes. No new breakpoint. The Inspector may stack and the surface may scroll. Nothing may overflow horizontally at 720.
12. **Component reuse (VI-61).** Prefer a shared CSS rule or class over an Angular component. Create a shared Angular component only when the same markup and behaviour is needed in two real places. Today only a panel frame recipe repeats, and it repeats as CSS.
13. **Semantics stay in the domain (VI-60).** No new number, range, relationship or sentence about the engineering concept is written in the template or stylesheet. Existing approved copy is unchanged.
14. **Decision statuses are preserved.** A temporary value used in the app is noted as temporary in the stage report. It is not written back to the spec as Locked or Provisional.

## 4. Staged implementation plan

Each stage is independently reviewable and needs owner approval to start. Completing a stage does not authorize the next. Validation is stage-specific; the full suite runs at most at the end of Stage 3 and Stage 4, or earlier only if a dependency or architecture risk appears (a tripwire below).

A **focused check** means: the specific spec file(s) named, run alone. A **viewport capture** means: the bench rendered at 720×480 and 1100×720, in light and dark, saved as images with fixed file names. The mechanism for capture is **Unknown** until Stage 0 establishes it (candidates seen: the built debug Tauri window used by earlier reports; the static build in `apps/desktop/dist`; `ng serve`). The stage reports must say which was used and what was not covered.

### Stage 0: Baseline and implementation mapping

- **Purpose.** Fix the starting point so later changes are comparable, and settle which decisions block which stage.
- **Scope.** Read-only plus captured evidence. No product change.
- **Deliverables.**
  1. A mapping table from spec rules (VI rows used in this plan) to the files in section 2.
  2. Baseline viewport captures of the bench: 720×480 and 1100×720, light and dark, in these states: initial; Position 2 selected; after one flip; Prediction locked; Prediction revealed. Twenty images at most.
  3. The method used to capture, and what the mechanism cannot show (for example whether light theme can be forced).
  4. One run of the bench's focused spec and the domain's `place-value` test file, recording pass or fail counts as run.
  5. A blocking-decision list with the owner's answers to D-01 to D-03 (section 5), or a note that Stage 3 parts are held.
- **Dependencies.** None.
- **MUST.** Record exactly what was and was not captured. Save evidence outside tracked source, or in a clearly named evidence folder the owner approves.
- **MUST NOT.** Edit source, styles, tests or assets. Commit.
- **Tripwires.** Light theme cannot be rendered by any available method (record as Unknown and continue dark-only for that stage, say so). The focused spec fails before any change (stop and report; do not fix in this stage).
- **Focused validation.** The two test files named above; the captures exist and open.
- **Exit criteria.** Baseline images and run results are recorded. The mapping table exists. The owner has seen the blocking-decision list.
- **Expected areas.** None changed. Evidence outside `src/`.

### Stage 1: Minimal visual foundation

- **Purpose.** Name only the roles the first workbench needs, so later rules read by meaning.
- **Scope.** A few semantic custom properties in `apps/desktop/src/styles.css` (or none, if Stage 3 rules can use existing tokens directly). **Proposal:** add a role only when a Stage 3 rule uses it, and define it from existing tokens.
- **Candidate roles (Proposal, none required until used).** A selection ink/tint pair; a structural-line role for frames and brackets. Names and values are temporary and not the spec's.
- **Deliverables.** The roles actually used, each defined with `light-dark()` from existing tokens or `color-mix()` of them; a one-paragraph note of each role's meaning.
- **Dependencies.** Stage 0.
- **MUST.** Keep every existing token and screen unchanged in appearance. Keep values replaceable in one place. Keep both themes.
- **MUST NOT.** Add a token catalogue, a spacing or type scale, a new package, a theme switch, a teal value, or a role no rule uses.
- **Tripwires.** A role would need a new literal colour (stop, ask D-02). A change alters the Worlds or Lab list screens visually (stop; Stage 1 is meant to be inert for them).
- **Focused validation.** Viewport captures of Worlds and the bench match the Stage 0 baseline (a human compare; state any pixel differences found). The bench spec and the Worlds spec pass.
- **Exit criteria.** No visible change anywhere; roles exist only if used.
- **Expected files.** `apps/desktop/src/styles.css` at most.

### Stage 2: Shared visual primitives

Decide each primitive on demonstrated need. Build none for completeness.

| Candidate | Real need in the Place Value Bench | Plan |
|---|---|---|
| Selection treatment | Yes: Position selection today | Build (CSS). It is the Stage 3 first task. |
| Panel / model-sheet frame | Yes: three panels repeat one recipe | A shared CSS rule or class is justified. An Angular component is **not** justified yet. Decide at Stage 3 after seeing the result. |
| Kind pill | Only if the owner approves the word "Model" (D-03) | Held until D-03 is answered. |
| Inspector shell | One Inspector exists, in one place | **Not** extracted. Style it in place. Revisit when a second screen needs an Inspector (Signal Relay later). |
| Technical value / identifier styling | Mono is already applied by selector in several places | A single small class may remove repetition. Optional, only if it reduces code. |
| State glyphs | Existing ▲/▼ and the digit cue suffice | None added. Success, warning, fault, unknown glyphs are **not** built; no real content in the bench needs them. |
| Tag chip | No relationship exists in a model-only bench | **Not built.** |
| Equipment plate | No equipment in the bench | **Not built.** |

- **Purpose.** Introduce a primitive only where the bench shows it is shared.
- **Deliverables.** The primitives marked "Build" above, as CSS, with a one-line statement of the shared responsibility each carries.
- **Dependencies.** Stage 1; D-03 for the pill.
- **MUST.** Keep primitives as CSS unless two real call sites need the same markup and behaviour. Keep existing class names that tests rely on (`sel`, `pos`, `bit`, `.places`, `.total .value` and so on) or update those tests with the owner's agreement.
- **MUST NOT.** Add components for equipment, tags, state glyphs or hybrids. Add a component folder or package for the visual system.
- **Tripwires.** A primitive needs a second call site that does not exist (do not build it). A primitive needs new learner-facing copy (stop, D-03).
- **Focused validation.** The bench spec passes; captures show no change beyond the intended primitives.
- **Exit criteria.** Each built primitive has two or more real uses, or is explicitly recorded as a single-use style kept in place.
- **Expected files.** `place-value-bench.css`, `styles.css`; `place-value-bench.html` only if a pill is approved.

### Stage 3: Place Value Bench vertical slice

- **Purpose.** Show the grammar working on real content, with the engineering representation primary.
- **Scope.** Presentation of the existing bench only. The bar and Worlds screens are **not** in this stage.
- **Deliverables, in order of size (each can be reviewed alone).**
  1. **Selection** as neutral corner brackets plus tint, replacing the accent box (VI-12). This is the first executable task (section 7).
  2. **Model-sheet frame** on the board: a restrained frame consistent with the spec's dashed model-sheet convention (VI-06), applied to the three panels through one shared rule, if it improves legibility. Skipped if it does not.
  3. **Inspector presentation:** header/typographic alignment with the model-sheet frame; no new controls; no new copy.
  4. **State roles:** Bit-on and the meter follow the owner's answer on D-01. If undecided, left unchanged.
  5. **Optional, owner-approved only:** a kind pill (D-03) and a domain-supplied readout (D-05).
- **Dependencies.** Stages 0 to 2. D-01 for item 4; D-03 and D-05 for item 5.
- **MUST.** Preserve domain behaviour, approved copy, DOM structure the tests assert, focus handling, the polite live region, the "Starting example" rule, Prediction mechanics, and the reduced-motion handling. Keep Total, Weight, Bit and Contribution as the visually primary content. Keep text at or above the current `0.75rem` floor. Keep both themes in step.
- **MUST NOT.** Add Width or Clear controls (brief T5 is separate). Add copy. Add a range or measurement string without D-05. Add equipment, tags, scenery, crop marks (D-07), a graduated scale, or new navigation. Change the domain module. Touch the shell bar, Worlds screens, routing, persistence, Rust or Tauri.
- **Tripwires.** A test fails that asserts structure or copy (stop; do not edit the test to pass). Horizontal overflow at 720 (stop). The frame or Inspector takes space from the table such that the bench needs scrolling it did not need before (stop and measure). A change needs a domain value that does not exist (stop; domain changes are outside this plan). Keyboard focus is no longer visible on any control.
- **Focused validation.** The bench spec and the domain `place-value` tests. Viewport captures in all eight combinations (2 sizes × 2 themes × sparse and dense states: initial, and Position selected with Prediction revealed). A manual keyboard pass at 720×480: Tab through every control, operate a Bit and a Position, lock and reveal a Prediction, confirming visible focus throughout. State plainly that this is a manual pass by the implementer, not an accessibility audit and not screen-reader testing.
- **Exit criteria.** Behaviour unchanged by the tests. The captures show the intended treatment in both themes at both sizes. Measured or visibly judged: the board's usable area at 720×480 is not smaller than the baseline.
- **Expected files.** `place-value-bench.css`; `styles.css` if a shared rule is used; `place-value-bench.html` only for approved additions.

### Stage 4: Evidence-based refinement

- **Purpose.** Compare what was built with the spec and record the truth.
- **Deliverables.** A short report with a table: each spec rule used, its status in the spec, what the implementation does, what was observed (with the capture file), and a verdict: works, fails, or unknown. A list of spec rows the evidence supports changing, with the evidence. A list of what remains provisional.
- **Dependencies.** Stage 3.
- **MUST.** Report failures. Propose spec revisions as separate proposals for the owner. Distinguish what was observed from what was assumed.
- **MUST NOT.** Edit the spec. Promote a Provisional row to Locked. Claim an audit, user testing or screen-reader testing. Treat one reviewer's view as validation.
- **Tripwires.** The evidence contradicts a Locked row (report to the owner; do not change the implementation to hide it).
- **Focused validation.** Re-run the bench spec once; re-capture any state changed since Stage 3. Run the full application suite once at this stage.
- **Exit criteria.** The report exists and the owner has reviewed it. Open questions are listed.
- **Expected files.** None in `src/`, unless the owner approves fixes found by the report, as a separate stage.

### Later expansion (conditions, not commitments)

| Item | Introduce when |
|---|---|
| **Shell bar (Treatment B: flat bar, graduated scale)** (VI-14) | The owner approves a bar change that also covers the Worlds and Lab list screens, after the bench slice has been reviewed. The bar is shared and its change is visible app-wide. It is a separate stage with its own captures. |
| **Equipment plates** (VI-09) | A real piece of equipment exists with a domain model behind it. No equipment exists in the application today. |
| **Tag chips, hybrid views, cross-highlighting** (VI-10, VI-11, VI-12) | A second representation of the same part exists in one screen. Place Value has none. |
| **Inspector shell as a shared component, Hide/Show control** (VI-32) | A second screen needs an Inspector, or a screen's Inspector must collapse. |
| **Facility scenery, bay plates** (VI-18, VI-25) | The Worlds screen is redesigned (VI-23 resolved) and the owner decides the "bay" vocabulary (VI-28). Scenery stays outside the engineering representation. |
| **Further shared primitives** (VI-61) | The same markup and behaviour is needed in two real places. |
| **Signal Relay as a validation case** | The owner asks for it as a separate, explicitly scoped experiment. It is not a production milestone. Its Lab name is Signal Relay (VI-29). It must not gain a curriculum claim. |
| **Keyboard model for a visual construction surface** (VI-62) | A construction surface exists. Not before. |

## 5. Decision and uncertainty register

**Locked by the spec** (not reopened here): VI-01, VI-02, VI-07, VI-09a, VI-13 (Treatment B), VI-16, VI-17 (no footer hint repeating the Inspector's empty state), VI-19, VI-20, VI-22, VI-24, VI-25, VI-26, VI-29 (Signal Relay), VI-30, VI-31, VI-37 (both themes), VI-40 (search path never teal), VI-44, VI-50 (720×480), VI-60, VI-63. Practical consequences for this plan: both themes ship together; no equipment or scenery is needed; no readout without a meaningful property; semantics come from the domain.

**Provisional rules used temporarily** (usable now, may change): VI-03, VI-04, VI-06, VI-08, VI-12, VI-14, VI-15, VI-32, VI-39, VI-42, VI-43, VI-45, VI-52, VI-53, VI-61. Used as stated in section 3. Any temporary value is recorded in stage reports and not written into the spec.

**Questions for the owner.** "Blocks" means that part of the work waits for the answer. IDs `D-nn` are this plan's row labels. They are not LE decisions.

| ID | Question | Blocks | Why it matters | Proposal (not a decision) | Evidence that would help |
|---|---|---|---|---|---|
| D-01 | Does an abstract stored Bit "1" take the teal/high role (spec C9, VI-39)? | Stage 3 item 4 only | The bench currently uses one accent for Bit-on. The spec reserves teal for energised/high. Place Value is about number representation, not signals. | Do **not** use the high role in Place Value; keep Bit-on in the current accent until a signal-bearing world exists. That keeps teal's meaning clean. The D3 mockup did the opposite. | Owner view; a look at the Stage 0 captures. |
| D-02 | May the plan add any new literal colour? | Any stage needing one | The spec does not lock palette values (VI-43). Inventing one is a design decision. | No. Derive from existing tokens with `color-mix()`; ask if that fails. | Stage 1 and 3 captures. |
| D-03 | Is a learner-facing "Model" pill approved copy? | Kind pill; Inspector chip if it adds a word | Brief tripwire 7: words beyond the approved terms need approval. "Model" is not in brief section 10. | Hold the pill. The bench is the only model screen and labels itself by its content, so a pill adds a word without separating two registers. Revisit when hybrid views exist. | Owner copy decision. |
| D-04 | Lab name appears in the breadcrumb, lab bar and facts row. Reduce it? | Not blocking; deferred | Spec VI-24 versus brief D5a. Conflict between non-locked sources. | Leave as is in this phase. Resolve with VI-36 when the facts strip and bar are redesigned. | Owner decision on VI-36. |
| D-05 | Show a domain-supplied range (`maxTotal(width)`, `patternCount(width)`) on the bench? | Stage 3 item 5 only | The brief lists "count of patterns and largest value" as always visible. The spec allows a readout only for a meaningful property and approved wording. | Defer. Decide with the Width and Clear work (brief T5), where the range actually changes. At fixed width 4 it is constant. | Brief T5 outcome; approved wording. |
| D-06 | Does the Inspector need Hide/Show in the bench? | Not blocking | Nothing hides it today. VI-32 is Provisional. | No. Do not add a control with no job. | Stage 4 evidence at 720×480. |
| D-07 | Are crop marks wanted on the bench model sheet? | Not blocking | VI-08 is Provisional and decorative-in-effect (a structural convention). Risk of clutter and of looking like measurement. | Skip in the first slice. Reconsider only if the frame alone leaves the sheet unrecognisable in Stage 4. | Stage 4 comparison. |
| D-08 | Does the facts row sit inside the Treatment B tool row? | Not blocking; deferred | VI-36 Unresolved. | Leave the facts row as is. | First redesign of the Lab frame. |

**Unresolved spec rows that do not block the first slice.** VI-23 (facility and Worlds-screen design), VI-27 (how a Lab label differs from a tag chip), VI-28 ("bay"), VI-33 (regions arrangement), VI-34 (Library, Investigation, probes), VI-35 (supplied example versus built), VI-38 (theme selection), VI-46 (fonts and numeric tokens), VI-49 (timing), VI-54 (relay at 720×480), VI-55 (Adder text size, not in the application), VI-59, VI-62. The plan neither resolves nor depends on them.

**Evidence still needed** for the two largest uncertainties: (a) whether the grammar reads as one identity on the real bench in both themes (Stage 3 and 4 captures); (b) whether the 720×480 layout stays usable after the change (Stage 3 captures and the keyboard pass). Neither can be answered from the mockups.

## 6. Risks and failure modes

| Risk | How it would show | Mitigation in this plan |
|---|---|---|
| **Overbuilding a design system.** | A new folder, a token catalogue, components with one use. | Stage 1 adds roles only when a rule uses them; Stage 2 table builds only demonstrated needs; no package; tripwires on single-use abstractions. |
| **Structural conventions that look like measurements.** | A tick, scale or bracket that reads as data; crop marks beside a number. | Principle 2; D-07 skips crop marks; no graduated scale in Stage 3. |
| **Values or relationships the domain did not supply.** | A range string or sentence typed in a template. | Principle 3 and 13; D-05; all numbers come from `@ele/domain`. |
| **Breaking Place Value behaviour while restyling.** | A spec test fails; focus lost; live region changes. | Presentation only; class and attribute hooks kept; MUST NOT list; spec run at every stage; stop on test failure, do not edit tests to pass. |
| **Losing 720×480 usability.** | Horizontal overflow; surface needing more scrolling; clipped text. | Captures at both sizes in both themes at every visual stage; text floor of `0.75rem`; stop conditions. |
| **Theme inconsistency.** | A rule works in dark and fails in light. | `light-dark()` only; every capture in both themes; Stage 0 records whether light can be forced. If it cannot, the plan says so and the owner decides whether to proceed. |
| **Inspector or framing competing with the representation.** | Frames, borders or tints draw the eye before the Total and bits. | Hierarchy in the spec section 6; Stage 3 exit check on usable area; a frame is skipped if it does not help. |
| **Abstractions that raise maintenance cost.** | A shared component whose inputs keep growing. | Prefer shared CSS; component only for two real call sites. |
| **Teal meaning drifts.** | Bit-on and the meter use the same colour as a future energised state. | D-01 settles the Place Value case before Stage 3 item 4. |
| **Evidence is thin.** | Conclusions drawn from one reviewer and a few captures. | Stage 4 labels each verdict observed, assumed or unknown; no audit claims. |
| **Capture method unreliable.** | Light theme cannot be forced in the webview, as earlier reports found for some methods. | Stage 0 establishes and records the method and its limits before any change. |

## 7. First executable task

**Title.** Place Value Bench: replace the Position-selection colour box with neutral corner brackets and tint (Stage 0 baseline plus Stage 3 item 1).

**Outcome.** One visible change: the selected Position's column is marked by corner brackets and a light neutral tint instead of a two-pixel accent border, in both themes, at 720×480 and 1100×720. Nothing else changes.

**Why this one.** It is needed by the grammar (VI-12), depends on no open decision (D-01 to D-08 do not block it), needs no new word, no new colour and no teal, touches one stylesheet, and is easy to review in images.

**Files.**
- Change: `apps/desktop/src/app/workspaces/place-value-bench.css`, the rules for `.places td.sel` and `.pos[aria-pressed='true']` (lines 226 to 248 at audit). `.places td.just` and all other rules are left alone.
- Read, not change: `place-value-bench.html`, `place-value-bench.ts`, `place-value-bench.spec.ts`, `styles.css`.
- If a role is needed, `styles.css` may gain **one** selection role defined with `light-dark()` or `color-mix()` from existing tokens (`--text`, `--edge`, `--raised`). No new literal colour.

**Steps.**
1. Capture the Stage 0 baseline for the selected-Position state (720×480 and 1100×720, light and dark) and record the capture method and what it cannot show. If light cannot be forced, say so and continue with dark only, and report it.
2. Run `place-value-bench.spec.ts` alone and the domain `place-value.test.ts` alone, and record the results before any change.
3. Change the two selectors so that selection is shown by corner brackets at the top of the Position row and the bottom of the Contribution row of the selected column, plus a neutral tint across the column. Keep the `2px`-weight or visible-line second cue for the pressed Position button so the cue is not tint-only. Choose any technique that keeps the DOM unchanged (for example pseudo-elements or layered gradients on the existing `td`).
4. Re-capture the same states. Re-run both test files.
5. Write a short report: baseline and after captures (file names), the CSS changed, test results as run, which of the four combinations were covered, and what was not covered.

**Preserve.** All behaviour, all template markup, class names and attributes used by tests (`sel`, `pos`, `aria-pressed`), approved copy, focus handling, `:focus-visible` outlines, the `.just` last-changed cue, motion handling.

**Do not.** Edit the template or TypeScript. Edit any test. Add a pill, chip, readout, scale, crop mark or glyph. Introduce a colour literal. Touch `app.css`, the shell bar, the Worlds screens, the domain package, the Signal Relay experiment, Rust or Tauri. Add Width or Clear. Clean up unrelated CSS (such as the three black shadows). Commit unless the owner asks.

**Focused validation.**
- The two test files pass, as run (state the counts).
- In captures, the selected column is identifiable without colour: it has brackets and a visible line on the pressed button. It is distinct from the `.just` cue when both apply on one column. Both themes show it.
- No horizontal overflow at 720×480; the bench's usable height is no smaller than the baseline.
- Keyboard: at 720×480, Tab to a Position button, press Space or Enter, and confirm the selection cue and the focus ring are both visible at once. A manual pass, not an accessibility audit.

**Stop and report if.** Brackets cannot be drawn without changing the template. A test fails. The tint or brackets are not visible in one theme. The selected cue cannot be told apart from `.just` on the same column. Any change spills outside `place-value-bench.css` and the one optional role.

**Exit.** The report is written, the single stylesheet change is reviewable as a small diff, and the owner has the images. Stage 1 and the remaining Stage 3 items are separate approvals.
