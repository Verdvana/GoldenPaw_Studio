# Social Post Prompt Assembly / Generation Record

- post_id: SOC_COMMUTE_002
- image_asset_id: SOC_COMMUTE_002_IMG_02
- candidate_id: SOC_COMMUTE_002_IMG_02_CAND_01
- model/tool: built-in ImageGen
- status: USER_APPROVED_L3
- reference_plan: `REFERENCE_PLAN.md`
- generation_inputs: `L0_OWNER_013`, `L0_OWNER_014`, `OWNER_HAIR_A_02_3Q_CANON_001`, `BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7`, `OWNER_WORK_SUMMER_01_WORN_FULL_BODY`
- qa_comparison_only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- face_generation_rule: source-derived L0 inputs plus the applicable Face method prompt; approved AI Face/Body Canon is QA-only

## 1. Everyday moment and composition

Full-body candid street photograph from across a quiet urban zebra crossing. The owner is mid-stride, tote in one hand and coffee in the other, briefly turning a 3/4 glance toward the camera. The sidewalk is lively enough to be public but not crowded; camera at ordinary chest height and modestly off-axis.

## 2. Identity locks

Use only supplied L0 sources for face structure and natural relationships; retain a refined smaller lower face and natural skin, not studio makeup. Use Hair-A 3/4 only for its long loose, near-center-parted dark-brown style. AI Face/Body Canons are never inputs.

## 3. Body and appearance locks

Face-excluded body derivative defines the adult 168 cm / 60 kg balanced silhouette and walking anatomy. One grounded foot, one advancing foot; normal long-leg perspective without limb stretching or bow-legged distortion.

## 4. Outfit and material contract

Same registered work outfit. Smoke-gray 15D matte sheer pantyhose runs continuously from the skirt hem to the taupe-gray buckle pumps; it must read as textile, not bare skin, opaque tights, plastic or gloss.

## 5. Cat, props and scale

No cat. Same unbranded tote and plain coffee cup; both have believable weight, grip and swing.

## 6. Environment and temporary dressing

Generic tree-lined downtown crossing with soft early morning sun, muted storefront façades with no readable signs, simple zebra lines, and a few distant anonymous commuters. No residential gate, home, office entrance or company site.

## 7. Carousel continuity-only instructions

Same morning and items as images 01 and 03, without using either as visual input.

## 8. Realism and negative constraints

Natural stride, correct shoe contact, subtle moving fabric, coherent sunlight and shadow direction. Avoid fashion runway pose, exaggerated height, plastic hosiery, warped crossing lines, fake text, watermarks, distorted hands/feet, face artifacts, logo clutter and artificial symmetry.

## 9. Output contract

- platform: social feed
- aspect ratio/resolution: 4:5 vertical / 2160x2700 px delivery target
- required safe areas: full figure, tote and cup clear of outer 5% edge
- expected filename/path: `candidates/SOC_COMMUTE_002_IMG_02_CAND_01/SOC_COMMUTE_002_IMG_02_CAND_01.png`

## Final assembled prompt

Use case: photorealistic-natural. Asset type: 4:5 vertical social carousel still. Create a believable early-morning full-body street photograph, camera across a generic tree-lined urban zebra crossing at ordinary chest height and slightly off-axis. An adult woman crosses in a natural mid-stride, carrying a plain white takeaway coffee cup in one hand and an off-white unbranded canvas tote in the other, with a brief relaxed 3/4 glance toward the camera. Use only supplied L0 images for facial identity: natural L0-consistent 3/4 feature relationships, a refined smaller lower face and ordinary skin texture. Use the face-excluded body source only for balanced 168 cm adult proportions and grounded walking anatomy. Use Hair-A reference only for long loose near-center-parted dark-brown hair. Use the registered outfit reference only for a fitted black low round-neck top, warm-champagne short skirt with irregular black dots, smoke-gray 15D matte sheer pantyhose continuous from skirt hem to light taupe-gray buckle pumps. Public city crossing with anonymous façades and a few distant commuters, no readable signs, no home, office, lobby or company entrance. Soft cool morning shade mixed with gentle low sun, realistic contact shadows and modest moving fabric. No logo, watermark, readable or garbled text, beauty filter, runway pose, stretched limbs, bowed legs, plastic hosiery, deformed hands or feet, face contamination or artificial symmetry.

## Generation settings/result

- generated_at: 2026-09-19
- seed/settings: built-in ImageGen; 4:5 vertical; seed unavailable
- original_candidate_path: `candidates/SOC_COMMUTE_002_IMG_02_CAND_01/SOC_COMMUTE_002_IMG_02_CAND_01.png` (moved on approval)
- output_path: `approved/SOC_COMMUTE_002_IMG_02_APPROVED_v1.png`
- output_checksum: `b184f1ce85f7d90095a88e1f961edb8993aa13752e549d812c161a214d612560`
- QA_record: `candidates/SOC_COMMUTE_002_IMG_02_CAND_01/QA.md`

## Approval record

- approved_by: user
- approval_date: 2026-09-19
- approval_evidence: “批准 登记”
- promotion: moved (not copied) to the approved L3 post-image path.
- scope: published only within this social post; not Canon and not a downstream visual input.
