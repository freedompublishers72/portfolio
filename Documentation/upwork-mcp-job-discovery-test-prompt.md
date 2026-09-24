# Upwork MCP Job-Discovery Test — Prompt Record

Date: 2026-09-24
Task type: Read-only capability test (no write operations)

The following is the exact prompt used for this task, preserved verbatim:

---

Now perform the first real Upwork job-discovery test.

DO NOT:
- submit any proposal
- confirm any draft
- consume Connects
- save jobs
- message clients
- alter my profile
- boost my profile
- accept offers
- perform any other write operation

Use ONLY read/discovery tools.

Search for currently available jobs matching my established WorkBot criteria:

PRIMARY:
- WordPress
- PHP
- JavaScript where relevant
- WordPress debugging
- plugin development
- performance optimization
- security/hardening
- migrations
- API integration
- WordPress customization

PREFER:
- fixed-price
- small/short projects
- work realistically completable by one developer
- $20+ budget
- no meetings/calls explicitly required
- no long-term/full-time engagement
- no Elementor/Divi/page-builder work
- no SEO/content/data-entry work
- no mobile-app work

For every result, retrieve whatever the MCP exposes for:
- job ID
- title
- description
- budget/rate
- fixed-price vs hourly
- posting time/age
- proposal/application count
- client location
- client history
- client spend
- hire rate
- relevant skills
- Connects required, if exposed

Return the 50 newest matching jobs you can retrieve.

DO NOT rank them by your own opinion yet.

Instead, give me the raw marketplace data first.

Then report:

1. How many matching jobs were found.
2. Whether posting age is exposed.
3. Whether proposal/application count is exposed.
4. Whether the MCP appears capable of discovering newly posted jobs quickly.
5. Whether there is pagination or a result limit.
6. Whether search results can be restricted to jobs posted within a specified time window.
7. Whether the API exposes enough information for WorkBot to perform our existing qualification rules automatically.

No proposal generation yet. No Connects consumed.
