# Asset Model and Provenance

## Identity and responsibility

Every visual asset must have a companion metadata record based on `templates/ASSET_METADATA.yaml`. An asset is authoritative only for the fields in `authoritative_for`; everything else is either context or explicitly excluded under `must_not_define`.

Examples:

- A real owner portrait: `face_identity`; not body, outfit, or material.
- A real hosiery foot photo: textile weave, transparency, foot coverage; not identity, skin tone, anatomy, or body proportions.
- `HAIRSTYLE_B_CANON`: B silhouette, length, parting, wave, volume, face framing; not face identity, skin, body, outfit, lighting, background, makeup, or artifacts.
- Previous shot: camera direction, blocking, object placement, pose transition; not persistent appearance.

## Dependency direction

Allowed direction is L0 -> L1 candidate -> approved L1, then L1 + L2 -> L3 -> L4. An asset may depend on the same or a lower level, never on a higher level. Promotion always creates a recorded decision; it never changes an L0 original.

## Version semantics

- Patch changes (`v1.0.1`) correct metadata without changing visual authority.
- Minor changes (`v1.1`) refine a compatible Canon while preserving recognizable identity.
- Major changes (`v2.0`) alter core identity, body, fixed prop geometry, or another breaking visual contract.

Locked releases remain available for reproducing earlier episodes. Episode and shot manifests pin exact Canon versions rather than “latest.”

## Single physical file rule

Each visual asset and deterministic reference derivative is stored as one physical image file. Other records refer to it with an asset ID, repository-relative path, and SHA-256. Candidate folders do not contain copied input images.

Reusable derivatives are stored once in the nearest scoped `reference_inputs/` directory with reproducible provenance. Approval moves the candidate raster to the approved Canon path; it does not copy it. The source candidate's original path and checksum remain in text records after the raster moves. If the approved Master is transcoded, only the active format remains and both the original and current checksums are recorded.

Hard links and symlinks are not used as deduplication substitutes because they weaken immutability and portability guarantees.
