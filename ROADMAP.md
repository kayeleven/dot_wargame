# Roadmap — revised concept proposal

Status: Scott’s scope/governance answers incorporated; episode and milestone below require review. No application implementation authorized.

## Concrete proposed episode

Use a fictional strategic regional-disruption episode inspired by DATE World context, without claiming an official DATE scenario or importing restricted material. A storm disrupts a fictional commercial port, threatening civilian trade, relief access and public confidence. Players offer high-level military relief support, negotiate access with economic pressure, and issue conflicting public accounts. These are example contributions, not prescribed player roles or an allowed-action list. Players communicate and reach an agreement, but promised action is not presumed executed. This exercises military, diplomatic, economic and information consequences without tactical plans, targeting or weapons optimization.

Turn 0 is a short Road to Crisis, agreed initial conditions, news-like World View and distinct intelligence additions for each player. The adjudication team meets, considers consequences and interactions, reaches consensus and receives director verbal final approval. A team member records the determination and reports that approval. Approved feedback gives each player an appropriate account of prior actions and known effects; a continuity packet carries unresolved consequences/commitments to the next episode. The director has no system role.

Synthetic qualitative military-support evidence is sufficient initially. A manual synthetic CSV example or another non-M&S method is optional if it helps test a material uncertainty. Exact turn duration, mandatory move fields, method taxonomy and release timing are not imposed by the example.

## Smallest useful milestone — proposal for review

Create a small adjudication-to-player-feedback slice for this episode: reuse a linked action/context record in a human-prepared analysis request and adjudication discussion, capture the team’s agreed outcome, and produce meaningful audience-specific prior-action feedback plus a compact carry-forward packet. A manually mapped synthetic CSV result may be used where it tests repeated entry; no real-tool format or automated translation is presumed. Link only the scenario context, actions, actual agreement, relevant evidence and cross-player interactions necessary to explain consequences. Start with a reviewable mockup and walkthrough; implement only the functions demonstrated useful afterward.

Proposed benefit test: a player can explain what happened to their prior action, its known cross-domain consequences and what remains unresolved; another adjudicator can continue with consistent commitments/context. Compare repeated entry/translation, player comprehension, missing cross-domain links and capture effort against current practice. This is more than storing an audit trail, but does not require a complete play platform.

Proposed acceptance:

- Scenario/adjudicated effects and actual communication occurrences remain distinct from claims, promises, inferred causality and execution.
- Shared news-like World View and player intelligence amplification support meaningful feedback without exposing withheld evidence/provenance; availability is not equated with individual knowledge.
- Team consensus and reported verbal director approval can be attributed by the recording team member; no votes/signatures/director account are invented. Capture design and exception handling await review.
- A replacement adjudicator identifies carry-forward effects, agreement status and unresolved questions; a player identifies known outcome and relevant uncertainties.
- Synthetic data only; higher-classification processing remains external with no digital connection. Any illustrative human-entered effect is explicitly synthetic and does not establish a release procedure.
- No new mandatory move types/fields, universal turn gates or numeric uncertainty scales are introduced.

## Deferred and optional work

All six frictions have concept tests in PROCESS_ANALYSIS.md, but are not mandatory milestone features. Optional experiments: operating-environment briefing view; manual CSV translation/re-entry comparison; mixed-method pairing; reviewed cross-player links; delayed/conflicting result handling. Use them only where the episode demonstrates need.

Defer real simulator integration and formats, GIS/world rendering, automated move translation, automated relation inference, broad adjudication-method library, AI, live federation, workflow designer, deployment and production access/handling authorization. Turn 0, ongoing RFI/CCIR/reporting and AAR remain the broader product horizon. Parent primary-source DATE/SWIFT/AFSIM research is incorporated with version/interface limits in RESEARCH.md. Review the episode/milestone before final packaging; no named tool or method is selected.

**Optional stress fixtures:** A late access agreement invalidates prior analytical assumptions; a delayed or duplicate synthetic result arrives; an adjudicator corrects an earlier consequence and the correction persists into feedback and the next discussion. Use only fixtures relevant to the approved episode. No number/length of turns, required fields, countries or universal method is prescribed. Higher-classification effects, if illustrated, are invented lower-classification-safe placeholders, not classified samples.

**Lightweight visualization test:** The proposed walkthrough can include a simple operating-environment view of relevant actors/locations, current conditions, related actions and audience information. Test whether it improves comprehension and feedback; full GIS remains deferred. Manual CSV is an interoperability fallback for exported results, not evidence that every counterpart accepts CSV input. Requests may need human translation into the installed tool’s supported format. Episode/milestone remains proposed for Scott’s review; draft packaging does not authorize implementation.

## Approved episode — first prototype delivered

Scott approved this episode; the subsequent delegated task authorized the bounded working prototype. The core walkthrough is now implemented with SQLite persistence rather than a static demonstrator. Run/test instructions and deliberate cuts are in README.md. Next: user walkthrough comparing repeated entry, feedback comprehension and handover effort with current practice. Expand only from observed gaps. Original proposal text above is historical framing; it does not block the authorized slice or approve production release. No push/deployment authorized.
