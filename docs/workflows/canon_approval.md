# Canon Approval and Freeze Workflow

## Gates

1. Gate 1 — L0 intake, manifest, quality/coverage review, identity analysis.
2. Gate 2 — Face Canon candidates; explicit user approval.
3. Gate 3 — Body proportions and calibration outfit; explicit user approval.
4. Gate 4 — Hairstyles A/B; explicit user approval.
5. Gate 5 — Expression anchors; explicit user approval.
6. Gate 6 — body/pose anchors; explicit user approval.
7. Gate 7 — hosiery/feet material Canon; explicit user approval.
8. Gate 8 — final Canon manifest review and character-version lock.

Do not proceed through a closed gate. Cat and prop programs use the same candidate -> QA -> approval -> manifest -> lock pattern, with category-appropriate checks.

## Approval evidence

For each approved item, create a record from `templates/approval/CANON_APPROVAL.md`. It must contain the user's exact approval statement or a faithful short record, date, scope, exclusions, asset hash if available, and the resulting asset/version ID.

## Physical promotion

After approval evidence is recorded and checksums are verified:

1. Move the candidate raster to the approved Canon path; never copy it.
2. Update the approved metadata and registry to the new path and checksum.
3. Keep the candidate generation record and QA. Record the original candidate path/checksum plus the current approved path/checksum, then remove any candidate raster sidecar that assumes a second pixel copy exists.
4. If the user transcodes the approved Master, verify the result, retain the old checksum in text provenance, and keep only the active-format raster.
5. Candidate input provenance must point to the single stored source or reusable derivative; candidate-local input image copies are forbidden.

## Lock procedure

1. Verify every manifest dependency is approved and uses a stable ID.
2. Verify every image has responsibility metadata and no unresolved QA blocker.
3. Instantiate the version manifest template at `canon/versions/<version>/CANON_MANIFEST.yaml` and enumerate exact paths/hashes; do not duplicate component rasters.
4. Set `lock_status: LOCKED` only after explicit user instruction to lock that version.
5. From then on, consumers pin this version. Changes require a new version directory and change record.

Folder placement does not grant approval. Filename words such as `canon`, `final`, or `approved` do not grant approval either.
