# Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
asset_id: OWNER_CASUAL_SUMMER_01_WORN_FRONT
outfit_id: OWNER_CASUAL_SUMMER_01
level: L2
candidate_version: v004
target_canon_version: owner_v1.0
spec_revision: draft_1.230
identity_revision: draft_0.177
status: APPROVED
approval_status: PENDING_USER_REVIEW
gate: L2 episode outfit fit-validation
reference_set_ids:
  - OWNER_BODY_FRONT_PROPORTION_OUTLINE_V17
  - OWNER_FACE_FRONT_NEUTRAL_RECOVERY_V1
  - OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE
reference_budget: 4 images
aspect_ratio: "3:4"
resolution: "1536x2048"
original_candidate_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v004_worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT_v004.png
approved_path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT.png
output_sha256: e555e1674408f46447b3d6a5ac866479cae805562ae56f690a0402334f75d25f
approval_date: 2026-09-18
approved_by: user
```

## Generation inputs and responsibilities

1. `OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE_v003` — outfit design only: camisole construction/print, high-waisted shorts, white suede low-heel tapered-band mule, earrings and light-nude micro-sheen hosiery concept. Must not define face, body, skin, hair, pose or identity.
2. `BODY_01_FRONT_V017_FACE_EXCLUDED_v1` — deterministic derivative of the user-selected v017 full-body image; body proportion and silhouette only, including waist/hip relationship, thigh-root contour, limb proportions, lower-leg axes, foot scale and neutral front stance. Must not define face, facial identity, skin tone/texture, hair, clothing, hosiery material, lighting or background.
3. `OWNER_FACE_SKIN_CONTEXT_NO_CROWN_001` — source-derived Face method input; face geometry, facial-feature relationships and warm-neutral skin appearance only. Must not define body, hair, clothing, pose, lighting or background.
4. `OWNER_HAIRSTYLE_A_FACE_MASKED_001` — source-derived masked L0 hair input; Hairstyle A pixels only. The gray face mask defines nothing.

The v017 full-body raster is not used as a face-generation input; only its deterministic face-excluded derivative is supplied. Approved AI Face/Body Canons are not generation inputs.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` — post-generation face identity/skin-contamination comparison only
- `OWNER_BODY_01_FRONT_CANON_005` — post-generation body contour comparison only; v017 remains the requested proportion target

## Prompt assembly

Generate one fresh photorealistic full-body frontal neutral standing owner wearing the exact summer outfit from the v003 clothing design reference. Use the face source and Face method constraints for the owner's face, use Hairstyle A only, and use the v017 face-excluded body derivative for the requested slimmer natural body proportions and front silhouette. Do not copy the v017 face or skin appearance. Keep a neutral eye-level 70–85mm-equivalent camera, full head and both feet in a 3:4 portrait, gray-white seamless studio, soft even light, relaxed arms, uncrossed legs and flat parallel stance.

Outfit fidelity is primary: white lightweight V-neck camisole with narrow straps, fine lace trim following the V neckline and sparse small blue floral motifs; clearly high-waisted light-blue denim shorts with a tall waistband, front pockets and slightly frayed/rolled hem; white suede open-toe one-band mule heels with a curved vamp strap whose width visibly tapers and is not uniform, and a modest lower slim heel; gold-tone dangling earrings with blue-green teardrop stones. Add light-nude sheer pantyhose as one continuous realistic textile with restrained micro-sheen from waist through feet; the open-toe shoes must still show fabric-covered front feet, with soft diffused burgundy nail color beneath the textile and delicate natural fabric tension curves between adjacent digits. No bare gaps, hard white rings, plastic/latex/PVC/rubber/liquid appearance or painted-on nail shapes.

Do not slim or redesign the user-selected v017 body outline beyond reproducing it. Do not change face identity, skin tone, hair, body proportions, pose, camera, lighting or background based on the outfit image. No extra garments/accessories, text, logos, watermark, collage or extra fingers/toes.

## QA status

- visual inspection: PASS_WITH_REVIEW — full-body frontal composition, no obvious extra anatomy or text
- v017 proportion/outline match: PASS_WITH_REVIEW — waist/hip, thigh, lower-leg axes and stance are consistent with the scoped v017 derivative
- Face-method compliance: PASS_WITH_REVIEW — face was generated from the source-derived Face input, not from v017 or the outfit image
- face contamination: PASS_WITH_REVIEW — no obvious outfit/body reference leakage into the face; comparison-only review remains required
- outfit fidelity: PASS_WITH_REVIEW — top, shorts, earrings and white shoe design are represented
- high-waist shorts: PASS — waistband reads clearly high-rise
- white suede and tapered lower heel: PASS_WITH_REVIEW — white matte shoe and modest heel are present; strap contour remains for user review
- hosiery continuity and toe-area material continuity: PASS_WITH_REVIEW — continuous pale sheer layer and muted burgundy detail are visible; user should confirm the toe opening meets the intended standard
- no white toe-root rings: PASS on preliminary view
