# Upwork Economic Viability — Phase 1 Report

Date: 2026-09-24
Status: Complete (read-only analysis; no proposals submitted, no Connects consumed)
Dataset: `upwork-mcp-job-discovery-raw.json` — 58 unique WordPress-tagged jobs collected 2026-09-24 ~03:00–03:47 UTC via `upwork__find_jobs` (search pages 1–5, `title=WordPress`, fixed, budget≥$20, sort=recency; smart_search `mode=most_recent`, `days_posted=1`, `skills=[WordPress]`, pages 1–3).

Evidence labels: **FACT** (vendor-documented) · **OBSERVED** (measured in this session's data) · **CALC** (computed) · **ASSUMPTION** (estimated, untested) · **UNKNOWN** (not determinable yet)

---

## 1. Economic assumptions

Marc's constraints are as stated in the prompt; no personal income target was provided, so all thresholds are parametric.

| Parameter | Value | Label |
|---|---|---|
| Freelancer service fee | **Variable 0–15% per contract** since 2025-05-01 (rate set at proposal submission, locked for contract life; older flat-10% sources conflict). Modeled at 10% and 15% | FACT (range) / UNKNOWN (per-contract value) |
| Connects price | $0.15 each, bundles of 10 min, no bulk discount | FACT |
| Connects per proposal | **9 observed** on a $50 job; third-party guides cite 4–16 typical | OBSERVED (n=1) |
| Free Connects | 10/month on Basic; up to 50 one-time new-account bonus (conditional on a Connects purchase or Plus subscription); 100/month on Freelancer Plus $19.99/mo | FACT |
| Account plan (Marc) | Freelancer Basic; `connects_balance` = **0** | OBSERVED |
| Membership required to bid | None — Basic bids free of subscription | FACT |
| Proposal prep time | 15–30 min manual; 5–10 min MCP-assisted drafting | ASSUMPTION |
| Discovery + evaluation time | ~10 min/job manual; ~2–3 min/job via MCP pipeline | ASSUMPTION |
| Per-bid total acquisition time | ~30 min manual / ~10 min assisted (central values) | ASSUMPTION |
| Delivery hours per tier | Low $50→2–4h; Median $180→6–12h; High $500→15–30h | ASSUMPTION — largest single unknown |
| Win rate | No reliable data; scenarios 1/2/5/10% modeled | UNKNOWN → scenarios |

## 2. General viability findings

**Project-value statistics (OBSERVED, n=51 fixed-price jobs):**

- min $20 · p25 **$50** · median **$180** · mean $592 · p75 **$500** · max $5,500
- Distribution: <$50: 4 · $50–99: 15 · $100–299: 11 · $300–999: 12 · ≥$1,000: 9
- The head of the distribution ($1k–5.5k) exists in volume but skews to redesign/team/long-duration work; the WorkBot sweet spot ($50–500, <1mo) is ~70% of observed fixed-price supply.

**Thresholds a viable channel must produce (CALC/ASSUMPTION):**

- *Minimum viable project value:* ~$100+ gross. Below ~$100, Connects cost (~$1.35/bid observed) plus 10–15% fee plus proposal time makes EV marginal even at 10% win rate. **CALC**
- *Acceptable acquisition effort:* ≤~10 min/bid (assisted) — at 20 bids/win that's ~3.3h unpaid per project. Manual 30 min/bid → ~10h unpaid per win, which breaks the model below $180. **CALC**
- *Required projects/month:* parametric — e.g., a $2,000/mo target needs ~11 median ($180) wins, ≈110–550 proposals/mo at 10–2% win rate, ≈18–92h unpaid acquisition time. **CALC/ASSUMPTION**
- *Sustainable effective hourly:* the model yields ~$5–26/h all-in depending on tier/win-rate/delivery speed — see §3. **CALC**

## 3. Bid-vs-project economics

Required inputs answered from the dataset:

| # | Item | Answer | Label |
|---|------|--------|-------|
| 1 | Bids per project | `proposals_tier` only on Basic: median tier "20 to 50"; midpoint est ~30/job | OBSERVED (tiered) |
| 2 | Typical value | median $180 fixed | OBSERVED |
| 3 | Distribution | see §2 | OBSERVED |
| 4 | Bid cost | ~9 Connects ≈ $1.35 (observed n=1; range 4–16) | OBSERVED/ASSUMPTION |
| 5 | Platform fee | 0–15% variable per contract | FACT |
| 6 | Membership cost | $0 required; Plus $19.99/mo optional (adds exact proposal counts, 100 Connects) | FACT |
| 7 | Connects cost | $0.15 each | FACT |
| 8 | Discover/evaluate time | ~10 min manual; ~2–3 min via MCP | ASSUMPTION |
| 9 | Proposal prep time | ~15–30 min manual; ~5–10 min assisted | ASSUMPTION |
| 10 | Win rate | no data | UNKNOWN |
| 11 | Scenarios | modeled below | CALC |

**EV model — fee 10%, 9 Connects/bid, assisted acquisition (10 min/bid):**

| Tier | Win% | Bids/win | Connect$/win | Unpaid min/win | Gross | Net pre-tax | Eff. $/h (fast\|slow delivery) |
|---|---|---|---|---|---|---|---|
| $50 | 1% | 100 | $135.00 | 1000 | $50 | **−$90.00** | −$4.8 \| −$4.4 |
| $50 | 2% | 50 | $67.50 | 500 | $50 | **−$22.50** | −$2.2 \| −$1.8 |
| $50 | 5% | 20 | $27.00 | 200 | $50 | $18.00 | $3.4 \| $2.5 |
| $50 | 10% | 10 | $13.50 | 100 | $50 | $31.50 | $8.6 \| $5.6 |
| $180 | 1% | 100 | $135.00 | 1000 | $180 | $27.00 | $1.2 \| $0.9 |
| $180 | 2% | 50 | $67.50 | 500 | $180 | $94.50 | $6.6 \| $4.6 |
| $180 | 5% | 20 | $27.00 | 200 | $180 | $135.00 | $14.5 \| $8.8 |
| $180 | 10% | 10 | $13.50 | 100 | $180 | $148.50 | $19.4 \| $10.9 |
| $500 | 1% | 100 | $135.00 | 1000 | $500 | $315.00 | $9.9 \| $6.7 |
| $500 | 2% | 50 | $67.50 | 500 | $500 | $382.50 | $16.4 \| $10.0 |
| $500 | 5% | 20 | $27.00 | 200 | $500 | $423.00 | $23.1 \| $12.7 |
| $500 | 10% | 10 | $13.50 | 100 | $500 | $436.50 | $26.2 \| $13.8 |

At 15% fee, nets drop ~$2.50/$9/$25 by tier; at 16 Connects/bid ($2.40), add ~$0.95–$2.40 × bids to acquisition cost. Full tables in computation notes.

**Reading:** low-tier jobs are net-negative below ~3–4% win rate (Connects alone exceed the fee-adjusted margin). Median tier breaks even ~1–2%. High tier stays positive even at 1% but delivery-time risk dominates. Effective hourly is bounded roughly **$1–26** — the economics only work if win rate ≥~3–5% *and* delivery is fast *and* proposal cost stays assisted (~10 min).

## 4. Competition / time decay

`proposals_tier` midpoint estimate vs. job age (OBSERVED, cross-sectional snapshot — not a longitudinal track):

| Age bucket | n | Midpoint est. proposals |
|---|---|---|
| <1h | 3 | ~22 |
| 1–6h | 6 | ~27 |
| 6–12h | 11 | ~32 |
| 12–24h | 18 | ~33 |
| >24h | 20 | ~34 |

**Interpretation (CALC + inference flagged):** Jobs arrive already carrying ~10–20 proposals within the first hour; growth is rapid to ~6h then plateaus ~33–35. Early access (<1h) faces roughly **⅔ the competition** of a day-old job — a real but moderate edge, not a decisive one. *Inference caveat:* cross-sectional data; tier granularity is coarse; survival/mix effects not controlled. A longitudinal re-poll of the same job IDs would refine this.

## 5. Bootstrap test

| Requirement | Answer | Label |
|---|---|---|
| Initial cash | $0–~$15. New-account bonus (up to 50 Connects) is conditional on first Connects purchase (~$1.50 min) or Plus. 10 free/month on Basic. Realistically one $10–15 Connects purchase to sustain ~30–60 proposals | FACT/CALC |
| Membership | None required; Plus optional ($19.99/mo) — buy only if exact proposal counts materially improve targeting | FACT |
| Verification | ID verification badge exists; payment method required only to *buy* Connects; payout method needed to get paid | FACT |
| Reputation | No hire/JSS gate observed on searched jobs; `preferred_qualifications` exposed per job (most sampled: "All freelancers", no JSS minimum) | OBSERVED (limited n) |
| Geography | Client-side country filters exist; no freelancer geo-block observed. Location-independent OK | OBSERVED |
| Automation | MCP is official; write tools are confirmation-gated (preview→confirm). Proposal *submission* consumes Connects — automation must respect that | FACT/OBSERVED |
| Min viable proposal volume | ~10–20 targeted proposals/mo feasible on ~$3–20 Connects spend | CALC |

**Verdict:** bootstrap is possible with ~$10–15 cash and no subscription — *if* win rate reaches ~5% within the first ~50 bids. Whether a zero-reputation account can hit 5% is the crux UNKNOWN.

## 6. Sensitivity analysis

| Variable | Direction | Effect |
|---|---|---|
| Project value ↑ | $50→$500 | Connect cost fixed ⇒ net margin scales ~linearly; high-tier stays EV+ even at 1% win |
| Win rate | 1%→10% | Nonlinear: Connects-per-win $135→$13.50; low tier flips positive only above ~3% |
| Proposal time | 30→10 min/bid | Unpaid acquisition per win: 50h→16.7h at 2% win — the single largest lever after win rate |
| Bids/win (competition) | tracked via proposals_tier | Rising competition lowers win rate; early-access edge ~1.5× (§4) |
| Fee | 10%→15% | −$2.50/−$9/−$25 per win by tier — material on low tier, noise on high |
| Job volume | 58 unique/34h observed in one niche | Supply is not the constraint; ~50 new matches/day plausible. Connects budget caps bid volume instead |
| Connects/bid | 9→16 | +$0.95/bid; at 2% win adds ~$48/win — meaningful on low tier |

## 7. Major economic failure points

1. **Sub-$100 jobs at low win rate are value-destructive** — Connects + fee + time exceed net revenue. **CALC**
2. **Win rate is everything** and is unknown for a zero-history account; below ~3% the channel loses money outright. **UNKNOWN**
3. **Unpaid acquisition time** can exceed paid delivery time at ≤2% win rates even with automation. **CALC**
4. **Delivery-time overrun** on fixed-price turns a $500 job below minimum wage if scope doubles. **ASSUMPTION-driven risk**
5. **Variable fee (0–15%)** is set per contract at bid time — worst-case 15% must be assumed until the shown rate is observed repeatedly. **FACT/UNKNOWN**
6. **Connects inflation:** observed 9/job vs. documented 4–6 typical — if real costs trend 12–16, low-tier economics degrade further. **OBSERVED (n=1)**

## 8. Unknowns requiring real-world testing

- Actual win rate for this account/profile (only measurable by bidding — consumes Connects)
- Per-contract fee % shown at proposal time (0–15% range)
- Whether `connects_cost` scales with budget or competition (need `get` across tiers)
- True delivery hours per job type (retro after first completions)
- Longitudinal proposal accumulation (re-poll job IDs at +1h/+6h/+24h)
- Whether profile gaps (no JSS, no portfolio) get auto-filtered by clients regardless of proposal quality

## 9. Raw evidence

- `Documentation/upwork-mcp-job-discovery-raw.json` — 58 jobs, full fields
- `upwork__find_jobs/get` on job 2102766397589503270: `connects_cost=9`, `connects_balance=0`, `plan=Freelancer Basic`, `activityStat.totalHired=1`, `preferred_qualifications` all-open
- Tool schema text for `find_jobs` (search/smart_search/get param docs)
- Upwork docs (web): Connects $0.15 & bundles; Basic 10/mo; Plus $19.99/100; up-to-50 new-account bonus; variable 0–15% contract fee (May 2025) — secondary source conflict on flat-10% noted
