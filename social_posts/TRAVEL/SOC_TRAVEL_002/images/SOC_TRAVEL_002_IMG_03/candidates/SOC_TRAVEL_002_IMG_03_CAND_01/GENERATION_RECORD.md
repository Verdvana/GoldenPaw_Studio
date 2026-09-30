# Generation Record — SOC_TRAVEL_002_IMG_03_CAND_01

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_03
candidate_id: SOC_TRAVEL_002_IMG_03_CAND_01
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATION_BLOCKED_SAFETY
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from scoped L0/L1-approved sources; no generated shot input
face_generation_method: FACE_01_FRONT_NEUTRAL_METHOD.md prompt constraints adapted to requested high-angle smile; its generated/L1 image inputs are excluded
face_generation_method_spec_revision: draft_1.11
reference_set_ids:
  - SOC_TRAVEL_002_REF_003_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_L0_FACE_013_GEOMETRY_CROP_V1
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01_TEXT_AUTHORITY
reference_budget: 5 image inputs; outfit is text-only
aspect_ratio: 4:5 vertical
resolution: native ImageGen output retained; delivery target 2160x2700
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_003
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/3.jpg
    sha256: 01101628a46108693b724a1f9dd868841f830c9c8bde2ae7d2b25f1227aaa0ca
    responsibility: pose mechanics, friendly smile action, high camera position, close vertical frame, cruise-deck/ocean geometry
    must_not_define: owner identity/face features, body proportions, hair, outfit, hosiery, footwear, watermark/text or exact ship design
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: owner neck-below body proportions and limb scale only
    must_not_define: face, hair, clothing, hosiery material/color, pose, camera, lighting or environment
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    source_asset_id: L0_OWNER_013
    source_sha256: 1851e8decaa3430f127c3e720f7fba8bb119370008ef7795313fd6e76b396af0
    responsibility: source-derived real-person facial identity and feature geometry only
    must_not_define: source hairstyle, makeup, jewelry, skin retouch/color, source camera/lighting, body, clothing or environment
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
  - asset_id: OWNER_CASUAL_SUMMER_01
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md
    approval_record: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/APPROVAL.md
    responsibility: approved white floral lace-trim camisole, light-blue denim shorts, continuous light-nude sheer pantyhose and earrings; no shoes visible in shot 03
    must_not_define: owner identity/face/body/hair, pose, camera, lighting or background
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: post-generation face identity drift, facial-feature relationship, skin contamination/texture, projection and framing QA only; never generation input
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: body-proportion QA comparison only; never generation input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_03/candidates/SOC_TRAVEL_002_IMG_03_CAND_01/SOC_TRAVEL_002_IMG_03_CAND_01.png
seed_settings: seed/sampler not returned; native vertical output
qa_status: not_applicable_no_output
approval_status: NOT_GENERATED
```
