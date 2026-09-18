# Generation Record — SOC_COMMUTE_001_IMG_02_CAND_11

- asset_id: SOC_COMMUTE_001_IMG_02
- candidate_id: SOC_COMMUTE_001_IMG_02_CAND_11
- asset_level: L3
- status: USER_APPROVED_L3
- generation_date: 2026-09-18
- generation_gate: User request to change the leg pantyhose to smoke gray, referencing `/home/verdvana/.codex/generated_images/01a0b360-c491-79f1-b3a1-f3075f8b23a5/exec-d4d9a905-9932-422b-a596-2f4f38a4e5e9.png`.
- original_candidate_path: `social_posts/COMMUTE/SOC_COMMUTE_001/images/SOC_COMMUTE_001_IMG_02/candidates/SOC_COMMUTE_001_IMG_02_CAND_11/SOC_COMMUTE_001_IMG_02_CAND_11.png`
- current_approved_path: `social_posts/COMMUTE/SOC_COMMUTE_001/images/SOC_COMMUTE_001_IMG_02/approved/SOC_COMMUTE_001_IMG_02_APPROVED_v2.png`
- output_sha256: `aac087b0751f8f24536401f7510ab3f4ee203e3d6c22834645583a18d359ba10`
- settings: ImageGen, 4:5 vertical social still; seed unavailable

## Generation inputs

| Asset / path | Responsibility | Must not define |
|---|---|---|
| `L0_OWNER_012` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg` | Owner identity for visible partial face | Body, hair, outfit, park, lighting |
| `L0_OWNER_010` — `characters/CHR_HUMAN_001_OWNER/source/identity/raw/12.jpg` | High-camera partial-face projection | Body, hair, outfit, park, lighting |
| `OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001` | HAIRSTYLE_A projection only | Face, body, outfit, park, lighting |
| `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | Walking scale, stride and feet | Face, skin, hair, outfit, park |
| `OWNER_WORK_SUMMER_01_WORN_FULL_BODY` | Same office outfit and smoke-gray 15D matte pantyhose material | Face, skin, body identity, hair, park |

## Continuity target, not a visual input

- `SOC_COMMUTE_001_IMG_02_APPROVED_v1.png` / user-attached `exec-d4d9a905-9932-422b-a596-2f4f38a4e5e9.png`: composition and non-hosiery acceptance target only. It is an L3 approved image and is deliberately not attached to the model; it must not define face, body, skin, hair or material in this generation.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: comparison only; never a generation input.

## Prompt assembly

Use case: photorealistic-natural. Create a candid 4:5 vertical high right-side smartphone walking selfie beside a generic city park at warm dusk. The composition is an ordinary after-work snapshot: a partial face on the upper-right edge, long dark-brown HAIRSTYLE_A worn down, black fitted work top, warm-champagne white skirt with irregular black dots, plain natural off-white canvas tote with matching canvas handles, walking stride and taupe buckle pumps. Preserve true low sunset warmth, cool shaded fill, localized walking motion at the tote/path/foliage, and coherent anatomy.

The required material correction is the visible pantyhose: it is clearly smoke-gray 15D matte sheer pantyhose, medium cool gray and visibly distinct from bare skin, continuous from the skirt hem through both visible legs, with only restrained natural light response. Do not render nude/skin-colored, black, glossy, plastic or opaque legwear. No text, logos, watermark, UI, beauty filter, studio styling, duplicate limbs, distorted hands, warped shoes, face-wide blur or artificial bokeh.

## QA targets

- Pantyhose is the specified smoke-gray 15D matte material, not nude or black.
- Other wardrobe, park-at-dusk and walking-snapshot constraints retain the prior approved scene intent without using that L3 output as input.
- Candidate remains L3 only and never a downstream visual input.

## Approval record

- approved_by: user
- approval_date: 2026-09-18
- approval_evidence: “很好，已发布，这篇帖子已完结。”
- promotion: moved (not copied) to the approved L3 post-image path as v2.
- scope: published only within this social post; not Canon and not a visual generation input.
