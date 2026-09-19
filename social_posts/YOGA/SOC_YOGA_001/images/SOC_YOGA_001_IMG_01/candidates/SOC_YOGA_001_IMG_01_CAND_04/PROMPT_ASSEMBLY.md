# Generation Record — CAND_04

- asset_id: SOC_YOGA_001_IMG_01
- status: READY_TO_GENERATE
- generation_inputs: `L0_OWNER_012` (`14.jpg`), `L0_OWNER_010` (`12.jpg`), `OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001` (hair only), `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`, `OWNER_SPORT_YOGA_01_WORN_FRONT`.
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` for post-generation contamination/drift check only.
- continuity target, not visual input: current approved image 01 defines only same-night arrival facts; it is not supplied to the model.

## Face-safe declaration

- face visible: yes, only a small partial face at upper edge.
- source face method: L0 neutral-face reconstruction from `L0_OWNER_012` and `L0_OWNER_010`.
- body derivative: `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`, SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b`.

## Final assembled prompt

Use case: photorealistic-natural. 4:5 vertical smartphone selfie in a generic nighttime shopping mall outside the yoga studio. The adult woman holds the phone high above her head with one hand and shoots down toward herself; include only a small partial portion of her face at the upper edge, never a complete face. Frame from at least below the knees upward so the body reads clearly to knees/lower legs. Use only L0 sources for the visible face: natural L0-consistent facial relationships, refined smaller lower face and ordinary skin texture. Hair-A high-camera projection only: long loose dark-brown hair, near-center part and natural crown. Use face-excluded Body01 only for 168 cm adult proportions and straight lower-leg anatomy. She wears the registered pink yoga set under a charcoal zip hoodie with neutral white running shoes; a full-size dark forest-green yoga mat is slung over her shoulder and she holds the shared matte off-white wood-cap bottle in her free hand. Public mall corridor at night, passing shoppers in the background with restrained, plausible motion blur while the selfie subject remains sharp; cool mall ambient light plus warm storefront glow. No home/office, no readable store/studio name, brand, watermark, fake UI, full facial portrait, distorted limbs, curved/bowed calves, plastic fabric, or staged symmetric pose.

## Result

- generated_at: 2026-09-19
- output_path: none
- output_checksum: none
- status: GENERATION_BLOCKED_NO_OUTPUT
- failure: built-in ImageGen safety rejection before output; no raster was created.
