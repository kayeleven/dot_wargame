# Vision — initial concept draft

Status: 2026-10-07; concept review, not an approved product specification.

**Charter direction:** Enable the conduct of wargames across human decisions, information exchange, adjudication, and state development. Develop an independent solution; do not import the other project's design. AI is optional. External M&S supplies specialized analysis, not the organizing premise of the product.

**Interpretation:** The central problem is maintaining a comprehensible, traceable relationship between what participants know, what they propose, what evidence supports an outcome, what a human determines, and what changes or is released. Digitizing the diagram alone could preserve possible bottlenecks and impose unvalidated rules.

**Observed users:** Player cells; White Cell/game control; adjudicators and SMEs; analysts; RFI and reporting coordinators; external information and simulation providers. The map names possible owners but explicitly calls for validation. These are activities and candidate responsibilities, not an approved permission hierarchy.

**Proposed boundary:** Support preparation, baseline and perspective information, action development/submission, RFIs, adjudication work, external-tool exchanges, human review, state proposals, audience-specific products, communication records, and after-action reconstruction. Keep specialist simulation, external organizational authority, and policy determinations outside the core. Higher-classification processing remains outside the application, with no digital connection; suitably authorized lower-classification effects enter through a human handoff, as Scott specified.

**Proposed concept of operation:** Establish a scenario baseline and approved information policy; provide the appropriate information to each participant; collect actions and questions; assemble evidence using applicable human, rule-based, probabilistic or simulation methods; review outcomes and proposed effects; reconcile state and information products; release and carry forward according to the game's approved policy. Activities may overlap. This is a discussion model, not a mandatory sequence or approval chain.

**Preparation and continuous support:** Turn 0 setup needs to represent the game's parameters and analytic objectives, live/simulated/enabler cell makeup and relationships, authoritative scenario baseline, initial World View and initial perspectives. Which setup fields or approvals are mandatory remains undecided. RFIs, CCIR monitoring, analysis and external task/reporting coordination continue across play; they are not merely attachments to one action or automatic turn-closure blockers. The first episode milestone samples this broader concept rather than defining its full scope. References to an approved policy describe a future prerequisite for applicable behavior; Scott has since specified the core authority, information-view and compartmented-boundary principles below; detailed access/release procedures remain open.

**Desired outcomes / hypotheses to evaluate:** Less re-entry and lost context; visible outstanding work; faster explanation of decisions; fewer conflicting state updates; traceable information releases; usable records for after-action analysis. No baseline performance measurements exist yet.

**Initial recommendation:** Identify a representative synthetic episode and its actual pain point, then implement only the smallest demonstrable benefit over the existing process. An evidence-to-reviewed-effect slice is one candidate, not the predetermined milestone. Mixed-method comparison and a fake asynchronous adapter are optional experiments if that episode exposes those uncertainties. Work without AI or live simulator coupling unless later evidence warrants them. See [ROADMAP.md](ROADMAP.md) and [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md).

**Explicit noncommitments:** No selected framework, database, hosting topology, scale target, fixed move vocabulary, mandatory turn structure, detailed role hierarchy, or detailed release procedure beyond Scott’s answers below. The map's UNCLASSIFIED banner and network terminology do not establish deployment authorization or security policy.

**Information distinctions:** A proposed action, adjudicator determination, accepted state effect and released account may legitimately differ. Shared World View availability does not establish what every player has actually received, understood or believes. External security authority remains outside the product, but application access handling remains a product responsibility under the eventual approved policy. Early experiments use synthetic information only; real policy and data boundaries remain unresolved.

## Scott’s approved answers — concept refinement

Source: Scott’s review answers supplied after the initial draft. “No substantial changes” is review feedback, not blanket approval of unanswered proposals.

- **Authoritative record:** Initial scenario documentation (Road to Crisis), adjudicated action/move results, and captured actual intra-player communications and agreements together form the authoritative record. A communication’s occurrence/content can be authoritative without its assertions being true. An agreement or promise is not evidence of execution. Separate recorded events, asserted propositions, intended commitments and adjudicated effects.
- **Information:** World View is open-intelligence-like information that “makes the news.” Player Perspective amplifies it with information available from that player’s intelligence community. Shared availability does not prove individual awareness. The adjudication team approves.
- **Governance:** The adjudication team meets and reaches consensus. The Game Director gives final approval verbally to that team and does not interact with the system. Individual voting, signatures and a director account are not specified.
- **Compartmented boundary:** Higher-classification information is processed at the appropriate location outside the system. The boundary is sneaker-net, with no digital connection. Only suitably authorized effects at the game’s classification enter through human handoff. This does not grant declassification authority. Do not request classified samples or add a digital cross-boundary connector.
- **M&S:** Exact tool/interface is unknown. Baseline interoperability must accommodate manual CSV export; API exchange is a possible better case. SWIFT and AFSIM are research candidates, not selected integrations or established formats.
- **Context:** Strategic games using US Army DATE World, with military, diplomatic, economic, information and other actions. Use a synthetic, non-tactical episode to evaluate cross-domain consequences and information flow.


**Revised value hypothesis:** The first useful result should give players meaningful prior-action feedback and help the adjudication team carry consequences, agreements and unresolved issues forward. Traceability supports that outcome; a generic audit record alone is not the intended benefit. Turn 0 and continuous RFI/CCIR/reporting/AAR remain in the product horizon.

**Current stage:** Scott approved the relief-access episode and the bounded synthetic working prototype is implemented. It connects open actions, manual analytical exchange, human cross-domain determination, useful audience feedback and continuity. This demonstrates the concept; player benefit and production access policy remain to be evaluated. See README.md for runnable scope and limitations.
