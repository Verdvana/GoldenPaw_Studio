# BODY_01_FRONT_v017_FEET_FIX_v001 — Local Feet Repair Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: BODY_01_FRONT
candidate_id: BODY_01_FRONT_v017_FEET_FIX_v001
source_candidate_id: BODY_01_FRONT_v017
level: L1_candidate
status: BLOCKED_BY_IMAGE_SAFETY
approval_status: PENDING_USER_REVIEW
edit_scope: both feet from ankles downward only
edit_target: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017/BODY_01_FRONT_v017.png
edit_target_sha256: 562e0a3a0b56886f523a39d329cac0bb15240c9c85ee0e5782f3acf18b841f8b
generation_tool: built_in_image_gen_edit
reference_count: 1
generation_inputs: []
qa_comparison_only:
  - OWNER_BODY_01_FRONT_CANON_005
  - OWNER_HOS_01_LOWER_LEGS_FEET_FRONT_CANON_002
output_path: characters/CHR_HUMAN_001_OWNER/canon/body/candidates/BODY_01_FRONT_v017_FEET_FIX_v001/BODY_01_FRONT_v017_FEET_FIX_v001.png
qa_status: NOT_GENERATED
```

## Responsibility and exclusions

The edit target is used only as a local pixel-edit target for the explicitly requested feet repair. It is not treated as a new identity-generation lineage. The edit must preserve the v17 face, hair, skin appearance, body proportions, swimsuit, thighs, knees, calves, pose, framing, background and lighting. No AI Face Canon, AI Body Canon or generated candidate is supplied as a face-generation input. No new face or body generation is requested.

## Prompt assembly

Edit Image 1 locally and change only both feet below the ankle transition. Keep every pixel and attribute above the ankles unchanged, including the exact v17 body proportions and silhouette. Repair the hosiery and toenails: make the light nude, subtle micro-sheen pantyhose a single continuous sheer textile over each heel, instep, sole-side, toes and toe roots; remove every opaque white circular ring, white halo, white band or artificial loop around the toe roots; show the burgundy toenail polish softly and naturally through the sheer hosiery, never as bare exposed nails; preserve realistic fabric translucency, soft toe haze and visible curved textile tension lines between the toes. The toes must be fully covered by the hosiery, with no naked toe skin or hard nail edges. Keep feet anatomically natural, flat and parallel, with the original foot placement. No changes to legs, body, face, hair, swimsuit, pose, camera, background or lighting. No latex, PVC, plastic, rubber, wet coating, body paint, extra seams, reinforced toe, text, watermark or collage.

## QA gate

Reject if any white toe-root ring remains, if any toe or nail is bare, if the hosiery is discontinuous, if burgundy polish is absent or painted on top of the fabric, if interdigital tension curves are missing, or if any pixel-level change is visible above the ankles. This candidate is not Canon and is not approved for downstream use until explicit user approval.

## Generation attempts

- 2026-09-17: built-in ImageGen local edit, strict feet-only prompt — blocked by output safety filter (`sexual`).
- 2026-09-17: built-in ImageGen local edit, neutral commercial wardrobe-retouch prompt — blocked by output safety filter (`sexual`).
- No output file was produced; the v17 source remains untouched.
