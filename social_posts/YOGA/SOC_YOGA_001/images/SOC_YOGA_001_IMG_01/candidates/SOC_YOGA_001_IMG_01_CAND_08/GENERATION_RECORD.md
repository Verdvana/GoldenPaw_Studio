# Generation Record — CAND_08

- asset_id: `SOC_YOGA_001_IMG_01`
- candidate_id: `SOC_YOGA_001_IMG_01_CAND_08`
- asset_level: L3 candidate
- status: GENERATION_BLOCKED_NO_OUTPUT
- spec_revision: `draft_1.233`
- reference_plan: `../../REFERENCE_PLAN.md`
- change_from_CAND_07: Crop the face to a genuinely incidental lower-face fragment at the extreme top edge; all other declared scene, outfit, body, and blur requirements remain unchanged.

## Inputs and exclusions

- generation_inputs: `L0_OWNER_012` and `L0_OWNER_010` (small visible facial identity only); `OWNER_HAIR_A_01_FRONT_CANON_001` (Hair-A only); `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` (neck-below anatomy only); `OWNER_SPORT_YOGA_01_WORN_FRONT` (registered outfit and hosiery only).
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`; comparison only, never a generation input.
- continuity_only: the post's generic mall-night setting; CAND_07 is explicitly excluded as a visual input.
- reference_budget: 5 of 8.

## Prompt assembly

Use case: photorealistic-natural. Four-by-five vertical candid smartphone selfie in a generic night-time shopping mall. An adult woman holds the phone high above her head and points it strongly downward toward her body. The crop deliberately cuts off almost all her head: only an incidental lower-chin and mouth fragment at the extreme top edge, no eyes, no full face, and no portrait framing. The raised arm and phone are physically plausible. Her full body remains the subject, framed from the tiny top-edge face fragment to below both knees, ideally including both shoes.

Use L0_OWNER_012 and L0_OWNER_010 only to preserve the little visible facial fragment; use the face-excluded Body01 derivative only for neck-below adult body geometry; use Hair-A only for long dark-brown loose hair; use the approved yoga outfit only for pale-pink top, coral leggings and light-skin-tone 15D matte hosiery. Add the post-specific charcoal zip hoodie and neutral-white low-profile running shoes, a rolled dark forest-green yoga mat over one shoulder, and a matte off-white wood-cap bottle in the other hand. Generic mall concourse with glass guardrail, distant city lights, cool ceiling illumination and warm shop-window fill. Anonymous tourists move in the background with subtle natural motion blur; subject remains sharp. No readable signage, branding, text, watermark, fake UI, mirror, home, office, studio interior, fashion pose, sexualized styling, warped phone, duplicate fingers or distorted limbs. Never use a generated image as an identity source.

## Settings and result

- tool: built-in ImageGen
- seed/settings: 4:5 vertical; seed unavailable
- output_path: pending
- checksum: pending
- generated_at: pending
- QA_status: NOT_RUN — built-in ImageGen safety rejection before output; no raster was created.
- failure: 2026-09-19 output safety rejection; no candidate image or downstream reference was produced.
