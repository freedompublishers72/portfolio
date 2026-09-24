# Upwork Phase 1.1B — Economic Ranking

**Date:** 2026-09-24 · **Status:** Complete (screening/ranking only — not a business verdict)
**Input:** Phase 1.1A corpus — 348 unique jobs, 39 probes (`upwork-phase-1-1a-technical-universe-raw.json`), plus a new 21-job `find_jobs:get` detail sample (`upwork-phase-1-1b-get-sample.json`), and the Phase 1.1 Connects distribution (n=58, median 14, range 7–27).

Evidence labels: **FACT** · **OBSERVED** · **CALC** · **ASSUMPTION** · **UNKNOWN**

---

## 1. Ranking methodology

The 39 search probes were consolidated into **22 evaluation areas** (multi-probe areas deduplicate jobs by ID; per-job problem-type classification applied via a documented keyword heuristic over title+snippet — FIX / SEC / PERF / MIGRATE / INTEG / BUILD / RECUR / ADVISE / COMMOD).

Each area is scored on seven dimensions (A–G), each normalised to 0–1, then combined by weighted sum. The model deliberately:

- **log-squashes project value** (`sig(log1p(v))`) so a $5k job cannot dominate a $300 job;
- **penalises competition directly** (proposal-tier midpoint as the denominator);
- **treats demand frequency as a floor, not a score** — enough flow to bid weekly is required, but extra volume beyond that earns almost nothing (G weights `sig(log1p)` of est/day and caps at ~30/day);
- **never rewards difficulty that doesn't restrict supply** — D (difficulty) and B (acquisition) are separate axes, so a hard-but-crowded niche (PHP title probe: 40% at 50+) and a soft-but-empty niche score differently.

**Baseline weights:** A 15% · B 15% · C 10% · D 20% · E 15% · F 15% · G 10%. D is weighted highest because the investigation's hypothesis is supply restriction via difficulty. §9 tests three alternative weightings.

All sub-score formulas are stated in §2; computed values for all 22 areas are in §4. This phase answers "where is deeper evidence-gathering justified" — it cannot and does not establish win rate.

## 2. Metric definitions

| # | Metric | Definition used | Status |
|---|---|---|---|
| 1 | Demand frequency | est/day = (n−1)/published_date span of newest-10 recency probe; merged areas = overlapping-sum upper bound | **CALC**, order-of-magnitude only |
| 2 | Median project value | median `budget` of fixed jobs (n≥3 required); else `med_hr_min × 20h` labelled proxy | **CALC** / **ASSUMPTION** (hourly proxy) |
| 3 | Budget distribution | p25 / p75 of fixed budgets | **CALC** (thin samples flagged) |
| 4 | Median proposal competition | median of tier midpoints (<5→2.5, 5–10→7.5, 10–15→12.5, 15–20→17.5, 20–50→35, 50+→60) | **CALC** from tiers (ranges, age-confounded) |
| 5 | Short-project frequency | share with duration "Less than 1 month" | **CALC** |
| 6 | Typical duration | modal duration bucket | **CALC** |
| 7 | Connects required | per-job `connects_cost` via `get` calls; cross-niche sample n=21: **median 15, range 6–26** (WP corpus n=58: median 14, range 7–27) | **OBSERVED** — no material niche differential found |
| 8 | Acquisition cost per proposal | connects × $0.15 = **~$2.25 median** (range $0.90–3.90); excludes unpaid bidding time, which dominates | **CALC** |
| 9 | Budget ÷ Connect cost | value_proxy ÷ $2.25 | **CALC** |
| 10 | Budget ÷ competition | value_proxy ÷ proposal midpoint | **CALC** |
| 11 | Competition-adjusted value | value_proxy × 1/(1+prop_mid) — naive expected-value-per-proposal index; NOT a win-rate model | **CALC**, rough |
| 12 | Troubleshooting/repair frequency | % jobs matching FIX/SEC/PERF keywords | **ESTIMATE** (heuristic) |
| 13 | Specialist-work frequency | % matching specialist-platform/skill regex set | **ESTIMATE** |
| 14 | Cross-system frequency | % with ≥4 distinct skills or integration vocabulary | **ESTIMATE** |
| 15 | Recurring-problem frequency | % matching RECUR (maintenance/ongoing/support/monitor) | **ESTIMATE** |
| 16 | Technical difficulty evidence | composite: 0.35·%expert + 0.25·%specialist + 0.25·sig(hr_min/40) + 0.15·%cross | **CALC** composite |
| 17 | Supply-restriction evidence | composite: 0.5·(1−sig(prop_mid/35)) + 0.3·%expert + 0.2·%specialist | **CALC** composite |
| 18 | Commodity/AI-solvability | % matching COMMOD keywords (listing, data entry, voice recording, beta test, content) + low-budget share | **ESTIMATE** |
| 19 | Solo-suitability | % with freelancers_to_hire ≤1 and no team/agency language | **CALC** — ~95–100% everywhere (not discriminating) |
| 20 | ≤1-business-week suitability | % <1mo duration AND (repair-flavoured OR fixed ≤$1,500) | **ESTIMATE** (proxy) |

Not computable from this evidence: actual win rate, actual hire/fill rate (2/21 sampled jobs were already filled at fetch time — **OBSERVED**), proposal counts (tiers only on Basic plan), competing-bid amounts (Freelancer Plus feature, unavailable).

## 3. Evidence-quality rules

| Grade | Rule | Areas |
|---|---|---|
| **HIGH** | n≥15 AND multiple probes feed the area | WP (34), Data eng (30), DevOps (28), Generic web dev (20), AI apps (20), NetSysAdmin (19), Desktop/legacy (19), ERP/CRM (18), Scraping/ETL (18), Automation (17) |
| **MED** | n=10–14, single probe, or single-window sample | Magento, Email/DNS, Stripe, Shopify, InfoSec, Python, PHP, QA, Mobile, Game, Blockchain, Embedded |
| **LOW** | only directional signals | — none of the 22; Engineering & Architecture and Customer Service & Tech Support were excluded as non-technical rather than graded |

Additional rules applied throughout:

- Areas with **n_fixed < 3** mark median value as hourly proxy (Blockchain — all hourly).
- `est/day` differences below ~2× are treated as noise.
- A 0% in a small sample means "none observed", never "none exist".
- `can_apply:false` appeared on all 21 `get` results — consistent with **connects_balance = 0** on this account (a proposal would require purchasing Connects — outside scope, per rules).
- `preferred_qualifications` was effectively empty on 19/21 `get` calls; formal gates are rare but real (1 hard gate found: JSS ≥80 + AU/NZ + native English + individuals-only on an AU government-adjacent analyst post).

## 4. Comparative table

| Area (conf) | n | est/day¹ | med val² | propMed | %50+ | %<10 | %<1mo | %≤1wk | %repair | %spec | %gate | val÷conn³ | val÷prop |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Network & SysAdmin (H) | 19 | ~34 | $100 / $20h | 12.5 | 0 | 47 | 58 | 21 | 16⁴ | 37 | 5 | 44 | 8.0 |
| Automation n8n/Zapier/scripts (H) | 17 | ~40 | $75 / $15h | 17.5 | 0 | 18 | 53 | 41 | 65 | 6 | 0 | 33 | 4.3 |
| Embedded / IoT / other-soft (M) | 10 | ~7 | $625 / $40h | 5.0 | 0 | 70 | 20 | 10 | 10 | 50 | 0 | 278 | 125 |
| InfoSec & compliance (M) | 10 | ~18 | $300 / $8h | 15.0 | 0 | 30 | 30 | 10 | 20 | 60 | 40 | 71 | 10.7 |
| ERP/CRM / Salesforce (H) | 18 | ~15 | $70 / $20h | 35.0 | 22 | 22 | 22 | 6 | 28 | 78 | 0 | 31 | 2.0 |
| Magento specialist (M) | 10 | ~1 | $100 / $17.5h | 35.0 | 20 | 10 | 20 | 20 | 50 | 80 | 0 | 156⁵ | 10 |
| Email / DNS / deliverability (M) | 10 | ~12 | $300 / $15h | 35.0 | 10 | 10 | 30 | 10 | 20 | 70 | 0 | 133 | 8.6 |
| DevOps / Cloud / AWS (H) | 28 | ~22 | $150 / $25h | 35.0 | 25 | 18 | 36 | 21 | 25 | 29 | 7 | 67 | 4.3 |
| Python general (M) | 10 | ~17 | $60 / $17.5h | 35.0 | 30 | 0 | 60 | 40 | 20 | 0 | 0 | 27 | 1.7 |
| Desktop & legacy apps (H) | 19 | ~10 | $70 / $30h | 35.0 | 37 | 11 | 37 | 21 | 53 | 21 | 0 | 31 | 2.0 |
| Payments / Stripe (M) | 10 | ~3 | $20 / $15h | 26.2 | 20 | 10 | 50 | 30 | 50 | 10 | 0 | 9 | 0.8 |
| Game dev (M) | 10 | ~14 | $120 | 12.5 | 0 | 20 | 50 | 20 | 10 | 30 | 0 | 53 | 9.6 |
| WordPress repair & ecosystem (H) | 34 | ~66 | $70 / $15h | 35.0 | 12 | 15 | 38 | 29 | 50 | 0 | 0 | 31 | 2.0 |
| QA / testing (M) | 10 | ~22 | $30 / $5h | 7.5 | 10 | 70 | 50 | 40 | 30 | 0 | 0 | 13 | 4.0 |
| Blockchain / Web3 (M) | 10 | ~6 | ~$1,200⁶ / $60h | 10.0 | 0 | 50 | 0 | 0 | 0 | 20 | 0 | 533 | 120 |
| Scraping / ETL (H) | 18 | ~13 | $75 / $8h | 35.0 | 44 | 6 | 61 | 33 | 11 | 0 | 0 | 33 | 2.1 |
| Data eng / DBA (H) | 30 | ~29 | $50 / $20h | 15.0 | 13 | 30 | 23 | 7 | 20 | 27 | 3 | 22 | 3.3 |
| Shopify / ecommerce setup (M) | 14 | ~60 | $30 / $13.5h | 17.5 | 7 | 36 | 29 | 14 | 14 | 0 | 0 | 13 | 1.7 |
| AI apps & ML (H) | 20 | ~55 | $50 / $8.5h | 17.5 | 10 | 25 | 30 | 15 | 45 | 0 | 5 | 22 | 2.9 |
| Generic web dev FE/BE (H) | 20 | ~175 | $35 / $25h | 17.5 | 25 | 30 | 30 | 10 | 10 | 0 | 0 | 16 | 2.0 |
| PHP general (M) | 10 | ~8 | $350 / $10.5h | 35.0 | 40 | 20 | 20 | 20 | 20 | 0 | 0 | 156 | 10 |
| Mobile dev (M) | 10 | ~42 | $12.5 / $15h | 35.0 | 20 | 20 | 20 | 20 | 0 | 0 | 0 | 6 | 0.4 |

¹ order-of-magnitude supply signal, not demand. ² fixed median / hourly-min median. ³ value_proxy ÷ $2.25 connects cost. ⁴ repair-kw understates here: many sysadmin posts are "check my server / M365 recovery" phrased as requests, not "fix" — see §5 note. ⁵ uses p75-ish case: med fixed $100 across only 2 fixed obs; hourly jobs dominate. ⁶ hourly-only area: $60h × 20h proxy — ASSUMPTION.

## 5. Economic ranking / sorting

Composite scores are **compressed (0.33–0.47)** — treat this as a top-cluster extraction, not a strict order:

| Rank (main) | Area | Main | A | B | C | D | E | F | G | one-line driver |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Network & SysAdmin | .47 | .44 | **.63** | .62 | .32 | .59 | .39 | .32 | lowest competition + highest short-share at real rates |
| 2 | Automation (n8n/Zapier/scripts) | .45 | .42 | .59 | **.72** | .22 | .63 | .47 | .20 | highest repair-share + highest ≤1wk share; budget question |
| 3 | Embedded / IoT / other-soft | .44 | .55 | **.72** | .55 | .35 | .60 | .15 | .13 | near-zero competition, good rates — **skill-gated for Marc** |
| 4 | InfoSec & compliance | .44 | .42 | .62 | .47 | .33 | .66 | .20 | .38 | thin competition; audit half is credential-gated |
| 5 | ERP/CRM / Salesforce | .44 | .42 | .49 | .58 | .38 | **.73** | .14 | .35 | highest specialist-share; platform-experience gates |
| 6 | Magento specialist | .43 | .46 | .53 | .52 | .37 | **.80** | .20 | .08 | highest commodity-resistance; ~1/day volume is the risk |
| 7 | Email / DNS / deliverability | .43 | .45 | .54 | .55 | .39 | .64 | .20 | .21 | specialist DNS/mail repair; n=10 thin |
| 8 | DevOps / Cloud / AWS | .42 | .45 | .50 | .59 | .30 | .60 | .28 | .27 | real infra work, 25% at 50+ competition |
| 9 | Python (general) | .42 | .41 | .47 | **.76** | .21 | .51 | **.50** | .16 | short+structured but commodity-leaning |
| 10 | Desktop & legacy apps | .41 | .45 | .46 | .55 | .28 | .66 | .29 | .16 | real legacy-repair signal; 37% at 50+ |
| 11 | Payments / Stripe | .41 | .36 | .48 | .70 | .23 | .62 | .40 | .10 | ~3/day, median $20 fixed — too thin/cheap alone |
| 12 | Game dev | .41 | .34 | .63 | .70 | .20 | .55 | .35 | .15 | low competition but design/asset-heavy |
| 13 | **WordPress repair & ecosystem** | **.40** | .40 | .50 | .63 | .19 | .60 | .33 | .27 | the baseline: real repair volume, but **not low-competition** |
| 14 | QA / testing | .39 | .36 | .61 | .66 | .15 | .45 | .45 | .19 | cheap + microtask-skewed |
| 15 | Blockchain / Web3 | .39 | .59 | .70 | .40 | .34 | .50 | **.00** | .15 | great economics, zero short-contract fit, skill-gated |
| 16 | Scraping / ETL | .39 | .39 | .46 | .71 | .16 | .46 | .47 | .19 | 44% at 50+, lead-gen race to bottom |
| 17 | Data eng / DBA | .38 | .42 | .57 | .52 | .28 | .55 | .15 | .24 | specialist tail exists; bulk is BI/dashboarding |
| 18 | Shopify / ecommerce setup | .37 | .39 | .55 | .59 | .20 | .46 | .21 | .28 | high volume, VA-priced |
| 19 | AI apps & ML | .37 | .38 | .56 | .59 | .16 | .54 | .22 | .22 | noisy; repair sliver real but $10-fix trap common |
| 20 | Generic web dev FE/BE | .37 | .41 | .53 | .60 | .23 | .46 | .20 | .24 | huge supply, undifferentiated |
| 21 | PHP general | .37 | .47 | .50 | .64 | .17 | .51 | .20 | .19 | language-probe noise, 40% at 50+ |
| 22 | Mobile dev | .33 | .34 | .43 | .55 | .20 | .45 | .20 | .21 | longest builds, $12 median, crowded |

**Reading:** the top cluster (ranks 1–8) is dominated by *infrastructure-adjacent and platform-specialist repair* — exactly the hypothesised shape. WP repair lands mid-pack (13th): good volume and structure, but competition and commodity-resistance are worse than in sysadmin/automation — consistent with the Phase 1.1 finding that repair is not less contested there.

## 6. Top candidate areas for Phase 1.1C

Selected from the top cluster + cross-area problem patterns, **filtered for Marc-accessibility** (no hardware/credential/platform-certification walls):

| Candidate | Score basis | Why it survives | Key unknown for 1.1C |
|---|---|---|---|
| **1. Network & SysAdmin repair** (VPS care, M365 recovery, DNS/mail, hosting moves, libvirt/LiteSpeed/cPanel issues) | #1; propMed 12.5, 0% at 50+, 58% <1mo | low competition + short + Linux/DNS-accessible; clients are desperate SMBs | budget floor ($15–20/hr observed); whether volume holds vs WP probe |
| **2. Business-automation repair** (n8n/Zapier/Make debugging + small builds) | #2; 65% repair-kw, 41% ≤1wk, ~40/day | strongest repair+short signal in corpus; new tooling = thin expert supply | budget bimodality — $10 fixes vs $500 systems; sample deeper for value floor |
| **3. Email / DNS / deliverability** | #7 composite but coherent problem cluster | recurring "mail doesn't arrive", DNS, M365↔Google migration; low competition | n=10 only; need synonym probes (SPF/DKIM/dmarc, "emails going to spam") for real volume |
| **4. Migration work (cross-area cluster)** — M365 tenant-to-tenant, Entra/AD, Magento EOL, Drupal, host moves | spans ranks 1,5,6,8; the legacy-migration probe exhausted at 9 results yet migration jobs appear under every platform name | high stakes, expert-priced, genuinely scarce supply | must be measured as a *problem cluster*, not a category — 1.1C must aggregate synonyms |
| **5. Magento specialist repair** (EOL upgrades, skimmer incident, indexing) | #6; 80% specialist, commodity-resistance .80 | end-of-life platform + payment risk = urgent expert work | ~1/day volume may not sustain a pipeline; check Magento+Adobe Commerce+Hyvä synonyms |
| **6. DevOps/Cloud paid assessments & fixes** (AWS gap analysis, HIPAA deploy, ClickHouse, Drupal+DevOps) | #8; real infra + ADVISE signals | assessment-as-deliverable is short, bounded, expertise-priced | competition is higher (25% at 50+); which sub-problems are uncrowded? |

## 7. Eliminated areas — factual reason

| Eliminated | Factual reason (not preference) |
|---|---|
| Generic web dev / generic PHP / generic Python | propMed 35, 20–40% at 50+, med fixed $35–60 — undifferentiated competition; difficulty doesn't restrict supply |
| Shopify setup / ecommerce commodity | med fixed $30; listing/setup posts dominate; VA-priced |
| Mobile dev | $12.50 med fixed, long durations, 50+ tier common — worst value×competition product in corpus |
| QA / testing microtasks | $5–40 tasks, device/location gates, cattle-call hiring (30 invites observed on one post) |
| Scraping / lead-gen ETL | 44% at 50+, med hr-min $8 — race to bottom (SERP-infra $25k tail noted but too rare to rank) |
| AI & ML subcat bulk | diluted by labeling/voice/tutoring at $3–20/hr; the real AI-apps sliver is tracked under candidate 2's repair umbrella |
| Blockchain / Web3 | strong economics but 0% <1mo and hard skill gate (Solidity/EVM) — fails F and accessibility |
| Embedded / IoT | #3 on score but hardware/firmware skill gate fails accessibility — eliminated on fit, not on market |
| Game dev | low competition but asset/design-heavy, not Marc's domain |
| Engineering & Architecture / Customer Service & Tech Support | non-software categories (taxonomy bleed) |
| ERP/CRM / Salesforce *as a primary niche* | highest specialist share but posts demand current platform-track record (Monday CRM screening questions, Checkmarx, Dynamics AL); not eliminated as adjacent opportunity — flagged for credential-gap check in 1.1C |

## 8. Areas requiring more evidence

| Area | Missing evidence |
|---|---|
| Email/DNS/deliverability | real volume (synonym probes needed) and budget distribution |
| Migration cluster | aggregate volume across M365/Entra/Drupal/Magento/host-move phrasings |
| MSP/subcontracted IT support | recurrence, response-time expectations, whether solo fits |
| Desktop/legacy (FileMaker, Crystal Reports, VB.NET) | 37% at 50+ may be age artifact — need fresh-only sample |
| InfoSec practical half (malware/hardening vs audits) | split credential-gated audit work from ungated remediation |
| Paid assessments/audits | does a new-profile freelancer win them at all? (credibility question, not measurable from search) |

## 9. Sensitivity analysis

Four weightings applied to identical inputs:

| Weighting | Scheme | Top-8 rank order |
|---|---|---|
| **Main** | A15 B15 C10 **D20** E15 F15 G10 | NetSysAdmin > Automation > Embedded > InfoSec > ERP/CRM > Magento > Email > DevOps |
| **Equal** | 1/7 each | NetSysAdmin > Automation > ERP/CRM > InfoSec > Embedded > Python > DevOps > Email |
| **Economics-heavy** | A30 B25 C10 D10 E5 F15 G5 | Embedded > NetSysAdmin > Automation > Blockchain > Python > InfoSec > QA > Email |
| **Short-contract-heavy** | A10 B15 C20 D15 E10 **F25** G5 | Automation > NetSysAdmin > Python > Stripe > QA > Game > Scraping > Embedded |

**Stability verdict:** Network & SysAdmin and Automation are top-3 under **all four** weightings — robust conclusions. InfoSec, Email, Embedded, Magento, ERP/CRM form a stable second band (in the top-8 under ≥3 of 4 schemes). Python/QA/Stripe only enter when structure or value is over-weighted — they are *fragile* candidates. Blockchain and Embedded flip position under economics-heavy weighting but are eliminated on accessibility regardless, so the practical shortlist (§6) is **insensitive to weighting choice within the tested range**. **CALC**

## 10. Phase 1.1C investigation plan

For each candidate in §6, in priority order:

1. **Synonym-expanded volume measurement.** For each candidate, run 3–5 query/title probes on problem phrasings (e.g., for email: `emails going to spam`, `dkim`, `dmarc`, `email deliverability`, `mail server`; for migration: `tenant to tenant`, `migrate m365`, `magento upgrade`, `drupal migration`, `move hosting`). Collect 30–50 jobs per candidate, not 10.
2. **Per-job `get` on every sampled job** in candidates — `connects_cost`, `preferred_qualifications`, `activityStat` (drop already-hired posts; 2/21 = ~10% stale rate observed, so liveness filtering matters).
3. **Manual classification** of the sampled jobs (replace keyword heuristics): repair vs build, ≤1-week feasibility, Marc-can-deliver yes/no, gate type.
4. **Budget realism test** for Automation specifically — histogram of fixed budgets; decide whether the $10-fix tail poisons the niche or whether $150–600 work is frequent enough.
5. **Competition aging check** — for the strongest niche, capture proposal tier vs job age across a 3-page window to separate "high competition" from "old posts".
6. **Win-rate proxy** — count `totalHired>0` share and invitesSent on gets to measure whether posts convert (a niche where jobs sit unfilled suggests either low demand-quality or supply scarcity — distinguish).
7. **Credential-gap check** for ERP/CRM-adjacent work and InfoSec remediation — is evidence-of-experience demanded in text, or is it the formal-gate exception (observed 1/21)?

Constraints preserved: read-only, no proposals, no Connects purchases; win rate remains **UNKNOWN** and cannot be established without a controlled bidding experiment — which is the decision this evidence chain ultimately feeds.

---

*Phase 1.1B ranks screening priority, not business outcome. The two robust findings: (a) infrastructure-adjacent repair (sysadmin, automation, email/DNS) outranks the WordPress baseline on competition and short-contract fit; (b) connects cost is ~flat across niches (~$2.25/proposal median), so acquisition economics discriminate on competition and value, not on Connect price.*
