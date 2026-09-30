# Generation Record — SOC_TRAVEL_002_IMG_03_CAND_02

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_03
candidate_id: SOC_TRAVEL_002_IMG_03_CAND_02
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATION_BLOCKED_SAFETY
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from scoped L0 sources; no generated shot input
face_generation_method: FACE_01_FRONT_NEUTRAL_METHOD.md prompt constraints adapted to the requested high-angle smile; no AI Face/Body Canon input
face_generation_method_spec_revision: draft_1.11
reference_set_ids:
  - SOC_TRAVEL_002_REF_003_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_L0_FACE_013_GEOMETRY_CROP_V1
  - OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01_TEXT_AUTHORITY
reference_budget: 5 image inputs; body proportions and outfit are text-only
aspect_ratio: 4:5 vertical
resolution: native ImageGen output retained; delivery target 2160x2700
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_003
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/3.jpg
    sha256: 01101628a46108693b724a1f9dd868841f830c9c8bde2ae7d2b25f1227aaa0ca
    responsibility: pose mechanics, friendly smile action, high camera position, close vertical crop, cruise deck/ocean composition
    must_not_define: identity/face features, body proportions, hair, outfit, hosiery, footwear, watermark/text or exact ship design
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    source_asset_id: L0_OWNER_013
    source_sha256: 1851e8decaa3430f127c3e720f7fba8bb119370008ef7795313fd6e76b396af0
    responsibility: real-source facial identity and feature geometry only
    must_not_define: source hairstyle, makeup, jewelry, skin retouch/color, source camera/light, body, clothing or environment
  - asset_id: OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001.png
    sha256: 89bc3208dfa46131e7d1a0f201e054fa38f8b3927d26ab12f4fb690426922abd
    source_asset_id: L0_OWNER_012
    source_sha256: f7a83644f202ebec95134c6d115397b9f52f12e79b5fb227a6b79182026bd788
    responsibility: natural warm-neutral skin color/texture baseline only
    must_not_define: fine face geometry, hairstyle, makeup, camera, body, clothing, lighting or background
  - asset_id: L0_OWNER_006
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg
    sha256: 734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17
    responsibility: real-source Hairstyle B construction only
    must_not_define: face identity/features/expression, body, outfit, pose, camera, lighting or environment
  - asset_id: OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg
    sha256: e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f
    responsibility: approved B design, color and appearance only
    must_not_define: face generation/identity, body, clothing, pose, camera, lighting or environment
text_only_generation_authorities:
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    responsibility: written owner proportion target only (168 cm / 60 kg, natural body proportions); raster is QA-only and is not an input
    must_not_define: face generation, hair, outfit, hosiery material, pose, lighting or background
  - asset_id: OWNER_CASUAL_SUMMER_01
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md
    approval_record: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/APPROVAL.md
    responsibility: approved white floral lace-trim camisole, light-blue denim shorts, continuous light-nude sheer pantyhose and earrings; no shoes in frame
    must_not_define: owner identity/face/body/hair, pose, camera, lighting or background
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: post-generation face identity drift, facial-feature relationship, skin contamination/texture, projection and framing QA only; never generation input
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: body-proportion QA comparison only; never generation input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_03/candidates/SOC_TRAVEL_002_IMG_03_CAND_02/SOC_TRAVEL_002_IMG_03_CAND_02.png
seed_settings: seed/sampler not returned; native vertical output
qa_status: not_applicable_no_output
approval_status: NOT_GENERATED
```
