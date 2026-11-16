# Career Research — Vietnam

Owner: learner approves conclusions; Claude records evidence. Single source for market conclusions. Source records: `career/POSTINGS.md`. Nothing elsewhere in the repository may state a market fact that is not supported here.

**Status: PRELIMINARY. No direct posting record exists yet.** Everything below comes from web-search result summaries (2026-11-16). No posting page was opened, because the session network could not reach the job sites. This is a convenience sample of 42 pointers (A 24, B 8, C 10). It says nothing about market share or representativeness.

## Evidence tiers (used throughout)

| Tier | What it is | Allowed use |
|---|---|---|
| **Direct record** | Posting page read in full; URL, observation date, title, seniority wording, exact years, skills, salary if shown | Counts, requirement statements |
| **Pointer** | URL from a search result, page unread; summary claim | Where to look next; never a count |
| **Aggregated observation** | A tally over direct records, with n and the selection method | Patterns, stated with n |
| **Interpretation** | A reasoned reading of observations | Labelled; may be wrong |
| **Unverified hypothesis** | A guess to test | Never cited as support |

Today only pointers exist. The statements below are therefore **pointer claims** (what a summary said about a listed URL) and **hypotheses**. They must not be quoted as market facts or counts.

## What the pointer summaries claimed (not verified)

Direction labels A, B, C are defined in `career/POSTINGS.md`. Row numbers refer to its pointer table.

**A — Backend (Go, data-intensive).** Summaries mention required Go or backend years of 2–5, 3+, 4+, 5+ and 6+ in several listings (rows with years in their claim column). SQL databases, microservices, Docker and AWS/GCP appear in titles and summaries. Kafka appears in the summaries of four listings (GFT 3803, Grab 5117, NexLab 2159 and 2105971), with Redis next to it in two. "Distributed systems" appears in summaries for DatVietVAC, a Masan listing and Vinrobotics. No summary mentioned ClickHouse.

**B — Platform / infrastructure.** Summaries mention Kubernetes in each of the four DevOps/SRE listings they described (Web3 Vietnam, Trustify, Saritasa, Cyberlogitec), a cloud provider in two (GCP), Terraform in one (Saritasa), and CI/CD tooling in one. One summary (VPS Securities) said a CKA certificate was required; the page was not read. KAFI, One Mount and VNG GreenNode listings were found with titles only.

**C — Distributed systems / reliability.** SRE summaries mention Kubernetes and Go, Java or Python coding (Grab 4505, HCL 4704); an on-call duty appeared in one summary that is not in the register. No summary described distributed-systems *design* work. Temporal appeared in one backend summary (Grab 5117) and one closed posting (Vietcetera); Airflow appeared in the Vietcetera and Saigon Technology summaries.

**Compensation.** Salary figures came from reports, not postings, and only through search summaries:
- ITviec IT Salary Report 2025/2026 (self-reported survey, 1,839 mixed respondents): mid-level backend 30–55 million VND/month. No senior band seen. The report is gated.
- Second Talent rate card (vendor estimate, not a survey): senior DevOps 80–110 million VND/month.
- Relia Software and Kyanon (vendor blogs): DevOps averages and ranges; methodology unknown.
- Levels.fyi, one employer (FPT Software): backend median yearly total compensation 215,163,132 VND.
- Platform engineering: no figure found. Most postings hid salary.

## Interpretations (labelled; may be wrong)

- I1. Years of *Go* are stated in many pointer summaries, which suggests they may be a barrier for a learner with none. A public project and a clean history may have to substitute for years.
- I2. Message brokers (Kafka) and Redis appear next to Go in several summaries, so a PostgreSQL-only course may leave a gap for direction A.
- I3. Platform/SRE summaries emphasise Kubernetes in production, a cloud provider and Terraform. This course teaches containers, CI and local Kubernetes, and no cloud provider or Terraform.
- I4. Pure "distributed systems engineer" roles were rare among the pointers; the phrase appeared mostly as a bullet inside backend postings.
- I5. The salary sources differ in quality (survey versus vendor marketing) and cannot rank the directions.

## Unverified hypotheses

- H1. Frontend-to-backend career changers are hired at mid-to-senior level on the strength of overall seniority plus a project.
- H2. A durable-workflow project is a stronger interview differentiator than a matching keyword.
- H3. Temporal/Airflow familiarity is a plausible talking point for orchestration-related roles.

## Unknown

Which direction hires career changers from frontend; whether target employers screen on data-structure puzzles; how much Kafka, Redis, Terraform and cloud matter relative to a project; what senior bands pay; the posting dates and whether these postings are still open.

## Snapshot protocol (the `P0-CAR-01` deliverable)

Goal: a defensible *initial* snapshot that supports a later career-priority decision. It does not make the decision and does not claim coverage.

1. Write down the search method first: sites, search terms, filters, the date. Do not change it to find more convenient postings.
2. For each direction A, B and C, record **at least 6 postings** in `career/POSTINGS.md` section 1, in the order the search returns them, until 6 are filled. Read each page in full. Skip none because it disagrees with a hypothesis; mark expired ones and replace them.
3. Tally from the direct records only: required years, skills (must-have separate from nice-to-have), stated salary, work mode. Give n for every count.
4. Write interpretations separately, each tied to the tally it rests on, and update the hypothesis list.
5. List what remains unknown and what evidence would resolve it.
6. Conversations with working engineers are an optional extra, outside the 7-hour budget.

The priority decision between directions can be deferred. If deferred, the order of optional unlocks in `CURRICULUM.md` stays as is.

## Credentials

None recommended. One pointer summary named a CKA; verify before treating it as a pattern.
