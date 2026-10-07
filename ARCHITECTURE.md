# Architecture — provisional alternatives

Status: concept hypotheses only; no production architecture or stack selected.

## Candidate responsibilities

1. Game context and records: scenario versions, participant/cell relationships, state references and record history.
2. Collaboration and coordination: actions, questions, CCIRs, tasks, supporting artifacts and visible outstanding work.
3. Adjudication workspace: method-specific evidence, alternatives, uncertainty, determination and proposed effects; usable for human-only methods.
4. Integration boundary: adapter-specific translation, external-job correlation/status and retained results; file exchange is a legitimate first adapter option.
5. State reconciliation: compare effects against their input context, expose conflicts and record accepted changes under an approved authority model.
6. Information products and release: distinguish authoritative conditions, public view, perspectives and narratives; core authority/view principles are specified by Scott; detailed access/release procedures remain unresolved.
7. Provenance and review: connect inputs, activities, people/tools, outcomes and later corrections for explanation and after-action use.

These are logical responsibilities, not seven services, final schemas or authorized roles.

## Alternatives

| Option | Benefit | Cost / evidence needed |
|---|---|---|
| Document-centered collaboration with indexed decisions/artifacts | Fast discovery; tolerates qualitative and evolving methods | State consistency and release auditing may remain manual; test whether records alone solve the main pain |
| Modular application with transactional records/history and adapter jobs | Coherent state/evidence relationships without distributed infrastructure | Requires explicit version/conflict behavior; leading prototype hypothesis, not production commitment |
| Configurable workflow engine | Useful if many validated procedures require long-running coordination | May encode unapproved gates; evaluate only after workflow variation is demonstrated |
| Event-sourced/distributed service platform | Potential historical replay and independent components | Version migration, projections and distributed failure costs; audit needs alone do not justify it |
| Live simulation federation behind a gateway | Supports counterpart requirements for time/state exchange | Much stronger synchronization and ownership assumptions; only pursue for demonstrated live-coupling needs |

**Recommended hypothesis:** Compare the first two using the same episode. If structured coordination is justified, prototype a modular core with explicit records/history and an asynchronous adapter boundary. Defer workflow engine, event sourcing, graph database, message broker and live federation until evidence warrants their costs. Deployment topology and expected scale are unknown.

## Proposed information distinctions

Keep action versions, input-context references, evidence/results, reviewer interpretations, determinations, proposed/accepted effects and released products distinguishable. Keep game-time validity distinct from receipt/record time. An authoritative baseline is not automatically visible to every participant. State acceptance does not automatically authorize release. Product issuance can itself be a recorded game occurrence without making all its narrative claims true.

## Adapter experiment contract

Candidate technical metadata: exchange/job/run identifier; source tool and adapter version; referenced state/input versions; schema/units/time interpretation; configuration and stochastic settings when available; submitted/received status; original artifact and interpretation provenance. Missing provenance is explicit, not invented. Method completion, human determination, state application and information release are separate concepts; this does not impose a four-stage game approval chain.

Exercise duplicate deliveries, timeouts, cancellation races, partial results, changed context, deliberate reruns and conflicting effects. Retrying transport should not create a new determination. A new run should remain distinguishable from a retry. Do not promise exact replay where external tools cannot provide it. The correct response to stale results (reject, re-evaluate, compare or apply selectively) is a game/authority decision, not an automatic technical rule.

## Open boundaries

Scott specifies higher-classification processing outside the application and a sneaker-net boundary with no digital connection. No adapter crosses that boundary. A team member may enter only suitably authorized effects appropriate to the game’s classification; this does not grant authority to declassify. Detailed handoff/handling procedures remain unresolved. Do not infer deployment on JTE/JTEN. AI may later assist retrieval, summaries or alternative assessments; deterministic lineage, version checks and human judgment are sufficient for the first experiment. Any AI output remains distinguishable from source evidence.

Visibility boundaries must also cover provenance links, arguments, metadata and derived summaries, which can expose information even when a final result is withheld. The policy is approval-required; technical enforcement must be evaluated against that approved policy. Distinguish likelihood, confidence, disagreement and randomness rather than forcing them into one score.

**Scope and policy clarification:** Architecture comparison and adapter experiments are optional learning work selected by the episode’s actual pain point, not mandatory first-milestone components. The map’s turn/approval sequence remains a configurable proposal, not authorized enforcement. An action, determination, accepted effect and released account may legitimately differ; do not force equality. Shared World View availability does not prove individual receipt, awareness, understanding or belief. Keeping external security authority outside the core does not waive application access handling. Use synthetic information only for early experiments and test illustrative access boundaries without claiming production authorization. Real data requires an established policy and authorized operating boundary.

## Refinement from approved answers

Authority attaches differently to scenario facts, actual communication records, adjudicated outcomes and claims/promises. Candidate records should preserve those distinctions without converting statements to world-state facts. An agreement can affect later adjudication while execution remains separately established.

The adjudication team’s consensus and director’s verbal final approval are the specified governance. Proposed minimal capture is a team member’s attributable record of meeting/determination and reported verbal approval, with correction history. Do not create a director account/workflow or individual voting/signature system. Detailed capture and exceptions await agreement.

M&S boundary must tolerate a human-operated file/CSV exchange on the game side: retain original file, context, interpretation and reviewed consequence; mapping is counterpart-specific. API adapters are optional later. CSV support does not imply a universal military-move schema or a higher-classification digital transfer. SWIFT/AFSIM remain research candidates.

Prioritize a compact adjudication-to-feedback and continuity workspace over a generic audit interface. Display cross-domain consequences, team-reviewed relations, open issues and audience-specific feedback using the approved record/view distinctions. Geographic rendering, automated relationship inference and simulator connectors remain hypotheses for later evaluation.


**Tool-boundary finding:** SWIFT’s historical game-conduct features overlap this product; integration would require explicit ownership boundaries for records, adjudication and views, not merely a calculator adapter. AFSIM evidence supports version-specific exports/scripted extensibility, not a verified strategic-action REST/CSV roundtrip. DATE supplies scenario-construction context. Support manual request/result handoffs before selecting any real adapter; see RESEARCH.md for sources and limits.

**Visualization and exchange clarification:** A lightweight operating-environment view can expose relevant actors/locations, current conditions, related actions and audience information without committing to full GIS. Manual CSV is a result-exchange fallback, not a universal input contract; counterpart request formats and human translation remain tool-specific and unverified.

## Implemented prototype boundary

`app.py` combines a loopback HTTP handler and small SQLite store; `static/` is a vanilla UI, `fixtures/baseline.json` initializes synthetic records, and `tests/` checks store/HTTP/browser behavior. SQLite retains latest JSON records and immutable prior revision snapshots, not a distributed event stream. Context has a coarse version; requests pin context/action versions, imports retain originals/mapping, and stale status is recomputed. Decisions link an action and optional matching result, distinguish draft effects from approved determinations, and retain amendments. Releases snapshot audience-authored accounts; prior releases remain historical after correction.

Player responses are explicitly built from public/own fixture information and public/own released accounts; controller metadata is never returned in that projection. The view selector is freely selectable, so this is a correctness demonstration rather than production authorization. Controller handover exports full records/revisions and carry-forward context. Detailed runtime/limits are in README.md.
