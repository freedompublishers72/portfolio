# Upwork MCP Capability Test — Prompt Record

Date: 2026-09-24
Task type: Diagnostic / capability test (no implementation)

The following is the exact prompt used for this task, preserved verbatim:

---

Test the connected Upwork MCP integration.

Objective: determine whether this account can actually use Upwork's official MCP functionality to discover freelance jobs and prepare proposals.

Do NOT submit, send, apply, purchase Connects, accept invitations, message clients, or otherwise perform any irreversible/write action.

Perform these tests in order:

1. Confirm that the Upwork MCP connection is authenticated and working.
2. Retrieve currently available jobs matching ALL of these criteria:
   - WordPress
   - PHP or JavaScript where relevant
   - bug fixing, troubleshooting, plugin development, performance optimization, security/hardening, migration, API integration, or WordPress customization
   - fixed-price preferred
   - short-duration work preferred
   - suitable for completion by one developer
3. Return at least 20 matching jobs if available.
4. For each job report:
   - title
   - job URL/ID
   - fixed-price or hourly
   - advertised budget/rate
   - estimated duration if available
   - client location if available
   - number of proposals/applicants if available
   - Connects required if available
   - posting age
   - relevant skills
5. Determine whether the MCP interface exposes enough information to identify newly posted jobs quickly.
6. Select the 5 strongest matches according to the criteria above.
7. For those 5 only, draft a proposal but DO NOT submit it.
8. Clearly report which operations were successful, which were unavailable, and which would require additional permissions, Connects, account eligibility, or user confirmation.

This is an API/MCP capability test, not a job-application session. Do not take any external action without explicit confirmation.
