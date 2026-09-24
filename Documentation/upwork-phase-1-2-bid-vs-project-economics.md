# Upwork Economic Viability — Phase 1.2: Bid vs Standing Projects Economics

Date: 2026-09-24 · Evidence base: Phase 1.1 corpus (438 jobs, 61 detail samples) + Upwork platform documentation + search-indexed Project Catalog pages · Account: Freelancer Basic, $35/hr profile rate, zero history, 0 Connects

Evidence labels: **A** = directly measured · **B** = directional · **C** = hypothesis · **D** = unknown/unobservable. Platform marketing claims are labeled as such.

---

## 1. Executive summary

The two acquisition hemispheres have **non-overlapping cost structures**:

- **Bidding** is pay-per-attempt: every proposal costs ~$17 effective (≈$2.10 Connects + ~30 min labour). Volume is controllable, feedback arrives in days, and failure cost is bounded — but marginal cost per attempt never falls.
- **Standing Projects** are pay-once-create: ~2–4h setup per Project, near-zero marginal cost per potential sale, a durable externally-linkable URL, and a purchase mechanism with no proposal friction — but discovery is unpriced and unproven for a zero-review account.

The models are not substitutes: bidding buys *attempts at existing demand*; a Project is a *checkout endpoint* that converts demand generated elsewhere (catalog search, portfolio site, GitHub, case studies). The evidence supports a **complementarity hypothesis** — bid first for fast feedback and reviews, Projects as persistent endpoints for the same archetypes — not a substitution.

## 2. The two acquisition hemispheres

| | Bidding Gigs | Standing Projects (Project Catalog) |
|---|---|---|
| Demand origin | client posts a specific need | supplier defines a purchasable service |
| Supplier action | find + propose + wait | create once + maintain visibility |
| Marginal cost per attempt | ~$17 effective | ~$0 (after setup) |
| Transaction initiation | client shortlists → offer | client purchases directly |
| Persistence | proposal dies with the job | URL persists; linkable externally (A — Upwork documents share links) |

## 3. Bidding Gig economics (consolidated from Phase 1.1 — A/CALC)

- Relevant posted demand: ~20–30 observable jobs/day across the winning vocabulary set (email/DNS, sysadmin, WP-hosting-DNS, migration/access-crisis slices)
- Per-bid cost: median 14 Connects (range 6–27; n=61) ≈ $2.10 + ~30 min proposal labour ($15 imputed) ≈ **$17/bid**
- Competition: median proposal-tier midpoint 17.5–35; 15% of <24h jobs already at 50+; archetype-level saturation 0–31%
- Dead/stalled share of aged visible inventory: ~55% (27% dead + 27% stalled funnels)
- Formal gates on ~11% of sampled posts (JSS 80–90, earnings floors, geography) — rising with post value
- Fill velocity: urgent jobs hire within days (4/8 migration-area samples already hired)
- Fee: **variable 0–15% per contract, shown before offer/contract, fixed once started** (A — current Upwork fee model; the old flat-10% era has ended)
- Win rate: **D — unmeasured; the controlling unknown**
- Required win rates for viability (CALC): ≥10% on $300+ work; ≥20% on $150–400 work; sub-$100 is unprofitable at any realistic rate
- Repeat/follow-on: ~15–20% of sampled clients show related posts; chains observed (migration→email-breakage→deliverability; compromise→hardening)
- Scalability: linear — each additional attempt costs the same ~$17

## 4. Standing Project economics

### Mechanics (A — platform documentation)

- Supplier creates a pre-scoped package: category, deliverables, requirements, delivery days, revisions
- Pricing: **$5–$500,000**; 1 or 3 tiers (Starter/Standard/Advanced) + add-ons (e.g., expedited delivery)
- Max 20 live Projects + 20 in review; human review before publication
- **Requirements gate**: client must submit mandatory inputs within 48h or the order auto-cancels and refunds — a built-in scope-entry control that protects supplier time
- Delivery clock starts on requirements receipt, not purchase
- Visibility toggle + concurrency cap (default 20 active orders)
- Same freelancer service fee applies (0–15% variable)
- A third adjacent product exists: **Consultations** — paid 30/60-min bookable sessions (max 3, eligibility-gated) — structurally a purchasable diagnostic conversation; relevant to the diagnosis-first archetype but currently untestable here

### Observed catalog evidence (B — search-indexed pages; direct fetch 403-blocked)

- Real technical Projects exist in the target archetypes: WordPress malware/security ("secure, clean WordPress site — 1 day delivery"), Core Web Vitals speed optimization (1-day delivery, add-on pricing observed: "+$200 / +2 days"), AWS server setup, NIST InfoSec roadmap, WooCommerce builds
- Catalog also contains junk (a "cracked software" listing) — moderation is imperfect
- Third-party claim (ESTIMATE, not verified): strong knowledge-work listings price ~$150–300 basic / $500–1,500+ premium

### Project cost structure (CALC/ASSUMPTION)

- Setup: ~2–4h per Project (copy, tier design, gallery, requirements) — one-time
- Maintenance: low — edits + visibility toggling; but review accumulation is the real asset
- Per-sale marginal acquisition cost: ~$0 cash; **the unpaid cost is discovery generation**
- Per-sale economics at $250/4h delivery: $212–225 net → **$53–56/hr** before discovery cost — matching bidding on a $400 job at ~20% win rate, *if* the sale happens

### The unpriced variable: discovery (D)

No observable data on: catalog search ranking factors for a zero-review account, per-Project view counts, conversion rates, or organic sales velocity. Upwork's own claim that shared links get "2x more views and 3x more purchases" is platform marketing — directionally plausible (it means external traffic is a designed-for behavior) but not a measured conversion rate.

## 5. External-acquisition economics

**A (mechanics):** Projects have durable public URLs (`/services/product/...`); Upwork explicitly supports sharing them on external sites; visibility-off keeps the page viewable but unpurchasable. A Project URL is therefore a genuine **persistent acquisition endpoint** — the portfolio site's case studies (or GitHub READMEs) can terminate in a purchasable transaction with platform payment protection, without the client ever posting a job.

**D (unmeasurable here):** external-traffic conversion rate; whether clients will purchase a service from a zero-review Upwork account reached via a portfolio link; whether Upwork's payment-protection framing helps or the platform-branding hurts.

**Structural note (B):** external linking moves the trust burden — the portfolio/case-study does the convincing, the Project does the transacting. This is the only acquisition route where *Marc's existing assets* (portfolio site, technical case studies) participate directly in the funnel.

## 6. Same service, two routes — worked comparison

Service: **email/DNS deliverability diagnosis-and-fix** (observed at $100–300 in bids; the $250 urgent post is the reference).

| | Bid route | Project route |
|---|---|---|
| Client state | already hurting, posted today | hurting, searching or referred |
| Supplier cost to attempt | ~$17 | ~$0 marginal |
| Conversion friction | proposal vs 17–35 competing proposals | purchase decision on a fixed package |
| Win mechanism | write better proposal, fast | client self-selects on defined scope |
| Price control | client-set budget (often low) | supplier-set tiers |
| Scope control | negotiate per-job | requirements gate + defined deliverables |
| Trust requirement | profile competes blind | package + reviews carry weight |
| EV at 10% win / unknown conv. | $250×0.85 − $170 = **$42 net** | $250×0.85 − discovery cost = **$212 net per sale** |
| Failure mode | repeated $17 losses | zero sales = setup cost lost (~3h) |

The Project route has ~4× better per-transaction economics **conditional on a sale occurring**. The bid route has measurable demand and controllable attempt volume. The conditioning variable is exactly what neither evidence nor documentation provides.

## 7. Project archetypes suited to each model

| Archetype | Bid fit | Project fit | Why |
|---|---|---|---|
| Deliverability diagnosis + fix | ✓ strong | ✓ strong | bounded, verifiable deliverable; recurring |
| DNS/SSL/record repair | ✓ (but cheap) | ✓ strong | perfectly packageable; $50–150 tier |
| Security/malware cleanup | ✓ | ✓ | exists in catalog already |
| Speed/CWV optimization | ✓ | ✓ | exists in catalog (1-day delivery observed) |
| Audit-first migration | ✓ strong | partial | audit milestone packageable; migration itself too variable |
| Access-crisis recovery | ✓ | ✗ weak | urgency doesn't wait for requirements-gate; crisis buyers post jobs |
| Sysadmin ongoing ops | ✓ (hourly) | ✗ | recurring support is not a fixed package |
| Integration builds | ✓ | ✗ weak | scope too variable to package safely |
| Legacy/EOL modernization | ✓ | ✗ | inherently unpackageable |
| "Diagnostic report" (generic) | weak | ✓ **the signature Project** | bounded deliverable: written diagnosis + fix plan; naturally tiered; upsells to custom work |

The pattern (**B**): packageable = bounded deliverable + repeatable scope + verifiable output. Diagnostic and repair-with-defined-boundary work fits Projects; open-ended investigation and recurring ops fit bidding (or post-purchase custom offers).

## 8. Client acquisition behaviour

| Dimension | Client posts job (bid) | Client buys Project |
|---|---|---|
| Buying intent | declared, active | declared, active — arguably *higher* (purchase is a stronger intent than posting) |
| Friction for client | write post, sift proposals | search → compare packages → purchase |
| Trust requirement | freelancer must prove in proposal | package + price + reviews prove |
| Price sensitivity | high (budgets often set low) | anchored by tier design (B — third-party tier-pricing guidance) |
| Scope clarity | often poor (34% underspecified) | supplier-defined by construction |
| Decision time | days (interview funnel observed: up to 39 invites/15 interviews) | can be minutes — purchase is direct |
| Client qualification | none required to post | payment method required to purchase |
| Repeat likelihood | ~15–20% of clients show related posts (A) | repurchase possible; workload cap exists (A) |

## 9. Complementarity analysis

| Combination | Evidence |
|---|---|
| BID → reviews → stronger Project ranking | **B** — platform docs confirm feedback drives catalog search placement; review accumulation starts with transactions, and bidding is the fastest route to first transactions |
| PROJECT → custom/follow-on work | **B** — requirements stage surfaces real problems; audit-type deliverables naturally expose the fix work (1.1D chain evidence) |
| Portfolio/GitHub → Project → purchase | **C** — mechanics confirmed (shareable URL); conversion unmeasured |
| BID → discover demand → create matching Project | **C** — the corpus is a Project-design dataset (archetypes, price bands, scope language) |
| PROJECT → Consultation upsell | **C** — consultations exist (A) but eligibility/fit unverified |
| Projects replace bidding | **Not supported** — zero discovery evidence for a fresh account |

## 10–13. Scenarios (monthly, per archetype; ASSUMPTION-labeled)

Assumptions: bid cost $17, proposal 0.5h, diagnostic job value $250, delivery 4h, fee 15% (worst case), Project setup 3h one-time, maintenance 1h/mo.

**Bidding-only** (10 bids/mo on ungated $150–500 diagnostics):
- 5% win → 0.5 wins → revenue $106 net of fee − $170 acq = **−$64/mo, ~9h**
- 10% win → 1 win → $212 − $170 = **+$42/mo, ~9h**
- 20% win → 2 wins → $425 − $170 = **+$255/mo, ~13h**

**Projects-only** (3 Projects, no external traffic):
- 0 sales → **−~4h/mo maintenance** (setup amortized separately)
- 1 sale/mo → $212 − ~$8 setup-share → **~$204/mo, ~5h** — but sale probability is D-unknown
- The failure mode is *silent zero*, not monetary loss

**Mixed** (recommended shape):
- Bidding produces income feedback + reviews; Projects convert portfolio/case-study traffic and repeat buyers
- Bids fund the review accumulation that makes Projects sellable; Projects give each completed bid a repurchase endpoint

**Break-even logic**: bidding wins whenever discovery×conversion < win-rate equivalent. Formally: Project EV/mo = P(sale)×$212; Bid EV/mo = B×(WR×$212 − $17). At 10 bids/mo the Project path needs only ~0.8–1.0 sales/mo to match a 10% win-rate bid funnel — but that P(sale) is precisely the unmeasured quantity. **B**

## 14. Sensitivity — variables that matter most

1. **Win rate** (bidding): the whole bid model hinges on it; only live bidding measures it
2. **Project discovery rate** (standing): hinges on catalog ranking + external traffic — measurable only by publishing
3. Fee tier (0–15%): ±$12–37 per $250 transaction — secondary
4. Delivery time overrun: each +1h on a $250/4h job cuts effective rate ~$11 — real but bounded
5. Proposal prep time: cutting 30→15 min halves acquisition cost — process leverage, measurable immediately

## 15. Platform constraints (A — verified current rules)

- Connects: median 14/bid; balance 0 on this account — first bids require purchase
- Freelancer fee: **variable 0–15% per contract**, disclosed before commitment, locked at start
- Project Catalog: ≤20 live; review-gated publication; requirements auto-cancel at 48h; $5–500k pricing; tiers + add-ons; visibility + concurrency controls; direct share links explicitly supported
- Consultations: ≤3, eligibility-gated ("if you're eligible you'll see the option")
- No contact-info sharing pre-contract (applies to Projects too)
- Contract initiation fee (client-side, ≤$4.99 under $100 contracts) — small friction on cheap purchases
- Boost/visibility ads exist (availability badge = recurring weekly Connects charge) — a paid-discovery lever for later

## 16. Evidence quality

- **A**: bid-side costs/competition/lifecycle (61 gets), platform mechanics, fee model, Project rules, share-link support
- **B**: catalog pricing norms, archetype fit, review-driven ranking, repeat-purchase potential
- **C**: external-traffic conversion, Project sales velocity for new accounts, consultation eligibility
- **D**: any per-Project sales/conversion data; catalog search visibility for a 0-review profile

## 17. Unknowns requiring measurement

1. Project-side conversion for a zero-review account (both catalog-organic and externally-linked)
2. Whether catalog discovery alone produces any sales without external traffic
3. Consultation eligibility for this account
4. Actual fee % offered on first contracts (0–15% band)
5. Win rate (carried from 1.1 — unchanged)

## 18. Implications for Phase 1.3

The two hemispheres answer different questions and can be tested in parallel for ~the cost of the bid test alone:

1. **Bid experiment** (from 1.1E): 15–25 targeted proposals → measures win rate + response. Cost ~$30–55 Connects + ~10h.
2. **Project experiment**: publish 2–3 diagnostic Projects matching the proven archetypes (email/DNS diagnosis-and-fix; WP emergency-recovery assessment; speed-audit) + link them from the portfolio site's case studies → measures whether the persistent-endpoint model generates any inbound at all. Cost ~6–10h setup, $0 cash.
3. **Complementarity is testable**: bids link portfolio → portfolio links Projects → reviews accumulate. The two tests share assets.

**Direct answer to the phase question**: bidding produces *measurable, controllable* acquisition at ~$17/attempt with negative unit economics below $200 job value; Projects produce *unmeasured, uncontrollable* discovery at ~$0/attempt with strong per-sale economics (~$53/hr at $250/4h) and genuine persistence+linkability. Neither is sufficient alone at current evidence. The combination — bids for fast feedback and review-seeding, Projects as persistent conversion endpoints for externally-generated trust — is the only model consistent with all observations. Which hemisphere ultimately dominates is unanswerable until both measurements exist.
