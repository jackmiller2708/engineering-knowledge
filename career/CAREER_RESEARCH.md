# Career Research — Vietnam

Owner: learner approves conclusions; Claude records evidence. Single source for market evidence. Nothing elsewhere in the repository may state a market fact that is not here.

**Status: PRELIMINARY. Low confidence.** Collected 2026-11-16 from web-search result summaries only. The posting pages themselves could not be opened (the session network could not reach `itviec.com`, `topdev.vn` and similar hosts), so no posting was read in full, no posting date was verified, and some postings may be expired. `P0-CAR-01` is the learner's own, deeper pass and replaces this file's conclusions.

Format rule: **Observation** = what a source says. **Interpretation** = my reading, labelled, may be wrong. **Unknown** = not found.

## Method and limits

- Searches (standard mode) for: Go backend roles, platform/DevOps roles, SRE roles, data-intensive Go roles, distributed-systems/orchestration roles, salary reports.
- Roughly 25–30 distinct postings surfaced across 6 searches. Counts below are "mentioned in the search summary", not counts from full reads.
- Search summaries are model-written and truncated; they can omit or compress requirements. Treat each as a pointer, not a record.
- Selection is not random: results favor postings that match my search words. Do not read counts as market share.
- Salary: only survey/recruiter figures were seen, and only through summaries.

## Direction A — Backend engineering (Go, data-intensive services)

**Observations** (source: ITviec and TopDev listings surfaced by search; check each page):
- Senior Go roles state years explicitly: Rikkeisoft (5+ years backend, 3+ Go), Vision Advisory & Analytics (5+ backend, 3+ Go), GFT Technologies (min 4 years Go, good English), Ban Vien (3+ years Go), Silver Tiger (2–5 years Go), Masan Group (3–5+), DatVietVAC principal (5+), Glints (6+), NexLab (5 years in one posting).
- Recurring skills: REST/GraphQL APIs, microservices, SQL databases (MySQL, PostgreSQL), Docker, AWS/GCP.
- Kafka appeared in 4 summaries (GFT with Redis and PostgreSQL; Grab with CDC, Spark, Temporal and Saga patterns; NexLab twice, with Redis, Kubernetes, AWS). Redis appeared with Kafka.
- Distributed systems named as a requirement in: Masan Group (microservices and distributed systems), DatVietVAC (distributed systems, event-driven architecture), Vinrobotics (reliable backend distributed systems for large-scale AI).
- Other languages paired with Go: Python, Java, C#.
- ClickHouse: no posting found. **Unknown** whether Go + analytical stores is a Vietnamese market pattern.

**Interpretation (hypothesis):** Postings asking for 3–5 years of *Go* are a barrier for a learner with none; the credible entry is likely "backend engineer, mid-to-senior" where overall seniority transfers and a strong public project substitutes for Go years. Message brokers (Kafka) and Redis appear often enough that a Postgres-only course leaves a visible gap.

## Direction B — Platform engineering and developer infrastructure

**Observations:**
- Web3 Vietnam (SRE, Hanoi): Kubernetes on GKE must-have, GCP networking.
- Trustify EU (Senior DevOps, HCMC): GCP, Kubernetes, VMs, CI/CD with Jenkins or GitLab.
- Saritasa (Mid/Senior DevOps, HCMC): 3+ years infrastructure, Terraform, Kubernetes, Linux.
- Cyberlogitec (DevOps, HCMC): Docker, Kubernetes, Helm, ingress, service discovery, autoscaling, rolling updates.
- VPS Securities (Senior DevOps Platform Engineer, Hanoi): on-premise OpenShift/Kubernetes; summary says a CKA certificate is required (verify the page).
- No posting titled plainly "platform engineer" with developer-tooling duties was confirmed; most were DevOps titles. VNG/GreenNode and KAFI have platform-titled roles that were not read.

**Interpretation (hypothesis):** Employers screen on Kubernetes in production, a cloud provider, Terraform, CI/CD, Linux. This course teaches Docker, CI and a local Kubernetes deploy, and nothing of Terraform or a public cloud. Building a workflow engine is better evidence for "backend/platform builder" than for "operate infrastructure".

## Direction C — Distributed systems and reliability

**Observations:**
- SRE postings surfaced: Grab Vietnam (5+ years, Go, Docker, Kubernetes), Ninja Van (entry; Go/Java, on-call), Carousell (GCP, GKE, Go among languages), Plus8soft (Kubernetes in production), Monroe Consulting (Go or Python, Kubernetes), HCL (Go/Java/Python, Kubernetes), Axon Networks (3+ years, Docker, Kubernetes, Terraform).
- None of the summaries described distributed-systems *design* work. The phrase appears mostly as a bullet in backend postings (see Direction A).
- Workflow-orchestration tools: Temporal appeared in one Grab summary and in a closed Vietcetera posting; Airflow appeared in data-engineering postings (Saigon Technology, a "PS | Data Engineer" role). No posting asked for building an orchestrator.

**Interpretation (hypothesis):** Pure "distributed systems engineer" roles are rare in this sample and concentrated in a few large or product companies; reliability work is mostly advertised as SRE/DevOps with Kubernetes and cloud. A durable-workflow project is a differentiator in interviews, not a keyword that matches many postings. Workflow-orchestration knowledge shows up via Temporal/Airflow familiarity, which the project makes easy to discuss.

## Compensation

**Observations** (from search summaries; pages not opened):
- ITviec IT Salary Report 2025/2026 (self-reported survey, 1,839 respondents of mixed roles): mid-level backend 30–55 million VND/month. Senior band **not seen**. Full report is gated.
- Second Talent rate card (recruiter/vendor estimate, not a survey): senior DevOps 80–110 million VND/month; lead/principal 110–150+ million. Says remote work for foreign companies pays in this range.
- Relia Software: average DevOps $32,126/year; lead DevOps over $3,500/month. Kyanon: 27–70 million VND/month for hard-to-hire roles including DevOps.
- Levels.fyi, one employer (FPT Software): backend median yearly total compensation 215,163,132 VND.
- Job postings: most showed no salary; one TopDev posting required login to see it. Benefits seen: 13th-month salary (GFT, Vision), lunch allowance.
- Platform engineering salary: **no figure found.**

**Interpretation:** Figures are inconsistent in source quality (survey vs vendor marketing). They are not evidence of what this learner would be paid. No conclusion about which direction pays most is supportable yet.

## Course consequences (proposed; need your decision)

| Evidence | Proposed response | Status |
|---|---|---|
| Kafka/Redis recur in Go backend postings | Add optional `P3-MSG-01` (same workload on a broker vs Postgres queue) | Proposed, optional |
| Terraform and a cloud provider recur in platform/SRE postings | Add optional `P4-IAC-01` (Terraform basics) | Proposed, optional |
| "Data-intensive" has thin evidence; SQL and Kafka are the visible parts | Add optional `P1-PG-04` (indexes, query plans on a large table) | Proposed, optional |
| Years of Go are demanded | The public project plus a clean commit history is the main substitute; do not claim Go years | Note |
| CKA seen once, certifications otherwise absent | Defer any credential decision until `P0-CAR-01` | Open |

## How to improve this evidence (learner task in `P0-CAR-01`)

1. Open each linked posting directly; record title, company type, date, level, years, must-have skills, salary if shown. Add at least 10 postings per direction you keep.
2. Add 5–10 postings from your own network or target employers.
3. Ask 2–3 working engineers in Vietnam which direction hires and pays for career-changers from frontend.
4. Replace this file's tables with your counts and mark conclusions with sample sizes.

## Sources (search summaries, 2026-11-16; pages not opened)

ITviec Go listings (e.g. Rikkeisoft 4531, Vision Advisory 4909, GFT 2444/3803, Masan 5734/5828, NexLab 2159, DatVietVAC 4329); TopDev DevOps/SRE listings (Web3 Vietnam 2078392, Trustify 2090922, Saritasa 2094867, Cyberlogitec 2105925); ITviec VPS Securities 4511 and Grab Vietnam SRE 4505; Lever (Amanotes), VNG careers; ITviec salary report page (itviec.com/report/vietnam-it-salary-and-recruitment-market); secondtalent.com DevOps rate card; levels.fyi FPT Software; reliasoftware.com and kyanon.digital DevOps salary pages.
