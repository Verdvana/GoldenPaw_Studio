# Generation Record — CAND_11

- asset_id: `SOC_YOGA_001_IMG_01`
- candidate_id: `SOC_YOGA_001_IMG_01_CAND_11`
- asset_level: L3 candidate
- status: SUPERSEDED_BY_USER_REVISION
- requested_change: Fix CAND_07's bottle handling and bottle continuity; retain the requested overhead selfie with a small face, below-knee body coverage, mall tourists, and camera-motion read. Update only the temporary top design.
- spec_revision: `draft_1.233`
- reference_plan: `../../REFERENCE_PLAN.md`

## Reference budget and responsibilities

- count: 5 of 8 maximum.
- generation_inputs:
  - `L0_OWNER_012` and `L0_OWNER_010` — source-derived high-camera face identity only, for a small incidental upper-edge face fragment.
  - `OWNER_HAIR_A_01_FRONT_CANON_001` — Hair-A structure/color only.
  - `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` — neck-below proportion and standing anatomy only.
  - `OWNER_SPORT_YOGA_01_WORN_FRONT` — coral yoga leggings and pale-nude 15D matte hosiery only; must not define the top.
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`; forbidden as a generation input.
- continuity_by_text_only: `PROP_TEMP_SOC_YOGA_001_BOTTLE` exactly matches image 03's declared prop — a 700 ml matte off-white insulated bottle with a plain wood-toned screw cap. Image 03's L3 raster is not supplied as a visual reference.
- must_not_define: L0 face sources do not define body/hair/clothes/scene; Hair-A does not define face/body/clothes; the body derivative does not define face/skin/hair/clothes/material; the yoga outfit input does not define face/body/hair/environment or the temporary top.

## Prompt assembly

Use case: photorealistic-natural. Create a 4:5 vertical candid, non-sexual after-work smartphone selfie in a generic indoor shopping mall at night. The adult woman holds the phone high above her head, pointing gently downward. Her face is only a small incidental fragment along the very top edge, never a portrait; show her ordinary standing body to below both knees, ideally both shoes. The raised camera hand is physically plausible. Her other hand visibly and securely grips the same 700 ml matte off-white insulated water bottle by its body, with all of the plain wood-toned screw cap and most of the bottle visible; it must read as being held in her hand, never tucked into a bag, resting on the mat, or floating.

Use the two L0 inputs only for that tiny high-angle face fragment, Hair-A only for long dark-brown loose hair, the face-excluded Body01 derivative only for neck-below anatomy, and the registered yoga outfit only for coral yoga leggings and pale-nude 15D matte hosiery. The visible top is instead the temporary `OUTFIT_TEMP_SOC_YOGA_001_IMG01_TOP_V2`: a modest dusty-lilac crew-neck long-sleeve athletic top beneath a casual unbranded charcoal-gray open zip hoodie. Plain neutral-white low-profile running shoes. A dark forest-green 6 mm yoga mat is rolled over one shoulder.

Scene: public mall concourse with glass guardrail, distant city lights, cool ceiling lighting, warm shop-window fill and anonymous tourists. Add slight natural handheld camera motion blur to the moving visitors and far background, with a gentle snapshot softness at frame edges; preserve enough sharpness to verify the body, bottle-in-hand and mat. Avoid posed fashion/ad imagery. No readable signs, logos, text, watermark, fake UI, mirror, home, office, studio interior, sexualized styling, distorted limbs, duplicate fingers, warped phone or warped bottle.

## Settings and result

- tool: built-in ImageGen
- seed/settings: 4:5 vertical; seed unavailable
- output_path: `SOC_YOGA_001_IMG_01_CAND_11.png`
- checksum: `23a2917323bb97de4fb253fb2a7ee65ae3ca929cce9ad294cc8513276873c033`
- generated_at: 2026-09-19
- QA_status: NOT_REVIEWED — output completed after the interrupted call, but user immediately replaced the outer-top design with the specified mint-green zipped jacket. No promotion performed.
