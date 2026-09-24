# Upwork Connects Cost — Empirical Distribution Test — Prompt Record

Date: 2026-09-24
Task type: Read-only investigation (no writes, no Connects spent)

The following is the exact prompt used for this task, preserved verbatim:

---

# Upwork Connects Cost — Empirical Distribution Test

We need an empirical answer to two questions:

1. What does a Connect actually cost for the types of WordPress jobs I would realistically bid on?
2. How quickly would 100 Connects be consumed under realistic WorkBot bidding criteria?

DO NOT submit, confirm, boost, save, or otherwise mutate anything. This is a READ-ONLY investigation. Do not spend Connects.

## 1. Build the sample

Use the Upwork MCP job-discovery tools to collect a sufficiently large sample of current WordPress jobs.

Target:
- At least 30 jobs if available
- Prefer 50+
- Focus on jobs that match my actual WorkBot profile:
  - WordPress
  - PHP
  - JavaScript
  - API integration
  - performance/speed optimization
  - debugging/troubleshooting
  - security/hardening
  - WooCommerce where technically relevant
- Prioritize fixed-price jobs because we are investigating bid-vs-project economics.
- Include a range of project values, especially:
  - $20–99
  - $100–249
  - $250–499
  - $500–999
  - $1,000+

Do not artificially select jobs because they have unusually low or high Connect costs.

## 2. Retrieve the actual Connect cost

For every sampled job for which the MCP `get` operation exposes `connects_cost`, retrieve it.

Record:

- job ID
- title
- publication age
- fixed-price budget
- Connects required
- proposal count/tier if available
- client country
- client spend
- client hires
- any other fields relevant to competition

If `connects_cost` is unavailable for a job, record UNKNOWN rather than estimating it.

## 3. Calculate the actual distribution

Calculate:

- number of jobs sampled
- number with known Connect costs
- minimum Connect cost
- maximum Connect cost
- mean Connect cost
- median Connect cost
- P25
- P75
- mode if meaningful
- percentage requiring:
  - 1–4 Connects
  - 5–8
  - 9–12
  - 13–16
  - 17+
- Connects by project-value band

Most importantly calculate:

### Connects per $100 of project value

For every fixed-price job:

    connects_cost / budget * 100

Report:
- median
- P25
- P75
- range

Also calculate the proposal cost in USD using:

    Connects × $0.15

## 4. Answer the 100-Connect question

Using the observed distribution, determine how many proposals 100 Connects would realistically purchase.

Give:

- best observed case
- worst observed case
- median case
- P25/P75 if statistically meaningful

Then calculate the same thing specifically for jobs that match my WorkBot criteria.

Example:

    100 / median_connect_cost = proposals

Do NOT simply assume 9 Connects because one job happened to cost 9.

## 5. Calculate acquisition cost against project value

For each value band, calculate the median observed Connect expenditure required to submit one proposal.

Example table:

| Project value | Jobs | Median Connects | USD bid cost | Bid cost as % of project |
|---|---:|---:|---:|---:|
| $20–99 | | | | |
| $100–249 | | | | |
| $250–499 | | | | |
| $500–999 | | | | |
| $1,000+ | | | | |

This is particularly important for small jobs.

## 6. Determine whether Connect pricing appears related to job value

Test empirically whether higher-value projects actually require more Connects.

Compare:
- project budget
- Connects required
- proposal volume
- project age

Do not claim causation.

If the sample is too small to establish a relationship, explicitly say so.

## 7. Determine whether the 9-Connect/$50 observation is representative

We previously observed:

- $50 fixed-price WordPress job
- 9 Connects required
- therefore $1.35 to submit one proposal

Determine where that observation sits in the new sample.

Report:

- percentile of the Connect cost
- percentile of bid-cost/project-value ratio
- whether comparable $20–99 jobs commonly have similar costs

## 8. Model actual WorkBot economics

Use the empirical Connect distribution to model:

### Scenario A
100 Connects purchased.

How many qualifying proposals can actually be submitted?

### Scenario B
$15 spent on 100 Connects.

How much project value is represented by:
- 10 proposals?
- median number of proposals?
- maximum number of proposals?

Do NOT assume any win rate.

## 9. Separate FACT from CALCULATION

Every conclusion must be classified as one of:

- OBSERVED — directly returned by Upwork MCP
- CALCULATED — mathematical calculation from observed data
- ASSUMPTION — explicitly stated assumption
- UNKNOWN — data not exposed

Do not use external estimates where the MCP can provide actual data.

## 10. Final answer

End with this exact structure:

### CONNECTS TEST RESULT

Sample size:
Known Connect costs:
Median Connects/job:
Mean Connects/job:
P25:
P75:
Minimum:
Maximum:

100 Connects buys approximately:
- Best case:
- Typical/median:
- Worst case:

Median bid cost:
Median bid cost as % of project value:

For my qualifying WordPress jobs:
100 Connects buys approximately ______ proposals.

### $15 PURCHASE TEST

$15 = 100 Connects.

Based on the observed qualifying-job distribution:

Expected proposal capacity:
Observed range:
Most important uncertainty:

### ECONOMIC SIGNIFICANCE

State plainly whether Connect costs appear:

1. negligible,
2. material but manageable,
3. materially restrictive for low-value jobs, or
4. materially restrictive across the market.

Do not recommend buying Connects yet.

The purpose is to establish the actual acquisition economics before we spend the first $15.
