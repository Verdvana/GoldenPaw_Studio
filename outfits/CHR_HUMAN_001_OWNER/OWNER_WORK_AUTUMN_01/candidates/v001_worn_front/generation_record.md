# Outfit Generation Record

- asset_id: OWNER_WORK_AUTUMN_01_WORN_FRONT_v001
- outfit_id: OWNER_WORK_AUTUMN_01
- asset_level: L2
- asset_purpose: worn_fit_validation
- view_type: worn_front
- head_policy: head_present_owner_face_method
- candidate_version: v001
- status: REJECTED
- generation_tool: built-in ImageGen
- generated_at: 2026-09-19T10:51:47Z
- output_path: removed at user request on 2026-09-19
- output_sha256: f469a0246ce02ee42751542d9975ccf2c6cdf094ab273c70a9aac72fb70d3649 (historical provenance only)

## Validation target

- fit_or_design_question: Does the defined autumn office outfit read coherently when worn in a neutral, full-body front fit-validation pose, while preserving source-derived owner face generation and face-excluded body geometry?
- acceptance_checks:
  - full body, head, hands, shoes, and both feet are visible in a straight-on neutral standing pose
  - owner face is generated only from `L0_OWNER_012` / `14.jpg` plus written source-derived face constraints; no AI face/body/candidate image is supplied for face generation
  - Hairstyle A follows the face-masked L0 derivative only
  - white collared knit sweater, gray cropped straight-leg tailored trousers, black sheer pantyhose, and black pointed-toe slingback pumps are unambiguous
  - trousers end visibly above the ankle; black pantyhose remains continuous under the trousers and inside the shoes
  - no toe-cap boundary, bare toe, latex/plastic sheen, duplicated limb, warped hand, or shoe-geometry drift
  - neutral studio fit-validation image; no text, logo, watermark, or unrelated prop

## Generation inputs

```yaml
generation_inputs:
  - asset_id: L0_OWNER_012
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/14.jpg
    sha256: f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788
    responsibility:
      - front-visible owner facial identity
      - natural facial-feature relationships
      - skin identity direction
    must_not_define:
      - hairstyle
      - body or proportions
      - outfit
      - hosiery
      - pose
      - lighting
      - background
      - photography style
  - asset_id: OWNER_HAIRSTYLE_A_FACE_MASKED_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/FACE_01_FRONT_NEUTRAL_METHOD_v1/DSC00847_HAIR_ONLY_MASKED.png
    sha256: 6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd
    responsibility:
      - Hairstyle A front construction only
    must_not_define:
      - mask
      - identity
      - face
      - skin
      - body
      - clothing
      - lighting
      - background
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility:
      - neck-below front body geometry
      - 168 cm / 60 kg proportion range
      - waist/hip, limb, lower-leg, and foot-scale matching
    must_not_define:
      - face
      - facial identity
      - hair
      - clothing design
      - hosiery material design
      - lighting
      - background
  - asset_id: OWNER_WORK_AUTUMN_01_REF_001
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_WORK_AUTUMN_01/reference_inputs/garment_references/IMG_2779.jpg
    sha256: 855f7cac41b7a097680663b11097cdebf86360dbdb02d92e927b29315e1e3886
    responsibility:
      - black pointed-toe slingback silhouette
      - rear strap and buckle construction
      - slender high heel proportion
    must_not_define:
      - model identity
      - face
      - body or proportions
      - skin or hair
      - pose
      - lighting
      - background
      - photography style
```

## QA comparison only

```yaml
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    comparison_scope:
      - identity drift
      - face contamination
      - framing/projection
```

## Reference isolation

- reference_set_ids: `OWNER_L0_FACE_FRONT_NEUTRAL`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`
- reference_budget: 4 images
- previous_candidate_pixels_used: false
- previous_shot_pixels_used: false
- model_identity_taken_from_garment_reference: false
- body_or_proportion_taken_from_garment_reference: false
- lighting_or_background_taken_from_garment_reference: false

## Prompt assembly

- face method: source-derived, front-facing application of `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` constraints; L0 `14.jpg` is the only face-image input, while AI Face Canon is QA-only.
- hairstyle method: HAIRSTYLE_A from face-masked L0 derivative only.
- body method: face-excluded Body01 v025 derivative only; exclude its calibration outfit and hosiery material responsibilities.
- outfit method: text contract for white collared knit sweater, gray nine-point straight-leg tailored trousers, black sheer pantyhose, and `REF_001` scoped shoes. The unreviewed clothing-only candidate is not an input.

## QA

- technical_status: FAIL
- fit_validation_status: FAIL
- face_contamination_check: FAIL
- face_generation_method_followed: true
- downstream_video_keyframe_reference_allowed: false
- downstream_identity_lineage_allowed: false
- decision: REJECTED — face drifts from the approved QA comparison; hair is half-up instead of HAIRSTYLE_A; sweater lacks the specified collar; both shoes visibly retain red outsole styling prohibited by the scoped shoe reference; these defects prohibit promotion and downstream use.
- reviewer: Codex initial QA
- reviewed_at: 2026-09-19
