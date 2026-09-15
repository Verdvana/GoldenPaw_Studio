# HAIR_B_04_BACK_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.187
identity_md_revision: draft_0.175
asset_id: HAIR_B_04_BACK
candidate_id: HAIR_B_04_BACK_v001
gate: "Gate 4 — Hairstyle Canon"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_BACK_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_04_BACK_v001/HAIR_B_04_BACK_v001.png"
actual_dimensions_px: [1086, 1448]
checksum_sha256: ba1ce7e6c6abde25e280adf525edf377e36837c32f375b5e75af5d747ef2e064
qa_status: PASS_USER_APPROVED
```

## Reference roles

- `OWNER_BODY_BACK_CANON_L1` / `OWNER_BODY_06_BACK_CANON_001.png`: exact 180-degree back-facing head/body direction, rear shoulder/neck/torso context, pink Calibration Outfit rear context and neutral studio framing only. Its conservative Hairstyle-A rear fall, face, skin, body, hosiery, lighting and background do not define this Hair-B asset.
- `OWNER_HAIRSTYLE_B_L0` / `8.jpg`: real B hairline relationship, pulled-back front, natural face-side wisps, gathered-updo direction and restrained volume only. Its face, surprised expression, hands, sweater, warm light and garden background are excluded.
- `OWNER_HAIRSTYLE_B_APPEARANCE_L1` / `CHR_WOMAN_001_HB04_HAIR_B.jpg`: approved B center-part projection, smooth rearward gathering, controlled crown, dark-brown color, restrained highlights and fine strands only. Its face, high-camera perspective, clothing, lighting and background are excluded.

## Candidate authority and exclusions

This candidate may define only the complete centered rear projection of Hairstyle B: near-center part as it disappears over the crown, controlled rear volume, smooth gathering, centered vertical medium claw clip at the occiput, compact folded hair held inside the clip, and a short 4–6 cm tuft projecting gently upward/backward above the clip. The back view must make the clip, folded section and tuft structurally legible without turning the folded section into a bun, topknot or ponytail.

It must not define face identity, skin, body proportions, clothing beyond the visible calibration context, hosiery, expression, lighting, background, props, other B views, any A/B blend, or any prior generated Hair pixels. No Face, Expression, Pose, Shot, B01, B02 or B03 raster is an input.

## Prompt assembly

```text
Use case: identity-preserve. Asset type: one adult technical Hairstyle-B Canon candidate for CHR_HUMAN_001_OWNER. Create one new photorealistic 3:4 portrait reference in parallel from the three declared references; do not use any prior generated Hair image.

Image 1, OWNER_BODY_BACK_CANON_L1, defines only an exact 180-degree rear-facing head-and-body direction, shoulder/neck/upper-torso context, the visible rear of the pink Calibration Outfit, neutral standing posture and plain studio framing. Ignore its conservative Hairstyle-A rear fall as Hair authority, and ignore face, skin, body proportions beyond rear context, hosiery, lighting and background.
Image 2, OWNER_HAIRSTYLE_B_L0, defines only real B hairline behavior, pulled-back front, natural gathered-updo direction and restrained volume. Ignore its face, surprised expression, hands, sweater, warm light and garden setting.
Image 3, OWNER_HAIRSTYLE_B_APPEARANCE_L1, defines only approved B center-part projection, smooth rearward gathering, controlled crown, dark-brown color, restrained highlights and fine strands. Ignore its face, high-camera perspective, clothing, lighting and background.

Show a precise centered 180-degree back view of the head and upper torso, with no face, ears, cheek edge or side glance visible. The camera is at neutral eye level, the head is straight and centered, and the crown, entire rear head, nape, both outer hair contours and the complete rear hairstyle are fully inside the frame. Keep a modest visible upper portion of the pink Calibration Outfit on a plain neutral gray-white studio background.

Hair-B rear structure: a near-center part flows over a compact natural crown into smooth rearward gathering. At the center of the occiput, show one medium matte dark-brown claw clip oriented vertically. The clip visibly grips a compact folded section of hair; the fold is tight and clearly clip-held, not a bun, not a topknot, not a ponytail. Above the clip, show only one small restrained 4–6 cm tuft that angles gently upward and backward. Keep the clip centered, with believable hinge/body/teeth geometry and hair tension. The clip and tail must remain subordinate to the coherent rear silhouette.

Use long dark-brown hair with controlled low-to-moderate crown volume, smooth predominantly straight strands, natural density, restrained highlights and a clean tapered lower edge around the upper torso. Preserve a realistic scalp/crown transition and consistent B design; do not invent curls, waves, braids or a different gathered hairstyle. Exact 3:4 portrait, complete crown, nape, clip, tuft and lower hair edge with breathing room. Soft even neutral studio lighting, natural hair texture, no props, scenery, text, logo, watermark, collage or multiple views. Produce one REVIEW_REQUIRED image only.
```

## Generation result

## Generation result

- generated_at: `2026-09-15`
- result: one built-in ImageGen call completed successfully.
- built_in_output: `/home/verdvana/.codex/generated_images/01a0a2c8-07e5-7173-b198-d4614c016ee4/exec-1e0bf522-e595-43f0-a110-4e0f12c15cff.png`
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_04_BACK_v001/HAIR_B_04_BACK_v001.png`
- project_candidate_checksum_sha256: `ba1ce7e6c6abde25e280adf525edf377e36837c32f375b5e75af5d747ef2e064`
- technical_precheck: exact centered rear view, no visible face or facial side edge, complete crown/nape/outer contours/lower edge in frame, centered vertical claw clip and compact folded section readable, neutral studio and pink calibration outfit context present.
- review_points: the upper tuft is more lifted and spread than the written target; confirm whether it remains an acceptable short 4–6 cm tuft. Confirm the folded hair reads as clip-held rather than a bun-like mass.
- promotion_status: promoted unchanged after explicit user approval.

## User approval and promotion

- statement: “不错，批准”
- decision: `APPROVED`
- promoted asset: `OWNER_HAIR_B_04_BACK_CANON_001`
- operation: `MOVE`; candidate raster retained: `NO`
- original candidate path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_04_BACK_v001/HAIR_B_04_BACK_v001.png`
- original candidate checksum: `ba1ce7e6c6abde25e280adf525edf377e36837c32f375b5e75af5d747ef2e064`
- current path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/approved/HAIR_B_04_BACK/OWNER_HAIR_B_04_BACK_CANON_001.png`
- current checksum: `ba1ce7e6c6abde25e280adf525edf377e36837c32f375b5e75af5d747ef2e064`
- full release lock: `NO`
