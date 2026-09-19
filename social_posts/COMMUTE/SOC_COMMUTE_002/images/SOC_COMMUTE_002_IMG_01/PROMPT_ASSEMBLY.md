# Social Post Prompt Assembly / Generation Record

- post_id: SOC_COMMUTE_002
- image_asset_id: SOC_COMMUTE_002_IMG_01
- candidate_id: SOC_COMMUTE_002_IMG_01_CAND_01
- model/tool: built-in ImageGen
- status: USER_APPROVED_L3
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: `L0_OWNER_012`, `L0_OWNER_010`, `OWNER_HAIR_A_02_3Q_CANON_001`, `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`, `OWNER_WORK_SUMMER_01_WORN_FULL_BODY`
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- face_generation_rule: source-derived L0 inputs plus the applicable Face method prompt; approved AI Face/Body Canon is QA-only

## 1. Everyday moment and composition

An early weekday morning at a generic sidewalk takeaway window. Waist-up candid 3/4 photograph from a companion standing one step away; the owner accepts an unbranded white takeaway coffee cup and glances toward it with a small, relaxed smile. Soft blue-hour shade and the first gentle warm sun edge; real public sidewalk texture and shallow, plausible depth of field.

## 2. Identity locks

Use only the supplied L0 sources for the face: a refined smaller lower face, gently narrowed natural jaw, ordinary skin texture and L0-consistent feature relationships. Hair-A is worn loose: near-center part, long dark-brown predominantly straight fall, controlled crown volume and tapered ends. No AI face/body Canon as input.

## 3. Body and appearance locks

Adult 168 cm / 60 kg proportion from the face-excluded body derivative; natural head-to-body scale, shoulders and hands. The camera shows only upper body and a small part of the skirt; no exaggerated slimness, beauty smoothing or fashion pose.

## 4. Outfit and material contract

Registered summer work outfit: fitted black low round-neck top and warm-champagne short skirt with irregular black dots. If legwear is visible, it is smoke-gray 15D matte sheer pantyhose, clearly distinct from bare skin and continuous. Carry the unbranded off-white canvas tote on the shoulder.

## 5. Cat, props and scale

No cat. Plain white paper coffee cup with kraft sleeve only; no logo, readable text or branded takeaway cup.

## 6. Environment and temporary dressing

Generic pale-tile street-corner coffee window; no indoor seating visible. Anonymous public sidewalk, distant indistinct pedestrians, no home, office, office lobby, office building branding or readable storefront text.

## 7. Carousel continuity-only instructions

Same morning, same outfit and tote as images 02–03. This fact is textual only and no other generated image is attached.

## 8. Realism and negative constraints

Physically consistent hand-to-cup contact, morning shadows, natural facial texture and textile folds. Forbid studio lighting, centered fashion-editorial posing, synthetic symmetry, plastic skin, incoherent bokeh, watermark, fake UI, garbled text, logos, duplicate fingers, deformed hands, face blotches or AI-to-AI identity drift.

## 9. Output contract

- platform: social feed
- aspect ratio/resolution: 4:5 vertical / 2160x2700 px delivery target
- required safe areas: face, cup and tote strap inside the central 90% of frame
- expected filename/path: `candidates/SOC_COMMUTE_002_IMG_01_CAND_01/SOC_COMMUTE_002_IMG_01_CAND_01.png`

## Final assembled prompt

Use case: photorealistic-natural. Asset type: 4:5 vertical social carousel still. Create a candid early-weekday-morning street photograph at a generic sidewalk takeaway coffee window. A 168 cm adult woman is shown waist-up in a natural 3/4 view, accepting a plain unbranded white coffee cup with kraft sleeve and glancing toward it with a small relaxed smile; off-white canvas tote strap on her shoulder. Use only supplied L0 sources for her face: refined smaller lower face, gently narrowed natural jaw, L0-consistent facial relationships and ordinary natural skin texture. Use the supplied face-excluded body source only for neck-below scale. Use the supplied Hair-A reference only for a near-center part, controlled crown and long loose dark-brown mostly straight hair with tapered ends. Use the supplied outfit only for the fitted black round-neck top and warm-champagne skirt with irregular black dots. Generic pale tiled coffee window, public sidewalk, distant indistinct commuters, soft cool early-morning shade with a subtle first warm sun edge, handheld companion-camera realism, no indoor seating. No home, office, office lobby or office-building scene. No readable signage, logos, watermarks, fake UI, garbled text, fashion-poster pose, plastic skin, face contamination, duplicate fingers or deformed hands.

## Generation settings/result

- generated_at: 2026-09-19
- seed/settings: built-in ImageGen; 4:5 vertical; seed unavailable
- original_candidate_path: `candidates/SOC_COMMUTE_002_IMG_01_CAND_01/SOC_COMMUTE_002_IMG_01_CAND_01.png` (moved on approval)
- output_path: `approved/SOC_COMMUTE_002_IMG_01_APPROVED_v1.png`
- output_checksum: `1f9688d121a35621e15d51b5a310912a17e703533d1a5dbf4b1677418245d35a`
- QA_record: `candidates/SOC_COMMUTE_002_IMG_01_CAND_01/QA.md`

## Approval record

- approved_by: user
- approval_date: 2026-09-19
- approval_evidence: “批准 登记”
- promotion: moved (not copied) to the approved L3 post-image path.
- scope: published only within this social post; not Canon and not a downstream visual input.
