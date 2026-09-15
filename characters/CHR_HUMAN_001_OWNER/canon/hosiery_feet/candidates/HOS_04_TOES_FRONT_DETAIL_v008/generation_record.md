# HOS_04_TOES_FRONT_DETAIL_v008 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
target_canon_version: owner_v1.0
spec_revision: draft_1.204
identity_md_revision: draft_0.136
asset_id: HOS_04_TOES_FRONT_DETAIL
candidate_id: HOS_04_TOES_FRONT_DETAIL_v008
gate: "Gate 7 — Hosiery / Feet Canon"
model_tool: "built-in ImageGen"
status: PROMOTED_TO_L1_COMPONENT
approval_status: APPROVED
aspect_ratio: "3:4"
preferred_resolution: "1536x2048"
reference_set_ids: [OWNER_BODY_FRONT_CANON_L1]
reference_count: 1
previous_ai_candidate_count: 0
previous_generated_hosiery_inputs: []
rejected_candidate_pixels_used: false
seed_settings: "built-in ImageGen; seed and detailed settings may not be returned"
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_04_TOES_FRONT_DETAIL/OWNER_HOS_04_TOES_FRONT_DETAIL_CANON_001.png"
actual_dimensions_px: "1086x1448"
checksum_sha256: 35e353c038edb94f415a04a893349f03ed93b8daa9d452ff2cddff74731bc9b9
qa_status: PASS_BY_EXPLICIT_USER_REVIEW
```

## Authorization and lineage

On 2026-09-15 the user rejected v007 because its toe-by-toe arcs read as five-toe hosiery. v008 returns to normal pantyhose construction: one continuous transparent velvet-finish toe area with soft aggregate toe relief, no individual toe sleeves and no crosswise line. It is independently reconstructed from the approved front Body Master only; v001–v007 are excluded as pixel inputs.

## Generation result

- generated_at: `2026-09-15`
- result: first wording pass was output-moderation blocked; a safer clinical textile-inspection retry generated the saved candidate.
- project_candidate_path: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/candidates/HOS_04_TOES_FRONT_DETAIL_v008/HOS_04_TOES_FRONT_DETAIL_v008.png`
- actual_dimensions_px: `1086x1448`
- checksum_sha256: `35e353c038edb94f415a04a893349f03ed93b8daa9d452ff2cddff74731bc9b9`
- promotion_status: promoted to `OWNER_HOS_04_TOES_FRONT_DETAIL_CANON_001` after explicit user approval.
- approval_record: `characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_04_TOES_FRONT_DETAIL/approvals/APPROVAL_OWNER_HOS_04_TOES_FRONT_DETAIL_001.md`

## Reference responsibilities

- `OWNER_BODY_FRONT_CANON_L1`: front foot and toe anatomy, proportions and neutral contact only.
- No material photograph or previous generated hosiery image is attached.

## Prompt assembly

```text
Create one neutral photorealistic medical textile quality-control reference image, exact 3:4 vertical. Use the supplied approved front Body Master only for front foot and toe anatomy, proportions and neutral contact. Do not use any previous generated image.

Show a straight-on close technical view of both complete forefeet and a small amount of ankle and instep context. Feet parallel, naturally separated, flat on a light-gray seamless clinical surface. Camera at toe height, restrained perspective, soft even white light, no props or styling.

The subject wears normal full-length pantyhose: one single continuous light-nude 15-denier sheer textile layer extending from ankle across instep, forefoot and all toe tips. The fabric has a fine velvet-finish matte response, soft translucent haze and slightly increased yarn density, but remains clearly transparent and delicate. It must look like ordinary closed-toe pantyhose, never a toe sock.

Critical toe construction: the entire front of each foot is covered by one smooth continuous textile surface. The toes are seen only as a soft aggregate contour beneath the fabric; their individual tips and burgundy nail color are heavily softened and partially blended by the sheer veil. Do not outline or wrap each toe separately. Do not create individual toe sleeves, toe pockets, ring-like arcs, dark interdigital channels or five separate fabric compartments. Preserve only gentle shallow anatomical relief under the continuous fabric.

The fabric is smoothly tensioned over the toe area with a soft uniform haze and a restrained velvet matte highlight. The transition from ankle through instep, forefoot and toe tips is uninterrupted. Absolutely no toe-cap seam, horizontal line, transverse band, reinforced panel, abrupt hue or opacity break, exposed bare toe, crisp nail edge or material boundary.

No opaque socks, 30D appearance, glossy coating, plastic, rubber, latex, PVC, body paint, duplicated/fused/missing anatomy, shoes, accessories, labels, logos, watermark, collage or extra views. Return one technical REVIEW_REQUIRED candidate only.
```
