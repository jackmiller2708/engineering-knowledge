---
id: P2-CONS-01
title: Idempotent step effects and delivery guarantees
phase: 2
requires: [P2-IDEM-01, P2-REC-01]
mastery: L5
---

# P2-CONS-01 — Idempotent step effects and delivery guarantees

## Objective
Make a step's effect on an outside system safe to repeat, show it by experiment, and state exactly what the engine does and does not guarantee.

## Problem
The engine runs steps at least once. Recovery, retries and expired ownership all re-run a handler. If the handler sends an email or creates a payment, a re-run repeats it. Request idempotency (`P2-IDEM-01`) does not help here: it protects the API call that creates a workflow, with a key chosen by the client. A step effect needs its own identity, chosen by the engine, and the outside system must cooperate. When it cannot, the engine must say so instead of promising more.

## Prerequisites
`P2-IDEM-01`, `P2-REC-01`.
Uses: recovery and persisted attempts (P2-REC-01); the idea of a stored key with a stored outcome (P2-IDEM-01).

## Techniques
Effect identity; idempotency key sent to an outside system; a fake outside service with fault injection; telling "effect did not happen" from "effect happened but the engine does not know"; a per-step policy for outside systems without idempotency.

## What you need first
Four statements, to be tested rather than trusted:
- **G1.** A handler may run more than once for the same step.
- **G2.** At most one successful result is committed per step.
- **G3.** A worker that lost ownership cannot commit (enforced later, `P3-FENCE-01`).
- **G4.** If the outside system honors the idempotency contract, repeated attempts produce one effect.

The contract: the same key always returns the same outcome and never causes a second effect, and the system remembers a key at least as long as the longest possible retry period. If the engine calls the outside system, the call succeeds, and the engine crashes before saving the result, the engine cannot know whether the effect happened. Only the outside system can answer that, and it can only do so through the key.

## Practical challenge
Build a small fake outside service (a "ledger" that records effects) with two modes: it honors idempotency keys, or it ignores them. It can fail before the effect, after the effect but before replying, or after replying. Add an effect call to a step. Then run these experiments and record each:

1. **Identity:** derive the effect key from workflow instance, step and effect name, not from the attempt number. Show the key is identical across attempts of one step and different across steps.
2. **Crash window:** crash the engine after the ledger recorded the effect and before the step result was committed. Restart. With the key-honoring ledger, count effects.
3. **Same crash, ledger ignores keys:** count effects. Observe the duplicate.
4. **Outside system without idempotency:** implement a step policy with two options. *Retry* (accepts possible duplicates). *No retry after an ambiguous failure*: the step ends failed with reason `outcome_unknown`, visible through the API, for a person to reconcile (accepts possible missing effects). Run experiment 3 under both.
5. **Key retention:** make the ledger forget keys sooner than the retry period. Show the duplicate and write the retention rule it breaks.

## Deliverable
Effect support in PRJ-ENGINE, the fake ledger and the five experiments as automated tests, and `project/design/delivery-guarantees.md` stating G1–G4 as demonstrated, what is not guaranteed, and the policy choice. Evidence bundle.

## Acceptance criteria
1. The effect key is deterministic and unchanged across attempts of the same step, and differs between steps (test).
2. Experiment 2: the handler runs at least twice, the ledger holds exactly one effect, and exactly one successful result is committed.
3. Experiment 3: the ledger holds two effects, and the design document records this as the expected result for an outside system that ignores keys.
4. Experiment 4, policy *no retry after an ambiguous failure*, against a ledger that ignores keys. An attempt is *ambiguous* when the engine cannot tell whether the call took effect: an attempt that started and has no recorded outcome after a restart, or a call that ended without a reply (timeout, lost connection). This unlock assumes one engine process, so after a restart every started attempt without an outcome counts as ambiguous; deciding that while other workers are running is the ownership problem of `P3-LEASE-01`. The tests show all of the following:
   a. **Durable attempt start.** The engine commits an attempt-start record to its database before it makes the external call. At the moment the ledger receives a call, a separate database connection already sees that committed record (test).
   b. **Crash after the attempt start, before the call.** Inject a crash there. After restart the step is failed with reason `outcome_unknown`, the ledger holds no effect, and no call is made.
   c. **Crash after the call succeeded, before the result is committed.** Inject a crash there. After restart the step is failed with reason `outcome_unknown`, the ledger holds exactly the one original effect, and no second call is made.
   d. **No crash, no reply.** A call that times out after the ledger recorded the effect ends the same way as (c).
   e. **Same restart state.** After restart, (b) and (c) leave identical engine records: an attempt that started and has no outcome. The design document says so.
   f. **No false claim.** In (b) to (d) the step is never committed as succeeded. The API, the history and the design document describe the outcome only as `outcome_unknown` together with the attempt history, and none of them says the effect happened or did not happen. The design document states that, with an outside system that offers neither idempotency nor a way to look the effect up, the engine cannot determine whether the effect happened, and that this policy accepts reporting an effect that was never attempted (b) as unknown.
   g. **Contrast with *retry*.** With policy *retry* and the same ledger, (b) ends with exactly one effect and (c) ends with two, the duplicate of experiment 3.
5. Experiment 5 reproduces a duplicate and the design document states the required retention rule.
6. The design document makes no claim of exactly-once execution, and says plainly that a stale or crashed worker's handler may still run.

## Verification
Run the five tests from the evidence bundle. Oral: "Why can the engine not tell whether the effect happened?"; "Why is the key derived from the step, not the attempt?"; "An outside API has no idempotency support. What do you tell its users, and what does each policy cost?"; "How is this key different from the request key in `P2-IDEM-01`?"

## Mastery target
L5.

## Next unlocks
- P2-INT-01 — the durability demonstration needs this effect behavior.
- P3-TST-01 — chaos tests with several workers must also check effects, not only commits.
- P5-AI-01 — an AI call is an outside effect with an unreliable result, and needs the same treatment.
- P3-DLV-01 — optional: write up the multi-worker version of these guarantees.
