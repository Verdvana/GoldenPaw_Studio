# Generation Record — CAND_13

- asset_id: `SOC_YOGA_001_IMG_01`
- candidate_id: `SOC_YOGA_001_IMG_01_CAND_13`
- asset_level: L3 candidate
- status: USER_APPROVED_L3
- requested_change: Correct CAND_12's bottle cap to the white loop-handle cap in image 03 and apply the burgundy fingernail polish visible in image 02. All other accepted CAND_12 decisions remain.
- spec_revision: `draft_1.233`
- reference_plan: `../../REFERENCE_PLAN.md`

## Input discipline

- generation_inputs: `L0_OWNER_012`, `L0_OWNER_010` (small face only); `OWNER_HAIR_A_01_FRONT_CANON_001` (hair only); `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7` (neck-below anatomy only); `OWNER_SPORT_YOGA_01_WORN_FRONT` (coral leggings and pale-nude hosiery only).
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`; never an input.
- continuity_by_text_only: no previous L3 pixels are supplied. From inspected image 03, the bottle is a 700 ml matte off-white insulated bottle with a matte-white integrated loop-handle screw cap. From inspected image 02, all visible fingernails use neat burgundy polish.
- temporary top: `OUTFIT_TEMP_SOC_YOGA_001_IMG01_JACKET_V3` — pale mint-green Lululemon zip-front yoga jacket, fully zipped, with no visible logo.

## Prompt assembly

Use case: photorealistic-natural. Create a candid, non-sexual 4:5 vertical evening high-held-phone selfie in a generic indoor shopping mall. An adult woman holds the camera phone high above her head and points it gently down. Keep only a small partial face at the extreme upper edge, not portrait framing. Show her standing figure to below both knees and preferably both white shoes. The free hand visibly and securely grips a 700 ml matte off-white insulated bottle around its body. The bottle has a precise matte-white integrated loop-handle screw cap, not wood, metal, black or any other color; the loop handle is clearly visible. The fingernails on the gripping hand are neatly painted a deep burgundy, matching the manicure in image 02.

She wears a pale mint-green Lululemon zip-front yoga jacket, fully zipped to a modest neckline, no visible logo, coral yoga leggings, pale-nude 15D matte hosiery and plain white low-profile running shoes. A dark forest-green rolled yoga mat rests over her shoulder. Generic mall concourse with glass railing, distant city lights, cool ceiling lighting, warm shop-window fill and anonymous tourists. Use mild handheld camera motion blur for tourists, distant background and outer edges while preserving the body, gripping hand, burgundy nails, bottle cap and mat clearly enough for QA. L0 images define only the tiny face fragment; Hair-A only hair; face-excluded body reference only neck-below anatomy; yoga outfit only leggings and hosiery. No readable signage, branding, logo, text, QR codes, watermark, fake UI, mirror, home, office, studio interior, sexualized styling, warped limbs, extra fingers, malformed nails, warped bottle or warped cap.

## Settings and result

- tool: built-in ImageGen
- seed/settings: 4:5 vertical; seed unavailable
- original_candidate_path: `SOC_YOGA_001_IMG_01_CAND_13.png` (moved on approval; no duplicate raster retained)
- output_path: `../../approved/SOC_YOGA_001_IMG_01_APPROVED_v2.png`
- checksum: `88f9ed6fa75d308b7dd0427e7f3186354460d23d6564a294470c95d9ddafa157`
- generated_at: 2026-09-19
- QA_status: USER_APPROVED_L3

## Approval record

- approved_by: user
- approval_date: 2026-09-19
- approval_evidence: “批准。这个帖子完结”
- promotion: moved, not copied
- approved_path: `../../approved/SOC_YOGA_001_IMG_01_APPROVED_v2.png`
- approved_checksum: `88f9ed6fa75d308b7dd0427e7f3186354460d23d6564a294470c95d9ddafa157`
- scope: post-specific L3 only; not Canon and prohibited as a downstream visual input.
