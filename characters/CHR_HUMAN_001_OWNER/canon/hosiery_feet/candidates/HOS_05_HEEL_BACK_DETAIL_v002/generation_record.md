# HOS_05_HEEL_BACK_DETAIL_v002 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05_HEEL_BACK_DETAIL
candidate_id: HOS_05_HEEL_BACK_DETAIL_v002
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_BACK_CANON_L1
  - HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001
reference_count: 2
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05_HEEL_BACK_DETAIL_v002/HOS_05_HEEL_BACK_DETAIL_v002.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "0748b98efbc013d24b05e62b067d8309ed87abe5a710b96c49a9f99ae97fd8cc"
qa_status: PASS_PENDING_USER_REVIEW
```

## Authorization and lineage

This is one independent retry of the incomplete `HOS_05_HEEL_BACK_DETAIL` component. The v001 request returned no raster after output moderation and is not an input. No previous generated hosiery, Pose, Shot, Face or other AI candidate is used.

## Reference responsibilities

1. `OWNER_BODY_BACK_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_06_BACK_v001/BODY_06_BACK_v001.png`
   - SHA-256: `2344a37e9355bbe1fb49865b5039275cebbbe5cfb043738b7e2edb6c777add7c`
   - responsibility: rear lower-leg, ankle, heel and foot geometry, proportions, direction and neutral floor contact.
   - must_not_define: hosiery color/denier/finish, identity beyond the visible scoped geometry, pose outside this rear detail, background or styling.
2. `HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001`
   - path: `materials/hosiery/reference_inputs/15d_nude_matte/1_material_v1/1_LOWER_LEGS_FEET_MATERIAL_CROP.png`
   - SHA-256: `36fba906cfb47002f6669133b336b5d47b25c1763450db8fd4fbce7412eb8948`
   - responsibility: 15D nude velvet-matte textile presence, fine opacity, continuous leg-to-foot coverage and restrained toe visibility only.
   - must_not_define: body/foot anatomy, skin pigmentation, nail color, clothing, shoes, pose, floor contact, lighting or background.

Reference budget: 2 scoped references. No previous AI candidate is attached.

## Authoritative candidate scope

- exact straight rear view of both complete heels and feet, with lower-calf context;
- neutral separated feet on one light-gray studio surface;
- continuous 15D sheer velvet-matte hosiery over lower calf, ankle, Achilles, heel, rear foot, instep and closed toes;
- inspectable ankle-to-heel textile continuity without a sock edge, seam, opacity break or exposed skin gap.

The candidate must not define reusable body identity, face, clothing design, nail color, other hosiery deniers/colors, other foot angles, lighting or environment beyond the neutral QA studio setup.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral clinical textile quality-control reference; exactly one HOS_05_HEEL_BACK_DETAIL_v002 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only approved rear lower-leg, ankle, heel and foot geometry and neutral floor contact. Image 2 defines only 15D nude velvet-matte textile appearance, fine opacity and continuous coverage. Reconstruct independently; do not use any previous generated image.
Scene/backdrop: seamless light-gray studio surface.
Primary request: show one straight rear view of both complete feet and heels from the lower calves downward, with both feet separated, parallel and neutrally resting on the same floor plane. Camera is at heel height with restrained natural perspective. Keep enough lower-calf context to inspect the ankle-to-Achilles-to-heel transition.
Style/medium: photorealistic neutral technical documentation, soft even white-balanced light.
Materials/textures: both legs and feet wear one continuous pair of light-nude 15D sheer pantyhose with a soft velvet-matte textile response. The textile follows the ankle, Achilles and heel contours continuously, continues across the rear foot and instep, and fully covers the toes. Show subtle fine-knit tension and natural translucency; any burgundy nail color remains only faintly beneath the fabric when visible.
Composition/framing: exact 3:4 vertical frame; one rear view only; both complete feet and lower-calf context fully inside frame.
Constraints: no shoes, no sock edge, no ankle cutoff, no reinforced heel patch, no seam or band, no opacity/color break, no bare-skin gap, no exposed heel, no duplicated limbs or extra feet, no text, logo, watermark or collage.
Avoid: glossy, wet, plastic, latex, PVC, rubber, liquid coating, body paint, opaque fabric, painted-on toes, fused or broken heel anatomy.
```

## QA status

Awaiting generated raster and visual review. This candidate remains `REVIEW_REQUIRED` and cannot be promoted or used downstream without explicit user approval.

## Technical pre-check

- Exact single straight rear view with both complete heels, lower-calf context and one floor plane.
- Ankle-to-Achilles-to-heel transition is continuous and anatomically readable; no shoe, sock edge, exposed heel or duplicated foot is visible.
- Hosiery reads as light-nude, thin and textile-based with restrained matte response; no latex/PVC/plastic/liquid coating appearance.
- Rear view does not expose the toe faces; front toe coverage remains covered by the separately scoped HOS_04 component.
- Candidate is ready for user review only; it is not approved or promoted.
