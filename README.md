# Relief-access synthetic prototype

A persistent local Python/SQLite prototype for Scott's approved strategic relief-access episode. No third-party runtime dependency. Synthetic data only; no actual SWIFT/AFSIM integration, AI, GIS, or digital higher-classification connection.

## Run

From this directory, using Python 3.10 or newer:

```sh
python3 app.py --port 8000 --db prototype.sqlite3
```

Open http://127.0.0.1:8000. Records persist in the chosen SQLite file across restarts. Use a new database path for a fresh fixture; stop the server before moving/deleting a database. This binds loopback only. Do not publish it or use sensitive data.

## Walkthrough

1. Read the synthetic Road to Crisis, actor/location/condition cards and recorded agreement. The agreement's occurrence is recorded; its promise is not execution.
2. Save an open-ended action and optional actor/context note. Prepare a request CSV that reuses the record. A human must translate requests into a real counterpart's format; no counterpart accepts this schema by implication.
3. Fill the synthetic result example for the latest request or paste one CSV row and explicitly map headers. Importing retains original bytes/mapping and aggregate estimates; it establishes no state effect. Repeating identical CSV plus mapping is visibly deduplicated.
4. Record a late agreement/context update or correct the action. The old result is marked stale. Describe the team's disposition if using it; no automatic adjudication occurs.
5. Capture human cross-domain assessment, proposed/established effects, uncertainty, related actions/agreements and carry-forward issues. Optional tool evidence must relate to the selected action. Draft effects remain proposed until team consensus and reported verbal director approval are captured.
6. Write public/Aster/Bellwether feedback. Save, then explicitly release the captured accounts. The recording team member reports governance; no director user, voting or signature process exists.
7. Inspect each player projection. It includes public information, that player's intelligence and public/own released feedback, without controller evidence/history or the other player's intelligence/feedback.
8. Revise a determination with a correction reason; recapture consensus and reported director approval. Release the corrected account. Earlier decision versions and release accounts remain available as history; superseded feedback is explicitly labeled. Download controller handover JSON to preserve the complete context and latest carry-forward notes.

## Synthetic manual exchange schema

Request export: `request_id,action_id,action_version,context_version,action,context_note,instructions`. It is a human preparation aid, not a simulator input contract.

Result import: exactly one row; explicit semantic-to-header mapping for `request_id`, `availability` (finite fraction 0–1), `delay_days` (finite nonnegative estimate), `note` (assumptions). This is a named prototype fixture schema only. No AFSIM/SWIFT compatibility or REST API is claimed. Duplicate detection covers identical original CSV and mapping; differently serialized equivalent results may require human review. Context/action revisions flag prior evidence stale. Decisions pin action revisions; changing an action blocks release of its prior determination until reviewed. Corrections require the current record version. Import and decision records remain separate.

## Checks

```sh
python3 -m unittest discover -s tests -v
python3 tests/browser_walkthrough.py
```

The browser check requires Python Playwright and Chromium at `/usr/bin/chromium` (available in the saved cloud environment). Runtime use does not require them. Tests use disposable SQLite databases. Browser checks write controller/player screenshots to `artifacts/`.

## Limits and deliberate cuts

- No authentication: the view selector and request header are freely selectable. Server projections and read-only demo player endpoints are tested, but provide no production access control. Users on the local server can select controller view. No information-isolation/security accreditation claim.
- A recorder attests consensus and verbal approval; software does not verify the meeting or approval. Stale-context and revision guards prevent accidental reuse in the demo, not establish complete game rules.
- Human-authored feedback can itself disclose information; no automatic release-policy validation. Use invented content only. No classified samples, connector or digital security boundary.
- Context revision is deliberately coarse. No full world-state engine, turn scheduler, scenario editor, RFI/CCIR/task system, multiuser conflict UX or operational recovery. History is record snapshots, not an event-sourced architecture.
- The operating environment is a lightweight context view; it is not GIS. Aggregate military estimates and human assessments are linked, not numerically merged. No tactical optimization or automated causality.
- This working workflow has not yet been evaluated by actual players for reduced entry burden or better feedback. Prototype tests demonstrate behavior, not product value.
