# Research — questions that change the concept

Status: initial findings and proposed experiments, 2026-10-07. Source evidence is distinct from recommendations. Parent-led independent research is coordinated separately; no additional agents were launched here.

## Asynchronous external analysis

**Evidence, checked directly:** [OGC API Processes Part 1](https://docs.ogc.org/is/18-062r2/18-062r2.html), especially sections 7.10–7.13 and 13, separates process descriptions, execution, job status, result retrieval and dismissal. **Inference:** This is a useful reference for an adapter job lifecycle; it does not establish wargame acceptance or release authority and does not require adopting OGC conformance. **Experiment:** Return the same synthetic result twice, deliver a result after its input state changes, and race cancellation with completion. Preserve outputs while making duplicate/stale status explainable. A successful run must not silently become an accepted state change.

## Provenance without a storage commitment

**Evidence, checked directly:** [W3C PROV Primer](https://www.w3.org/TR/prov-primer/) describes entities, activities and agents and their derivation/responsibility relationships. **Inference:** Use these concepts to test whether evidence-to-decision-to-effect lineage is sufficient; neither RDF nor a graph database is selected. **Experiment:** Ask a reviewer to reconstruct who determined an outcome, with what input version, method, uncertainty and dissent, including a later correction.

## Additional independent research supplied by parent

These leads and summaries were provided by the parent; not independently re-verified here:

- [IEEE HLA 1516](https://standards.ieee.org/ieee/1516/6687/) and [NASA time-management discussion](https://ntrs.nasa.gov/citations/20250001356): investigate only if a named counterpart requires live simulation time/state/ownership coordination. A batch analysis exchange is not evidence of that need.
- [IEEE DIS 1278.1](https://standards.ieee.org/ieee/1278.1/4949/): domain-specific PDU exchange may warrant an adapter gateway. Parent reports the linked 2012 entry as Inactive-Reserved; do not characterize it as a current active standard.
- [RFC 9110](https://www.rfc-editor.org/rfc/inline-errata/rfc9110.html): conditional writes are a candidate conflict-prevention mechanism, not a technology commitment or a decision about whose game judgment prevails.

## Mixed adjudication: investigate before standardizing

**Charter evidence:** Matrix-based, structured rules, SME/controller judgment, qualitative, probabilistic, hybrid and AI-assisted approaches must be considered. **Hypothesis:** A common record of context/evidence/determination/effects can support them, while method-specific structures remain different.

| Candidate method | What a prototype should preserve | Evaluation question |
|---|---|---|
| Matrix/argument-based | Claim, reasons, counterarguments, resolution basis | Can competing causal explanations remain visible without imposing a numeric score? |
| Structured rules | Rule/version, inputs, exceptions and interpretation | Can participants explain both computed outcome and human exception? |
| SME/controller or qualitative | Judgment, basis, uncertainty and dissent | Does recording support judgment without adding artificial precision? |
| Probabilistic | Distribution/assumptions, draw or seed if available, interpretation | Can uncertainty and repeat-run variation be distinguished from errors? |
| M&S / hybrid | Original output, model/input versions, applicability, reviewed interpretation | Can a human challenge or partly use the result without losing its origin? |
| AI assistance | Sources, generated output, review/corrections, fallback | Does it outperform search/templates on a named task, with acceptable unsupported claims? |

These are experimental recording candidates, not mandatory player forms. No empirical claim of method superiority is made. “Matrix” is unresolved: argument-based matrix gaming and lookup-table matrices require different records; do not silently choose between them.

**Independent method research supplied by parent (not re-verified here):** The [UK MOD Wargaming Handbook](https://assets.publishing.service.gov.uk/media/5a82e90d40f0b6230269d575/doctrine_uk_wargaming_handbook.pdf), sections 3.6, 3.11–3.12 and figure 4.2, distinguishes free, rigid, semi-rigid and consensual adjudication and places models/spreadsheets among adjudicator inputs. The [Influence Wargaming Handbook](https://assets.publishing.service.gov.uk/media/6494481b9e7a8b00139329d8/Influence_Wargaming_Handbook_web.pdf), sections 4.26–4.28 and 4.50, supports mixed techniques and deliberation around computed starting results. [Downes-Martin](https://digital-commons.usnwc.edu/nwc-review/vol66/iss3/6/) examines adjudicator influence. **Design inference:** Preserve interventions, overrides, independent assessments, aggregation and dissent, rather than treating a tool or table as self-authorizing.

Parent also supplied [UK intelligence uncertainty guidance](https://www.gov.uk/government/publications/explaining-uncertainty-in-uk-intelligence-assessment/explaining-uncertainty-in-uk-intelligence-assessment). **Proposal:** Distinguish likelihood, analytical confidence, disagreement and randomness, retaining qualitative scales without invented precision. For lookup tables retain table version/cell; for argument-based methods retain claims/counterarguments and facilitation; none become mandatory player fields.

**Refined experiment:** Resolve a fictional, non-tactical disruption with several human methods, then ask a fresh analyst to reconstruct rationale, authority, consequences and disagreement. Measure capture effort and missing context, not agreement between methods. Add stale external output versus conflicting SME assessment and an explicit override. Provenance and argument links can themselves expose hidden information, so audience tests must include those links and derived summaries, not only the final products.

## Bounded next work

The following is an optional experiment menu. Select only work that reduces uncertainty exposed by the chosen episode and pain point; neither a two-method comparison nor a fake asynchronous adapter is a mandatory first-milestone feature. Use synthetic information pending real policy and authorized data boundaries.

1. Walk one real or approved synthetic episode with players/control: record handoffs, re-entry, delay, disagreement and what each audience knows. Reject pain-point hypotheses not observed.
2. Compare a document-centered mockup with the proposed linked-record concept using that episode; evaluate user effort and reconstruction quality.
3. Exercise at least two non-M&S methods and one fake adapter through the same evidence/review path. Do not collapse method-specific reasoning into a universal numeric result.
4. Obtain the smallest sample exchange from a named M&S counterpart: determine units, identity, timing, fidelity, file/API availability and provenance before selecting standards.
5. Use synthetic audience examples to test whether approved information policy is representable; actual protected data awaits an authorized boundary.

AI, workflow engines, event sourcing and knowledge graphs remain optional research topics tied to demonstrated problems, not milestone prerequisites.

## Research questions from Scott’s answers

DATE World should inform a strategic synthetic context, not require a tactical simulator or import a scenario/license without review. Parent primary-source findings are incorporated below. SWIFT/AFSIM are candidate tools to investigate for actual exchange modes, access and applicability; do not infer public APIs, CSV schemas or availability. Test manual exchange feasibility with synthetic data first. No higher-classification connector or classified sample is needed.

The six reported frictions are mapped to hypotheses/tests in PROCESS_ANALYSIS.md. The leading value test is whether approved prior-action feedback supports player decisions and whether another adjudicator can continue the episode without losing consequences, commitments or unresolved issues. Record reconstruction is supporting evidence rather than the product goal.


## DATE, SWIFT and AFSIM — parent primary-source findings

Source snapshot: 2026-10-07; primary sources inspected by parent, not independently re-verified here. Separate documented capabilities from historical/version-specific evidence and unverified interfaces.

| Subject | Supported evidence | Limits / design consequence |
|---|---|---|
| DATE | [Army ODIN DATE explanation](https://odin.t2com.army.mil/How-To/DATE/Decisive_Action_Training_Environment_%28DATE%29) describes an environment for constructing scenarios, not a scenario itself. [Current Army OE site](https://oe.t2com.army.mil/) describes five regions and 24 notional countries | Do not reuse stale four-region descriptions or call our synthetic fixture an official DATE scenario. No API/CSV contract verified; source/content version must be pinned if later used |
| SWIFT | Developer-authored [2016 article, pp. 24–27](https://www.cdi.marines.mil/LinkClick.aspx?fileticket=8n3ILtdwe7c%3D&mid=40125&portalid=172&tabid=18370) describes turns, human/computer adjudicators, fog-of-war views, playback, White Cell selection of proposed outcomes, Excel import/export and XML storage. [2022 DoD GEMS report, p. 59](https://ac.cto.mil/wp-content/uploads/2022/12/Advancing-Gaming-Exercising-Modeling-and-Simulation-GEMS-Capabilities.pdf#page=59) describes visualization, recording, extraction, branching, automated adjudication and human override | Historical evidence, not a verified current CSV/API schema. SWIFT-Global development in 2022 does not prove current availability. SWIFT overlaps game conduct, so establish ownership of state, adjudication and information products before integrating |
| AFSIM | [Official 2022 overview, p. 87](https://ac.cto.mil/wp-content/uploads/2022/12/Using-Modeling-and-Simulation-to-Increase-Speed-to-Market-Reduce-Risk-and-Foster-Interoperability-in-the-Industrial-Base.pdf#page=87) describes a military multiresolution/multidomain framework with controlled access. [AFRL v2.0 reference, p. 12](https://imlive.s3.amazonaws.com/Federal%20Government/ID156700649043486100007468415908987547373/Attachment_1_-_AFSIM.pdf#page=12) documents historical scripted outputs/plugins/DIS/HLA/XIO. [Core developer DCS](https://dcscorp.com/home/what-we-do/afsim/) describes Mystic filtered-event CSV export, scripted input/custom output, Warlock panels and API documentation | “Open source” does not mean unrestricted public distribution. No REST API, strategic-action CSV import, full state roundtrip or native DIE/FIL adjudication verified. Installed tool/version/schema and authorized access are required before an adapter commitment |

**Design inference:** Baseline support is a manually prepared request package plus retained, mapped and human-reviewed results. CSV export capability does not establish compatible input/output schemas, eliminate human translation or make a result authoritative. API and live federation are conditional future options. No tool is selected; no higher-classification digital connection is contemplated.

**Refined proposed test:** Synthetic relief-access crisis, with aggregate availability/delay evidence only. Human adjudicators handle political/economic/information consequences. Exercise a late agreement changing assumptions, delayed/duplicate result, enduring correction across adjudicator handoff, and appropriate player feedback. Measure repeated entry/translation, missing cross-domain links, continuity and player understanding; generic audit completeness alone is insufficient.

**Prototype learning:** Persistence and revision history fit this bounded workflow using SQLite snapshots without an event-sourcing framework. Browser checks demonstrate explicit result mapping, original retention, duplicates/stale context, audience projections and correction/handover continuity. No new source research or actual counterpart interface verification was needed. Product-value hypotheses still require player/team evaluation.
