# Requirements — status-separated register

Status: initial draft. C = charter direction; A = Scott’s supplied answer; T = proposed technical support; P = unresolved product/game/security proposal requiring approval. Observed map details alone are not approved requirements.

| ID | Status | Requirement / intended validation |
|---|---|---|
| C1 | Charter | Enable wargame workflows beyond simulation; maintain independent concept and living repository documentation |
| C2 | Charter | Support external M&S exchange, state references, human review and multiple adapters without recreating high-fidelity simulation |
| C3 | Charter | Support multiple non-M&S adjudication approaches and identify method, evidence, determinant, uncertainty, dissent/alternatives and resulting effects |
| C4 | Charter | Treat AI as optional; assess provenance, validation, review, failure/fallback and usefulness before adoption |
| C5 | Charter | Obtain approval for game restrictions, substantial workflow/product changes, organizational authority and release/security policy |
| T1 | Technical proposal | Give records stable identities and versions so evidence, decisions, effects and products can be traced; test reconstruction across revisions |
| T2 | Technical proposal | Retain original external output separately from normalized interpretation and reviewed effects; test rejection and partial acceptance without losing originals |
| T3 | Technical proposal | Detect duplicate delivery and changed input context; distinguish delivery retry from new analytical run; no silent overwrite or double application |
| T4 | Technical proposal | Express method-specific evidence without forcing numerical certainty or a universal move form; exercise human judgment, matrix/rules and external output |
| T5 | Technical proposal | Link RFIs, CCIR observations, tasks and narratives to decisions without assuming each item blocks play; validate against a play episode |
| T6 | Technical proposal | Record time of occurrence, recording and release separately where relevant; game time semantics await validation |
| T7 | Technical proposal | Represent Turn 0 parameters/objectives, cell makeup/relationships, scenario baseline and initial World View/perspectives; validate setup examples without fixing mandatory fields |
| T8 | Technical proposal | Support ongoing RFI response/defer/unresolved status, CCIR monitoring and updates, and external task/report routing/status across play; approval-required policy determines any blocking effect |
| P1 | Approval required | Which fields, move types and completeness criteria players must supply; free text plus optional structure is a prototype alternative |
| P2 | Approval required | Turn timing, overlapping work, mandatory gates, corrections and closure details beyond Scott’s consensus/verbal-approval governance |
| P3 | Approval required | Detailed permissions, release recipients/timing, authorized effect handoff and correction procedures within Scott’s stated authority/view/boundary principles |
| P4 | Approval required | Specific strategic DATE-oriented synthetic episode/user cohort, external counterpart and method-selection details |

Technical identifiers and version checks need not require extra player fields or a particular game sequence. A common evidence envelope is a software representation proposal; its user-visible mandatory content requires separate agreement.

Scott has established higher-classification separation and no digital cross-boundary connection. Exact game classification, operating authorization, deployment, identity provider, retention, availability, scale and performance requirements remain unestablished. The map's marking and vocabulary do not supply them. No production acceptance thresholds are invented; prototype acceptance criteria are in [ROADMAP.md](ROADMAP.md).

This register describes the product horizon, not a mandatory first-milestone feature list. Choose the smallest useful slice from a representative episode and observed pain point. Mixed-method comparisons and fake adapter work are optional targeted experiments. Keep action, determination, accepted effect and released account distinct where they legitimately differ; shared information availability is not evidence of individual knowledge. External security authority does not remove the application’s responsibility to enforce the eventual approved access policy. Early experiments use synthetic data only.

## Requirements from Scott’s answers

| ID | Status | Requirement |
|---|---|---|
| A1 | Scott answer | Authoritative record combines Road to Crisis/scenario documentation, adjudicated results and actual intra-player communications/agreements; occurrence/content is distinct from assertion truth or execution |
| A2 | Scott answer | World View is open-intelligence/news-like; player Perspective adds intelligence-community information; adjudication team approves |
| A3 | Scott answer | Team meets and reaches consensus; Game Director approves verbally to team and has no system interaction |
| A4 | Scott answer | Higher-classification processing remains external; sneaker-net boundary, no digital connection; only suitably authorized game-classification effects enter through humans |
| A5 | Scott answer | Accommodate manual external CSV export; API is optional when available; formats/tool selection unknown |
| A6 | Scott answer | Strategic DATE World context and six reported frictions guide discovery; they do not mandate one move taxonomy |
| T9 | Technical proposal | Team member minimally records the determination and attributable report of consensus/director verbal approval, without adding votes/signatures or a director login |
| T10 | Technical proposal | Produce useful audience-appropriate prior-action feedback and carry-forward context; measure player comprehension and adjudicator continuity |

T9 capture could identify recording team member, meeting reference/date, agreed determination and reported verbal approval/time, with amendments. This is a minimal candidate representation, not an approved mandatory form or permission to release higher-classification material.

## First-prototype coverage and limits

Approved episode now implemented as a persistent synthetic local workflow. Covered: lightweight context view; open-ended action; reusable human-prepared request; explicit one-row result mapping; original/result/assessment distinctions; duplicate/stale visibility; team consensus and reported verbal approval; corrections/history; handover; audience feedback. No actual counterpart format is verified. Draft effect entries are proposed until approved. No fixed move vocabulary, domain fields or turn length introduced; form fields needed for technical correlation and attributable capture are prototype interface choices, not generalized game requirements.

Acceptance exercised by 14 unit tests and real-HTTP browser walkthrough, including player JSON/DOM leakage, repeated import, corrections and continuity. Production authorization and user-value evaluation remain open; see README.md and STATUS.md.
