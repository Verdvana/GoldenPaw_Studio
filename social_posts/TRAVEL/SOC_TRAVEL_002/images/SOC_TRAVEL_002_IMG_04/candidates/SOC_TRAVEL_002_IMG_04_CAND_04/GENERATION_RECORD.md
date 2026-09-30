# Generation Record — SOC_TRAVEL_002_IMG_04_CAND_04

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_04
candidate_id: SOC_TRAVEL_002_IMG_04_CAND_04
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATED_REVIEW_REQUIRED
generation_mode: built-in ImageGen
source_lineage: independent parallel generation from approved scoped assets and L0 sources; no generated shot image input
face_generation_method: FACE_01_FRONT_NEUTRAL_METHOD.md source-derived constraints adapted to open-mouth laughter and side-seated shot
face_generation_method_spec_revision: draft_1.11
owner_l1_generation_spec_revision: draft_1.233
reference_set_ids:
  - SOC_TRAVEL_002_REF_004_POSE_ONLY_FACE_HAIR_EXCLUDED_V1
  - OWNER_L0_FACE_014_GEOMETRY_CROP_V1
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_HOS_07_INTERTOE_NAIL_DETAIL_CANON_L1
reference_budget: 5 image inputs (hard maximum); body proportions and wardrobe are text-only
aspect_ratio: "4:5 vertical"
resolution: native ImageGen output 1071x1469; target 2160x2700 not met, no stretching applied
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_004_POSE_ONLY_FACE_HAIR_EXCLUDED_V1
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/reference_inputs/REF_004_POSE_EXCLUDED_V1/REF_004_POSE_EXCLUDED.png
    sha256: 6b6c5166627ba68437cdd5de43852971d12db94c05506a39b04f72ea22a63e17
    source_asset_id: SOC_TRAVEL_002_REF_004
    source_sha256: b5e59e498f1c67e19f661c595cc68ff251bcab1484d4ca7ffda84a3a94b37034
    responsibility: seated body pose, bent/extended leg arrangement, near-hand placement, camera angle/crop and passenger-deck composition; head turn/laugh are text-specified
    must_not_define: owner identity/face/expression pixels, hair, body proportions, clothing, accessories, hosiery, footwear, exact ship design or watermark/text
  - asset_id: OWNER_FACE_L0_OWNER_014_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_014_FACE_GEOMETRY_CROP_001.png
    sha256: 4b8c56d695ab768e1820b5b8ea826282f811f2ecbce3d0a3b061bff4c793fd29
    source_asset_id: L0_OWNER_014
    source_sha256: 488c2d59dc414ddb056462f3d1158b0360ca221d93b53337d0ea2d1239b26686
    responsibility: real-source owner identity, adult age and facial-feature geometry only
    must_not_define: source hairstyle/makeup/jewelry, retouched skin, camera/light, body, clothing, pose or environment
  - asset_id: L0_OWNER_006
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg
    sha256: 734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17
    responsibility: real-source Hairstyle B construction only
    must_not_define: face identity/features/expression, body, outfit, pose, camera, light or environment
  - asset_id: OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg
    sha256: e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f
    responsibility: approved Hairstyle B appearance/color/construction only
    must_not_define: face generation/identity, skin, body, clothes, pose, camera, light or environment
  - asset_id: OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png
    sha256: 29833b2de7a2c91b822a542e42843b5902d80ce9597123dce481a9b1bb462df3
    responsibility: scoped approved 15D gray-matte foot textile diffusion, explicit intertoe tension curves and softened burgundy nails under fabric; gray color explicitly excluded for this post
    must_not_define: owner identity/body proportions, other views, pose, outfit, hosiery color for this post, lighting or background
text_only_generation_authorities:
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    responsibility: written body proportion target only (168 cm / about 60 kg, natural adult proportions); raster not supplied
    must_not_define: face generation, hair, clothing, hosiery material, pose, lighting or background
  - asset_id: OWNER_CASUAL_SUMMER_01
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md
    approval_record: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/APPROVAL.md
    responsibility: approved white floral lace-trim camisole, light-blue denim shorts, light-nude sheer pantyhose, earrings; no shoes visible
    must_not_define: owner identity/face/body/hair, pose, camera, light or background
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: after-generation owner identity/feature relationship, skin contamination/texture, projection and framing check only; never a generation input
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: after-generation body proportion comparison only; never a generation input
  - asset_id: SOC_TRAVEL_002_IMG_02_CAND_08
    path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_02/candidates/SOC_TRAVEL_002_IMG_02_CAND_08/SOC_TRAVEL_002_IMG_02_CAND_08.png
    purpose: after-generation day/camera/exposure/color continuity check only; never a character/material/design input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_04/candidates/SOC_TRAVEL_002_IMG_04_CAND_04/SOC_TRAVEL_002_IMG_04_CAND_04.png
output_sha256: f9b78e2358b241486c905d87f961a6e5306fa1c10309cb887a9841ba6dad3cf7
seed_settings: seed/sampler not returned; native output 1071x1469 RGB PNG
qa_status: REVIEW_REQUIRED_HEAD_TURN_TOO_EXTREME_AND_HOSIERY_NOT_VISIBLE
approval_status: REVIEW_REQUIRED
```

Prompt assembly is recorded in sibling `../PROMPT_ASSEMBLY.md`. The complete role-labelled prompt was assembled before generation.
