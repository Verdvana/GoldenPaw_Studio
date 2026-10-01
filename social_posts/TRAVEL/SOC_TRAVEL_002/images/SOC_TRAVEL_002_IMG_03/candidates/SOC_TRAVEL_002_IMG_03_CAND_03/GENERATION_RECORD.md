# Generation Record — SOC_TRAVEL_002_IMG_03_CAND_03

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_03
candidate_id: SOC_TRAVEL_002_IMG_03_CAND_03
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATED_REVIEW_REQUIRED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from scoped L0 sources; no generated shot input
face_generation_method: FACE_01_FRONT_NEUTRAL_METHOD.md prompt constraints adapted to high-angle smile; sole face authority is L0 face crop
face_generation_method_spec_revision: draft_1.11
reference_set_ids:
  - SOC_TRAVEL_002_REF_003_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_L0_FACE_013_GEOMETRY_CROP_V1
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01_TEXT_AUTHORITY
reference_budget: 3 image inputs
aspect_ratio: 4:5 vertical
resolution: 928x1152
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_003
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/3.jpg
    sha256: 01101628a46108693b724a1f9dd868841f830c9c8bde2ae7d2b25f1227aaa0ca
    responsibility: pose mechanics, friendly smile action, high camera position, close vertical crop, cruise deck/ocean composition
    must_not_define: identity/face features, body proportions, hair, outfit, hosiery, footwear, watermark/text or exact ship design
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    responsibility: real-source facial identity, feature geometry and natural smile expression only
    must_not_define: source hairstyle, makeup, jewelry, skin retouch, camera, body, clothing or environment
  - asset_id: OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg
    sha256: e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f
    responsibility: approved B design, claw clip updo construction and hair appearance only
    must_not_define: face generation/identity, body, clothing, pose, camera, lighting or environment
text_only_generation_authorities:
  - asset_id: OWNER_CASUAL_SUMMER_01
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md
    responsibility: approved white floral lace-trim camisole, light-blue denim shorts, light-nude sheer pantyhose; no shoes visible
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: post-generation face identity drift, facial-feature relationship, skin contamination QA comparison only; never generation input
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: body-proportion QA comparison only; never generation input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_03/candidates/SOC_TRAVEL_002_IMG_03_CAND_03/SOC_TRAVEL_002_IMG_03_CAND_03.jpg
output_sha256: 5159557b16857c1849609edf90f1aecfadff8db242e32f09622931e8acb6074c
qa_status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
```
