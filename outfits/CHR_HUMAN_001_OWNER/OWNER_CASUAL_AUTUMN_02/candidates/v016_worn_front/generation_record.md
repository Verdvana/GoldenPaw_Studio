# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v016

- character_id: `CHR_HUMAN_001_OWNER`
- asset_id: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v016`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `worn_front`
- candidate_version: `v016`
- status: `SUPERSEDED_BY_USER_APPROVED_v015`
- generation_tool: `built-in ImageGen`
- generation_method: `OWNER_BODY_01_FRONT_METHOD_V2 face/body/hair role split, adapted to this approved L2 outfit`
- user_authorization: `2026-10-27: user directed using the approved front-appearance asset generation method after rejecting previous face results`
- reference_set_ids: [`OWNER_FACE_APPEARANCE_L1_CONTEXT_NO_CROWN_DERIVATIVE`, `OWNER_L0_BODY_FRONT_CONTEXT`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`]
- responsibility: approved front-face appearance and skin target; L0 body context; L0 Hairstyle A; previously approved Autumn 02 worn clothing appearance only
- reference_budget: `5 generation inputs; no prior unapproved candidate or full-body AI Canon is an input`
- aspect_ratio: `3:4 portrait`
- requested_resolution: `native exact 3:4; preferred 1536x2048`
- seed_settings: `ImageGen does not expose seed or sampler settings`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v016_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v016.png`
- generated_at: `2026-10-27`
- output_sha256: `3a4fa345251fbae4544b0b23744e7271d5428eb7fd0e073fe663e8749eada9be`
- output_dimensions: `1086x1448`
- qa_status: `SUPERSEDED_BY_USER_APPROVED_v015`

## Generation inputs

1. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png`; exact approved front-face appearance and natural skin target only; exclude Hairstyle B, crown/camera, body, makeup, outfit, lighting, background and rendering artifacts. Uses the face-reference role from approved `BODY_01_FRONT_v025`, as directed by the user.
2. `L0_OWNER_002` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/3.jpg`; stature, torso, waist/hip placement, limb length and stance context only; face/hair/clothing excluded.
3. `L0_OWNER_003` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/4.jpg`; torso, waist, hip, thigh, calf and limb-volume cross-check only; face/hair/clothing excluded.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — `characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png`; Hairstyle A only; mask defines nothing.
5. `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png`; outfit fit/drape, colors, white matte hosiery, mule design/sole only; face, likeness, skin, body proportions, hair and identity strictly excluded.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: post-generation face comparison only.
- `OWNER_BODY_01_FRONT_CANON_007`: post-generation full-body front appearance and proportions only.
- `OWNER_HAIR_A_01_FRONT_CANON_001`: Hairstyle A post-generation comparison only.

## Superseded attempts

v013 failed clothing-texture QA; v014 was explicitly rejected by the user for face likeness; v015 repeated the design-reference texture. None is supplied to this generation. The design-reference raster is also deliberately omitted because its visible texture is absent from the approved worn appearance.
