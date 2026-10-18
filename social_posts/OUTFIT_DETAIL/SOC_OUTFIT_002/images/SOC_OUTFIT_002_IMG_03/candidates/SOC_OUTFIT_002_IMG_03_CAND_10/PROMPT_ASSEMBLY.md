# Prompt Assembly / Generation Record — SOC_OUTFIT_002_IMG_03_CAND_10

- tool: OpenAI ImageGen
- status: GENERATED; REVIEW_REQUIRED
- candidate_id: `SOC_OUTFIT_002_IMG_03_CAND_10`
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: L0-derived face geometry crop (tiny visible face only); L0-derived natural skin-context crop (skin only); deterministic face-excluded body derivative (neck-below proportions only); approved Autumn 02 clothing design reference (garments/colors only); approved Autumn 02 worn-front reference (white matte hosiery material/coverage only).
- qa_comparison_only: approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` after generation only; never a generation input.
- reference_budget: 5 of maximum 5
- seed/settings: not exposed by ImageGen
- expected output: `SOC_OUTFIT_002_IMG_03_CAND_10.png` in this candidate directory
- required output metadata: native dimensions and SHA-256 after generation
- QA: pending; candidate remains `REVIEW_REQUIRED`, never automatically promoted
- attempt 1: rejected by ImageGen output safety system (`sexual`); no image returned. Retry uses concise everyday picnic styling wording.
- attempts 2–3: one result was not surfaced to the workspace and is not used; one retry was rejected by the ImageGen output safety system (`sexual`).
- successful generation: 2026-10-18, seed/settings not exposed; final output 1122×1402 PNG, SHA-256 `7ece7d91682667cf3dcc16508f33ada63ce6fa8b15658a0e4f7dc21fab342889`.
- visual QA: brown/ivory outfit and orange mat present; prone pose and raised calves present. Toe ends angle upward, so this is retained as an earlier pose variant and does not satisfy the revised ground-facing toe direction.

## Final assembled prompt

Create one photorealistic, candid vertical 4:5 front-camera phone photo for a casual autumn forest-park picnic. An adult woman wears the approved Autumn 02 outfit: tailored dark chocolate-brown blazer, fitted ivory fine-ribbed high-neck knit, dark chocolate-brown pleated mini skirt, and continuous thick soft-white matte pantyhose. Match the clothing colors to the supplied approved outfit design reference. She lies prone on a warm saturated orange picnic mat on grass, upper body comfortably supported on her elbows. Compose it like a handheld selfie from near her head, angled down along the outfit; keep her face almost entirely outside the frame, at most a tiny edge glimpse. Her knees are bent and both lower legs lift upward so the calves are nearly vertical to the ground; ankles flex so the toe ends draw upward toward the feet/instep, with feet pointed toward the ground side of the pose. Keep the feet relaxed and anatomically natural. No shoes. Pantyhose remains one continuous opaque, fabric-like textile from waist over legs, heels, soles, insteps and toes; no bare toes, gaps, latex/plastic shine, or material break. Only slight natural translucency at stretched heel areas while textile still covers them. Use Hairstyle A only for any tiny visible hair sliver. Generate the tiny visible face only from the supplied L0-derived face crops using the source-derived face method; preserve natural feature relationships and warm-neutral skin, without beautification, smoothing, patches, or muddy relighting. Use the body derivative for neck-below proportions only. Autumn leaves and trees, public park grass, a few simple unbranded picnic snacks. Natural daylight and casual phone-camera perspective, believable contact and shadows, relaxed everyday mood. Match the orange mat color in the written scene specification. Do not copy any pose, person, reflection, camera framing, or park composition from the inspected image-02 candidate. No text, logo, fake UI, watermark, private-residence cues, second photographer, extra limbs, malformed hands/feet, or synthetic studio look.
