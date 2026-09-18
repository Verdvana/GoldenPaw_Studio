# HOS_05A_SOLE_UNDERSIDE_DETAIL_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v001
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids:
  - OWNER_BODY_FRONT_CANON_L1
  - HOS_15D_NUDE_MATTE_BAREFOOT
reference_count: 2
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v001/HOS_05A_SOLE_UNDERSIDE_DETAIL_v001.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "f5ef2ad38d9d0129b59b7c173fa5ce8b436b85c1db2b3f0e224a16ba17f8a298"
qa_status: PASS_PENDING_USER_REVIEW
```

## Authorization and lineage

This is a newly added sole/underside-foot asset explicitly requested by the user, inserted after HOS_05 without renumbering existing HOS_06. No generated Hosiery, Pose or Shot image is used as input.

## Reference responsibilities

1. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v009/BODY_01_FRONT_v009.jpg`
   - responsibility: owner foot proportions and neutral identity context only.
   - must_not_define: sole-facing pose, hosiery material or source person's styling.
2. `HOS_15D_NUDE_MATTE_BAREFOOT`
   - path: `materials/hosiery/source_library/raw/15d_nude_matte/IMG_2562.jpg`
   - SHA-256: `2f869afc5af953b971b68621f7cbc7c3696a129774dec1838dfec0f0a0a15869`
   - responsibility: 15D nude matte/velvet textile, transparency, sole coverage and fabric tension only.
   - must_not_define: owner identity, body/foot anatomy, nail color, pose or background.

## Authoritative candidate scope

- one technical underside-foot view, with both complete feet raised toward the camera and soles visible;
- soft neutral flexion with ankles and lower-leg continuation readable where possible;
- one continuous 15D nude velvet-matte sheer pantyhose layer across heels, arches, balls of feet and closed toes;
- realistic translucent knit response, gentle tension over the sole and naturally softened burgundy toenails beneath the fabric.

The candidate must not define other foot views, other hosiery deniers/colors/finishes, complete owner identity, episode wardrobe, lighting or background.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral textile and underside-foot coverage inspection reference; exactly one HOS_05A_SOLE_UNDERSIDE_DETAIL_v001 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only the owner's approved foot proportions and neutral identity context. Image 2 defines only 15D nude matte velvet textile appearance, sole coverage, transparency and tension. Reconstruct independently; do not use any previous generated image.
Primary request: show one technical underside-foot view of both complete feet raised toward the camera, soles facing the lens, with ankles and a small amount of lower-leg continuation visible if naturally possible. Keep both feet separated, symmetrically arranged and neutrally flexed, with no shoes and no support object.
Scene/backdrop: seamless light-gray studio background, restrained natural perspective and soft even white-balanced clinical light.
Materials/textures: both complete feet wear one continuous pair of light-nude 15D sheer pantyhose with a soft velvet-matte finish. The fabric remains visibly present across the heels, arches, balls of feet and all closed toe tips, with fine translucent knit, subtle sole tension and gentle matte response. Burgundy toenails may appear only softly beneath the textile.
Composition/framing: exact 3:4 vertical frame; both complete soles, heels, arches and toe tips fully inside the frame; one view only.
Constraints: preserve natural foot proportions and continuous ankle-to-foot hosiery coverage. No sock edge, toe-cap seam, opacity break, bare toe, exposed sole, nail polish on top of fabric, extra feet, fused toes, shoes, props, text, logo, watermark or collage.
Avoid: latex, PVC, rubber, plastic, wet coating, body paint, opaque socks, exaggerated anatomy, harsh glossy highlights or sexualized framing.
Output one REVIEW_REQUIRED candidate only.
```

## QA status

Awaiting generated raster and visual review. This candidate cannot be promoted or used downstream without explicit user approval.

## Technical pre-check

- Both complete soles, heels, arches, forefeet and toe tips are inside the exact 3:4 frame.
- The view is a single neutral underside-foot inspection composition with separated feet and visible ankle/lower-leg continuation.
- 15D light-nude sheer textile is visibly continuous across the sole, heel, arch and closed toes, with fine matte knit texture and no shoe or material boundary.
- Candidate remains `REVIEW_REQUIRED`; no Canon promotion was performed.
