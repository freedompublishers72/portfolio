# Portfolio Site Mapping Nexus

**Date:** 2026-09-23 GMT+7  
**Repository:** `freedompublishers72/portfolio`  
**Branch:** `Main`

## Purpose

This document is the site-level information architecture for the technical portfolio.

The portfolio is a small, predominantly text-based technical wiki. It documents real engineering work, selected technical systems, verified code demonstrations, and future availability for paid work. It is not an agency site, corporate marketing site, product landing page, or visual showcase.

The nexus is the controlling map for subsequent page audits and rewrites.

## Current repository pages

| Page | Path | Role |
|---|---|---|
| Home | `index.html` | Site index and orientation |
| About & Contact | `about.html` | Author, engineering focus, working approach, contact |
| Multilingual Publishing Architecture | `case-studies/multilingual-publishing-architecture.html` | Technical system documentation |
| Event-Driven Full-Page Caching | `case-studies/event-driven-full-page-cache.html` | Technical system documentation |
| Framework-Independent Research & Data Engine | `case-studies/research-data-engine.html` | Technical system documentation |
| Verification & Certification as a Deliverable | `case-studies/verification-and-certification.html` | Engineering-process documentation |
| Page Not Found | `404.html` | Infrastructure/error page |

The repository also contains seven standalone code demonstrations under `examples/`. These are content assets referenced by the technical pages, not separate portfolio pages.

## Intended information architecture

```
PORTFOLIO
│
├── HOME
│   ├── orientation
│   ├── feature project: SRIA
│   ├── SRIA technical paper: Travel Bonanza
│   ├── selected code examples
│   └── contact / future hiring links
│
├── PROJECTS
│   └── SRIA
│       ├── live production project
│       └── Travel Bonanza
│           └── subsystem / technical paper
│
├── TECHNICAL SYSTEMS
│   ├── Multilingual Publishing Architecture
│   ├── Event-Driven Full-Page Cache
│   ├── Research & Data Engine
│   └── Verification & Certification
│
├── CODE EXAMPLES
│   └── seven verified/sanitized demonstrations
│
├── ABOUT
│   └── engineering focus / approach / scope
│
├── AVAILABLE WORK
│   └── future marketplace/service links
│
└── 404
```

This is a conceptual information architecture, not a requirement to create a page for every node. Existing pages should be reused where possible.

## Page ownership and relationships

### 1. Home

**Role:** The index of the portfolio.

It should answer, quickly:

- What is this site?
- What real project is being presented?
- What technical systems can be examined?
- Where can the reader go deeper?
- How can the reader contact or eventually hire Marc?

The current homepage contains:

- feature project: Siem Reap Inside Asia
- Travel Bonanza technical-paper reference
- five selected code-example links
- contact links
- GitHub link

The eventual homepage should remain concise and wiki-like.

**Does not own:** detailed technical explanations, long case studies, or duplicated code documentation.

---

### 2. About

**Role:** Human and professional context.

It currently contains:

- engineering focus
- WordPress/PHP/Python/performance/debugging/integration/data-processing areas
- working approach
- portfolio disclosure/scope
- contact

The page should explain who is doing the work and how he works, without becoming a personal-brand marketing page.

**Does not own:** detailed descriptions of individual systems.

---

### 3. Multilingual Publishing Architecture

**Role:** Documentation of the multilingual publishing system.

Primary subject:

- language-aware routing
- translation resolution
- multilingual content architecture
- language isolation/query enforcement
- native-language URLs
- related verification and code examples

The page should ultimately distinguish documented architecture from optional/manual visitor controls and should not invent a simplified routing model that contradicts the source implementation.

Relevant code demonstrations currently include:

- Accept-Language Locale Matcher
- Protected-Token Translation Validator

---

### 4. Event-Driven Full-Page Caching

**Role:** Documentation of the custom full-page cache.

Primary subject:

- cache serving decisions
- generation
- invalidation
- pending generations
- stale handling
- regeneration
- concurrency/recovery behavior

Relevant code demonstration:

- Bounded-Staleness Cache Serve Cascade

Any future cache diagram must be derived from the documented cache workflow and verified against the source implementation before publication.

---

### 5. Framework-Independent Research & Data Engine

**Role:** Documentation of the research/data engine architecture.

Primary subject:

- provider contracts
- acquisition
- normalization
- persistence
- analysis
- scheduling boundaries
- WordPress presentation boundary
- collection reliability
- forecast/calibration evaluation

Relevant code demonstrations:

- Capability-Contract Provider Layer
- Calibration Metrics
- Resilient Collector Primitives

The page must distinguish the framework-independent engine from its WordPress presentation layer.

---

### 6. Verification & Certification as a Deliverable

**Role:** Documentation of the engineering verification/certification discipline.

Primary subject:

- scope
- implementation
- independent verification
- certification
- remediation
- deferral
- evidence preservation
- runtime verification
- historical versus current state

Relevant code demonstration:

- Immutable Domain Primitives

This page documents an engineering process rather than a standalone software product.

---

### 7. Travel Bonanza

**Current location:** Homepage technical-paper section.

**Architectural status:** A facet/subsystem of SRIA, not a competing project.

The eventual detailed presentation should be treated as a technical paper/documentation page only if the source evidence supports a separate page.

It should explain the subsystem's architecture and workflow rather than market Travel Bonanza as an independent portfolio product.

No technical claims or diagrams should be invented until the underlying SRIA documentation/source has been audited.

---

### 8. Code demonstrations

**Current location:** `examples/`

There are seven demonstrations:

1. Protected-Token Translation Validator
2. Bounded-Staleness Cache Serve Cascade
3. Capability-Contract Provider Layer
4. Calibration Metrics
5. Resilient Collector Primitives
6. Accept-Language Locale Matcher
7. Immutable Domain Primitives

These are evidence assets.

A code demonstration must remain traceable to the documented workflow or engineering principle it claims to represent. It must not imply that the published miniature is the complete private production implementation.

Each published demonstration should therefore be checked against:

**documented source workflow → extracted implementation → tests → page description**

---

## Navigation model

The current navigation is:

```
Home
Work
About
Contact
GitHub
```

The redesign should simplify rather than expand this.

The conceptual destination structure is:

```
Home
  ├── SRIA
  ├── Technical systems
  ├── Code examples
  └── Contact / available work

About

Technical pages
  ├── Multilingual
  ├── Cache
  ├── Research/data
  └── Verification
```

There is currently no requirement for a separate Projects index, Technical Systems index, or Code Examples index. The small size of the site argues against adding intermediary pages unless the content later grows enough to justify them.

## Future hiring layer

A future **Available Work** section may link to:

- Upwork
- Freelancer, if useful
- fixed-price service pages or other legitimate hiring destinations

These links are an acquisition layer around the portfolio, not the portfolio's primary identity.

No marketplace-specific design should dictate the site's information architecture before the relevant marketplace features are verified.

## Visual/design governance

The portfolio is intentionally:

- predominantly text
- wiki-like
- technically documented
- minimally decorated with CSS
- easy to scan
- lightweight
- readable
- free of unnecessary marketing components

Flowcharts and diagrams are optional explanatory assets.

They are not decorative requirements.

### Diagram approval chain

```
Documented workflow
      ↓
Technical audit
      ↓
Diagram proposal
      ↓
Joint review / correction
      ↓
Commit verified asset
      ↓
Reference asset from page
```

A diagram must not be published merely because a page appears to need a graphic.

## Page rewrite governance

Every substantive page is handled independently through three phases:

### Phase A — Accuracy Audit

Compare the existing page against:

- recorded project documentation
- historical reports
- source code
- verified implementation evidence
- existing code-demo provenance

Record unsupported, outdated, ambiguous, or overstated claims.

### Phase B — Visual Representation Plan

For the audited page:

- decide which information needs visual explanation
- decide whether a diagram is actually useful
- design diagrams together before committing them
- identify screenshots or other assets only where they add evidence
- verify every technical visual against the relevant documented workflow
- commit approved assets before page integration

### Phase C — Rewrite

Rewrite the page from the verified audit and approved visual plan.

Then verify:

- factual accuracy
- terminology
- links
- code-example relationships
- asset references
- accessibility
- responsive behavior
- absence of unsupported claims

## Simplification rules

1. Do not create a new page merely because content exists.
2. Prefer linking to an existing page over duplicating information.
3. Do not turn a subsystem into a separate "project" merely for presentation.
4. Do not add visual elements that do not improve understanding.
5. Do not use marketing language where straightforward technical description is sufficient.
6. Do not publish a technical diagram until its workflow has been verified.
7. Do not publish a code example whose documented behavior differs materially from the source workflow it represents.
8. Preserve the distinction between private production systems and sanitized public demonstrations.
9. Keep historical evidence separate from current-state claims.
10. The site should remain a portfolio/wiki, not evolve into a corporate or template-driven marketing site.

## Planned page sequence

The substantive pages will be audited in this order:

1. Home
2. Multilingual Publishing Architecture
3. Event-Driven Full-Page Caching
4. Framework-Independent Research & Data Engine
5. Verification & Certification as a Deliverable
6. About & Contact

Travel Bonanza will be addressed when its source evidence is specifically audited.

The 404 page receives a lightweight infrastructure/UI review after the substantive pages.

## Current-state note

This nexus describes the repository as it exists on Main on 2026-09-23 GMT+7 and establishes the intended simplified information architecture for the subsequent redesign work. It does not itself rewrite or remove existing pages.
