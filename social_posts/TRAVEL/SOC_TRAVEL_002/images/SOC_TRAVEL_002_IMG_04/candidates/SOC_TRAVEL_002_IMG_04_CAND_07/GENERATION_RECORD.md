# Generation Record — SOC_TRAVEL_002_IMG_04_CAND_07

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_04
candidate_id: SOC_TRAVEL_002_IMG_04_CAND_07
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATED_REVIEW_REQUIRED
generation_mode: built-in ImageGen
source_lineage: independent parallel generation from approved scoped assets and L0 sources; no generated shot image input
face_generation_method: FACE_01_FRONT_NEUTRAL_METHOD.md source-derived constraints adapted to open-mouth laughter and side-seated shot
face_generation_method_spec_revision: draft_1.11
owner_l1_generation_spec_revision: draft_1.233
reference_set_ids:
  - SOC_TRAVEL_002_REF_004_POSE_ONLY_WITHOUT_IDENTITY_OR_ACCESSORIES_V2
  - OWNER_L0_FACE_014_GEOMETRY_CROP_V1
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_HOS_02_FEET_3Q_CANON_L1
reference_budget: 5 image inputs (hard maximum); body proportions and wardrobe are text-only
aspect_ratio: "4:5 vertical"
resolution: native ImageGen output 1071x1469; target 2160x2700 not met, no stretching applied
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_004_POSE_ONLY_WITHOUT_IDENTITY_OR_ACCESSORIES_V2
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/reference_inputs/REF_004_POSE_EXCLUDED_V2/REF_004_POSE_EXCLUDED.png
    sha256: 4f900b1401642898f5990a9f45e8dffdb55e698f840f01ee3bde7df470c65341
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
  - asset_id: OWNER_HOS_02_FEET_3Q_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_02_FEET_3Q/OWNER_HOS_02_FEET_3Q_CANON_001.png
    sha256: 0d0d5b55c0a33bed682465328e278b99e27de38aee472203c862aa4389ae6427
    responsibility: approved 15D light-nude velvet-matte sheer foot coverage, textile diffusion, subtle intertoe tension and softened burgundy nails beneath hosiery only
    must_not_define: owner identity/body proportions, other foot views, pose, outfit, lighting or background
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
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_04/candidates/SOC_TRAVEL_002_IMG_04_CAND_07/SOC_TRAVEL_002_IMG_04_CAND_07.png
output_sha256: ee8cbee426024df4d05e986f9e42618a369a56a3b13189c9419efe237b37beba
seed_settings: seed/sampler not returned; native output 1071x1469 RGB PNG
qa_status: REVIEW_REQUIRED_HOSIERY_NOT_VISIBLE
approval_status: REVIEW_REQUIRED
```

Prompt assembly is recorded in sibling `../PROMPT_ASSEMBLY.md`. The complete role-labelled prompt was assembled before generation.
