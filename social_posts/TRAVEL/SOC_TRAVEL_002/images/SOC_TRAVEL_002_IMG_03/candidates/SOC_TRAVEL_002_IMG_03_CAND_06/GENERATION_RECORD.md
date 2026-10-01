# Generation Record — SOC_TRAVEL_002_IMG_03_CAND_06

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_03
candidate_id: SOC_TRAVEL_002_IMG_03_CAND_06
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATED_REVIEW_REQUIRED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from registered owner assets and L0 face/body sources; pose reference strictly restricted to pose/environment
reference_set_ids:
  - SOC_TRAVEL_002_REF_003_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_BODY_01_FRONT_CANON_007
  - OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE
reference_budget: 3 image inputs
aspect_ratio: 4:5 vertical
resolution: 928x1152
user_feedback_addressed:
  - strict body proportion matching to registered Body Canon OWNER_BODY_01_FRONT_CANON_007 (168 cm, 60 kg real adult build, natural waist/hips/thighs)
  - strict face identity matching to owner real identity photos / Body Canon face (round face shape, single eyelids, gentle expression)
  - top corrected to strictly SLEEVELESS spaghetti-strap camisole (no sleeves, no cap sleeves, bare upper arms)
  - full-body vertical framing with bare feet in pantyhose resting on glass deck floor
  - continuous 15D light-nude sheer pantyhose with intertoe fabric tension and muted burgundy toenail polish beneath cloth
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_003
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/3.jpg
    sha256: 01101628a46108693b724a1f9dd868841f830c9c8bde2ae7d2b25f1227aaa0ca
    responsibility: pose mechanics, high camera position, vertical crop, cruise deck/ocean composition ONLY
    must_not_define: identity/face features, body proportions, hair, outfit, hosiery, footwear, watermark/text or exact ship design
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    sha256: 078e87d6affaad080dd59e61ac0e5e16674dc8d2777133bc43a543e39703ba4a
    responsibility: real owner face identity (round face shape, single eyelids, gentle smile) and 168 cm / 60 kg real adult woman body build
    must_not_define: pose, clothing, background
  - asset_id: OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE.png
    sha256: a5e35b77fc25ba5ae80d6097c1138eaeba6bd3341360733912d8598f53d119c7
    responsibility: approved white V-neck floral camisole top with thin lace trim and thin spaghetti straps (strictly SLEEVELESS), denim shorts, 15D nude hosiery
    must_not_define: owner identity, body shape, pose, background
qa_comparison_only:
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: post-generation face identity QA comparison only; never generation input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_03/candidates/SOC_TRAVEL_002_IMG_03_CAND_06/SOC_TRAVEL_002_IMG_03_CAND_06.jpg
output_sha256: 2e811712dcc1292fc3291b04e5cea21ecb422199fe3f43e45ff96855471b8e28
qa_status: REVIEW_REQUIRED
approval_status: REVIEW_REQUIRED
```
