# Generation Record — CAND_12

- asset_id: `SOC_YOGA_001_IMG_01`
- candidate_id: `SOC_YOGA_001_IMG_01_CAND_12`
- asset_level: L3 candidate
- status: REJECTED_PROP_AND_NAIL_CONTINUITY
- requested_change: User-directed revision of CAND_11: pale mint-green Lululemon zip-front yoga jacket, fully zipped; bottle must be held; retain the specified water-bottle continuity, camera-motion read, small face and below-knee framing.
- spec_revision: `draft_1.233`
- reference_plan: `../../REFERENCE_PLAN.md`

## Reference budget and responsibility

- generation_inputs: `L0_OWNER_012`, `L0_OWNER_010` (small source-derived high-camera face only); `OWNER_HAIR_A_01_FRONT_CANON_001` (Hair-A only); `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` (neck-below anatomy only); `OWNER_SPORT_YOGA_01_WORN_FRONT` (coral leggings and pale-nude 15D matte hosiery only).
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`; never used in generation.
- text-only prop continuity: exactly one 700 ml matte off-white insulated bottle with a plain wood-toned screw cap, matching image 03's declared temporary prop. Image 03's generated pixels are prohibited as an input.
- text-only temporary outfit: `OUTFIT_TEMP_SOC_YOGA_001_IMG01_JACKET_V3`; Lululemon garment identity is requested, while all logos/word marks remain out of frame under the post's no-brand-mark policy.
- reference budget: 5 of 8.

## Prompt assembly

Use case: photorealistic-natural. A candid, completely non-sexual 4:5 vertical evening smartphone selfie in a generic indoor shopping mall. An adult woman holds her phone high above her head, angled gently downward. Only a small incidental partial face is allowed at the very top edge; it must not become a portrait. Her ordinary standing body is the focus and extends below both knees, preferably with both shoes visible. The raised-camera arm is physically plausible.

Her free hand securely holds a 700 ml matte off-white insulated water bottle around its body; its entire plain wood-toned screw cap and most of the bottle are visible, unmistakably in-hand, not tucked under an arm, in a bag, on the mat or floating. A dark forest-green 6 mm yoga mat is rolled over the other shoulder. She wears a pale mint-green Lululemon zip-front yoga jacket, fully zipped closed to a modest crew neckline, with no visible logo or readable branding, coral yoga leggings, pale-nude 15D matte hosiery and plain white low-profile running shoes.

Use L0 images only for the small partial face; Hair-A only for long dark-brown loose hair; face-excluded Body01 only for neck-below adult anatomy; yoga-outfit image only for leggings and hosiery. Generic mall concourse with glass railing, distant city lights, cool ceiling lighting, warm shop-window fill, and anonymous tourists. Include mild realistic handheld camera motion blur in the visitors, distant background and outer frame edges but keep the body, bottle-in-hand, mat, raised arm and phone viewpoint sufficiently sharp for QA. Documentary snapshot, not fashion advertising. No signage, visible logo, text, QR code, watermark, fake UI, mirror, home, office, studio interior, sexualized styling, distorted anatomy, extra fingers, warped phone, or warped bottle.

## Settings and result

- tool: built-in ImageGen
- seed/settings: 4:5 vertical; seed unavailable
- output_path: `SOC_YOGA_001_IMG_01_CAND_12.png`
- checksum: `bb90e046560d2c4c4e1c066a5815232316b0145ce0ab75979342fdf253526462`
- generated_at: 2026-09-19
- QA_status: REJECTED — user identified a wood-toned cap instead of the image-03 matte-white loop cap, and missing burgundy nail polish continuity.
