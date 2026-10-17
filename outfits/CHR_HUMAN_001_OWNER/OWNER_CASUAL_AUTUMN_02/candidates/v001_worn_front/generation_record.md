# Generation Record — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v001

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v001
outfit_id: OWNER_CASUAL_AUTUMN_02
level: L2
asset_purpose: worn_front
view_type: worn_front
head_policy: head_present_owner_face_method
candidate_version: v001
target_canon_version: owner_v1.0
spec_revision: draft_1.234
identity_revision: draft_0.187
status: REVIEW_REQUIRED
approval_status: USER_REVIEW_REQUIRED
gate: L2 outfit front fit-validation
generation_tool: built-in ImageGen
generated_at: 2026-10-17
output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v001_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v001.png
output_sha256: 4b6b62f8300df13286ac95f4ac53503b15d1ec766f6fa1133865c66fef76757e
reference_set_ids:
  - OWNER_L0_FACE_013_GEOMETRY_CROP_V1
  - OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE
reference_budget: 5 image inputs; 3 QA-only comparisons
aspect_ratio: "3:4"
resolution: "native tool output, exact 3:4 requested"
seed_settings: ImageGen did not expose seed or sampler settings
```

## Validation target

- fit_or_design_question: Does the approved autumn-casual outfit fit naturally on the current owner body proportions, with a source-derived face, Hairstyle A, subtly sheer continuous white pantyhose, and pale beige-tan fuzzy open-toe slippers?
- acceptance_checks:
  - Face generated only from applicable deterministic L0 face/skin derivatives and FACE_01 method prompt constraints; no AI face/body or previous candidate is a generation input.
  - Approved face Canon appears only in `qa_comparison_only` for identity drift, face contamination, and projection QA.
  - The face is natural, recognizable, adult, neutral, evenly lit, and free of blotches, patches, muddy relighting, smudges, or generated-face artifacts.
  - Hairstyle A only: long, straight, loose dark-brown hair, low crown, restrained near-center part; no B styling or hybrid.
  - Face-excluded Body01 derivative defines neck-below proportion and front stance only; don't slim or reshape the body.
  - Outfit matches the approved v004 design: oatmeal cardigan, warm-ivory tee, lighter warm-brown wool mini skirt, thin white pantyhose with slight show-through, pale beige-tan fuzzy open-toe slippers.
  - White pantyhose stays continuous over waist/hips, thighs, knees, calves, ankles, heels, insteps and toes, with textile visibly present over toes.
  - Slippers are open-toe; covered hosiery toes remain visible through the opening. No bare skin gaps, plastic/latex shine, fused footwear or anatomy errors.
  - Full body, head and both slippers in frame; natural front standing pose with both feet grounded, no cropping.
  - No logos, readable text, watermark, extra person or collage.

## Generation inputs

Only the listed scoped references are image inputs. Do not pass any other project image.

```yaml
generation_inputs:
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    responsibility: L0-derived recognizable facial feature geometry and identity only
    must_not_define: source makeup, hair, skin color/retouch, camera, lighting, clothing, body, background
  - asset_id: OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png
    responsibility: natural L0 skin color and texture baseline only
    must_not_define: fine facial geometry, source hairstyle, makeup, camera, body, clothing, lighting, background
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    responsibility: L0 Hairstyle A pixels and construction only
    must_not_define: face, skin, identity, body, clothing, lighting, background, or the gray mask
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    responsibility: neck-below front body geometry, waist/hip relationship, limb proportions, stance and foot scale only
    must_not_define: face, facial identity, hair, clothing design, hosiery material/color, lighting, background
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png
    responsibility: approved outfit garments, colors, layering and footwear design only
    must_not_define: face, body, proportions, skin, hair, identity, pose, hosiery anatomy, lighting, background
```

## QA comparison only

These approved AI images are post-generation comparison references and must not be attached to ImageGen.

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: identity drift, facial-feature relationships, skin contamination, face projection and framing
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    comparison_scope: front body proportion and stance only
  - asset_id: L0_HOS_15_WSS_002
    path: materials/hosiery/source_library/raw/15d_white_soft_sheen/IMG_2604.jpg
    comparison_scope: post-generation white tone, slight sheerness, and textile response only
```

## Reference isolation

- face_generation_method: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` prompt constraints plus source-derived L0 crops above
- hairstyle: `HAIRSTYLE_A`
- approved_ai_face_or_body_used_as_generation_input: `false`
- approved_ai_face_used_qa_comparison_only: `true`
- body_reference_is_face_excluded_derivative: `true`
- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- garment_reference_used_for_identity_or_body: `false`
- hosiery_material_source_used_qa_only: `true`

## Prompt assembly

Use case: photorealistic-natural. Create exactly one independent L2 front worn-outfit
fit-validation candidate, full body, 3:4 portrait; do not edit or continue any prior
candidate. Use the L0-derived geometry crop and L0 skin crop only for the face, with
the source-derived FACE_01 method constraints: preserve the same recognizable adult
woman and natural feature relationships; neutral closed-mouth expression and gentle
direct gaze; natural warm-neutral skin tone and texture; no beautification, age change,
face slimming/widening, enlarged eyes, narrowed nose, pointed chin, whitening, cooling,
or smoothing. Never use an AI face or body image to generate the face. Use the masked
DSC00847 source only for Hairstyle A: long straight loose dark-brown hair, near-center
part, close roots, low restrained crown, fine face-framing strands and tapered ends;
no bun, updo, Hairstyle B, or hybrid. Use the face-excluded Body01 derivative only for
neck-below proportions, front stance and foot scale. Use the approved outfit design
only for the outfit, including the declared pantyhose material design.

Show the exact approved outfit: cream-oatmeal crew-neck cardigan with small matte
wood-look buttons over a plain warm-ivory crew-neck tee; lighter warm medium-brown
wool-blend A-line mini skirt; thin white pantyhose with slight natural show-through
and a matte textile finish; pale beige-tan fuzzy open-toe mule slippers. Preserve the
cardigan, tee, skirt and footwear design. Keep the tights as one continuous textile
from waistband through hips, thighs, knees, calves, ankles, heels, insteps and toes.
At each open slipper, show a subtle but unmistakable white fabric veil over the toes;
the textile must not disappear, break, form a hard ring, or look oily, plastic, latex,
rubber, liquid or body paint. Because the hosiery is white and slightly sheer, allow
only gentle natural skin tone to show through; don't darken it or expose bare skin.

Natural relaxed front-facing standing pose with arms at ease, both feet grounded and
visible. Keep body proportions consistent with the face-excluded Body01 reference;
do not redesign or exaggerate waist, hips, thighs, calves, legs or feet. Use a neutral
gray-white seamless studio, soft even 5200–5600K light and a level 70–85mm-equivalent
camera. Include full head, hair, hands and both slippers, with safe margins and no
cropping. No props, jewelry unless present in the approved outfit design, logos,
readable text, watermark, collage, extra person or extra limbs. One candidate only;
status REVIEW_REQUIRED, not Canon.

## QA

- technical_status: `PASS` — PNG 1086 × 1448 px, exact 3:4; checksum recorded
- fit_validation_status: `PASS`
- face_contamination_check: `PASS` — compared only after generation against approved Face Canon; no visible blotches, patches, muddy relighting, smudges, or obvious identity drift
- face_generation_method_followed: `true`
- source_derived_face_inputs_check: `PASS` — only the two declared deterministic L0 face/skin derivatives were generation inputs
- hairstyle_a_scope_check: `PASS` — long straight loose hair and restrained near-center part; no B styling or hybrid
- body_proportion_check: `PASS` — face-excluded body derivative used only for neck-below comparison; front stance and proportions appear consistent
- hosiery_continuity_and_material_check: `PASS` — thin white textile reads slightly sheer and continuous to the visible open-toe areas; no apparent hard break or plastic finish
- outfit_fidelity_check: `PASS` — approved cardigan, tee, lighter brown skirt, hosiery and pale fuzzy slippers are present
- downstream_video_keyframe_reference_allowed: `false`
- downstream_identity_lineage_allowed: `false`
- decision: `REVIEW_REQUIRED — QA passed; awaiting user's L2 worn-fit approval.`
- reviewer: `Codex`
- reviewed_at: `2026-10-17`
