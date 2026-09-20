# Generation Record — CAND_07

- asset_id: `SOC_YOGA_001_IMG_01`
- candidate_id: `SOC_YOGA_001_IMG_01_CAND_07`
- asset_level: L3 candidate
- status: REJECTED_COMPOSITION
- requested_change: Replace the prior masked-face arrival composition with an overhead-phone selfie: a very small partial face, full body to at least below the knees, generic mall and tourists, and subtle motion blur.
- spec_revision: `draft_1.233`
- reference_plan: `../../REFERENCE_PLAN.md`

## Reference budget and responsibilities

- count: 5 of 8 maximum.
- generation_inputs:
  - `L0_OWNER_012` — source-derived high-camera face identity only.
  - `L0_OWNER_010` — source-derived high-camera face identity only.
  - `OWNER_HAIR_A_01_FRONT_CANON_001` — Hair-A structure and dark-brown color only.
  - `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` — neck-below proportions, limbs, and grounded standing anatomy only.
  - `OWNER_SPORT_YOGA_01_WORN_FRONT` — registered yoga outfit plus light-skin-tone 15D matte hosiery only.
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — identity, face-contamination, and projection checks only; forbidden as a generation input.
- continuity_only: the published image-01 framing and mall-night setting; no generated image is supplied as a visual reference.
- must_not_define: L0 face sources do not define body, hair, outfit, setting, tourists, or pose. Hair reference does not define face, skin, body, clothes, or setting. Body derivative does not define face, skin, hair, clothing, hosiery material, or setting. Outfit input does not define identity, hair, body, environment, pose, or temporary hoodie/shoes.

## Prompt assembly

Use case: photorealistic-natural.

Asset type: replacement candidate for social-post carousel image 01, 4:5 vertical.

Primary request: an ordinary after-work mall arrival check-in, photographed by the adult woman herself with one smartphone arm lifted high over her head, camera pointing gently downward. Her body is shown in a natural walking-pause stance, from a tiny incidental partial face along the upper edge through at least below both knees; do not make the face a portrait or the compositional focus. The raised phone must be physically plausible in her raised hand; no mirror.

Scene/backdrop: generic indoor shopping-mall public concourse at night, glass guardrail and distant urban lights, cool ceiling lights with warm shop-window fill, several anonymous tourists/shoppers moving behind her. Apply subtle authentic background motion blur to the passing people only; keep the subject, raised hand, phone and legs readable.

Subject: use L0_OWNER_012 and L0_OWNER_010 only for the small visible facial identity at a high camera angle. Use the face-excluded Body01 derivative only for neck-below adult proportions and standing leg anatomy. Use Hair-A only for long dark-brown loose hair. Use the approved yoga outfit only for its fitted pale-pink sports top, coral-pink leggings and light-skin-tone 15D matte hosiery; layer a charcoal-gray unbranded zip hoodie and plain neutral-white low-profile running shoes for this arrival image. A dark forest-green 6 mm yoga mat is rolled over one shoulder; a 700 ml matte off-white insulated bottle with a plain wood-toned cap is in the other hand.

Style/medium: candid smartphone social photo, documentary rather than fashion advertising.

Composition/framing: 4:5 portrait. The camera is above head height and looks down gently. A small partial face occupies no more than the top 12% of the image; body remains the clear compositional subject and is visible to below both knees. Preserve natural limb lengths and straight knee-to-shin-to-ankle alignment.

Constraints: no readable signs, store names, brand logos, text, QR codes, watermark, fake UI, home, office, studio interior, mirror, glamour pose, sexualized styling, distorted limbs, duplicate fingers, warped phone, or blurred primary subject. Do not use any generated image as an identity source.

## Settings and result

- tool: built-in ImageGen
- seed/settings: 4:5 vertical; seed unavailable
- output_path: `SOC_YOGA_001_IMG_01_CAND_07.png`
- checksum: `eec6ec85a64d3a8514190b695d53fbeee39359fd9018ccbfd2835f29601934e5`
- generated_at: 2026-09-19
- QA_status: REJECTED — overall pose, mall setting, tourists and background-only motion blur pass; the visible face is substantially larger than the requested small incidental upper-edge fragment.
