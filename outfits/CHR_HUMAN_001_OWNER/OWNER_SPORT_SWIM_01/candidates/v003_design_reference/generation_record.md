# Outfit Generation Record

- asset_id: `OWNER_SPORT_SWIM_01_DESIGN_REFERENCE`
- outfit_id: `OWNER_SPORT_SWIM_01`
- asset_level: `L2`
- asset_purpose: `design_reference`
- view_type: `design_reference`
- head_policy: `not_applicable`
- candidate_version: `v003`
- status: `APPROVED`
- generation_tool: `built-in ImageGen`
- generated_at: `2026-09-17`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_SWIM_01/candidates/v003_design_reference/OWNER_SPORT_SWIM_01_DESIGN_REFERENCE_v003.png`
- promoted_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_SPORT_SWIM_01/approved/design_reference/OWNER_SPORT_SWIM_01_DESIGN_REFERENCE.png`
- promoted_sha256: `6243e48fc11d8c9dbdb736bfacc76de0f10db74594899e73b7c4e3ecdaa5cfbc`
- reference_budget: `text-only; no supplied garment reference images`

## Generation inputs

```yaml
generation_inputs: []
qa_comparison_only: []
```

## Reference isolation

- previous_candidate_pixels_used: `false`
- previous_shot_pixels_used: `false`
- model_identity_taken_from_garment_reference: `false`
- body_or_proportion_taken_from_garment_reference: `false`
- lighting_or_background_taken_from_garment_reference: `false`

## Prompt assembly

Use case: `product-mockup`. Create a clean clothing-only product design board with
no person, mannequin, head, face, body, hands, or feet. Show the same white high-cut
one-piece swimsuit in two clearly separated flat product views: FRONT VIEW on the
left and REAR VIEW on the right.

FRONT VIEW: show only the front exterior. The front gusset/pelvic panel must be the
widest part across the front, then taper cleanly toward the lower crotch edge. Do
not show any rear panel, rear extension, back fabric, or hidden back portion from
the front view. The front silhouette must not appear wider behind or below the
front gusset.

REAR VIEW: show a very large open-back cutout. Leave only a narrow center rear
gusset/bridge at the bottom; this rear panel must be clearly much narrower than the
front gusset, approximately one third of the front width or slightly narrower. Do
not mirror the front panel onto the back. Keep the garment technically coherent as
one-piece swimwear and non-sensational in a catalog plate.

Cover the white swimsuit evenly with many small repeated strawberry motifs. Add a
separate plain solid-white swim cap and plain solid-white swim goggles. Add a
separate skin-tone 15D matte pantyhose material swatch with fine sheer textile
texture. No footwear.

Use an opaque solid light neutral gray background, soft even studio catalog lighting,
standardized vertical 3:4 composition, clean spacing, ample margins, no labels,
text, or watermark. Define only garment construction, accessories, hosiery
material, and outfit coordination. Do not define any person or identity.

Avoid: front view showing rear fabric, rear extension wider than front, mirrored
front/back panels, person, model, mannequin, face, body, skin, hair, hands, feet,
patterned cap, patterned goggles, opaque tights, glossy hosiery, latex, PVC,
plastic, rubber, logo, readable text, watermark, or collage clutter.

## Settings

- aspect_ratio: `3:4`
- preferred_resolution: `1536x2048` or closest supported native 3:4 size
- seed: unavailable in built-in ImageGen

## QA

- technical_status: `PASS`
- visual_status: `PASS_WITH_USER_REVIEW`
- garment_reference_isolation_check: `PASS`
- face_contamination_check: `NOT_APPLICABLE`
- decision: `APPROVED_BY_USER`
- approval_evidence: `User message: 批准`
- approved_at: `2026-09-17`
- observed_note: `Front view is isolated to the front exterior: the front gusset is widest across the pelvic area and tapers toward the lower edge. Rear view separately shows a large open-back cutout with a substantially narrower rear center panel. Plain white cap/goggles and skin-tone 15D matte hosiery swatch are present.`
