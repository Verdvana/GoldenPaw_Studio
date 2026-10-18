# Social Post Prompt Assembly / Generation Record

- post_id: `SOC_OUTFIT_001`
- image_asset_id: `SOC_OUTFIT_001_IMG_01`
- candidate_id: `SOC_OUTFIT_001_IMG_01_CAND_03`
- model/tool: OpenAI ImageGen
- status: APPROVED_L3
- reference_plan: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_001/images/SOC_OUTFIT_001_IMG_01/REFERENCE_PLAN.md`
- generation_inputs:
  1. `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` — source-derived facial geometry/identity only
  2. `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` — natural skin color/texture context only
  3. `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` — face-excluded neck-below body proportions only
  4. `OWNER_HAIR_A_01_FRONT_CANON_001` — Hair A only
  5. `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` — outfit/materials only; absolutely no face or hair responsibility
- qa_comparison_only:
  1. `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — inspect only after generation for identity, facial feature relationships, skin contamination and projection/framing
- face_generation_rule: source-derived L0 inputs plus applicable Face method prompt constraints; approved AI Face/Body Canon is QA-only

## 1. Everyday moment and composition

A candid arm-length front-camera selfie taken outdoors beside a generic café's street-facing glass window during an autumn walk in soft afternoon daylight. The real person is primary. Phone lens is slightly above eye height and angled naturally; relaxed partial side turn, a small amused half-smile, eyes looking into the front camera. The window sits to one side and carries only a subtle, physically plausible partial reflection of the same subject; no mirror selfie. Crop is head to mid-torso, with blazer and high neck readable. A few blurred autumn leaves and vague passersby appear outside; no identifiable venue. Casual smartphone perspective, mild natural wide-angle but no face or body distortion.

## 2. Identity locks

Generate adult owner face solely from the selected L0-derived geometry and skin-context inputs following `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`: preserve facial feature relationships and natural face width; no slimming, eye enlargement, nose refinement, V-line shaping or age shift. Warm-neutral natural skin and texture; no whitening, cooling, brightening, pink cast, plastic smoothing, blotches or muddy relighting. Hair must not leak from face-source crops. Use Hair A reference for the long straight dark-brown hair, near-center natural part, flat close-to-scalp roots, modest volume and tapered loose lengths only. Keep plausible camera projection and avoid broad overhead crown.

## 3. Body and appearance locks

Use only the deterministic face-excluded body derivative for neck-below proportions. Keep visible shoulders and torso natural and consistent; no body reshaping. Relaxed arm-length selfie gesture, anatomically plausible hand/phone. Do not include the derivative's clothing or rendering.

## 4. Outfit and material contract

Use Autumn 02 exactly: tailored dark chocolate-brown blazer with notched lapels over fitted ivory fine-ribbed high-neck knit; lower portion if visible is the dark-brown high-waisted crisp pleated mini skirt; soft-white medium-thick matte continuous textile pantyhose only if visible; cream-ivory plush open-toe mule slippers only if visible. This tight upper-body framing may omit skirt, hosiery and shoes naturally. Keep garments unbranded, no graphics. Outfit reference defines clothing/material/fit only, never face, hair, skin or body.

## 5. Cat, props and scale

No cat or fixed props. The selfie phone may be visible only as a natural edge/hand detail; no duplicate phone, device UI, legible screen or brand.

## 6. Environment and temporary dressing

One-off public café street window, generic and non-identifiable. Faint reflection obeys angle, brightness and glass physics and remains secondary; avoid a clean mirror-like duplicate. Soft autumn street context beyond glass, muted warm foliage, no legible signage, logos or private residence cues. No recurring venue canon is implied.

## 7. Carousel continuity-only instructions

Autumn 02 outfit and same general daytime walk only. Do not use this image as a reference for later images; other carousel frames will be generated independently from approved masters.

## 8. Realism and negative constraints

Photorealistic, candid social selfie, tactile fabric and natural skin. Physically consistent light, shadow, glass reflection and perspective. No synthetic symmetry, studio backdrop, plastic skin, face contamination, muddy patches, incoherent bokeh, duplicate limbs/fingers/phone/reflection, watermark, fake UI, garbled text, unexplained logo or brand. No face/hair leakage from outfit reference, and no body/skin/identity leakage from body derivative.

## 9. Output contract

- platform: Instagram-style social feed draft
- aspect ratio/resolution: portrait 4:5, target 1024×1280 or nearest native 4:5
- required safe areas: retain full hair silhouette, face and phone-hand; no text overlay
- expected filename/path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_001/images/SOC_OUTFIT_001_IMG_01/approved/SOC_OUTFIT_001_IMG_01_APPROVED_v2.png`

## Final assembled prompt

Create one photorealistic, candid 4:5 vertical social selfie of the adult owner on an autumn walk, taken with the phone's FRONT CAMERA at arm's length beside a generic café's street-facing window. This is NOT a mirror selfie. Crop head to mid-torso; the subject holds a believable relaxed partial side turn, looks directly into the phone camera with a small amused half-smile. Keep the real subject primary and the window only at one side, showing a faint partial physically correct reflection as a secondary accent. Soft afternoon light; a few out-of-focus autumn leaves and indistinct passersby outside; no identifiable venue or readable signs. Generate the face only from the provided L0-derived face geometry crop and natural L0 skin-context crop using the approved source-derived face method constraints. Preserve exact natural facial relationships and warm-neutral skin; no beautification, face slimming, eye enlargement, altered age, retouching, plastic smoothing or skin patches. Apply the provided Hairstyle-A reference only for its long straight dark-brown hair, near-center part and low natural crown. Apply the face-excluded body derivative only to neck-below proportions. Apply the approved Autumn-02 outfit reference only to clothing: tailored dark chocolate-brown blazer over fitted ivory fine-ribbed high-neck knit; show at least the lapels and high neck clearly. Restrict the outfit image to clothing responsibilities; it must not affect face, hair, skin or body. Plausible smartphone perspective with only mild natural front-camera wideness; no distortion. Natural hand and phone, no duplicate fingers or phone. Coherent glass reflection and lighting, no logos, text, watermark, fake interface, private home cues, duplicated reflection, or artificial studio look. Casual, fresh and slightly playful rather than posed fashion advertising.

## Generation settings/result

- generated_at: 2026-10-17
- seed/settings: not exposed by ImageGen; native 1122×1402 PNG, approximately 4:5
- output_path: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_001/images/SOC_OUTFIT_001_IMG_01/approved/SOC_OUTFIT_001_IMG_01_APPROVED_v2.png`
- output_checksum: `4bc5842a23ce17c3fdff3e2414b7e33329cef7a4240f49041f8ca9fa472e0ed7`
- QA_record: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_001/images/SOC_OUTFIT_001_IMG_01/qa/QA.md` (pending image review)
