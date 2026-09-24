# Upwork Phase 1.1A — Technical Universe Scan

**Date:** 2026-09-24 · **Status:** Complete (read-only; no proposals, no writes, zero Connects consumed)
**Baseline:** `upwork-phase-1-1-general-economic-viability.md` (WordPress-niche economics), `upwork-connects-cost-test-report.md` (Connects distribution), `upwork-mcp-job-discovery-raw.json` (58-job WP corpus).
**New evidence this phase:** 348 unique job records across 39 search probes covering 21 subcategories, 1 category, 10 title filters, and 7 query filters, collected ~03:55–05:30 UTC 2026-09-24. Raw dataset: `upwork-phase-1-1a-technical-universe-raw.json`.

Evidence labels: **FACT** · **OBSERVED** · **CALC** · **ASSUMPTION** · **UNKNOWN**

This phase is **discovery, not ranking**. No niche is declared a winner; §6 lists candidates for deeper investigation and §7 lists areas that look structurally unattractive.

---

## 1. Executive findings

1. **Paid technical demand exists across the entire universe sampled.** Every populated probe returned live jobs. Observable posting volume varies ~3 orders of magnitude by area: Web Development ~160+ jobs/day at the top end down to ~1/day for Magento-specific or firewall-specific phrasing, and literal zero for COBOL/mainframe. **OBSERVED/CALC**

2. **The market splits into two economic regimes.**
   - *Commodity regime:* high volume, low budgets, heavy competition — generic web builds, Shopify store setup/listings, mobile app builds, scraping/lead-gen, microtask QA/testing, AI data-labeling. **OBSERVED**
   - *Specialist regime:* lower volume, higher rates, thinner competition — platform migrations (M365/Entra tenant-to-tenant, Magento EOL upgrades, Drupal 10, Salesforce Classic→Lightning, AD 2016→2025), incident response (Magento payment skimmer), infrastructure troubleshooting (FileMaker Server, SAP HANA/Veeam, Aurora PostgreSQL perf, ClickHouse self-hosting), email/DNS deliverability, embedded/IoT, blockchain. **OBSERVED**

3. **Specialist work skews hourly; commodity work skews fixed.** Overall sample: 226 hourly / 122 fixed (65/35) — the inverse of the Phase 1.1 WordPress corpus (12% hourly). Hourly median posted-minimum $16 (p25 $10, p75 $30, p90 $45); fixed median $100 (p25 $29, p75 $500, p90 $1,570, max $125,000). Specialist areas routinely post $30–120/hr; blockchain $45–170/hr. **OBSERVED/CALC**

4. **Troubleshooting/repair/diagnostic demand is not a WordPress-only phenomenon.** Equivalent repair work appears in every technical area: n8n workflow debugging, Stripe webhook failures, Databricks debugging (due next day), Magento malware/skimmer incident response, M365 tenant lockout recovery, VB.NET→QuickBooks integration failure ("need an immediate answer"), DNS/email-domain blocking, Lovable-built apps needing productionizing. Keyword-signal share of sampled jobs labelled repair-flavored: malware query 60%, speed-optimization 50%, WordPress title 40%, Network & SysAdmin 40%, Magento 40%, Desktop App Dev 40%, Scripts & Utilities 30%. **OBSERVED** (heuristic — keyword signal on title+snippet, not manual classification)

5. **"Paid diagnostics" is a real deliverable category.** Jobs paying for assessment/audit/roadmap rather than implementation: AWS implementation gap analysis ($500 fixed), eCommerce platform migration roadmap (Magento/Shopify/Sylius, $30–45/hr), Cloud/DevOps assessment for an existing platform, WCAG 2.2 AA compliance audit ($50 fixed), SOC 2 audits, ISO 27001 audit pools, code review for a court case. Short, bounded, expertise-priced work. **OBSERVED**

6. **Competition (proposal tiers) is unevenly distributed and does not track difficulty.** 50+ tier share: React title 50%, scraping title 50%, Data Extraction/ETL 40%, DevOps subcat 40%, PHP title 40%, legacy-migration query 56% — versus ~0% in Blockchain, VPN/firewall, Network & SysAdmin subcat, InfoSec subcat, Zapier query, Game Dev, Other-Software-Dev, AI&ML, Customer Service & Tech Support, Engineering & Architecture. *Confound: proposal counts accumulate with post age; narrow recency samples contain older posts.* **OBSERVED + caveat**

7. **Credential/identity gates are real but localized.** SOC 2/ISO 27001 audit work explicitly wants CPAs/lead auditors; one AWS partner post wanted certified individuals; "US-only" and geography-restricted posts appear occasionally (Brazil device testing, Hong Kong on-site, Australia/NZ analyst); HIPAA/STQC/GMP contexts appear as domain requirements. Most technical posts observed carry no such gate. **OBSERVED**

8. **Short-contract demand (<1 month stated duration) is commonest in exactly the repair-flavored niches:** malware query 70%, Data Extraction/ETL 70%, Network & SysAdmin 60%, Desktop App Dev 60%, Scripts & Utilities 60%, scraping 60%, AWS title 50%, Stripe title 50%, Zapier query 50%, Game Dev 50%, QA 50%. **OBSERVED**

9. **Hardcore legacy is nearly absent as named work, but legacy-adjacent work is real.** `title:cobol` → zero results; `query:"COBOL FoxPro Delphi VB6 mainframe AS400"` → zero; `query:"legacy system migration modernization"` → only 9 results marketplace-wide (hasMore exhausted). Yet the same corpus contains: Magento 2.4.5 out-of-security-support upgrade, Drupal 10 migration, AD 2016→2025 runbook, Salesforce Classic→Lightning, FileMaker Server troubleshooting, VB.NET client-server app fix, Crystal Reports updates for "Merlin business software", legacy PHP/MySQL "modernize — no rewrite" (Germany). Legacy demand on Upwork wears modern labels. **OBSERVED**

10. **"AI" is the largest source of both noise and new repair demand.** AI & Machine Learning subcat (~45/day) is heavily diluted by data-labeling, voice-recording, tutoring, and eval tasks at $5–20/hr. AI Apps & Integration (~17/day) contains real builds and *fixes* (n8n+Retell integration repair, voice agents, agent prototypes) with median fixed ~$500 in sample. A recurring emergent pattern: apps built with Lovable/Cursor/AI-tools that need deployment, debugging, or productionizing — observed in Web Dev, Mobile, AWS, and Stripe probes. **OBSERVED**

---

## 2. Technical-universe taxonomy used

Upwork's actual taxonomy was probed live (invalid-value rejection returns the valid list). **FACT**

Top-level categories (12): Accounting & Consulting · Admin Support · Customer Service · Data Science & Analytics · Design & Creative · Engineering & Architecture · IT & Networking · Legal · Sales & Marketing · Translation · Web, Mobile & Software Dev · Writing.

Subcategories are a **global vocabulary** (not scoped per-category in the filter). Technically relevant ones sampled or noted:

| Sampled (21) | Related/unsampled |
|---|---|
| Web Development · Mobile Development · Ecommerce Development · Desktop Application Development · Game Design & Development · DevOps & Solution Architecture · Network & System Administration · Information Security & Compliance · Database Management & Administration · Scripts & Utilities · QA Testing · ERP/CRM Software · Data Extraction/ETL · Data Mining & Management · Data Analysis & Testing · AI & Machine Learning · AI Apps & Integration · Blockchain, NFT & Cryptocurrency · Other - Software Development · Customer Service & Tech Support · (category) Engineering & Architecture | Web & Mobile Design · Product Management & Scrum · 3D Modeling & CAD · Electrical & Electronic Engineering · Contract Manufacturing · Customer Service & Tech Support (sampled, mostly non-technical) |

Because client self-classification is noisy (a "Developer-Tool Listing Copy" writing job sits in Web Development; supermarket photography sits in Customer Service & Tech Support), title- and query-based probes were added for platform/problem niches that don't map to subcategories: wordpress · shopify · woocommerce · magento · salesforce · AWS · devops · react · python · php · stripe · scraping · cobol · malware · speed-optimization · email-deliverability · zapier-make-n8n · vpn-firewall-network · legacy-migration.

---

## 3. Evidence by technical area

Per-probe stats (n=10 newest each unless noted; `est/day` = (n−1)/span of published_date — an order-of-magnitude supply signal, not true demand):

| Probe | ~est/day | fixed/hrly | med fixed $ | med hr min | <1mo | 50+ tier | repair-kw |
|---|---:|---|---:|---:|---:|---:|---:|
| subcat Web Development | ~160 | 3/7 | $20 | $25 | 20% | 0%* | 10% |
| title wordpress | ~66 | 4/6 | $185 | $15 | 40% | 10% | 40% |
| title shopify | ~71 | 5/5 | $30 | $10 | 30% | 10% | 0% |
| title woocommerce | ~1.2 | 5/5 | $50 | $10 | 10% | 10% | 10% |
| query magento | ~1.0 | 2/8 | $800 | $18 | 20% | 20% | 40% |
| subcat Ecommerce Development | ~48 | 3/7 | $30 | $14 | 30% | 10% | 0% |
| subcat Mobile Development | ~42 | 3/7 | $15 | $15 | 20% | 20% | 0% |
| title react | ~15 | 6/4 | $1,350 | $20 | 40% | 50% | 0% |
| title python | ~17 | 6/4 | $110 | $18 | 60% | 30% | 0% |
| title php | ~8 | 6/4 | $350 | $10 | 20% | 40% | 20% |
| subcat DevOps & Solution Architecture | ~21 | 1/9 | $50 | $20 | 40% | 40% | 10% |
| title devops | ~6 | 2/8 | $2,150 | $35 | 20% | 10% | 0% |
| title AWS | ~6 | 5/5 | $200 | $35 | 50% | 20% | 10% |
| subcat Network & System Administration | ~34 | 2/8 | $125 | $20 | 60% | 0% | 40% |
| query vpn-firewall-network | ~1.2 | 1/9 | $100 | $20 | 60% | 0% | 0% |
| subcat Information Security & Compliance | ~18 | 2/8 | $300 | $8 | 30% | 0% | 10% |
| query malware-hacked | ~30 | 3/7 | $200 | $15 | 70% | 10% | 60% |
| query speed-optimization | ~18 | 4/6 | $122 | $25 | 40% | 10% | 50% |
| subcat Database Management & Administration | ~1.3 | 3/7 | $500 | $20 | 30% | 10% | 10% |
| subcat Data Extraction/ETL | ~12 | 6/4 | $112 | $9 | 70% | 40% | 10% |
| subcat Data Mining & Management | ~0.7 | 2/8 | $925 | $28 | 30% | 20% | 10% |
| subcat Data Analysis & Testing | ~27 | 1/9 | $50 | $10 | 10% | 10% | 0% |
| subcat Scripts & Utilities | ~28 | 7/3 | $75 | $15 | 60% | 0% | 30% |
| query zapier-make-n8n | ~35 | 5/5 | $75 | $18 | 50% | 0% | 20% |
| subcat AI & Machine Learning | ~45 | 1/9 | $5 | $7 | 40% | 0% | 0% |
| subcat AI Apps & Integration | ~17 | 7/3 | $500 | $75 | 20% | 20% | 10% |
| subcat QA Testing | ~22 | 5/5 | $40 | $5 | 50% | 10% | 10% |
| subcat ERP/CRM Software | ~13 | 3/7 | $70 | $28 | 30% | 10% | 0% |
| title salesforce | ~5.5 | 5/5 | $70 | $12 | 20% | 30% | 0% |
| subcat Desktop Application Development | ~10 | 4/6 | $335 | $25 | 60% | 20% | 40% |
| subcat Game Design & Development | ~14 | 5/5 | $120 | — | 50% | 0% | 10% |
| subcat Other - Software Development | ~7 | 3/7 | $750 | $40 | 20% | 0% | 0% |
| subcat Blockchain, NFT & Cryptocurrency | ~6 | 0/10 | — | $60 | 0% | 0% | 0% |
| query email-deliverability | ~12 | 2/8 | $1,900 | $15 | 30% | 10% | 10% |
| title stripe | ~3.2 | 5/5 | $20 | $15 | 50% | 20% | 20% |
| query legacy-migration | ~0.2 (9 total, exhausted) | 0/9 | — | $38 | 11% | 56% | 0% |
| title cobol | **0** | — | — | — | — | — | — |
| cat Engineering & Architecture | ~150 | 4/6 | $150 | $15 | 40% | 0% | 0% |
| subcat Customer Service & Tech Support | ~57 | 5/5 | $10 | $5 | 20% | 0% | 0% |

*0% = none of the 10 sampled jobs sat at 50+; not "no competition exists".*

### Area notes (representative observations, not cherry-picked outliers)

**General web development** — Largest visible supply (~160/day). Mix ranges from $5 fixed to $49–187/hr CTO-type roles; includes off-topic postings (copywriting, admin work). Typical competition 20–50. Commodity-dominant; specialist slivers exist (browser-security engineer C++/Rust/Chromium; Android emulator device-profile work for banking apps).

**WordPress (baseline check)** — Consistent with the Phase 1.1 corpus: ~66/day visible in title search, fixed median $185, ~40% <1mo, repair-flavored share ~40% (speed, SEO cleanup, LiteSpeed/cPanel stabilization, migration, formatting). No contradiction with prior findings. **OBSERVED**

**Shopify / generic ecommerce** — ~48–71/day but dominated by store setup, product listing, theme tweaks at $5–30 and retainers at $12–27/hr. Technical sliver: Bright Data→Shopify integration, Shopify migration specialist, custom theme sections. Mostly commodity.

**WooCommerce** — Low volume (~1/day title-visible): cart-button fix $10, Facebook Pixel attribution, plugin config $50, Printful integration, store build $180. Small-ticket repair, WP-adjacent.

**Magento** — Low volume (~1/day) but the *strongest specialist-repair signal in the scan*: URGENT security incident response / payment-skimmer investigation on a customized store; Magento 2.4.5-p1 out-of-security-support upgrade ($1,500 fixed); platform-migration roadmap ($30–45/hr); Magento 2 technical-SEO indexing issue ($100). End-of-life platform + payment risk = recurring specialist demand. **OBSERVED**

**DevOps / cloud / AWS** — Subcat ~21/day, title probes ~6/day. Real migration/assessment work: AWS gap analysis ($500 fixed), HIPAA-compliant AWS deployment, STQC e-procurement environment, Drupal 10 migration + SLA, ClickHouse self-hosting at scale ($35–60/hr), Kubernetes/Ansible/OpenShift modernization ($20–35/hr), DEX/DeFi DevOps ($45–65/hr), plus career-coaching noise. Hourly-skewed, $20–50/hr typical.

**Network & system administration** — ~34/day subcat; ~1/day for hard-networking phrasing. VPS care contracts (Contabo WP+PeerTube "check in case of trouble"), M365 tenant lockout recovery, Linux L3 support, IPv4/IPv6 consulting, SharePoint intake system, MSP remote-tech subcontract ("1 hour response"), Fortinet design advisory, FortiGate mentoring, libvirt outbound-SMTP blocking, MDM/UEM tender support, on-site superyacht Wi-Fi 7 refresh. Low proposal tiers (mostly <20). Mix of micro-budget and expert work.

**Information security & compliance** — ~18/day. Two distinct populations: (a) credential-gated audit/compliance work — SOC 2 auditor/CPA, contracted CISO, ISO 27001 lead-auditor pool, certification manager; (b) ungated practical work — WP SEO-spam malware cleanup ($5–20/hr), HIPAA backend integration, IAM hands-on training ($100), plus junk (Snapchat/Instagram account recovery). **OBSERVED**

**Databases / data engineering** — Database Mgmt is *low-volume* (~1.3/day) but specialist: Aurora PostgreSQL 17.7 performance optimization ($500), SAP HANA/SUSE/Veeam backup integration ($20–40/hr), FileMaker Server admin-delay troubleshooting ($20–58/hr), SQL Server/MongoDB/Cassandra DBA ($40–75/hr). Data Mining & Management ~0.7/day similar shape (Databricks medallion debugging due next day; Airflow/dbt ETL modernization $65–85/hr). Data Extraction/ETL ~12/day but commodity-weighted (lead scraping $5–10/hr, Excel dedupe $5) with a serious tail (SERP collection infra $25k; MaidCentral no-API session scraping $150). Data Analysis & Testing ~27/day, mostly BI/dashboards, low rates.

**Scripts, automation, Zapier/n8n/Make** — ~28–35/day combined. n8n debugging ($75, $10 fixed), Teachable/Whop/Sheets/Telegram Zapier system ($600), Python batch-processing scripts ($150, $10 homework-level), Pine Script codebase takeover ($450), Jotform logic ($75), Copilot/Power Automate setup. Real recurring "my automation broke" repair cluster; budgets bimodal ($10 vs $150–600).

**AI/ML** — High volume, heavy noise: voice-recording and evaluation microtasks at $3–20/hr alongside real work. AI Apps & Integration is the cleaner subcat: n8n/Retell debugging, AI voice-agent builds ($500–1,100 fixed), support-workflow automation ($380), drilling-company agent builds. Note several "$10 fixed" repair jobs in this space — clients underestimate broken-integration work.

**QA / testing** — ~22/day but mostly microtasks: 5-min usability tests ($20, 99 hires), beta testers ($3–10/hr), device-restricted app tests (Brazil iOS $15). Technical sliver: JMeter performance benchmark engineer, manual+automation QA retainer ($300/mo), WCAG audit. Commodity-dominant for a solo freelancer.

**ERP/CRM / Salesforce / business systems** — ~13/day subcat, ~5/day title. Specialist ecosystem: Salesforce Classic→Lightning migration ($60–120/hr), Checkmarx security-review remediation, HIPAA email→Salesforce automation, SAP ABAP/BW consulting ($25–40/hr), Zoho One architecture, Monday CRM build, Dynamics 365 Business Central review, SharePoint/PowerApps integration, on-prem Sage 50/200→Zoho/M365 bidirectional sync. Stated rates span $10–120/hr; meaningful budgets; moderate competition (10–50 tiers).

**Desktop applications** — ~10/day. Legacy-flavored repair exists here: VB.NET→QuickBooks bill-send failure ($30–100/hr, urgent), Crystal Reports template updates ($30–40/hr), Raspberry Pi self-hosted n8n/Paperless/ChromaDB stack fix+extend ($600), plus noise (music-plugin listening test, "clean my computer").

**Embedded / IoT (via Other-Software-Dev + Eng&Arch)** — Low volume, low competition, real rates: Bosch automotive ECU firmware ($500), ESP32 IoT pod features ($2,500, on-site Rotterdam), embedded Linux audio device ($23–45/hr), embedded-AI-failure benchmarking ($60–100/hr). Skill-barriered.

**Blockchain / Web3** — ~6/day, all hourly, $45–170/hr, expert-level, zero 50+ tiers in sample. Solidity/EVM/Solana contract engineering, DEX builds, RWA tokenization, plus an expert-witness code review (Kadena/Pact, Delhi court). Specialist and uncrowded — but requires real Web3 competence; not reskilling-friendly. **OBSERVED**

**Mobile** — ~42/day; long-duration builds dominate (dating apps, kids' learning), $10–30/hr, 50+ competition common. Short sliver: SDK smoke-test ($15), Lovable→App Store packaging, app recode+audit.

**Email / DNS / hosting / deliverability** — ~12/day by query. Email-domain blocking check, DNS records on Bluehost, self-hosted SMTP delivery system ($300), M365→Google Workspace migration (10 users), email-infrastructure manager, newsletter deliverability operator ($25–160/hr). A coherent "mail doesn't arrive / site DNS broken" repair cluster exists.

**Payments (Stripe)** — ~3/day title-visible. Webhook failure ($10 fixed — commodity end), Stripe Connect marketplace builds, Cordova gateway integration, currency-conversion bugs, Amelia-booking build ($250). Payment bugs recur but budgets vary wildly.

**Legacy/modernization (named)** — The `legacy-migration` query exhausted at 9 jobs (hasMore:false): M365/Entra migration architect, tenant-to-tenant migration ($35–75/hr), Entra ID domain migration/UPN conversion ($40–80/hr), AD 2016→2025 runbook design, legacy PHP/MySQL modernization "no rewrite", legacy PHP e-commerce platform (Japan, $25–50/hr), M&A file-server discovery ($40–70/hr). Tiny by this phrasing; the same demand disperses under platform names (Magento EOL, Drupal 10, Classic→Lightning).

**Non-technical bleed** — Engineering & Architecture (~150/day) is mostly CAD/rendering/drafting; Customer Service & Tech Support (~57/day) is mostly cold-calling, photography errands, and customer reps. Both are dead ends for a software specialist despite the taxonomy names.

---

## 4. Cross-market observations

1. **Client vocabulary, not technical domain, determines placement.** The same underlying problem lands in different probes: "WP migration to Lightsail" appears in Network & SysAdmin, the AWS title probe, and the malware query; "email domain blocking" appears in Net&SysAdmin, email-deliverability, and malware probes. 36/348 jobs were returned by ≥2 probes. A problem-centric search strategy covers platform-centric postings. **OBSERVED**

2. **Hourly-vs-fixed flips with specialization.** WordPress corpus was 88% fixed; this technical-universe sample is 65% hourly. Enterprise/specialist clients post hourly; SMB commodity clients post fixed. Implication for short-contract work: *fixed-price* is where bounded scope lives; *hourly* specialist posts often carry <1mo or part-time engagement anyway. **OBSERVED**

3. **"Assessment/audit/roadmap" is a recurring paid deliverable across domains** — AWS gap analysis, migration roadmap, cloud/devops assessment, WCAG audit, SOC 2, code review-for-court, FileMaker diagnosis. Diagnostic work is sellable in its own right, not just a lead-in to implementation. **OBSERVED**

4. **Mentoring/teaching demand is a cross-cutting micro-market** — FortiGate mentor, Azure cloud mentor, AI/MCP tutor, PHP/Laravel teacher ($15/hr), IAM hands-on training ($100), DevOps interview prep. Low budgets but low effort. **OBSERVED**

5. **"Vibe-coded app rescue" is an emerging pattern** — multiple jobs of the form "built in Lovable/Cursor, now need deployment/productionizing/finishing" across Web Dev, Mobile, AWS, Stripe probes. An AI-generated-code repair niche that didn't exist in earlier phases' framing. **OBSERVED**

6. **Urgency is usually implicit.** Explicit ASAP/urgent markers are rare; actual urgency shows through content ("site is offline", "checkout broken", "due tomorrow", "URGENT — incident response"). **OBSERVED**

7. **Very cheap repair jobs coexist with expensive ones in every niche.** $5–10 fixed debugging posts appear in AI, Stripe, WooCommerce, Shopify. The low end is a Connects trap (10+ Connects to win $10 is irrational); the same problem types appear at $100–600 from better clients. **OBSERVED**

8. **Geography:** US ~39% of sampled clients, then Australia/India/UK/Philippines/Canada/Pakistan/Germany. Client-side geo is broadly distributed; freelancer-side geo gates were rare in snippets (a few "US-only", "Philippines only", "Australia/NZ", on-site requirements). **OBSERVED**

9. **Verified-payment clients dominate** (288/348 = 83%); new clients with no history are common in commodity areas. **OBSERVED**

10. **Multi-hire and staffing-agency posts exist inside technical categories** (freelancers_to_hire>1 in 9 jobs; several posts are recruiters/agencies subcontracting — e.g., MSP tech, audit pools, AWS cert partners). Subcontracted demand is real but usually wants credentials or standing. **OBSERVED**

---

## 5. Areas requiring deeper investigation (Phase 1.1B candidates)

Not ranked; listed with the open questions that decide viability.

| Candidate area | Evidence trigger | What 1.1B must measure |
|---|---|---|
| **Migration work, all kinds** (M365 tenant-to-tenant, Entra/AD, platform migrations, host moves, Magento/Drupal upgrades) | Recurs across 5+ probes; expert-priced; real scarcity signal | volume across synonyms; per-job gates; connects cost; win-rate proxies |
| **E-commerce platform specialist repair** (esp. Magento; WooCommerce tail) | EOL upgrades, skimmer incident response, indexing failure | whether ~1/day volume supports a pipeline; competition aging |
| **Email/DNS/deliverability repair** | coherent recurring cluster; ~12/day; low competition tiers | budget distribution at scale; gate check |
| **Business-automation repair** (n8n/Zapier/Make debugging) | high volume ~35/day, repair-flavored, low competition | budget realism — many posts are $10–75 fixed |
| **Vibe-coded app rescue / AI-build productionizing** | recurring pattern across 4 probes | whether it sustains volume; typical budgets |
| **Paid assessments/audits/roadmaps** | appears in DevOps, AWS, Magento, QA, InfoSec | whether a solo new account can win them (credibility gate) |
| **Self-hosted stack care** (VPS, self-hosted n8n/Paperless, libvirt, Lightsail) | several low-competition maintenance/troubleshoot posts | recurrence vs one-offs |
| **Database specialist troubleshooting** (FileMaker, SAP HANA, Aurora) | specialist rates, thin supply of practitioners | volume is genuinely low (~1/day) — pipeline feasibility |
| **Salesforce/enterprise-platform work** | Classic→Lightning $60–120/hr, Checkmarx, HIPAA flows | certification expectations; likely requires evidence of platform experience |
| **MSP/IT subcontract support** | MSP remote-tech post; subcontract language | usually wants availability windows — fit with solo short contracts |
| **Embedded/IoT** | low competition, decent rates | hard skill gate — likely excluded by Marc's stack |
| **Blockchain/Web3** | least crowded observed ($45–170/hr, thin proposals) | hard skill gate — likely excluded by Marc's stack |

---

## 6. Areas that appear commodity / poor-economics

| Area | Why it looks poor |
|---|---|
| Microtask QA/beta/usability testing | $5–40 fixed or $3–10/hr; device/location gates; 99-hire cattle calls |
| Data labeling / voice recording / AI eval tasks | $3–20/hr; not technical differentiation |
| Shopify store setup / product listing | $5–30 fixed, VA-priced, high volume of identical posts |
| Generic full-stack/web builds | ~160/day supply, 20–50+ proposals standard, $10–30/hr norms, long durations — undifferentiated competition |
| Lead scraping / contact-list building | $5–10/hr, 50+ proposals, race-to-bottom (separate from SERP-infra specialist work at $25k) |
| Bubble / low-code builds | demand exists but platform-exclusive and price-pressured |
| $5–10 fixed "fix my site/webhook/integration" | Connects cost alone exceeds gross; clients systematically underprice repair |
| Commission-only "partnerships" | appear inside technical searches (Salesforce BDM post); not paid work |
| Customer Service & Tech Support subcat | mostly non-technical despite the name |
| Engineering & Architecture category | mostly CAD/rendering — wrong discipline |

---

## 7. Areas where evidence is insufficient

- **True posting frequency**: `est/day` is derived from the newest-10 published_date span through a filtered search index — an order-of-magnitude signal only. No date filter exists on `search`; `smart_search` date filters are personalized and would not measure the whole market.
- **Proposal competition**: Basic-plan results expose tiers, not counts; tiers accumulate with post age, inflating apparent competition in slow-moving niches (legacy-migration's 56% at 50+ reflects 38-day-old posts).
- **Qualification gates / preferred_qualifications / connects_cost**: not visible in search results — require per-job `get` calls, which were not run this phase (348 jobs × get was out of scope; belongs to 1.1B on shortlisted areas).
- **Hire/fill rates**: `activityStat` (invites, hires) not sampled; a job sitting open may be dead.
- **Subcategory purity**: no per-job subcategory field is returned in search output, so noise share per subcat is estimated from snippets, not measured.
- **Hourly job effective value**: 80/226 hourly jobs state no rate at all; real rates unknown.
- **Mobile dev, game dev, design-adjacent areas**: sampled once each (n=10); findings are directional.
- **Non-English/regional markets**: scan was English-language biased by search phrasing.

---

## 8. Raw evidence & statistical limitations

- **Sample:** 348 unique jobs from 39 probes (37 with results; `title:cobol` and the COBOL-compound query returned zero). Single collection window ~03:55–05:30 UTC 2026-09-24 — intraday seasonality not controlled (mitigated for cross-probe comparison since all probes ran in the same window).
- **Per-probe n=10** → small-sample noise; medians on 3–6 fixed-budget observations are unstable (e.g., `title:devops` med-fixed $2,150 is a 2-observation artifact).
- **Arrival-rate heuristic** assumes the newest-10 window is representative; a burst or quiet hour skews it. Treat all `est/day` as ±an order of magnitude.
- **Snippet-truncated descriptions** (~300 chars) — classification signals come from title+snippet only; full bodies would change some labels.
- **Repair-share %** is a keyword heuristic over title+snippet, not manual classification — reported as a signal, not a measurement.
- **Search index coverage** of the true market is UNKNOWN (invite-only/private posts invisible; index lag unknown).
- **No dedup against the Phase 1.1 corpus** — a few WordPress jobs overlap both datasets (same id seen: e.g., the WP-Engine speed job). Cross-phase join possible via job id.
- **Proposal tiers are coarse** (Fewer than 5 / 5–10 / 10–15 / 15–20 / 20–50 / 50+).
- **`no rate stated` hourly jobs** (80) bias budget stats downward-invisibility rather than toward zero.

---

## 9. Dataset & search methodology

- **Source:** Upwork MCP `find_jobs action=search` (signed-in freelancer marketplace search), `sort=recency`, `limit=10`, `include_full_details=false`.
- **Probes:** 21 subcategory filters, 1 category filter (Engineering & Architecture), 10 title filters, 7 query filters, plus 2 taxonomy-enumeration calls (invalid category/subcategory probes returning the valid lists). Full probe manifest with per-probe new/dup counts: `probes[]` array in the raw dataset.
- **Records:** verbatim per-job search records (all returned fields) annotated with `_probe`/`_probes`.
- **Account:** freelancer, Basic plan — proposal counts exposed as tiers; `connects_cost` requires `get` calls (not exercised this phase). Account plan, not the marketplace, sets proposal visibility.
- **Taxonomy discovery:** category list obtained via rejection message on `category:"zzz-invalid-probe"`; the subcategory vocabulary is global.
- **Empty probes are evidence:** `title:cobol` → `filters_no_match` (zero); COBOL-compound query → zero; `query:"legacy system migration modernization"` → 9 total with `hasMore:false`.
- **Reproducibility:** probes are deterministic filters + recency; re-running yields a different sample as new jobs arrive.
- **Compliance:** read-only throughout; no proposals, no Connects consumed, no write tools invoked.

---

## 10. Handoff dataset for Phase 1.1B

**File:** `Documentation/upwork-phase-1-1a-technical-universe-raw.json` (436 KB)

```
metadata : collection window, account constraints, method notes, empty-probe list
probes   : [{probe, files, n_returned, n_new, n_dup, ts}] — 39 manifest entries
jobs     : [348 job records] — id, title, description_snippet, job_type, budget,
           duration, engagement, experience_level, proposals_tier, skills[],
           client{country, verification_status, rating, total_posted_jobs,
           total_reviews, total_spent, total_hires}, created_date,
           published_date, url, _probe/_probes
```

**Suggested 1.1B procedure per shortlisted area:**
1. Re-probe the area with synonyms/platform names; paginate 2–3 pages (cursor) for a 20–30-job window.
2. Run `find_jobs action=get` on each job for `connects_cost`, `preferred_qualifications`, `activityStat` (liveness) — the same method the Connects test used on the WP corpus.
3. Compute per-area: arrival rate (multi-page span), fixed-vs-hourly, budget bands, <1mo share, proposal-tier-at-fixed-age, gate share, repair share (manual classification, not keywords).
4. Feed the empirical Connects distribution (median 14, range 7–27) into band-level economics — do not re-derive.

**Do not repeat:** taxonomy enumeration, COBOL-level emptiness checks, the WP baseline (Phase 1.1 corpus already measured it), or anything covered by §8 limitations that this method cannot fix.

---

*Phase 1.1A maps where paid technical demand exists and how it is structured. The question of which specific niches combine volume, weak competition, sane economics, and Marc-accessible skills is deferred to Phase 1.1B.*
