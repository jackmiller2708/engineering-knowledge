# ELE Visual Identity Specification

Owner: learner approves; Claude proposes. Status: **approved by the owner as the canonical visual identity reference** after review of commit `f3c162c44bbce71c332ce3ae6c7c4bf9a6853360`. Rows marked Provisional or Unresolved in section 17 keep those statuses. Nothing in this document has been implemented, and it does not authorize implementation.

This is the canonical home of the visual identity for the Engineering Learning Environment (ELE). The application repository holds experiments and evidence only. It does not hold the specification.

Related: [LE-PRODUCT.md](LE-PRODUCT.md) (product definition), [LE-DESIGN.md](LE-DESIGN.md) (interaction structure), [LE-DECISIONS.md](LE-DECISIONS.md) (decision log, LE-nnn), [LE-FIRST-WORKBENCH-BRIEF.md](LE-FIRST-WORKBENCH-BRIEF.md) (first workbench). This file edits none of them.

## 0. How to read this document

**Decision status.** Every rule below has one of three statuses. The register in section 17 lists each with its evidence.

| Status | Meaning |
|---|---|
| **Locked** | Explicitly selected or approved by the owner (a recorded LE decision, or stated in the task that commissioned this document). Preserve it. |
| **Provisional** | Accepted as the current foundation. Open to change on implementation evidence. |
| **Unresolved** | Not decided, or the evidence is insufficient. Do not treat any current mockup value as the answer. |

Inline tags such as `[VI-13]` point to the register row. Register IDs are row labels in this document. They are not entries in LE-DECISIONS.md, and no decision here has been logged there.

**Evidence labels.** Claims about evidence use the Knowledge Standard section 6.1 labels: Fact, Assumption, Interpretation, Observation, Hypothesis, Unknown. "Mockup" means a page in `design-stage-5/` (section 16). A mockup is evidence of a proposal. It is not proof of approval.

**Source hierarchy used.**
1. Owner decisions in the commissioning task and in the decision records (LE-001 to LE-021).
2. Approved product principles and architecture decisions (LE-PRODUCT, LE-DESIGN where stated as decided).
3. D3 and D4 evidence and findings.
4. Earlier proposals and mockup details (A, B, C, D, D2).
5. My interpretation. Where a rule rests on this, it says so.

**What this document does not contain:** numeric design tokens, font choices, shader or texture definitions, asset files, component code, or curriculum content. Those are either unresolved or belong elsewhere. Concept content stays in the curriculum and is linked, not copied (LE-002).

### 0.1 Source conflicts and gaps (reported, not silently reconciled)

| # | Conflict or gap | What I did |
|---|---|---|
| C1 | LE-009 says "Palette, typography and visual identity are not decided", and LE-PRODUCT lists visual identity as Unknown. No LE entry records Direction D or Treatment B. | Followed the commissioning task (hierarchy 1): Treatment B is selected, Direction D is the provisional foundation. The owner may want a decision-log entry. I did not write one. |
| C2 | The exploration principle "Expose concepts, hide mechanisms" can be read against LE-PRODUCT principle 4 "Expose, do not hide" and LE-006/LE-010 (internals are inspectable). | Interpretation: "mechanisms" means interface and simulation machinery, not the engineering mechanism under study. The engineering behaviour is never hidden. The wording stays Provisional `[VI-05]`. |
| C3 | The mockups use facility terms: "hall", "bay", "Bay 3". LE-005 fixes the learner vocabulary (World, Lab, Bench). LE-FIRST-WORKBENCH-BRIEF tripwire 7 says to stop if a word beyond the approved terms is needed. | Treated "bay" as a design metaphor, not approved learner vocabulary `[VI-28]`. Unresolved. |
| C4 | LE-DESIGN recommends the Inspector at the right. D3 puts it at the bottom in linked mode, and at the right only in equipment-first at 1100×720. LE-011 says the arrangement is not decided. | Recorded the D3 placements as Provisional `[VI-32]`. No conflict with a decision, but a deviation from a recommendation. |
| C5 | LE-DESIGN recommends light and dark following the system setting. The mockups use a manual toggle. The task says do not choose a primary theme. | Both themes in scope `[VI-37]`. How the theme is chosen stays Unresolved `[VI-38]`. |
| C6 | Treatment B as mocked shows a range string on every framed panel. The task says a readout must represent a meaningful property and not every panel needs one. | Followed the task `[VI-16]`. The mockup's strings are illustrations. |
| C7 | LE-FIRST-WORKBENCH-BRIEF D5a requires a facts strip (World, Lab, Created, ID) in its own row below the bench. No D3 or D4 mockup shows it. D4 also removes a footer hint. | Left the facts strip and its relation to Treatment B unresolved `[VI-36]`. |
| C8 | The mockups show the Signal Relay gate, 0 / 5 V, a Lossy link and a place-value bench with mock logic. The curriculum has no concept, term or lab for gates, adders or networking (brief section 1.2). Signal Relay is an application experiment. | Mock semantics are not specified here. Networking stays hypothetical `[VI-63]`. |
| C9 | The mockup teal fills the abstract bit "1" in Place Value. Teal is reserved for "energised/high". A stored bit is not literally energised. | Recorded as an open reading under `[VI-39]`. |
| C10 | The mockups called the relay lab "Signal relay" on the plate and "Remote relay" in the heading. | Resolved by the owner: the Lab is **Signal Relay** `[VI-29]`. "Remote relay" describes only the equipment or outpost context. |
| C11 | The evidence directory `design-stage-5/` is untracked in the application repository. In the knowledge repository, `LE-DECISIONS.md` has uncommitted changes and `LE-DESIGN.md`, `LE-PRODUCT.md` and `LE-FIRST-WORKBENCH-BRIEF.md` are untracked. | I read the working-tree versions. They may differ from what is later committed. |

## 1. Product identity

ELE is a persistent, hands-on engineering environment. The learner builds, connects, manipulates and observes systems, and understands why they behave as they do (LE-006, LE-009). The visual identity has one job: make that experience read as **an engineering laboratory with a bench**, not as a course platform, a dashboard, or a game.

What the product should feel like:

- **Purposeful.** Every element has a stated role: an engineering indicator, a structural convention, or environmental context (principle 6). Nothing is there only to look technical, and nothing implies a measurement, property or state that does not exist.
- **Precise.** Values, units, identifiers and states are exact and legible.
- **Tactile.** Controls look operable. A switch looks like a switch. State is visible on the control itself.
- **Technically credible.** Diagrams look like engineering diagrams. Equipment looks like it was built to do something.
- **Quiet.** The learner's system is the loudest thing on screen.

What it must not be (LE-009, locked `[VI-01]`): an LMS with lessons, percentages, quizzes or locked modules; a generic dashboard that buries engineering work behind cards and navigation; a game with rewards, resource grinding or decorative gamification. It does not rely on intrusive storytelling. Narrative is limited to context a challenge needs, such as the remote outpost in Signal Relay.

**What makes it recognisable.** Hypothesis: a coherent grammar, not industrial decoration. Specifically the pairing of two visual registers (sheet and plate), technical type (mono values, tag identifiers), the Inspector, and the instrument-like bar. The D4 evidence is honest on this point: at one third scale the screens stay close to the D3 baseline, and no single cue survives a stripped screenshot (section 16). Recognisability therefore comes from the combination, applied consistently, and is not yet proven.

## 2. Visual identity principles

Each principle states how it guides a decision.

1. **Industrial Scientific Environment** `[VI-03]` (Provisional). The product borrows from a working lab: instruments, drawings, plates, labels. Test: a proposed element must correspond to something a real instrument, drawing or piece of equipment would carry. If it does not, it needs another reason to exist.
2. **Expose concepts, hide mechanisms** `[VI-05]` (Provisional; see C2). Show the engineering concept, its state and its relationships. Do not show interface machinery (ids with no meaning to the learner, framework structure). Never hide engineering behaviour the learner is trying to understand (LE-010).
3. **Two registers** `[VI-04]` (Provisional). Abstract models and physical equipment look different, and the difference carries meaning (section 3, 4). Test: can a learner tell at a glance whether something is a model of a thing or the thing?
4. **One product.** The registers share type, geometry, state treatment and interaction. Test: removing the Model/Equipment pills, would the two still look like the same product?
5. **State and relationships are legible.** State uses more than one cue. A relationship is shown only where it exists `[VI-10]`, `[VI-42]`.
6. **Every element has a stated role** `[VI-16]` (Locked). Three kinds exist, and an element must be one of them:
   - **Engineering indicator.** Communicates an actual property or state of the system: a value, unit, range, lamp, state glyph, tag or relationship. It must be true. The concept supplies it.
   - **Structural convention.** A restrained, consistent mark that organizes or identifies a model sheet, equipment plate or workbench, for example crop marks, the bar's graduated scale, a frame or a kind pill. It carries no engineering information, serves a compositional or identity purpose, and is applied the same way everywhere. It must never look like a measurement, imply a system property, or imitate state. A scale that could be read as a quantity, a tick that looks like data, or a mark that changes without cause is not allowed. A structural convention is not a licence for arbitrary technical decoration. A new one needs a stated compositional or identity purpose, and it must not be needed for recognition or understanding.
   - **Environmental scenery.** Establishes atmosphere and context (section 7). It never carries state and recedes when it competes with the work.
7. **Environment supports engineering.** Context recedes when it competes with the engineering representation `[VI-19]`.
8. **Practicality and maintainability.** Prefer CSS and small SVG the team can maintain. Count the production burden before adding a visual idea (section 14).

## 3. Abstract model grammar

An abstract model is a diagram of an idea: the structure and values of a concept, with no claim about physical form. Status: the sheet register is Provisional `[VI-06]`. The rule against a universal diagram style is Locked `[VI-07]`.

**Rules (Provisional, except where stated):**

- **Model sheet.** A flat surface with a dashed frame. It reads as a drawing, not an object. No gradient, no screws, no bevel.
- **Kind pill.** A small "Model" pill in the sheet header says what register this is.
- **Lines and symbols.** Thin ink lines. Symbols follow the convention of their discipline (a logic gate drawn as a gate symbol, a message exchange drawn as a sequence diagram). The grammar does not dictate the diagram type `[VI-07]`.
- **Connections and relationships.** A connection carries direction and, where meaningful, its current value. Relationships between parts use a line or a shared identifier. They are never implied by adjacency alone.
- **Values.** Technical values and identifiers are set in monospace. Names and prose are set in sans-serif.
- **Bit patterns.** A bit shows its digit as well as its state, so state does not depend on colour (also LE-FIRST-WORKBENCH-BRIEF 9.3). A cause-and-effect chain, such as Position to Weight to Bit to Contribution to Total, reads in a consistent direction.
- **Framing (from Treatment B)** `[VI-08]`. Model sheets may carry small corner crop marks. They are structural conventions: graphics that carry no information and are not needed for recognition. They may be dropped where they cause clutter. In the 720×480 mockups they are dropped.
- **Identifiers.** A tag such as `U1` is applied to a part only where a second representation of the same part exists `[VI-10]`. A pure model with one representation does not need tags.
- **Selection.** Corner brackets plus a light tint `[VI-12]`. Selection is a mark on the thing, not a colour change of the thing.
- **Range and measurement information.** Shown only when it states a real property of the system, for example the span of a quantity or the time interval of a diagram. It is supplied by the concept, not invented by the interface `[VI-16]`.

**Not specified:** a standard layout for a model sheet, a symbol library, or how a model of a concept not yet explored should look. Place Value and Lossy link show two different diagrams in one grammar. That is the extent of the evidence.

## 4. Physical equipment grammar

Equipment is the thing itself, or a representation of it as an object: solid, operable, measured in units. Status: the plate register is Provisional `[VI-09]`. The two limits below are Locked: do not invent equipment for a concept that has no physical counterpart, and do not turn every panel into a literal metal box `[VI-09a]`.

**Rules (Provisional):**

- **Plates.** Equipment sits on a plate: a gradient surface with a visible edge, and small fixings where an enclosure reads as hardware. A plate is for equipment only. A model sheet, a toolbar or the Inspector is not a plate.
- **Kind pill.** An "Equipment" pill in the header.
- **Controls.** Switches, buttons and knobs look operable and show their state on the control: position, lamp, legend (for example I / 0).
- **Instruments and measurement surfaces.** Readouts show a value with its unit. A measured value is labelled as measured and kept distinct from the model's value for the same part. The Signal Relay mockup shows "Output (model)" beside "Output (measured)".
- **Functional geometry.** Form follows function. A shape suggests what the part does. Detail beyond that is not added.
- **Materials.** Painted metal, dark composite, glass and concrete are the reference vocabulary, used with restraint `[VI-47]` (section 11).
- **Identifiers.** An equipment identifier is a tag chip (`S1`, `U1`, `H1`, `W1`) used only where the equipment relates to a model element `[VI-10]`.
- **State indicators.** Lamps, readouts and cable animation show state from the domain model. The picture does not hold state (section 14).
- **Relationship to the model.** Equipment realises a model. A learner can find the model element behind a piece of equipment and the reverse, where a real relationship exists (section 5).

**Not specified:** an equipment illustration style, a kit of equipment parts, or how a piece of equipment for a future world should look.

## 5. Hybrid representation

A hybrid screen shows a model and equipment together. The only evidence is Signal Relay.

- **Two registers, side by side or stacked.** The model sheet and the equipment plate stay visually distinct, each with its kind pill. They do not merge into one object.
- **Shared identifiers only where a genuine relationship exists** `[VI-10]`. The gate in the equipment view and the gate symbol in the model carry the same tag (`U1`). A part with no counterpart carries none.
- **No artificial one-to-one mapping.** If a model element has no physical counterpart (a node label, a logical level) it appears only in the model. If equipment has no model counterpart (an enclosure, a mount) it appears only in the equipment. Do not draw the missing half to make the screen symmetrical.
- **Selection and cross-highlighting** `[VI-12]`. Selecting a part marks it with brackets and a tint in every view in which it appears. The Inspector then describes it.
- **Inspector.** For a hybrid part the Inspector shows both kinds of information with their kind pills, and labels which value comes from the model and which is measured. It may show a small schematic of the model element ("twin") when equipment is selected, scoped to the selected part.
- **Relationship statements are factual.** Text in the Inspector that says how parts relate comes from the concept. The interface does not make it up.
- **Hybrid is optional.** A concept may have only a model (Place Value, Lossy link). A hybrid screen is not required for every concept `[VI-09a]`. Side-by-side layout is optional. The mockups also show an equipment-first layout where the model is available through a control.

Unresolved: how hybrid representation looks for components the learner built, and for hierarchical inspection (entering a component) `[VI-34]`.

## 6. Workbench composition

Treatment B (D4) is the selected workbench foundation `[VI-13]` (Locked). Its individual mockup details are Provisional unless stated.

**Idea.** The workbench is expressed as an instrument. Identity comes from how surfaces are framed and labelled, not from a scene.

**Elements (Provisional):**

| Element | Rule | Status |
|---|---|---|
| Bar | Flat, instrument-like. Carries the brand, the breadcrumb (Worlds, World, Lab) and the save state. No gradient plate. | `[VI-14]` |
| Graduated scale | A fine ruled scale along the lower edge of the bar. A structural convention: it carries no information and must not be given labels, numbers or any quantity meaning. | `[VI-14]` |
| Model-sheet crop marks | See section 3. A structural convention. | `[VI-08]` |
| Technical framing | Each framed surface has a header: kind pill, title, and, where justified, a readout. | `[VI-06]` |
| Inspector selection chip | The Inspector header shows the selected item's name as a chip, in the same chip material as tags. | `[VI-15]` |
| Footer hint removed | A footer hint must not repeat the Inspector's empty state. Locked. | `[VI-17]` (Locked) |

**Readouts are not mandatory** `[VI-16]` (Locked). The mockups show a range string in every framed panel header (`8 bits · 0 to 255`, `rails 0 / 5 V`, `logic 0 | 1`, `t = 1 to 4`). Those strings illustrate the position and style of a readout. They are not content to reproduce.

- A readout appears only if it states a meaningful property of the represented system.
- The **concept owns the semantics and values**. The **visual system owns the presentation** (position, size, type, colour).
- If a panel has no meaningful property to state, its header has no readout. An empty slot is not filled for appearance.
- A wrong or stale readout is worse than none. Whoever adds a readout is responsible for its truth.

**Hierarchy.** From most to least prominent: the engineering representation; the state it shows and the selection; the Inspector; panel headers and readouts; workbench context (bar, crumbs, tool row). Context uses smaller, quieter type and less contrast than the representation. The bar and framing must not compete with the representation.

**How identity survives without environmental illustration.** It rests on the register pair, technical type, tags, the Inspector, the instrument bar and consistent framing. Two structural conventions of Treatment B (the bar scale and crop marks) carry no engineering information, which is why they must never be read as measurements. If they were removed the workbench would still work, and, per the D4 removal test, it would look close to D3. The identity therefore depends on grammar more than on these two marks.

**Not specified:** the arrangement of Library and Investigation regions, whether the facts strip (LE-FIRST-WORKBENCH-BRIEF D5a) sits inside the tool row, and the relation of a "tool row" to LE-DESIGN's regions `[VI-33]`, `[VI-36]`.

## 7. Facility and environmental identity

ELE is a persistent facility. The learner returns to it. The facility supports identity at the level of Worlds and Labs. It does not carry the workbench.

**Facility (Provisional `[VI-18]`).** A hall of the engineering facility is the Worlds-level setting. Its architecture and material references are concrete, steel, painted metal and glass, under practical light. Each World can be represented in the hall by a bay or similar marker. The mockups show the Worlds screen as a hall with bay faces. The hall does not depend on any one World's equipment, cables or window. The hypothetical Networking world reused the hall with only a different bay face.

**Relationship of World, Lab and Bench.** This follows LE-005 and does not add terms.
- A **World** is an engineering domain.
- A **Lab** is the learner's persistent environment in a World.
- The **Bench** is the surface the learner works on.
- The Worlds screen helps the learner enter a World and open a Lab. How lab selection works when a World has several labs, and how the Worlds screen looks, remain open `[VI-23]`.

**Contextual environment (Provisional `[VI-21]`).** A challenge may add its own context. Signal Relay adds a remote outpost window that shows the consequence of the circuit state. Such context belongs to the challenge. It is not a product-wide device.

**Treatment A (Locked limits).** Treatment A, the "bay from inside" with wall gutters and a floor band, is **not** the global workbench treatment `[VI-19]`. Its floor treatment may be used as contextual scenery in a physical environment where it fits `[VI-20]`. It must not become a mandatory element on every workbench.

**Receding.** Environmental context gives way when it competes with the engineering work:
- It takes no workspace from the model or equipment.
- It is outside the primary representation.
- It is reduced or removed at small sizes.
- It never carries state.

**Low-contrast wall and floor tokens (Locked `[VI-22]`).** The D3 wall and floor tokens sit very close to the ground. The computed contrast with the ground is 1.13:1 and 1.18:1 for the wall (Night shift, Day shift), and 1.32:1 and 1.86:1 for the floor. Nothing identity-critical may depend on them. Anything that must be seen needs a stronger edge or a different treatment, which is not specified here.

**Not specified:** facility architecture drawings, per-World environment art, how an environment changes between challenges beyond the Signal Relay outpost example `[VI-23]`.

## 8. Lab identity and bay plate

Two kinds of label serve two different purposes. Keep them apart.

| | **Lab identity label** | **Engineering-element tag chip** |
|---|---|---|
| Names | A Lab (the learner's persistent environment) | A part inside a system (`S1`, `U1`, `H1`) |
| Purpose | Say which Lab this is, where that is not already clear | Link two representations of the same part |
| Appears | Breadcrumb or similar identity position, only when useful | On the part, in each view where it exists, and in the Inspector |
| Source of the text | The Lab (the learner may name it, LE-018) | The engineering model |
| Must not be | Styled as a part tag | Used for anything that is not a real part relationship |

Decisions (Locked unless stated):

- A Lab name may be shown where it helps tell Labs apart or identifies a user-named Lab `[VI-24]`. Labs may share a name (LE-018), so the interface cannot rely on the name alone to distinguish them.
- A **bay plate is optional**, not mandatory `[VI-25]`.
- A **bay number alone is weak metadata** and is not a permanent identity element `[VI-25]`.
- Do not duplicate a Lab name that is already visible (for example as both a plate and a heading) `[VI-24]`.
- A Lab identity label and a tag chip must look different `[VI-26]`. How they differ is Unresolved `[VI-27]`. In the mockups both use the same chip material (the plate's number is inverted); whether learners confuse them was not tested.

D4 evidence behind this (Observation, one reviewer, mockups): the lab name told labs apart on Place Value, where nothing else named the Lab. The number added little. On Signal Relay the plate and the heading both carried a name. The plate said nothing about activity, system or physical location, and claiming any of those would invent metadata.

Whether the word "bay" is shown to learners is Unresolved `[VI-28]`, because LE-005 sets the vocabulary. The relay Lab is named **Signal Relay** (Locked `[VI-29]`). "Remote relay" is used only for the equipment or outpost context, never as a Lab name. A rule for when a Lab shows a label (for example "where the Lab has no heading of its own") is a Hypothesis, not a decision.

## 9. Information hierarchy and Inspector

**Layers** (LE-009, LE-010, LE-DESIGN). From always visible to on demand:

| Layer | What the learner sees |
|---|---|
| Always (nothing selected) | Component identities, connection direction, inputs and outputs, compact live values, current state `[VI-30]` |
| On selection | The Inspector shows details of the selected object `[VI-30]` |
| By entering | A component's internals, level by level (LE-010; visual form not designed) `[VI-34]` |
| On demand | Probes and overlays (LE-010; visual form not designed) `[VI-34]` |

**Inspector rules.**
- It is contextual to the selected object, not a generic properties list (LE-010) `[VI-30]`.
- It provides one consistent way to inspect, and it does not hide the primary representation `[VI-31]` (Locked).
- Provisional guidance from D3 `[VI-32]`:
  - It has a permanent header: title, selected item name, and a Hide/Show control that announces its open state (`aria-expanded`, `aria-controls` in the mockup).
  - Selection never changes whether the Inspector is open.
  - Placements: right column in equipment-first at 1100×720; bottom drawer in linked mode; collapsed handle when hidden.
  - When collapsed, the header bar and its Show control stay visible so the learner can find it.
  - The surface scrolls rather than shrinking technical text.
- The Inspector shows identifiers and relationships for the selected item, with kind pills where both registers appear.

**Technical readouts and identifiers.** Readouts follow section 6. Identifiers follow section 8. System state follows section 10.

**Known constraint.** In Signal Relay at 720×480 with the Inspector open, about 130 px of surface remains for the linked representation. The surface scrolls. This is a **known limitation**, not evidence that the layout is ideal `[VI-54]`.

## 10. Colour and themes

Both dark ("Night shift") and light ("Day shift") are in scope `[VI-37]` (Locked). No primary theme is chosen, and the mechanism for choosing one is open `[VI-38]`. A change to either theme's palette is outside this document.

**Established rules (carry meaning, do not depend on a hex value):**

| State or use | Rule | Status |
|---|---|---|
| Energised / high | Teal. Reserved for this meaning. | Provisional `[VI-39]` |
| Inactive / low | Neutral, with a distinct form. | Provisional `[VI-42]` |
| Selected | Brackets plus tint, in the neutral/ink family | Provisional `[VI-12]` |
| Search-path membership | **Never teal.** Structural and ink-based (double outline, double-rail edges, numbered step badges in the D3 mockup). | Never teal: Locked `[VI-40]`. The specific marks: Provisional `[VI-41]` |
| Success | A check mark and a sentence | Provisional `[VI-42]` |
| Warning | A warning triangle and text | Provisional `[VI-42]` |
| Fault | A boxed cross and text | Provisional `[VI-42]` |
| Unknown | A dashed form and a question mark | Provisional `[VI-42]` |

- **No state is carried by colour alone** `[VI-42]`. Every state has a second cue: a glyph, a weight, a fill or a dash.
- **Meaning stays the same across themes.** A state uses the same cues in both themes. Tone adapts.
- The Place Value bit "1" uses teal in the mockup. Whether a stored abstract bit should read as "high" in the same colour as an energised wire is open (C9).
- **Environmental colours, model and equipment surfaces.** The three groups are visually distinct: the facility (concrete, painted metal, glass), the sheet (a flat, light-on-dark or dark-on-light drawing surface), and the plate (a darker, graduated equipment surface). The specific values are Provisional `[VI-43]`.
- **Palette values are not locked.** D3 added two tokens (a muted-text token for plates and a lighter light-theme recess) to raise plate text contrast. These, and every other mockup hex value, are Provisional. Do not copy them into a permanent requirement.
- **Contrast.** The D3 and D4 checks are token-level calculations of WCAG relative luminance. They are not an audit (section 16). Target 4.5:1 for text and 3:1 for graphics. All computed pairs met the target in the final mockups. Graphics such as crop marks and scale ticks are not scored as text.
- **Colour-vision.** Greyscale and a simulated deuteranopia view were made as approximations. They are not a validated simulator. **No claim of colour-blind safety is made** `[VI-44]`.

## 11. Typography, geometry and materials

Direction (Provisional). No font, shader, texture or numeric token is locked `[VI-46]`.

- **Typography.** A legible sans-serif for prose and interface text `[VI-45]`. A technical monospace for values and identifiers where it helps (digits that must align, tags, readouts). Technical text is not shrunk to fit a layout. The mockups use fallback system fonts. The named font candidates in earlier boards were never bundled or checked.
- **Geometry.** Functional forms: rectangles, straight lines, circles for lamps and terminals. Small radii. Shapes explain function.
- **Materials.** Painted metal, dark composite, glass and concrete are references, not shaders `[VI-47]`. Surface detail is restrained (a screw, an edge highlight, a sheen on glass). Lighting is practical: a lamp, a lit readout, a glow where state calls for it.
- **Restraint.** If a surface treatment does not say what the object is or does, leave it out.

## 12. Motion and interaction

Principles (Provisional `[VI-48]`; the owner direction is in LE-FIRST-WORKBENCH-BRIEF section 11a, not in LE-DECISIONS):

- **State-driven.** Motion shows a change in the system: a switch moves, a lamp lights, a signal flows. Motion that communicates no system consequence is not used.
- **Meaningful transitions.** A transition helps the learner see what changed. It is brief.
- **Selection and relationship feedback.** Selecting an item gives immediate feedback in every view that shows it.
- **Physical-feeling interactions.** Controls respond like physical controls (a switch has two positions and settles) where that matches the equipment. A model control may be more abstract.
- **Reduced motion is respected.**
- **No rewards.** No animations that celebrate, score or grade (LE-009).

Implementation details are not specified. The mockups use a short snap timing, which is a mock value, not a rule `[VI-49]`.

## 13. Responsive behaviour

- **720×480 is the minimum supported window** `[VI-50]` (Locked, LE-021). Below it, behaviour is not defined.
- **1100×720** is the reference layout used in the exploration `[VI-51]` (Provisional).
- **No other breakpoints are defined.** Do not infer any.

Provisional guidance from D3 and D4:
- Linked representations remain available at 720×480. Stacking and scrolling are acceptable when needed. The representation stays usable `[VI-52]`.
- Technical text keeps its size. The surface scrolls instead `[VI-53]`.
- The Inspector stays discoverable at both sizes. Collapsed, it shows a header bar with a Show control. It starts collapsed at 720×480 in the mockups `[VI-32]`.
- The main representation stays visible. Measured in D4, Treatment B used 100% of the D3 baseline panel area in every measured state.
- Environmental context shrinks or disappears first.

**What is not guaranteed.** The behaviour above was validated only on the three sample screens (and, in D3, a search tree and an adder), in two themes at two sizes, by script and by looking at screenshots. It was not validated on real hardware, at other sizes, or with the real application's content. The 130 px limit in section 9 applies. The Adder tag text renders at 7.8 px, below the 9 px floor of the other screens, and was not fixed `[VI-55]`.

## 14. Asset production strategy

**One visual identity, several production techniques.** Art creates the world. Authored graphics communicate the system.

| Asset | Technique | Status |
|---|---|---|
| Interactive engineering symbols, state-driven circuits and diagrams | Custom SVG, driven by domain state | Provisional `[VI-56]` |
| Instrument faces, interface illustrations | SVG and CSS | Provisional `[VI-56]` |
| Equipment illustrations | Custom authored; static art with state overlays | Provisional `[VI-56]` |
| Environmental backgrounds | Original or generated artwork, where appropriate | Provisional `[VI-56]` |
| Textures | Procedural, or properly licensed | Provisional `[VI-56]` |
| External assets | Selective, only if they fit the established identity | Provisional `[VI-56]` |
| Blender or reusable 3D scenes | Only when complexity justifies the burden | Provisional `[VI-56]` |
| Interface icons | Not decided (the earlier boards mentioned an icon set by name only) | Unresolved |

**Rules.**
- **State is never in an image.** Lit, faulted, selected and in-range come from the domain model through SVG or CSS. Images set atmosphere only `[VI-57]`.
- The identity does not depend on an unbounded supply of generated images `[VI-58]`.
- Generated artwork needs a locked palette, horizon and light rule before use. None has been produced or evaluated in this exploration.

**Choosing a technique (criteria, Provisional).**
1. Does it carry system state or respond to input? Use SVG or CSS.
2. Does it explain a concept? Author it. Do not use generated or stock imagery.
3. Is it atmosphere only, outside the representation? Art is allowed.
4. How many variants will it need over time? A high count favours parametric SVG or CSS over bespoke art.
5. Can the identity survive its removal? If not, it is carrying too much.
6. Is the production cost proportionate? Choose the cheapest technique that does the job. Add Blender or 3D only if two-dimensional authoring cannot do it.
7. Is it licensed, and does it match the grammar?

Numeric thresholds for these criteria are not set `[VI-59]`.

D4 estimate (Hypothesis): Treatment B is CSS-only and needs a content owner for readouts. The A-style floor costs a footer strip and placement rules for each workbench. No generated art, external assets or dependencies were used in D3 or D4.

## 15. Implementation guidance

This guides future work. It does not authorize changes to the application.

- **Semantics belong to the domain.** Engineering properties, values, ranges, relationships and behaviour come from the pure TypeScript domain layer (LE-001) or the curriculum. The presentation layer shows them. The interface must not invent a property, value, range or behaviour `[VI-60]` (Locked).
- **Presentation belongs to the design system.** A component decides how a readout, tag, pill or panel looks. It does not decide what is true.
- **Reusable components only where a visual or interaction responsibility is demonstrably shared.** The demonstrated candidates are: kind pill, tag chip, Inspector shell, model sheet frame, equipment plate, state glyph set. Do not design a universal component framework in advance `[VI-61]`.
- **Mock logic is not the application's logic.** The mockup relay lamp, messages and place-value totals are illustrative and must not be copied as behaviour.
- **Check the identity against real content.** The mockups use mock content. The first real workbench (LE-FIRST-WORKBENCH-BRIEF) is the test of the grammar.
- **Practical accessibility stays in scope.** Practical keyboard operation, visible focus, readable text, contrast and responsive behaviour remain in scope for implementation. Keyboard operation of the visual construction surface is unresolved `[VI-62]`. This specification does not require screen-reader or assistive-technology testing, and none was performed.
- **Keep the specification current.** If implementation shows a Provisional rule is wrong, change its status and record why.

## 16. Validation and known limitations

### 16.1 Where the evidence lives
`apps/desktop/design-stage-5/` in the application repository: pages `a-…`, `b-…`, `c-…`, `d-…`, `d2-…`, `d3-validation-…`, `d4-workbench-identity.html`; sources in `tools/`; measurements in `tools/d3-validation.json` and `tools/d4-validation.json`; judgement text in `tools/d4-judgement.json`. This directory is untracked (C11).

### 16.2 What was done

| Kind | D3 | D4 |
|---|---|---|
| **Scripted measurement** (headless Firefox 160, exact viewports, per-screen script) | 49 screen states and 3 stability runs: no clipped containers, no text overlaps, Inspector body fits, toggle always visible. Smallest text 9 px on changed screens; the Adder 7.8 px. | 60 screen states (D3 baseline, A and B; two themes; 1100×720 and 720×480) and 9 stability runs: no clipping, no overlaps, no text below 9 px. Visible panel area: A 95 to 100% of D3, B 100%. Select-shift 0 px in all. |
| **Manually inspected screens** (viewed by me as screenshots) | Most Night shift screens and a subset of Day shift. Listed on the page and in `tools/d3-looked.txt`. | Most Night shift screens, the three-way side-by-sides, the removal tests, plate variants; a few Day shift. Listed in the validation section and `tools/d4-looked.txt`. |
| **Synthetic keyboard checks** (synthetic events in headless Firefox) | 25 passed, 0 failed. | 22 passed, 0 failed, no new controls to test. |
| **Token contrast calculation** (WCAG luminance from token hex) | D2 failures found and fixed. Plate pairs 4.84 to 6.68 after the fix. | All added pairs meet target in both themes. |
| **Approximate colour-vision images** | Greyscale and deuteranopia approximation. | Not repeated. |
| **Uninspected states** | The script measured states I did not view. Examples: Networking in Day shift and several 720×480 Day shift states. | Treatment A in Day shift at full size, B at 720×480, Lossy link at full size, all D3 reference screens. |

All of these were run at 1100×720 and 720×480 only. The page records the full matrix.

### 16.3 What was not done
- **No formal accessibility audit.** Contrast is a token calculation. Composited states (a tint over a plate) were not measured.
- **No screen-reader or assistive-technology testing was performed.** This specification does not require it.
- **The keyboard checks are synthetic.** They are not real keystrokes. They do not test Tab order or visible focus. In headless Firefox the document has no focus, so one focus-retention check was skipped.
- **No user testing.** The evidence is mockups and one reviewer (the author of the mockups).
- **No low-DPI, long-session or learner testing.**
- **No comparison against the real application's styles.** The mockups are separate from the application.
- **Hypotheses not tested:** that the register pair is what makes ELE recognisable; that learners will not confuse a lab label with a tag chip; that a lab label should show only where a Lab has no heading of its own.

### 16.4 Findings that qualify the evidence
- At one third scale the D4 treatments looked close to D3. The workbench identity is modest. The D4 removal test found the bar scale and crop marks carry no information.
- The D3 wall and floor tokens are too close to the ground to carry identity (section 7).
- Signal Relay linked at 720×480 leaves about 130 px (section 9).
- The Networking world and the Lossy link are a **hypothetical design probe**, not curriculum and not validated. The same holds for the search tree and the adder, which are D2 samples. Nothing there shows that the curriculum will include them `[VI-63]`.

## 17. Decision register

Statuses: **L** Locked, **P** Provisional, **U** Unresolved. "Changes if" says what evidence would reopen the row. A Locked row can change only by owner decision.

| ID | Decision | Status | Evidence or rationale | Changes if |
|---|---|---|---|---|
| VI-01 | ELE reads as an engineering lab. It is not an LMS, a generic dashboard, or a game. No rewards or decorative gamification. | L | LE-009 | Owner changes LE-009 |
| VI-02 | Default density is high and layered. The bench is primary and takes most of the screen. | L | LE-009, LE-011 | Owner changes them |
| VI-03 | Direction D, Industrial Scientific Environment, is the foundation of the visual grammar and components. | P | Task statement for D4; D, D2, D3 mockups | Implementation shows the grammar fails on real content |
| VI-04 | Abstract models and physical equipment are two visual registers, coherent in one product. | P | D to D3 mockups; D3 judgement | A real concept fits neither register |
| VI-05 | Principle "Expose concepts, hide mechanisms", read as: show the engineering concept, not interface machinery. | P | Exploration brief; reading is my interpretation (C2) | Owner words it differently |
| VI-06 | A model is a flat sheet with a dashed frame, thin ink lines, mono values, and a Model pill. | P | D3 mockups | Real models need another form |
| VI-07 | There is no universal diagram style for all abstract concepts. | L | Commissioning task | Owner decides otherwise |
| VI-08 | Model sheets may carry corner crop marks as a structural convention. They carry no information and are not needed for recognition. | P | D4 Treatment B; removal test | Clutter in real use, or owner drops them |
| VI-09 | Equipment is a plate with solid forms, operable controls, lamps and measured units. | P | D3 mockups | Equipment for another world needs another form |
| VI-09a | No invented equipment for concepts with no physical counterpart. Not every panel is a metal box. | L | Commissioning task | Owner decides otherwise |
| VI-10 | Shared identifiers (tags) appear only where two representations of the same part exist. | P | D3 foundation | A real case needs another rule |
| VI-11 | In a hybrid screen, Model and Equipment pills distinguish the two registers. | P | D3 mockups | Pills prove noisy or unnecessary |
| VI-12 | Selection is corner brackets plus a tint, applied in every view of the selected part. | P | D3 foundation; D3 fix of relay selection | Selection proves unclear in use |
| VI-13 | Treatment B is the workbench foundation. | L | Commissioning task (product-owner selection after D4) | Owner decides otherwise |
| VI-14 | The bar is flat and instrument-like, with a graduated scale along its lower edge. The scale is a structural convention that implies no quantity. | P | D4 Treatment B | Scale distracts or adds cost |
| VI-15 | The Inspector header shows the selected name as a chip. | P | D4 Treatment B | Confusion with tags or Lab labels |
| VI-16 | Every element has one stated role: engineering indicator, structural convention or environmental scenery. Structural conventions are restrained, consistent and never imply measurements, properties or state. A technical readout appears only for a meaningful property. The concept owns its semantics and values. The visual system owns presentation. No readout on every panel. | L | Commissioning task | Owner decides otherwise |
| VI-17 | A footer hint must not repeat the Inspector's empty state, so the redundant hint is removed. | L | D4 finding; owner approval of the removal | Owner decides otherwise |
| VI-18 | The persistent facility (hall, bays) is the Worlds-level identity. | P | D to D3 mockups | Worlds screen design finds another form |
| VI-19 | The workbench stays recognisable without environmental scenery. Treatment A is not the global workbench treatment. | L | Commissioning task | Owner decides otherwise |
| VI-20 | A floor treatment may be used as contextual scenery in a suitable physical environment. It is never mandatory. | L | Commissioning task | Owner decides otherwise |
| VI-21 | Challenge-specific environments are contextual, not a product-wide device. | P | D3 foundation | A challenge needs a permanent device |
| VI-22 | The D3 wall and floor tokens are not identity-critical. | L | Commissioning task; computed contrast 1.13 to 1.86:1 | Owner approves a stronger palette |
| VI-23 | Facility architecture, per-World environment art, Worlds-screen layout, lab choice among several labs. | U | LE-DESIGN open questions; LE-011 | A Worlds-screen design and a lab-selection decision |
| VI-24 | A Lab name may appear where it distinguishes Labs or names a user-named Lab. It is not duplicated unnecessarily. | L | Commissioning task; LE-018 | Owner decides otherwise |
| VI-25 | A bay plate is optional. A bay number alone is not a permanent identity element. | L | Commissioning task; D4 plate test | Owner decides otherwise |
| VI-26 | A Lab identity label must look different from an engineering-element tag chip. | L | Commissioning task | Owner decides otherwise |
| VI-27 | The visual form that separates Lab labels from tag chips. | U | D4 mockup uses the same chip material; confusion untested | A test with real use |
| VI-28 | Whether "bay" is shown to learners. | U | LE-005 vocabulary; brief tripwire 7 (C3) | Owner decides vocabulary |
| VI-29 | The relay Lab is named Signal Relay. "Remote relay" describes only the equipment or outpost context. | L | Owner selection after review of the D4 finding (C10) | Owner decides otherwise |
| VI-30 | Selection inspection with a contextual Inspector is the default. With nothing selected, structure and state stay visible. | L | LE-010 | Owner changes LE-010 |
| VI-31 | The Inspector is a consistent mechanism and does not hide the primary representation. | L | Commissioning task; LE-011 | Owner decides otherwise |
| VI-32 | Inspector placements: right column (equipment-first, 1100), bottom drawer (linked), collapsed handle; permanent header with Hide/Show; selection never changes open state. | P | D3 validation (0 flagged rows; shift 0 on select in linked mode) | Real content or a larger region design needs another placement |
| VI-33 | The arrangement of Library, Bench, Inspector and Investigation regions. | U | LE-011 "not decided"; LE-DESIGN recommendation | Owner decides the arrangement |
| VI-34 | Visual treatment of Library, Investigation, probes, overlays, and entering a component. | U | LE-010 not included; never designed | A design pass for them |
| VI-35 | How a supplied example is shown as distinct from built work. | U | LE-DESIGN open question | A design pass |
| VI-36 | The relation of the facts strip (World, Lab, Created, ID) to the Treatment B bar and tool row. | U | Brief D5a; no mockup shows it (C7) | First workbench layout work |
| VI-37 | Dark and light themes are both in scope. | L | Commissioning task | Owner decides otherwise |
| VI-38 | Primary theme, and how the theme is chosen. | U | LE-DESIGN recommends system setting; task says no primary theme | Owner decision |
| VI-39 | Teal is reserved for energised/high. Whether an abstract bit "1" uses it is open. | P | D3; C9 | Teal proves ambiguous in real use |
| VI-40 | Search-path membership is never teal. It uses a structural, ink-based treatment. | L | Commissioning task | Owner decides otherwise |
| VI-41 | The specific search-path marks: double outline, double-rail edges, numbered badges. | P | D3 mockup on a hypothetical tree | A real search concept needs another form |
| VI-42 | State always has a non-colour cue. Success, warning, fault and unknown use a glyph and text. Meanings match across themes. | P | LE-DESIGN recommendation; D3 state sheet | A state needs another cue |
| VI-43 | Palette values and tokens (including the two D3 additions) are provisional, not requirements. | P | D3 contrast table | Owner approves a palette |
| VI-44 | No claim of colour-blind safety or of an accessibility audit. | L | Commissioning task | A real audit is done |
| VI-45 | Sans-serif for prose and interface text. Mono for values and identifiers where useful. | P | D to D3 mockups | Real content finds a problem |
| VI-46 | Specific fonts, shaders, textures and numeric design tokens. | U | Not supported by the sources | A type and token pass |
| VI-47 | Material references: painted metal, dark composite, glass, concrete, used with restraint. | P | D, D2 | A material proves unworkable |
| VI-48 | Motion is state-driven and meaningful. No motion without a system consequence. Reduced motion respected. | P | Brief section 11a (owner direction, not in LE-DECISIONS) | Owner records or changes it |
| VI-49 | Timing values (mock snap timing). | U | Mock value only | An implementation timing pass |
| VI-50 | The minimum window is 720×480. | L | LE-021 | Owner changes LE-021 |
| VI-51 | 1100×720 is the reference layout in this exploration. | P | Task statement; used in all validation | Owner names another reference |
| VI-52 | Linked representations stay available at 720×480. Stacking and scrolling are acceptable. | P | Task statement; D3, D4 validation | Real content makes it unusable |
| VI-53 | Technical text is not shrunk to fit. | P | D3 rule | A layout needs it |
| VI-54 | Signal Relay linked at 720×480 with the Inspector open leaves about 130 px of surface. Known limitation. Not a decision that this is acceptable. | U | D3 validation | A decision on acceptable minimum surface |
| VI-55 | The Adder renders tag text at 7.8 px. Known limitation, not fixed. | U | D3 validation | A fix or an exception is decided |
| VI-56 | Production techniques: SVG for interactive symbols and circuits; SVG and CSS for instrument faces; authored equipment illustrations; art for environments; procedural or licensed textures; selective external assets; Blender only when justified. | P | Task statement; index of earlier boards | A technique fails on real work |
| VI-57 | State is never carried by an image. | P | Earlier boards' rule; consistent with LE-001 | A counterexample |
| VI-58 | The identity does not depend on an unbounded supply of generated images. | P | Task statement | Owner decides on a generated-art policy |
| VI-59 | Numeric thresholds for choosing an asset technique. | U | Not supported by the sources | Production experience |
| VI-60 | Engineering semantics come from the domain or curriculum. The interface does not invent them. | L | LE-001, LE-002; commissioning task | Owner decides otherwise |
| VI-61 | Reusable components only where a visual or interaction responsibility is demonstrably shared. No speculative framework. | P | Task statement; LE-PLAN non-goal on frameworks | Real shared use shows a different need |
| VI-62 | Keyboard operation model of the construction surface (focus order, selection and activation by keyboard). Screen-reader and assistive-technology work is outside this specification. | U | LE-DESIGN Unknown (keyboard part); synthetic keyboard checks only | A keyboard-interaction design for the construction surface |
| VI-63 | Networking and Lossy link remain hypothetical. They are not curriculum and not validated. | L | Commissioning task; curriculum gap | Curriculum content exists and is reviewed |

**Counts.** Locked 22, Provisional 28, Unresolved 14, total 64. Counts are by register row, where VI-09a is its own row.

## 18. Review against the brief's checks

1. One coherent identity: yes, as a grammar (sections 1, 2). Recognisability is a hypothesis.
2. Models and equipment distinguished: sections 3, 4.
3. Hybrids explained: section 5.
4. Treatment B adopted without all mockup details: section 6 keeps B's elements as Provisional and drops the per-panel range requirement.
5. Facility preserved, decoration not mandatory: section 7.
6. Lab identity separated from element identity: section 8.
7. Decorative readouts prevented: sections 3, 6 and `[VI-16]`.
8. Both themes: section 10 and `[VI-37]`.
9. Locked, provisional, unresolved separated: section 17.
10. A future designer can use it without reopening the exploration: the register states what is decided and what needs evidence. It does not reproduce mockup tokens.
