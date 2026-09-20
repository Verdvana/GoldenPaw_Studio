# Generation Record — CAND_09

- asset_id: `SOC_YOGA_001_IMG_01`
- candidate_id: `SOC_YOGA_001_IMG_01_CAND_09`
- asset_level: L3 candidate
- status: GENERATION_BLOCKED_NO_OUTPUT
- spec_revision: `draft_1.233`
- reference_plan: `../../REFERENCE_PLAN.md`
- change_from_CAND_08: Retain the required overhead-selfie crop and mall visitors, but describe a fully non-sexual, modest arrival snapshot with the charcoal hoodie as the dominant visible garment.

## Inputs and exclusions

- generation_inputs: `L0_OWNER_012`, `L0_OWNER_010` (small visible facial identity only); `OWNER_HAIR_A_01_FRONT_CANON_001` (Hair-A only); `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` (neck-below anatomy only); `OWNER_SPORT_YOGA_01_WORN_FRONT` (registered clothing/hosiery only).
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`; never a generation input.
- explicit exclusion: CAND_07 and CAND_08 are not visual inputs; each candidate is generated in parallel from approved/source inputs.
- reference_budget: 5 of 8.

## Prompt assembly

Use case: photorealistic-natural. A completely ordinary, modest after-work snapshot in a generic indoor shopping mall at night. The adult woman takes a practical overhead phone selfie while arriving for yoga, with the phone held above head height and aimed gently down. Deliberately crop nearly all of her head outside the frame: only a very small, incidental chin/mouth edge may appear at the very top; no eye-level face, no portrait framing. Show the ordinary full standing figure to below the knees, preferably both white shoes, as the main subject.

Her charcoal-gray zip hoodie is the dominant visible garment, worn casually over the registered pale-pink yoga top and coral leggings; plain white running shoes. She carries a rolled dark forest-green yoga mat over one shoulder and a matte off-white bottle with a plain wood cap. She stands normally in a shopping-mall concourse with a glass railing, distant city lights and a few anonymous passing tourists. Gentle background-only motion blur on the visitors conveys movement. Keep her body, legs, raised arm and phone sharp, natural and proportionate. Informal documentary phone photo; athletic arrival, no glamour styling.

Reference roles: use the two L0 images only for the tiny face fragment; use the Hair-A input only for hair; use the face-excluded Body01 input only for neck-below anatomy; use the yoga outfit input only for its clothing and hosiery. No signs, logos, readable text, QR codes, watermark, fake UI, mirror, home, office, studio interior, revealing clothing, fashion posing, distorted anatomy, duplicate fingers or warped phone.

## Settings and result

- tool: built-in ImageGen
- seed/settings: 4:5 vertical; seed unavailable
- output_path: pending
- checksum: pending
- generated_at: pending
- QA_status: NOT_RUN — built-in ImageGen safety rejection before output; no raster was created.
- failure: 2026-09-19 output safety rejection; no candidate image or downstream reference was produced.
