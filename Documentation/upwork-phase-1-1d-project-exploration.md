# Upwork Economic Viability — Phase 1.1D: Project Exploration

Date: 2026-09-24 · Corpus: 438 unique jobs (Phases 1.1A+1.1C) · Detail samples: 61 `find_jobs:get` calls (21 in 1.1B + 29 deep-dive + 11 aged-job lifecycle sample)

Project-centric analysis. Evidence labels: FACT / OBSERVED / CALC / ASSUMPTION / UNKNOWN.

---

## 1. Project lifecycle findings — what is observable

| Stage | Observable? | Mechanism / evidence |
|---|---|---|
| Job creation | FACT | `created_date`/`published_date` present on every record |
| Proposal accumulation | PARTIAL | `proposals_tier` band only (Basic plan); no counts, no bid amounts |
| Proposals over time | INDIRECT | cross-sectional age-vs-tier (below); no per-job time series |
| Client activity | FACT (sampled) | `activityStat`: invitesSent, totalInvitedToInterview, totalHired — on `get` only |
| Interviews | PROXY | `totalInvitedToInterview` count; content not visible |
| Hiring | FACT (sampled) | `totalHired` + matching `client_work_history` contract rows |
| Time to hire | BOUNDED | upper bound = job age when `totalHired≥1`; lower bound = contract `started` date vs post date when both visible |
| Closure | PARTIAL | `workFlowState.status` (ACTIVE observed); closed/expired jobs disappear from search rather than showing a terminal state — **unobservable negative** |
| Reposting | OBSERVED | same-title duplicates in `client_work_history` (see §8) |
| Subsequent related jobs | OBSERVED | client history samples show chains (below) |

**Lifecycle measurement (aged sample, n=11, jobs 9–51 days old):**

- 4/11 hired≥1 (36%) — including the 51-day "urgent" job filled twice over
- 3/11 unfilled with zero invites and zero interviews — **apparently dead posts** (27%)
- 3/11 unfilled but actively interviewing (invites 1–39, interviews 2–15) — **stalled funnels** (27%)
- 1/11 enterprise role (Upwork Inc itself) — never intended as a short contract

Interpretation (OBSERVED): of jobs still listed ≥9 days, roughly a third are filled, a third are dead, a third are stalled funnels. A recency-sorted search surface therefore contains ~25–35% zombie inventory at any moment — **effective live demand is meaningfully smaller than listing counts suggest.** This is the flip side of 1.1C's "fill fast" finding: urgent jobs fill in days, and what remains visible is disproportionately dead or stalled.

## 2. Project statistics (corpus, n=438)

| Metric | Value |
|---|---|
| Fixed / hourly | 185F / 253H (42%/58%) — CALC |
| Advertised duration | <1mo 36% · 1–3mo 33% · 3–6mo 10% · >6mo 21% — CALC |
| Median skills listed | 5; 51% list ≥5; 23% list ≥8 — **most posts are multi-system by declaration** — CALC |
| Explicit urgency | 4% (urgent/ASAP/emergency markers) — CALC |
| Diagnose-first language | 12% — CALC |
| Production-access language | 11% — and these carry **median fixed budget $400** (4× corpus norm) — OBSERVED |
| Big-scope markers | 5%, medF $250 — CALC |
| Vague ask ("need help/expert", thin brief) | 14%, medF $50 — vagueness correlates with low budget — OBSERVED |
| Milestone/acceptance-criteria briefs | 1% of corpus — but medF $2250 — the best-specified work is rare and expensive — OBSERVED |
| Experience level | intermediate mode everywhere; EXPERT share highest in email/DNS (44%) and migration (50%) — CALC |

Client-side (61 get-samples): `client_record` exposes contracts_total, jobs_with_hires, spend_total, feedback. Serial buyers are common at the high end ($2.8M spend/61 contracts; $285k/103; Upwork Inc itself at 44k contracts). Zero-history clients (0 contracts) made up ~20% of the deep-dive sample — concentrated in the cheapest posts.

## 3. Short-contract statistics

Advertised `<1 month` is the platform's shortest duration bucket — it spans same-day to 4-week work and **cannot be subdivided via the duration field** (UNKNOWN inside the band). Using fixed-price budget as the practical delivery proxy:

| Class (proxy) | n | propMed | %50+ | urgent% | Note |
|---|---|---|---|---|---|
| ≤$50 same-day micros | 38 | 12.5 | 5% | 8% | least competitive, worst economics |
| $50–150 (1–2d) | 18 | 35 | 6% | 11% | competition jumps at $50+ |
| **$150–400 (3–5d)** | **12** | **26.2** | **0%** | **33%** | **sweet spot: highest urgency share, zero saturation** |
| $400–1k (<2wk) | 6 | 35 | 17% | 0% | thin, more competitive |
| $1k+ (<1mo) | 3 | 35 | 33% | 0% | rare |
| hourly <1mo | 79 | — | — | — | short-duration hourly = trial engagements |

## 4. Scope/ambiguity analysis (fixed-price n=165)

- moderate scope: 53%
- **underspecified (<350 chars total): 34%**
- diagnostic-oriented brief: 12%
- milestone/acceptance-structured: ~4%
- budget-scope mismatch (big scope ≤$150): only 1% by strict heuristic — the deeper pathology is the inverse: **$600 for a full-time senior Drupal role** (~$3.50/hr equivalent, 30 invites/15 interviews/0 hires) and EXPERT-level posts at $10–60 fixed budgets. Unrealistic pricing concentrates in *hourly-disguised-as-fixed* and *seniority-inflated* posts, not naive scope.

"Symptom ≠ cause" cases (OBSERVED, qualitative): the WP/LiteSpeed post where the client already knows Site Health reports PHP 7.4 under an 8.1 panel — unusually well-diagnosed by the client; more typical is "emails land in spam" (symptom) where the cause is DNS/warmup/reputation (unknown to client). Clients describing symptoms rather than causes is the norm in repair posts; a minority (~12%) explicitly ask for diagnosis-first.

## 5. Client behavior (61 get-samples)

- **Formal qualification gates**: 7/61 (11%) — JSS 80–90, min earnings $1k–10k, native/fluent English, geography. Gates cluster in aged/high-value enterprise posts (4/11 aged vs 3/50 earlier samples). **A new account is locked out of the best-documented briefs** — this is the single largest structural barrier found in this phase.
- **Screening questions**: present on ~40% of detailed samples; the best briefs use them as proof-of-work filters (portfolio artifacts, "start with word X", mandatory Loom video for one GCP role).
- **Interview behavior**: invitesSent ranges 0–39; high-invite stalled funnels (30 invites/15 interviews/0 hires on the $600 Drupal role) indicate clients shopping without buying.
- **Hiring speed**: filled jobs in the aged sample bound time-to-hire at ≤ their age; fresh-sample fills (same-day $10 Elementor job hired within days) show micro-jobs close fastest.

## 6. Competition behavior

Cross-sectional age-vs-tier (n=438):

| Age band | n | propMed | %50+ |
|---|---|---|---|
| 0–1d | 295 | 17.5 | 15% |
| 1–2d | 65 | 35 | 32% |
| 2–4d | 27 | 35 | 7% |
| 4–8d | 23 | 17.5 | 9% |
| ≥8d | 23 | 35 | 35% |

OBSERVED with confound: tiers are NOT cleanly monotone in age — the 2–8d bands contain thin, self-selected tail results from recency search. The robust findings are: (a) **~15% of <24h jobs already show 50+** — competition accrues within the first day on visible work; (b) aged visible posts skew back to high tiers — consistent with a survivor pool of unfillable/stalled posts accumulating proposals.

**Competition by project type** (archetype census, first-match over title+snippet, 184/438 classified):

| Archetype | n | medF | propMed | %50+ | <1mo% |
|---|---|---|---|---|---|
| deliverability infra | 15 | $300 | 17.5 | 7% | 33% |
| perf/speed | 31 | $135 | 17.5 | 6% | 29% |
| prod deploy/config | 42 | $100 | 17.5 | 17% | 50% |
| record-fix (DNS/SSL) | 10 | $77.5 | 35 | 10% | 90% |
| access/lockout crisis | 2 | $60 | 18.8 | 0% | 100% |
| workflow repair | 3 | $75 | 35 | 0% | 100% |
| migration/upgrade | 36 | $300 | 35 | 31% | 19% |
| integration build | 42 | $100 | 35 | 24% | 33% |
| (unclassified/other) | 254 | — | — | — | — |

## 7. Acquisition economics — project-level model

Per-bid cost ≈ connects×$0.15 (median 14 → $2.10) + ~30 min proposal time imputed $15 → **~$17/bid**. Effective hourly = (budget − win-rate-adjusted acquisition cost) / delivery hours:

| Project | win 5% | win 10% | win 20% |
|---|---|---|---|
| $60 crisis fix / 2h | **−$141/hr** | −$56/hr | −$13/hr |
| $100 record fix / 3h | −$81/hr | −$24/hr | +$5/hr |
| $200 deliverability diag / 5h | −$28/hr | +$6/hr | +$23/hr |
| $300 emergency recovery / 6h | −$6/hr | +$22/hr | +$36/hr |
| $800 audit+migration / 20h | +$21/hr | +$30/hr | +$35/hr |
| $1500 automation build / 25h | +$45/hr | +$53/hr | +$56/hr |
| $3500 infra build / 40h | +$79/hr | +$83/hr | +$85/hr |
| $30/hr × 40h recurring role | +$20/hr | +$24/hr | +$27/hr |

CALC. Three consequences:

1. **Sub-$200 fixed work is structurally unprofitable under cold-start win rates** regardless of competition level. Same-day micros ($10–60) are traps, not entry points.
2. The two viable shapes: **$300+ fixed diagnostics/migrations** and **recurring hourly roles** — the latter is the only structure still positive at a 5% win rate.
3. False-attractiveness flag: cheap *urgent* jobs look winnable (low competition, fast close) but a $60 "URGENT mailbox deletion" fix has negative expected value at any win rate < ~25% — acquisition economics only clear if win probability is implausibly high.

## 8. Repeat / related-demand evidence

Demand chains are directly visible in `client_work_history` (OBSERVED):

| Client | Chain observed |
|---|---|
| Deliverability client (AU) | same "Urgent SPF/DKIM/DMARC" title: hired→closed→**reposted**→hired again; 3 related deliverability posts |
| Google Workspace client | identical $100 urgent post rehired 5 days later (1.1C) |
| Drupal client | "Find and remove malware from Drupal 7" contract open since **2022** → new "Drupal 11 updates" post — the same estate generating work across an EOL chain |
| Drupal-7-triage client | previously paid for a D7→latest migration (1.1C) |
| SMTP-engine client | 4+ related bulk-mail/Playwright automation posts (see anomaly below) |
| MailWizz client | parallel "Connect SES to Mumara" post — same infra need, different tool name |
| Migration client (Painter Ready-class) | audit→staging→cutover→handoff milestone structure = built-in follow-on chain |
| Enterprise buyers | serial infra posts (Cisco→3CX→Nimble→Entra on one $2.8M account) |

**The demand chain is real and observable**: migration→email-breakage→deliverability fix→ongoing ops; compromise→cleanup→hardening→monitoring; setup→support. A single win exposes follow-on work — client history proves it happens, and ~15–20% of get-sampled clients show visible related posts.

## 9. Important anomalies

1. **$600/month full-time senior Drupal role** — 30 invites, 15 interviews, 0 hires; extreme budget-scope mismatch (~$3.50/hr equivalent). FACT.
2. **Serial reposter with spam-infrastructure profile** — detailed 500-emails/day/SMTP-engine spec, prior contractor ended on 1/1 feedback, 3+ open related posts. Detailed spec ≠ good client. OBSERVED.
3. **Upwork Inc hires on Upwork** — the $2.8M-spend aged job's client is Upwork itself (44k contracts; "UPWORK HAS AN MCP" beta-testing gigs in history). FACT.
4. **4-year-old still-open contract** ("Drupal 7 malware removal", started 2022) — open-contract records persist indefinitely; client history "active" ≠ currently buying. FACT.
5. **Agency churner**: 2,143 contracts / 2,112 hires — micro-job volume client; explains part of the $10-job supply. OBSERVED.
6. **Client-side AI usage**: one job's spec is a ChatGPT share link; several briefs are AI-polished. Clients use AI to write *better* specs — raising the floor on brief quality while leaving diagnosis unsolved. OBSERVED.
7. **EXPERT-level posts at $10–20 budgets** — seniority inflation is common at the bottom of the market.

## 10. What cannot be observed

- Actual proposal counts, bid amounts, proposal content (Basic plan)
- Message/interview content and interview→hire conversion
- Job view counts / client page activity between `get` calls
- Closed/expired listings (search returns only ACTIVE workFlowState — dead jobs vanish rather than report closure)
- True time-to-hire below the granularity of job age + contract start dates
- Whether unfilled posts failed for price, supply, or client abandonment
- Win rate for this account (requires spending Connects)

## 11. Representative project records

Compact records for the 11 aged lifecycle samples are stored in `upwork-phase-1-1d-project-exploration-raw.json`, keyed by job ID with connects, gate, hire, invite, and repeat-chain fields.

## 12. Implications for the final Phase 1.1 economic model

1. **Effective demand ≠ listing count.** ~25–35% of aged visible inventory is dead or stalled; fresh-response (≤24h) is where live demand concentrates — monitoring speed matters more than search breadth.
2. **Bid-side economics dominate.** At ~$17 effective cost per proposal (mostly unpaid time), only $300+ fixed diagnostics or recurring hourly roles clear a cold-start funnel. The deliverability-infra and audit-first-migration archetypes are the only shapes that combine adequate budgets with sub-10% proposal saturation.
3. **Gates are the real wall, not competition.** The best-documented, highest-budget briefs carry JSS/earnings gates ~11% overall and rising with post value — a new account cannot reach them. The viable funnel is: ungated $200–500 diagnostic/repair wins → JSS → gated enterprise work later.
4. **Repeat-demand is the multiplier.** ~15–20% of sampled clients show visible related posts; winning one diagnostic job plausibly opens a chain (fix→migration→ops). Single-project EV understates client EV — the model should price jobs as *chain entries*.
5. **Client quality is a filtering dimension**, not a given: serial reposters, churner agencies, and stalled funnels are detectable in `client_record`/`activityStat` before bidding — screening clients costs less than screening jobs.
