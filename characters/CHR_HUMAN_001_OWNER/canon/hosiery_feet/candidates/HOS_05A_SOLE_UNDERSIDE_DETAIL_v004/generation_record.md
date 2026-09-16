# HOS_05A_SOLE_UNDERSIDE_DETAIL_v004 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_05A_SOLE_UNDERSIDE_DETAIL
candidate_id: HOS_05A_SOLE_UNDERSIDE_DETAIL_v004
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: USER_REJECTED
approval_status: REJECTED
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
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_05A_SOLE_UNDERSIDE_DETAIL_v004/HOS_05A_SOLE_UNDERSIDE_DETAIL_v004.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: "a77a589ad8087e760c8058d86e6ecacd8fd7e1b62488f9ee97f524de0e7106a3"
qa_status: FAIL_USER_REJECTED_FOOTNAIL_ARTIFACT
```

## Authorization and lineage

This is an independent rebuild requested after the user identified iterative contamination in v003. v001–v003 are explicitly excluded as pixel inputs. The candidate is reconstructed in parallel from the approved Body Master and the registered real 15D material source only.

## Reference responsibilities

1. `OWNER_BODY_FRONT_CANON_L1`
   - path: `characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON.jpg`
   - SHA-256: `964c3b9d72c6688881b8ebfa4c6fc1bcfea04c998351352fabfdc8f4951666f6`
   - responsibility: owner foot proportions and neutral identity context only.
   - must_not_define: sole-facing pose, hosiery material or source person's styling.
2. `HOS_15D_NUDE_MATTE_BAREFOOT`
   - path: `materials/hosiery/source_library/raw/15d_nude_matte/IMG_2562.jpg`
   - SHA-256: `2f869afc5af953b971b68621f7cbc7c3696a129774dec1838dfec0f0a0a15869`
   - responsibility: 15D nude matte/velvet textile, transparency, sole coverage and fabric tension only.
   - must_not_define: owner identity, body/foot anatomy, nail color, pose or background.

## Authoritative candidate scope

- one independent technical underside-foot view with both complete soles raised toward camera;
- a visibly present, slightly denser interpretation of 15D nude velvet-matte sheer hosiery, still translucent;
- clear textile structure: fine mesh/knit grain, directional stretch over the arch and ball, and shallow curved tension bands between toe bases;
- one continuous fabric layer across heel, arch, ball, forefoot and closed toe tips, with no separate toe pockets.

## Prompt assembly

```text
Use case: photorealistic-natural.
Asset type: neutral textile coverage and foot-structure documentation; exactly one HOS_05A_SOLE_UNDERSIDE_DETAIL_v004 candidate, REVIEW_REQUIRED.
Input images: Image 1 defines only approved foot proportions and lower-leg-to-foot geometry. Image 2 defines only 15D nude matte velvet textile appearance, density, mesh grain, sole coverage and stretch behavior. Do not use any previous generated image.
Primary request: independently reconstruct one technical underside-foot view with both complete soles elevated toward the camera, soles facing forward, ankles and a small amount of lower-leg continuation visible. Both feet are separated, naturally aligned and neutrally flexed. No shoes or support object.
Scene/backdrop: seamless light-gray clinical studio, soft even white-balanced light, restrained camera perspective, exact 3:4 vertical frame.
Materials/textures: the feet wear one continuous pair of 15D nude sheer pantyhose with a clearly visible but still translucent velvet-matte textile layer. Make the hosiery more visually substantial than bare skin: show fine regular mesh grain across the soles, soft yarn density, and directional stretch lines following the arch, heel pad and ball of foot. Between adjacent toe bases, show several shallow, curved, diffuse tension arcs and slight changes in knit direction caused by fabric stretching over the toe relief. These arcs must be textile tension, not drawn lines.
Toe construction: one uninterrupted closed-toe textile surface over every toe tip. Toes may appear as softened aggregate relief beneath the fabric, but do not create individual toe sleeves, pockets, ring outlines, hard channels or split-toe construction.
Constraints: preserve natural approved foot proportions, toe count and anatomy. Burgundy nail color, if visible, stays faintly beneath the textile. No exposed sole, bare gaps, sock edge, seam, opacity break, shoes, props, text, logo, watermark or collage.
Avoid: skin-like bare feet, invisible fabric, smooth untextured skin rendering, opaque socks, latex, PVC, rubber, plastic, wet coating, body paint, harsh gloss, exaggerated anatomy or sexualized framing.
Output one REVIEW_REQUIRED candidate only.
```

## QA status

Awaiting generated raster and visual review. This candidate cannot be promoted or used downstream without explicit user approval.

## Technical pre-check

- Independent rebuild from the approved Body Master and registered 15D material source; v001–v003 were not used as pixel inputs.
- The hosiery layer is visibly denser than prior attempts while remaining translucent, with clear fine mesh grain across the sole.
- Directional tension is visible over the arch/ball and as soft curved textile changes between adjacent toe bases; the surface remains continuous rather than separate toe sleeves.
- Both complete soles, heels, arches and closed toe tips are inside the 3:4 frame.
- User rejected the candidate because purple/hard nail-like artifacts appeared beneath the forefoot/toe area, visually suggesting nails growing on the sole side of the toes.
- Candidate is permanently excluded from Canon promotion and downstream use.
