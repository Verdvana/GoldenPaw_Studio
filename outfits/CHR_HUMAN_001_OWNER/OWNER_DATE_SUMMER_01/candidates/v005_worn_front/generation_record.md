# Outfit Generation Record — registered Face recipe
- asset_id: OWNER_DATE_SUMMER_01_WORN_FRONT_v005
- outfit_id: OWNER_DATE_SUMMER_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_registered_face_recipe
- candidate_version: v005
- status: APPROVED
- generation_tool: built-in image_gen.imagegen
- generated_at: 2026-10-30
- output_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v005.png
- original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/candidates/v005_worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v005.png
- original_candidate_sha256: b93f96f8d354cf3aa1b434ee19d9acd90777937c1bf1471611f0cd798710b801
- output_sha256: b93f96f8d354cf3aa1b434ee19d9acd90777937c1bf1471611f0cd798710b801

## User instruction and method selection
- authorization: user 2026-10-30 “参考女主正脸已登记资产的生产方式来生产图片”
- Successful registered source checked: canon/face/candidates/FACE_01_FRONT_NEUTRAL_v011/generation_record.md and inputs/PROVENANCE.md, FACE_01_FRONT_NEUTRAL_METHOD.md, stable REFERENCE_INPUTS.md.
- The actual registered successful recipe uses B_FACE_SKIN_CONTEXT_NO_CROWN, a deterministic crop from generated scoped B appearance asset; it is NOT L0. Prior v004 used different L0 geometry/skin crops and was rejected for drift.
- Current direct user instruction to use the registered production recipe is applied as a scoped method override for this candidate. The broad L0-only face rule is not globally rewritten or represented as satisfied by B pixels. No new L1 approval, no approved Face Canon or prior worn candidate input.
- Scope: original B-derived source crop for face/skin and original masked L0 Hair-A input; face-excluded Body geometry; approved clothing-only v003. No future blanket permission inferred.

## Validation target
- fit_or_design_question: restore approved frontal face relationships through the registered successful recipe while retaining approved outfit and waist hierarchy
- acceptance_checks: exact facial relationships/skin first; then low crown short part, neutral frontal head; body proportion, neck/chest, cropped blouse and high hosiery waistband; continuous covered toes in silver sandals

## Generation inputs
```yaml
generation_inputs:
  - asset_id: OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001
    version: FACE_01_FRONT_NEUTRAL_METHOD_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/B_FACE_SKIN_CONTEXT_NO_CROWN.png
    sha256: d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d
    responsibility: registered recipe exact face relationships, face shape, adult age and skin appearance
    must_not_define: [Hairstyle B, crown, camera angle, body, pose, outfit, source lighting, background]
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    version: v1 deterministic L0 derivative
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd
    responsibility: Hairstyle A only
    must_not_define: [face, gray mask, skin, body, clothes, camera, lighting, background]
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    version: v7 / Canon 007 crop
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: neck-below body proportions and geometry only
    must_not_define: [face, skin, hair, outfit, hosiery material, lighting, background]
  - asset_id: OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003
    version: v003 approved
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/design_reference/OWNER_DATE_SUMMER_01_DESIGN_REFERENCE_v003.png
    responsibility: normal-neck blouse, regular-rise shorts, high white hosiery and silver sandals only
    must_not_define: [owner face, body proportions, skin, hair, identity, pose, lighting, background]
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope: [identity drift, face contamination, facial relationships, projection]
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    comparison_scope: [body proportion QA]
reference_budget: {maximum_images: 4, actual_images: 4}
```

## Reference resolution / provenance
- Registry OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1 resolves face and Hair A.
- Registry OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE resolves body.
- Outfit manifest resolves approved design v003.
- Body provenance: crop x=0,y=308,w=1086,h=1140; no resizing or generative transformation.
- B face provenance: deterministic 900x1000+93+350 crop from OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001; no retouch/resize/color change.
- Checksums of actual inputs: INPUT_CHECKSUMS.txt.

## Reference isolation
- garment_references_used: approved v003 clothing-only design
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_garment_reference: false
- no raster input copies; single authoritative repository output

## Prompt assembly and settings
- PROMPT.txt is exact submitted prompt.
- Face/skin/Hair-A/crown blocks reproduce registered method in intent; full-body outfit framing adapts L1 calibration presentation to L2 approved design.
- One independent candidate; 3:4 portrait requested; opaque background.
- Seed/model/quality/exact resolution: tool defaults/not exposed.

## QA
- technical_status: PASS
- fit_validation_status: APPROVED_BY_USER
- face_contamination_check: PASS (no obvious blotches/smudges; exact identity remains user review)
- face_generation_method_followed: true (registered B-crop method under current user direction; not L0-only)
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: user explicitly approved v005; moved unchanged to L2 approved/worn_front; not L1 Canon
- reviewer: Codex visual comparison after generation
- reviewed_at: 2026-10-30


## Result

- Native output 1086 × 1448 PNG, exact 3:4; one repository raster at output_path.
- Detailed visual inspection in QA.md. No raster input or output duplicates created in repository.

## User approval and promotion

- approved_by: user
- approval_date: 2026-10-30
- evidence: “这就对了，批准”
- approval_record: approved/worn_front/APPROVAL_v005.md (relative to outfit root)
- current_approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_DATE_SUMMER_01/approved/worn_front/OWNER_DATE_SUMMER_01_WORN_FRONT_v005.png
- current_approved_sha256: b93f96f8d354cf3aa1b434ee19d9acd90777937c1bf1471611f0cd798710b801
- promotion_operation: MOVED; candidate directory contains records only, no raster
- approval_scope: L2 front outfit fit and appearance including likeness as shown; no new identity/Canon authority or future generation input
