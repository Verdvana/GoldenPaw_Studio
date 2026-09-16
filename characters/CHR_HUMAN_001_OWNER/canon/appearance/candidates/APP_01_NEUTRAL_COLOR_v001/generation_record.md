# APP_01_NEUTRAL_COLOR_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.220
identity_md_revision: draft_0.175
asset_id: APP_01_NEUTRAL_COLOR
candidate_id: APP_01_NEUTRAL_COLOR_v001
gate: "Appearance Canon — optional supplement"
status: APPROVED
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_FACE_FRONT_NEUTRAL_CANON_L1, OWNER_HAIR_A_FRONT_CANON_L1]
reference_count: 2
previous_generated_appearance_inputs: []
rejected_candidate_pixels_used: false
generator: "built-in ImageGen"
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/appearance/approved/APP_01_NEUTRAL_COLOR/OWNER_APP_01_NEUTRAL_COLOR_CANON_001.png"
qa_status: PASS_USER_APPROVED
```

## Reference responsibilities

- `OWNER_FACE_FRONT_NEUTRAL_CANON_L1`: approved owner face identity, stable facial geometry, natural warm-neutral skin appearance and neutral expression only; must not define lighting, background or new geometry.
- `OWNER_HAIR_A_FRONT_CANON_L1`: Hairstyle-A front presentation and dark-brown hair color/texture only; must not define face, body, lighting or background.

## Prompt assembly

```text
Use case: identity-preserve
Asset type: optional owner L1 Appearance color-calibration candidate
Primary request: Create exactly one photorealistic 3:4 vertical neutral studio color-calibration portrait for APP_01_NEUTRAL_COLOR. Preserve the approved owner's face and stable facial geometry. This image is authoritative only for neutral-light face, skin-tone and Hair-A color appearance; it must not redefine facial geometry or hairstyle structure.
Input images: Image 1 defines only the approved owner identity, stable facial geometry, natural warm-neutral skin appearance and neutral expression. Image 2 defines only the approved Hairstyle-A front presentation and dark-brown hair color/texture.
Scene/backdrop: seamless neutral light-gray studio background.
Subject: same adult owner, relaxed neutral closed-mouth expression, front-facing head-and-shoulders portrait; pink calibration one-piece visible at the shoulders if clothing appears.
Style/medium: photographic realism, natural skin texture, no beauty retouching.
Composition/framing: standard eye-level front view, head top through upper chest, hair edges visible, even neutral exposure and white balance.
Lighting/mood: broad soft neutral studio light, approximately 5200–5600K, low contrast, no colored cast, no dramatic shadow.
Color palette: warm-neutral natural skin, dark-brown Hair-A, restrained pink calibration garment, neutral gray background.
Constraints: preserve face identity, facial proportions, age, expression and Hair-A appearance; calibrate only neutral color and exposure. No color grading, whitening, cooling, oversaturation or beauty filter.
Avoid: face reshaping, eye enlargement, nose or jaw changes, hairstyle change, Hair-B, dramatic lighting, colored ambient light, strong specular highlights, plastic skin, text, watermark, extra views, previous AI candidates.
```

User approved this candidate with “登记”. The raster was moved (not copied) to the approved Canon path. Approval is scoped to neutral color/exposure appearance; full `owner_v1.0` remains unlocked.
