# Upwork Economic Viability — Phase 1.1C Prompt Record

Exact prompt used for the Phase 1.1C Winner Deep Dive task.

---

You are executing Upwork Economic Viability Phase 1.1C — Winner Deep Dive.

INPUT

Use:

- Phase 1.1A Technical Universe Scan
- Phase 1.1B Economic Ranking
- underlying Upwork marketplace evidence

OBJECTIVE

Perform detailed economic investigation of the strongest candidate technical areas identified in Phase 1.1B.

Do not assume that the Phase 1.1B ordering is correct. Test it against deeper project-level evidence.

For each selected technical area, investigate:

1. Demand
   - How frequently relevant projects appear.
   - Whether demand is persistent or episodic.
   - Whether demand comes from recurring operational problems.

2. Project economics
   - Fixed-price distribution.
   - Hourly-rate distribution.
   - Median and quartiles where sample size permits.
   - Short-project economics.
   - Relationship between budget and scope.

3. Competition
   - Proposal distribution.
   - Competition by budget band.
   - Competition by project type.
   - Whether technically difficult jobs actually have fewer proposals.

4. Acquisition economics
   - Connects required.
   - Cost per proposal.
   - Expected acquisition cost under different win rates.
   - Break-even win rates.
   - Economics at realistic delivery times.

5. Project structure
   - Typical scope.
   - Typical duration.
   - Client interaction requirements.
   - Access requirements.
   - Whether work can be performed asynchronously.
   - Whether the freelancer needs ongoing involvement.

6. Technical structure
   - Common underlying problems.
   - Diagnostic uncertainty.
   - Required systems knowledge.
   - Cross-system dependencies.
   - Legacy/poorly documented environments.
   - Production-risk characteristics.

7. Supply restriction
   Look for evidence that explains why a technically capable freelancer might face less effective competition.

   Examples:
   - specialist knowledge
   - unusual combinations of technologies
   - difficult diagnosis
   - production risk
   - legacy systems
   - infrastructure access
   - operational experience
   - difficult-to-reproduce failures
   - cross-domain expertise

   Do not assume that technical difficulty creates low competition. Test it.

8. Commodity/AI resistance
   Determine whether the work can plausibly be solved by:
   - a generic search,
   - ChatGPT,
   - code generation,
   - a standard tutorial,
   - a plugin,
   - a managed service,
   - or a junior developer following instructions.

   Distinguish:
   - generating a solution,
   - diagnosing the actual problem,
   - safely deploying the solution,
   - verifying the production result.

9. Recurring work
   Identify recurring problem chains such as:

   symptom → underlying cause → repair → secondary damage → follow-up work

10. Work archetypes
    Convert the market evidence into concrete project archetypes.

    Examples:
    - broken site diagnosis
    - migration fallout
    - server configuration
    - API integration failure
    - database repair
    - performance diagnosis
    - security remediation
    - legacy PHP debugging

    Use actual evidence to determine the archetypes rather than relying on these examples.

11. Marc capability overlap
    Only after the market characteristics have been established, assess whether the technical area overlaps with the existing capability set.

    Do not allow personal capability to hide an economically interesting market.

OUTPUT

For every deep-dived area provide:

- market summary
- demand evidence
- budget evidence
- competition evidence
- Connects economics
- project-duration evidence
- project archetypes
- technical difficulty
- supply restriction evidence
- commodity/AI resistance
- recurring demand
- representative jobs
- unknowns
- evidence quality
- economic interpretation

Then produce a cross-area comparison identifying which technical characteristics repeatedly appear in economically interesting projects.

Do not stop at category names.

The goal is to discover the actual type of work that may be economically viable.
