# Upwork Connects Cost — Empirical Distribution Test

**Date:** 2026-09-24 (~03:47–04:30 UTC)
**Method:** Read-only. `upwork__find_jobs` `search` + `smart_search` (discovery) → `get` per job for `connects_cost`. Zero writes, zero Connects consumed, zero proposals/drafts/saves/messages.
**Sample:** 58 unique current WordPress jobs (the discovery dataset from `upwork-mcp-job-discovery-raw.json`, same calendar window).
**Coverage:** 58/58 `connects_cost` values retrieved. **0 UNKNOWN.**

---

## 1. Sample construction

Jobs were collected by marketplace discovery (title="WordPress", fixed-price, budget ≥$20, sort=recency, 5 pages) plus the personalized most-recent feed (skills=WordPress, days_posted=1, 3 pages), deduped by ID. No job was selected or excluded based on its Connects cost — costs were unknown at selection time. The sample deliberately spans the requested value bands ($20–$5,500) and includes hourly jobs (7) for completeness; value-band and per-$100 statistics are computed on fixed-price jobs only (n=51).

## 2. Empirical distribution — all 58 jobs

| Statistic | Value |
|---|---|
| Sample size | 58 |
| Known Connect costs | **58** |
| Minimum | **7** |
| P25 | **11.5** |
| Median | **14** |
| Mean | **14.71** |
| P75 | **17.5** |
| Maximum | **27** |
| Mode | **14** (13 of 58 jobs) |

### Cost-band histogram

| Connects required | Jobs | % of sample |
|---|---:|---:|
| 1–4 | 0 | 0.0% |
| 5–8 | 3 | 5.2% |
| 9–12 | 12 | 20.7% |
| 13–16 | 28 | 48.3% |
| 17+ | 15 | 25.9% |

**Key observation:** no job in the sample costs fewer than 7 Connects. The distribution is centered on 13–16, not on 9. The earlier single observation of 9 Connects was at the *cheap* end of the real distribution.

### Proposal cost in USD (Connects × $0.15)

- Median bid: 14 × $0.15 = **$2.10**
- Mean bid: 14.71 × $0.15 = **$2.21**
- Range: 7 × $0.15 = **$1.05** → 27 × $0.15 = **$4.05**

## 3. Connects by project-value band (fixed-price jobs, n=51)

| Project value | Jobs | Median Connects | USD bid cost | Bid cost as % of median project |
|---|---:|---:|---:|---:|
| $20–99 | 19 | 14 | $2.10 | 4.2% (median budget $50) |
| $100–249 | 10 | 14 | $2.10 | 1.7% (median budget $125) |
| $250–499 | 9 | 13 | $1.95 | 0.7% (median budget $300) |
| $500–999 | 4 | 14 | $2.10 | 0.4% (median budget $550) |
| $1,000+ | 9 | 19 | $2.85 | 0.2% (median budget $1,200) |

Connects ranges per band: $20–99 → 7–18; $100–249 → 9–18; $250–499 → 7–18; $500–999 → 9–27; $1,000+ → 13–27.

**Reading:** bid cost is nearly flat (~$2) across low/mid bands and rises only at $1,000+. As a percentage of project value it is ~10× worse for a $50 job than for a $300+ job.

## 4. Connects per $100 of project value (fixed-price, n=51)

`connects_cost ÷ budget × 100`:

- Minimum **0.3** ($5,500 job @ 26)
- P25 **2.8**
- Median **9.0**
- Mean **14.4**
- P75 **20.8**
- Maximum **70.0** ($20 job @ 14)

The metric is dominated by small budgets: a $20 job costs the same 14 Connects as a $200 job, so per-$100 cost ranges 70× across the sample.

## 5. The 100-Connect question

### Full sample (all 58 jobs)

| Case | Basis | Proposals per 100 Connects |
|---|---|---:|
| Best observed | 7 Connects | **14** |
| P25-cost case | 11.5 Connects | **8.7** |
| Typical/median | 14 Connects | **7.1** |
| P75-cost case | 17.5 Connects | **5.7** |
| Worst observed | 27 Connects | **3** |

### WorkBot-qualifying subset (29 jobs)

Qualifying rule (documented exclusions, applied per-job, not by Connects cost): excluded page-builder-primary work (Elementor/Divi/Wix), SEO/content/tracking-primary roles, non-WP platforms (Shopify/Webflow), mobile apps, design-only tasks, explicit long-term/full-time engagements (>3–6 mo or 140+h), agency-only requirements, unusual payment terms, and 2 jobs where a hire was already made (`totalHired:1`). 29 of 58 qualify.

| Statistic | Qualifying (n=29) |
|---|---|
| Min / P25 / Median / Mean / P75 / Max | 7 / 11 / **14** / 13.41 / 14 / 27 |
| 100 Connects at median | **7.1 proposals** |
| Observed range | 3–14 proposals |
| Cost to bid all 29 qualifying jobs | 389 Connects = **$58.35** |
| Median qualifying fixed budget | **$100** (n=26 fixed, sum $8,110) |

**Answer:** 100 Connects buys approximately **7** realistic WorkBot proposals (median), not 11. The earlier "9 Connects" figure would have overstated capacity by ~55%.

## 6. Is Connect pricing related to job value?

| Relationship | Pearson | Spearman | Reading |
|---|---:|---:|---|
| Budget vs Connects (fixed, n=51) | 0.372 | 0.226 | weak–moderate positive; visible mainly at $1,000+ |
| Proposal volume (tier midpoint) vs Connects | 0.498 | 0.481 | moderate positive |
| Job age vs Connects | 0.053 | 0.154 | none |

Mean Connects by proposal tier: `<5`→10.5 · `5–10`→9.0 · `10–15`→14.0 · `15–20`→13.5 · `20–50`→14 · `50+`→19.3.

**Interpretation (CALCULATED, no causation claimed):** Connects are roughly flat ($2 bid) across small/mid budgets and rise at $1,000+ and at 50+ proposals. The correlation with proposal volume is stronger than with budget — consistent with Upwork pricing Connects against demand/competition rather than contract size — but n=58 is small and tier midpoints are coarse, so this is directional only.

## 7. Where does the earlier $50 / 9-Connect observation sit?

- **Connect cost percentile:** 9 Connects is cheaper than ~86% of the sample (only 14% of jobs cost ≤9). It was a *low* observation, not typical.
- **Cost-per-$100 percentile:** 9/$50 = 18 Connects per $100 sits at ~P75 of fixed jobs — i.e., an *expensive* bid relative to project value, because the budget was small.
- **Comparable $20–99 band:** 19 jobs; costs [7,7,9,9,11,13,14×9,16,18,18]; median **14**. A $50 job at 9 Connects was **below** the band's typical cost. Comparable low-value jobs *commonly* cost 13–14 Connects (~$2.00–$2.10), not $1.35.
- **Corrected expectation:** a typical $20–99 bid costs ≈ **$2.10** (56% more than the single earlier observation suggested).

## 8. WorkBot economics model

### Scenario A — 100 Connects purchased

- Qualifying proposals possible at median cost: **~7** (14 Connects each)
- Best observed case (7-Connect jobs): **14**
- Worst observed case (27-Connect jobs): **3**
- Bidding on *every* qualifying job in this snapshot would need **389 Connects** ($58.35) — i.e., 100 Connects covers roughly a quarter of the currently visible qualifying supply.

### Scenario B — $15 = 100 Connects

Represented project value (median qualifying fixed budget = $100; ASSUMPTION: bids target median-budget qualifying jobs):

- 10 proposals → ~**$1,000** of project value targeted — *but* 10 median-cost proposals need 140 Connects ($21), so $15 only affords this if cheaper-than-median jobs are picked.
- Median capacity ~7 proposals → ~**$700** of project value targeted.
- Maximum capacity 14 proposals (all 7-Connect) → ~**$1,400** of project value targeted.

No win rate assumed. Every dollar of Connects targets ~$47 of project value at median cost ($2.10 per $100 job), before platform fees.

## 9. Classification of conclusions

- **OBSERVED:** all 58 `connects_cost` values; budgets, types, ages, proposal tiers, client records; `connects_balance: 0`; `bid_stats_available: false`; `totalHired` flags.
- **CALCULATED:** all distribution statistics, band medians, per-$100 ratios, correlations, 100-Connect capacities, USD conversions ($0.15/Connect).
- **ASSUMPTION:** the qualifying-subset definition (documented per-job above); tier-midpoint mapping for proposal-volume correlation; $0.15/Connect unit price; median-budget targeting in Scenario B.
- **UNKNOWN:** exact proposal counts (tier-only on Freelancer Basic); competing bid amounts (Plus-gated); whether Connects cost varies over a job's lifetime; Connects costs for jobs outside this snapshot window.

## 10. Economic significance

Connect costs are **materially restrictive for low-value jobs** (option 3), not negligible and not restrictive across the whole market:

- On the $20–99 band — which supplies ~37% of this sample and most of the qualifying work — a single bid costs a median $2.10 ≈ **4.2% of a $50 project's gross**. At a hypothetical 5% win rate that is ~$42 of Connects per won $50 contract — comparable to the entire project value.
- On $250+ jobs the same ~$2 bid is ≤0.7% of project value — material but manageable (option 2 territory).
- The flat ~14-Connect pricing means the constraint is driven by *job value*, not by Connects price volatility.

Do not buy Connects yet — this establishes cost structure only; win rate remains the crux unknown.

---

## Appendix — full 58-job evidence table

(Ages at 03:47 UTC 2026-09-24. "YES" = WorkBot-qualifying.)

| Job (ID suffix) | Age | Title | Type | Budget | Connects | Proposals | Qualifying |
|---|---|---|---|---|---:|---|---|
| 273136 | 0.4h | Experienced WordPress Developer Needed to Improve Website  | hourly | — | **9** | 15 to 20 | YES |
| 948081 | 0.7h | WordPress Speed, SEO & Tracking Expert (Flywheel + Cloudfl | fixed | $400 | **11** | 20 to 50 | YES |
| 385816 | 0.7h | WordPress / LiteSpeed Developer Needed for Security Update | hourly | — | **11** | 10 to 15 | YES |
| 244912 | 1.8h | Website Maintenance and Fix | hourly | $15 | **11** | 20 to 50 | no — hourly + >6mo |
| 410072 | 2.2h | Remove Bitcoin and Blockchain References | fixed | $70 | **9** | 5 to 10 | YES |
| 748557 | 2.3h | Mailpoet Task inside Wordpress Site | hourly | — | **26** | 10 to 15 | YES |
| 627371 | 5.0h | WordPress Elementor Website Migration & Ongoing Support | hourly | — | **10** | 20 to 50 | no — Elementor+ongoing |
| 351149 | 5.6h | WordPress Migration: Single Site → AWS Lightsail (Sydney)  | fixed | $200 | **14** | 20 to 50 | YES |
| 588840 | 5.6h | Wordpress settings for existing website | fixed | $50 | **14** | 20 to 50 | YES |
| 020909 | 6.2h | WordPress Website Formatting Fix | hourly | $15 | **18** | 50+ | no — hourly formatting |
| 396973 | 7.5h | Need 5-7 page wordpress website and ongoing SEO | fixed | $1,000 | **26** | 50+ | no — build+ongoing SEO |
| 191448 | 7.7h | Need a wordpress developer for my Restaurant website | fixed | $500 | **9** | 5 to 10 | YES |
| 343704 | 7.8h | Meta Pixel Setup on WordPress | fixed | $50 | **14** | 15 to 20 | no — pixel/marketing |
| 203818 | 8.0h | WordPress Malware Removal: SEO Spam Injection Cleanup | hourly | $5 | **22** | 20 to 50 | no — hourly $5-20 |
| 957656 | 8.1h | WordPress/WooCommerce Store Build — Small SA Online Store  | fixed | $180 | **9** | 5 to 10 | YES |
| 846320 | 8.4h | WordPress / WP rocket Speed and Website optimization | fixed | $200 | **14** | 10 to 15 | YES |
| 570794 | 8.6h | Expert WordPress Developer | fixed | $4,000 | **19** | 50+ | no — 140-160h engagement |
| 348525 | 8.7h | Webflow Developer Needed to Migrate
a B2B SaaS Marketing S | fixed | $150 | **18** | 20 to 50 | no — Webflow |
| 964397 | 8.9h | WordPress Developer for Quick Customization | fixed | $50 | **14** | 20 to 50 | YES |
| 167395 | 11.6h | WordPress/Elementor Designer & SEO Expert – Medical Websit | fixed | $450 | **14** | 20 to 50 | no — Elementor+SEO |
| 133674 | 12.8h | Full redesign of my WordPress website | fixed | $2,750 | **13** | 50+ | YES |
| 925623 | 13.3h | Créateur de sites WordPress ( elementor) – sites d'entrepr | fixed | $1,000 | **13** | 10 to 15 | no — Elementor+long-term |
| 503270 | 13.3h | WordPress troubleshooting is required. | fixed | $50 | **9** | 20 to 50 | YES |
| 676906 | 13.9h | WordPress Speed Optimization Expert | fixed | $50 | **14** | 20 to 50 | YES |
| 897975 | 14.1h | Senior WordPress DevOps & Cloudflare Engineer | fixed | $300 | **7** | 20 to 50 | YES |
| 686506 | 14.6h | WordPress Developer Needed to Build a Single Landing Page  | fixed | $60 | **18** | 20 to 50 | YES |
| 162214 | 14.6h | Content & SEO Specialist (WordPress, Elementor & AI) | fixed | $500 | **14** | 50+ | no — content/SEO |
| 073322 | 15.1h | Wordpress Developer with CRM integration | fixed | $300 | **13** | 10 to 15 | YES |
| 355686 | 15.9h | WordPress / WooCommerce Meta Pixel /GTM   Conversion Track | fixed | $25 | **11** | 10 to 15 | no — pixel/GTM marketing |
| 709482 | 16.1h | Wordpress & WooCommerce Developer Needed - Elementor - Web | fixed | $250 | **16** | 20 to 50 | no — Elementor-primary |
| 000938 | 17.1h | Shopify & WordPress Developer – Custom Coding & Website De | fixed | $200 | **18** | 20 to 50 | no — Shopify+long-term |
| 280611 | 17.1h | WordPress Developer for Food Website Redesign | fixed | $20 | **14** | 20 to 50 | YES |
| 980258 | 17.8h | Help with clearing cache. Fix WordPress,elementator and si | fixed | $100 | **18** | 10 to 15 | YES |
| 145820 | 18.4h | WordPress Website for Vacation Rental Management Business  | fixed | $1,000 | **13** | 50+ | YES |
| 207884 | 18.9h | Premium WordPress Website Development for Optical Store | fixed | $80 | **14** | Fewer than 5 | YES |
| 245838 | 19.6h | WordPress TECHNICAL SEO Specialist Needed for Established  | fixed | $1,000 | **22** | 50+ | no — SEO audit |
| 957388 | 20.3h | WordPress/WooCommerce developer — B2B dealer portal, domai | fixed | $5,500 | **26** | 50+ | no — 6-10wk portal |
| 540066 | 23.5h | Elementor Design Expert Needed for Two Custom WordPress Te | fixed | $50 | **14** | 15 to 20 | no — Elementor design |
| 735319 | 24.1h | WordPress Developer needed for Local Business Showcase Web | fixed | $100 | **14** | 20 to 50 | no — Elementor/Divi+LT |
| 767685 | 24.6h | WordPress Site Optimization Specialist | fixed | $350 | **13** | 10 to 15 | no — already hired |
| 583196 | 25.2h | Expert WordPress Developer Needed to Setup Demo Website | fixed | $25 | **14** | 20 to 50 | no — content updates |
| 159910 | 25.3h | Integrate Web Badging API into WordPress PWA | fixed | $75 | **18** | 20 to 50 | YES |
| 557094 | 29.2h | Wordpress Developer for Quick Woocommerce Fix | fixed | $50 | **7** | Fewer than 5 | YES |
| 896482 | 29.4h | Build a new wordpress website for start up business | fixed | $300 | **11** | 20 to 50 | YES |
| 835490 | 30.0h | WordPress/Elementor Developer to Build 12 Child Pages from | fixed | $1,200 | **27** | 50+ | no — Elementor pages |
| 676933 | 30.9h | WordPress Website Migration and Complete Ownership Transfe | fixed | $800 | **27** | 50+ | YES |
| 118236 | 31.0h | Experienced WordPress Developer Needed - Website Redesign, | fixed | $5,000 | **14** | 50+ | no — large 3-6mo scope |
| 324101 | 31.3h | Quick WordPress & SEO Migration Cleanup (Fix 404s & Redire | fixed | $100 | **14** | 20 to 50 | YES |
| 645988 | 33.7h | Wordpress Web Designer needed for UI UX Design Moodboard | fixed | $50 | **7** | 10 to 15 | no — design-only |
| 306263 | 33.7h | WordPress Blacklist Removal Specialist – Google Safe Brows | fixed | $100 | **14** | 20 to 50 | YES |
| 365090 | 34.0h | Wordpress Developer (Elementor + ACF) | fixed | $300 | **18** | 50+ | no — Elementor+ACF |
| 961183 | 36.0h | Rebuild a WordPress website using Elementor page builder | fixed | $100 | **14** | 15 to 20 | no — Elementor+$5/hr |
| 304924 | 36.4h | WordPress Developer Needed  for Small Website | fixed | $25 | **14** | 20 to 50 | YES |
| 092390 | 36.5h | Fix WordPress SSL Issue | fixed | $55 | **13** | 20 to 50 | no — already hired |
| 086438 | 37.9h | WordPress Website Clean-Up and Optimization | fixed | $300 | **11** | 20 to 50 | YES |
| 200314 | 39.1h | WordPress to Shopify Migration Expert | fixed | $50 | **14** | 15 to 20 | no — to Shopify |
| 507570 | 39.8h | CRO-Focused Landing Page Designer & WordPress Developer | fixed | $95 | **16** | 15 to 20 | no — CRO/design |
| 071285 | 39.8h | Long-Term WordPress & Wix Developer for Marketing Agency | fixed | $600 | **14** | 50+ | no — Wix+long-term |

*Sources: `upwork__find_jobs` search/smart_search/get, org_uid 2102952945681921910, Freelancer Basic plan. Raw discovery dataset: `upwork-mcp-job-discovery-raw.json`.*
