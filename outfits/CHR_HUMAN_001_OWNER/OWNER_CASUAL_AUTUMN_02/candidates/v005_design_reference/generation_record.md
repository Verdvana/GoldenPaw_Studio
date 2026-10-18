# Generation Record — OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005

- asset_id: `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005`
- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `clothing_only_flat_lay`
- candidate_version: `v005`
- status: `APPROVED`
- generated_at: `2026-10-17`
- original_candidate_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v005_design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005.png` (promoted by move)
- approved_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`
- output_sha256: `216f7621c422471bdb0cdcf6e8b9e881c69b3c7169182c0c92ea6e51ed2a9b63`

## Validation target

Replace the prior approved design reference with a newly designed autumn outfit using Photo 1 for the blazer, knit top and pleated skirt, and Photo 2 for the hosiery appearance and fuzzy open-toe slippers. This is a clothing-only L2 design candidate; it does not approve or alter owner Canon.

## Generation inputs

```yaml
generation_inputs:
  - asset_id: USER_UPLOAD_PHOTO_1
    path: /tmp/codex-remote-attachments/01a149cb-3b3c-7fb3-a002-abc1ad6ae53d/D9EC3B92-CFE1-4EBF-AC87-624FF34A95BB/1-Photo-1.jpg
    responsibility: [dark brown blazer construction, ivory ribbed high-neck knit, dark brown pleated mini skirt]
    must_not_define: [person, face, body, skin, hair, identity, pose]
  - asset_id: USER_UPLOAD_PHOTO_2
    path: /tmp/codex-remote-attachments/01a149cb-3b3c-7fb3-a002-abc1ad6ae53d/D9EC3B92-CFE1-4EBF-AC87-624FF34A95BB/2-Photo-2.jpg
    responsibility: [pale ivory plush open-toe mule slipper design, sheer pale hosiery appearance]
    must_not_define: [person, face, body, skin pigmentation, identity, pose, anatomy]
  - asset_id: OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v004_design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v004.png
    responsibility: [clothing-only flat-lay presentation, neutral studio background, complete product arrangement]
    must_not_define: [new garment design, person, body, proportions, identity]
qa_comparison_only: []
```

- reference_budget: `3 images; each limited to declared responsibilities`
- prompt_assembly: `Photorealistic clothing-only product flat-lay on neutral light gray. Photo 1 defines only dark chocolate tailored notched-lapel blazer, ivory fine-ribbed high-neck turtleneck, and dark brown pleated mini skirt. Photo 2 defines only pale sheer hosiery material and plush cream open-toe mule slipper design. The prior v004 design reference defines only flat-lay catalog arrangement and background. No human, mannequin, limbs, feet, face, hands, skin, identity, or body-shaped hosiery form; no text/logo/watermark. Real textile, soft studio shadows; hosiery must not look like latex, rubber, plastic, wet surface, or body paint.`
- seed/settings: `Not available`
- face_contamination_check: `Not applicable; candidate contains no person or face`
- hosiery_checks: `single continuous matte sheer textile; enclosed toes; no latex/plastic look; see docs/qa/hosiery_material_rules.md`
- QA_status: `PASS — clothing-only design approved by user`

## Approval and promotion

- decision: `APPROVED_BY_USER`
- reviewer: `user`
- approved_at: `2026-10-17`
- user_approval_statement: `不错，批准`
- promotion_operation: `MOVED — candidate raster relocated unchanged; prior approved raster restored to its v004 candidate archive; no duplicate raster retained`
