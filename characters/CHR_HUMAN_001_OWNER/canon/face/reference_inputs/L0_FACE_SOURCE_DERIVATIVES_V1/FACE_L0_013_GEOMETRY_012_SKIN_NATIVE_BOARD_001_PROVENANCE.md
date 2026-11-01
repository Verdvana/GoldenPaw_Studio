# Native L0 face input board provenance

{
  "asset_id": "OWNER_FACE_L0_013_GEOMETRY_012_SKIN_NATIVE_BOARD_001",
  "asset_level": "L0",
  "generated_or_real": "REAL",
  "approval_status": "REVIEW_REQUIRED",
  "file_path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_013_GEOMETRY_012_SKIN_NATIVE_BOARD_001.png",
  "physical_file_role": "UNIQUE_DERIVATIVE",
  "source_images": [
    {
      "asset_id": "OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png",
      "sha256": "1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91",
      "operation": "paste at (0,0), native size; geometry only"
    },
    {
      "asset_id": "OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001",
      "path": "characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png",
      "sha256": "89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd",
      "operation": "paste at (700,0), native size; skin only"
    }
  ],
  "authoritative_for": [
    "left panel: inherited L0 face identity/feature geometry only",
    "small right panel: inherited L0 skin context only"
  ],
  "must_not_define": [
    "AI identity",
    "panel borders or gray mask",
    "source hair/makeup/jewelry",
    "body",
    "outfit",
    "pose",
    "lighting",
    "background"
  ],
  "checksum_sha256": "c2fccf2229c42206947edc41e9cacc04a0a702e9ca94f2a866b96f14d1f0ade0",
  "operation": "Pillow RGB native-pixel side-by-side montage on neutral gray. No resize, recolor, retouch, AI or identity averaging. References each retained at original dimensions.",
  "created_at": "2026-10-31"
}

Created to satisfy the built-in tool maximum of five image paths. Both individual derivatives retain their existing immutable-original provenance in PROVENANCE.md; no new identity or Canon authority. Exactly one physical file for this board. The source crops remain separate existing assets, not duplicated files of this derivative.
