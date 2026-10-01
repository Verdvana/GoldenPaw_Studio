# Generation Record — SOC_TRAVEL_002_IMG_03_CAND_04

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_03
candidate_id: SOC_TRAVEL_002_IMG_03_CAND_04
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATED_REVIEW_REQUIRED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from scoped L0 sources; no generated shot input
face_generation_method: FACE_01_FRONT_NEUTRAL_METHOD.md prompt constraints adapted to high-angle smile; sole face authority is L0 face crop
face_generation_method_spec_revision: draft_1.11
reference_set_ids:
  - SOC_TRAVEL_002_REF_003_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_L0_FACE_013_GEOMETRY_CROP_V1
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_HOS_02_FEET_3Q_CANON_L1
  - OWNER_CASUAL_SUMMER_01_TEXT_AUTHORITY
reference_budget: 3 image inputs
aspect_ratio: 4:5 vertical
resolution: 928x1152
user_feedback_addressed:
  - full-body vertical framing showing feet resting on glass deck
  - hosiery material fidelity (15D light-nude sheer textile, soft sheen, intertoe fabric tension)
  - burgundy toenail polish softly diffused beneath sheer nude textile
  - faithful owner face and body proportion rendering
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_003
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/3.jpg
    sha256: 01101628a46108693b724a1f9dd868841f830c9c8bde2ae7d2b25f1227aaa0ca
    responsibility: pose mechanics, friendly smile action, high camera position, vertical crop, cruise deck/ocean composition
    must_not_define: identity/face features, body proportions, hair, outfit, hosiery, footwear, watermark/text or exact ship design
  - asset_id: OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/reference_inputs/L0_FACE_SOURCE_DERIVATIVES_V1/FACE_L0_OWNER_013_FACE_GEOMETRY_CROP_001.png
    sha256: 1c6ad34c3f51c2d9fae4d69630a54af50f6629cd9def55e0caca2a8234193e91
    responsibility: real-source facial identity, feature geometry and natural smile expression only
    must_not_define: source hairstyle, makeup, jewelry, skin retouch, camera, body, clothing or environment
  - asset_id: OWNER_HOS_02_FEET_3Q_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_02_FEET_3Q/OWNER_HOS_02_FEET_3Q_CANON_001.png
    sha256: 0d0d5b55c0a33bed682465328e278b99e27de38aee472203c862aa4389ae6427
    responsibility: 15D light-nude sheer foot coverage, soft textile sheen, intertoe tension and diffused burgundy toenails under sheer cloth only
    must_not_define: owner identity, body proportions, other foot angles, clothing or background
text_only_generation_authorities:
  - asset_id: OWNER_CASUAL_SUMMER_01
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md
    responsibility: approved white floral lace-trim camisole, light-blue denim shorts, continuous light-nude sheer pantyhose; no shoes visible in shot 03
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: post-generation face identity drift, facial-feature relationship, skin contamination QA comparison only; never generation input
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: body-proportion QA comparison only; never generation input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_03/candidates/SOC_TRAVEL_002_IMG_03_CAND_04/SOC_TRAVEL_002_IMG_03_CAND_04.jpg
output_sha256: 0ffff9132c000f045b536d79c46d4f4f2011f36aca9457057429893735ada556
qa_status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
```
