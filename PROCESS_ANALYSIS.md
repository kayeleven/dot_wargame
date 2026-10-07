# Process analysis — source observations and interpretations

Status: initial draft, 2026-10-07. **Observation** means the supplied map says it; **hypothesis** means a possible implication, not measured behavior. The inventory preserves original map uncertainties. Scott’s later answers below resolve core adjudication/approval and compartmented-boundary questions; remaining ownership and criteria need validation.

## Source basis and coverage

- Charter: Library `libfile_4e0e92f4631881919f306b720e485222`, Pasted text(3).txt, reported 13,389 bytes; complete 396-line text read.
- Map: Library `libfile_1ec027fee9a88191b9fb1d1f6331d7a8`, Pasted text(4).txt, reported 87,629 bytes; complete 4,066-line HTML source read, including CSS, visible definitions, all NODE_INFO entries, EDGES, FLOW_GROUPS, and interaction code.
- Local materialization failed; the supported Library text reader supplied the complete content instead. Original local bytes/checksums and browser rendering are unverified. Chromium and Playwright are available, but no successfully materialized input is available to render. No source files were fabricated from snippets.
- DETAIL_PAGES contains commented examples only. The hidden-on-selection process details are embedded in NODE_INFO; they were included in this review. UI highlighting is navigation behavior, not evidence of runtime workflow enforcement.

## Observed process inventory

| Map node(s) | Information and decision | Candidate responsibility / uncertainty |
|---|---|---|
| START | Approved prior state or authorized start condition opens the cycle | Turn-control authority unvalidated; initialization is not necessarily a prior turn |
| GSU | Prior approved state, validated scenario changes and carry-forward information establish current conditions | White Cell/state manager unvalidated; player visibility ambiguous |
| PCTD | Current information, perspective, CCIRs and RFI responses inform actions and rationale | Player-cell lead unvalidated; actual planning collaboration undefined |
| PCTI | Structured action submission enters intake/routing | Player lead and intake authority unvalidated; format/completeness not approved |
| COMPQ / COMP | Handling decision either goes directly to adjudication or through protected RFIs, adjudication and M&S support, then returns | Handling/security authority and protected-process lead unvalidated; release/reintegration unresolved |
| ADJ | Action, parameters, SMEs and applicable M&S results produce outcomes and rationale | Adjudication lead/delegation unvalidated; methods and standards undefined |
| ARI | Outcomes, rationale and release guidance become recorded downstream inputs | Results manager unvalidated; record/schema/system of record unspecified |
| PERRQ / PERSP | Decide whether player-specific products are needed; develop perspective/COP products | White Cell/product lead unvalidated; audience, timing and intelligence rules unresolved |
| GSD | Results, perspective products and scenario information contribute to proposed next state | State manager unvalidated; integrating products must not promote beliefs to facts |
| EOT | Review proposed state, external outputs and outstanding issues; close and authorize carry-forward | Approval authority and closure criteria unvalidated |
| RFI | Bidirectional questions/responses support development; response may be delivered, deferred or unresolved | RFI coordinator unvalidated; external channels and disclosure unspecified |
| CCIR | Persistent critical-information monitoring and updates support decisions | Manager/approval authority unvalidated |
| ANALYSIS | Actions, scenario, SMEs and M&S inform effects and uncertainty | Analytic lead unvalidated; analysis may continue through the turn |
| TASKS | Tasking, reports and suspense/status converge on closure | Reporting lead unvalidated; outstanding-item treatment unspecified |

The 18 explicit edges encode a primary sequence START → GSU → PCTD → PCTI → COMPQ → ADJ → ARI → PERRQ → GSD → EOT; conditional COMPQ → COMP → ADJ and PERRQ → PERSP → GSD branches; PCTD ↔ RFI; CCIR → PCTD; ANALYSIS → ADJ; TASKS → EOT; and EOT → GSU carry-forward. This is evidence of a turn-oriented process, not approval to hard-code these gates. Nine subprocess cards explicitly request further definition.

Turn 0 information includes parameters (turn length, action types, metrics, objectives, thresholds), cell makeup (live/simulated/enabler cells, relationships, authorities, SMEs), and scenario/truth (initial player and simulated-cell perspectives, World View, authoritative baseline). These are topics to resolve, not approved required player fields. JTE/JTEN are defined but no integration edge or required deployment is specified.

## State, knowledge, and authority ambiguity

**Observation:** GSU produces current authoritative state and says current state becomes available to player cells. Elsewhere World View is White Cell-provided reality equally available to players, and Perspective is a particular player's view/intelligence. GSD consumes perspective products while proposing authoritative state.

**Alternative A:** GSU distributes a public baseline plus authorized player-specific products derived from a richer authoritative record. **Alternative B:** The particular game intentionally exposes its complete baseline equally, with perspective products adding differentiated information. **Alternative C:** “Game state” is an umbrella package containing authoritative facts and separately labeled knowledge products. The map does not choose among these.

**Approval-required proposal:** Keep adjudicated world conditions, shared World View, player-specific knowledge/beliefs, and narrative products conceptually distinct and linked by provenance. A perspective can be incomplete, delayed or inaccurate without changing adjudicated truth. Record that a player received a product separately from asserting its contents are true. Scott must determine authority, audience, release timing and whether any product is itself authoritative. Narrative claims and causal explanations can remain disputed; their authorship/status should remain identifiable.

## Possible pain points, not established facts

| Hypothesis | Why plausible from map | Validation / opportunity |
|---|---|---|
| Re-entry and loss of rationale at handoffs | PCTI, ADJ, ARI and GSD each package information | Walk one action and compare artifacts; preserve linked evidence/effects |
| Protected branch delays or leaks context | Return requires authorized releasable output | Trace one permitted/synthetic case; define boundary and handoff policy |
| Stale or contradictory outcomes | Analysis and external support can continue while state evolves | Exercise late/duplicate results and competing updates |
| Release confused with acceptance | ARI, perspective and state stages overlap | Separate evidence acceptance, state effect and audience release in examples |
| Turn closure becomes a queue bottleneck | Reports and outstanding issues converge on EOT | Ask what actually blocks progress; do not require all work to finish by default |
| Missing decision context after play | RFIs, uncertainty and rationale distributed across activities | Reconstruct one outcome and assess completeness/time |

Absent from the map: measured workloads/delays, rejection/rework paths, cancellation, revisions, disputes, simultaneous actions, late results, correction after release, conflict resolution, record retention, outages and adjudication-method selection. Their absence is not evidence they are forbidden. Preparation and after-action needs come from the charter, beyond the map's turn emphasis.

**Review clarification:** Shared availability of World View does not imply actual receipt, awareness, understanding or belief by every player. Proposed action, determination, accepted state effect and released account can legitimately differ; such differences are not necessarily reconciliation errors. The observed turn/approval sequence is at most a configurable workflow proposal, not mandated enforcement.

## Scott’s approved answers — concept refinement

Source: Scott’s review answers supplied after the initial draft. “No substantial changes” is review feedback, not blanket approval of unanswered proposals.

- **Authoritative record:** Initial scenario documentation (Road to Crisis), adjudicated action/move results, and captured actual intra-player communications and agreements together form the authoritative record. A communication’s occurrence/content can be authoritative without its assertions being true. An agreement or promise is not evidence of execution. Separate recorded events, asserted propositions, intended commitments and adjudicated effects.
- **Information:** World View is open-intelligence-like information that “makes the news.” Player Perspective amplifies it with information available from that player’s intelligence community. Shared availability does not prove individual awareness. The adjudication team approves.
- **Governance:** The adjudication team meets and reaches consensus. The Game Director gives final approval verbally to that team and does not interact with the system. Individual voting, signatures and a director account are not specified.
- **Compartmented boundary:** Higher-classification information is processed at the appropriate location outside the system. The boundary is sneaker-net, with no digital connection. Only suitably authorized effects at the game’s classification enter through human handoff. This does not grant declassification authority. Do not request classified samples or add a digital cross-boundary connector.
- **M&S:** Exact tool/interface is unknown. Baseline interoperability must accommodate manual CSV export; API exchange is a possible better case. SWIFT and AFSIM are research candidates, not selected integrations or established formats.
- **Context:** Strategic games using US Army DATE World, with military, diplomatic, economic, information and other actions. Use a synthetic, non-tactical episode to evaluate cross-domain consequences and information flow.


## Six reported frictions — hypotheses and tests

Scott reports these frictions; magnitude and proposed remedies are not yet measured.

| Reported friction | Concept hypothesis | Targeted test / first-slice treatment |
|---|---|---|
| Entering military moves into M&S | A linked human-prepared exchange package may reduce translation/re-entry | Count re-entry and lost assumptions with a synthetic manual CSV handoff; defer automated move translation and real formats |
| Visualizing the operating environment | A compact view of context, actor relationships and changed conditions may improve comprehension | Ask players to explain current conditions from a briefing mockup; defer GIS/world rendering unless needed |
| Pairing military M&S with DIE/FIL adjudication | A cross-domain review can retain distinct methods and reveal dependencies without forcing one score | Compare synthetic tool evidence with diplomatic/economic/information judgments; ask whether consequences/conflicts are visible; confirm DIE/FIL usage rather than infer a fixed taxonomy |
| Maintaining adjudication continuity | Carry-forward consequences, commitments and unresolved issues may reduce repeated or inconsistent reasoning | A replacement adjudicator conducts the next episode using the prior record; identify missing context and contradictions |
| Surfacing relations between players’ actions | Explicit, team-reviewed dependency/interaction links may reveal reinforcing or conflicting actions | Review a paired commitment and action affecting the same issue; distinguish observed communication from inferred causality; defer automated relation inference |
| Meaningful feedback on prior-turn actions | An approved account of outcome, relevant consequences and unresolved effects may help the next decision | Ask a player what happened, what they can reasonably infer and what remains open; check audience correctness and effort versus current practice |

These tests use synthetic information. They do not optimize weapons, targeting or tactical employment. Not all six require first-milestone features.

**Prototype evidence:** The lightweight actor/location/condition view, reusable request record, linked aggregate evidence/human assessment, explicit relation/carry-forward notes and audience feedback make all six friction hypotheses testable in a walkthrough. Unit/browser checks establish behavior, not measured friction reduction. Actual communication occurrence, claims/promises and approved effects remain distinguishable. No full GIS or real-tool compatibility is claimed.
