# Transmission derivative provenance

{
  "asset_id": "OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_TRANSPORT_Q95_v1",
  "asset_level": "L1",
  "generated_or_real": "GENERATED",
  "approval_status": "REVIEW_REQUIRED",
  "physical_file_role": "UNIQUE_DERIVATIVE",
  "file_path": "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/transport_v1/BODY_01_FRONT_FACE_EXCLUDED_TRANSPORT_Q95.jpg",
  "source_path": "characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png",
  "source_sha256": "59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b",
  "checksum_sha256": "4139759b58e20ff5a2dde3193afb1833f12103fb86a17f92c0e2ae16f74dab0e",
  "operation": "Deterministic Pillow RGB JPEG quality=95, subsampling=0, optimize=True; original dimensions; no resize, geometry/pose changes, retouch, AI or color adjustments. JPEG compression may discard fine detail; this is transport only, not a new design/Canon.",
  "authoritative_for": [
    "Inherited source responsibility only: neck-below body geometry"
  ],
  "must_not_define": [
    "face",
    "skin",
    "identity",
    "hair",
    "hosiery material",
    "light",
    "background"
  ],
  "created_at": "2026-10-31"
}

Scoped sole authoritative derivative file. Original remains unchanged. Created after repeated image_gen connection failures with five PNG references while two-input design generation succeeds; payload-size cause is unconfirmed. Do not use this derivative to establish fine textile detail.
