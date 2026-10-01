# Generation Record — SOC_TRAVEL_002_IMG_01_CAND_02

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_01
candidate_id: SOC_TRAVEL_002_IMG_01_CAND_02
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: APPROVED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation; no generated shot input
reference_set_ids:
  - SOC_TRAVEL_002_REF_001_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01
reference_budget: 3 images
aspect_ratio: 4:5 vertical
resolution: 928x1152
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_001
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/1.jpg
    sha256: ec907c94f64d2651346107b312ded2a670672146b840e6312113d3312b222d26
    responsibility: sitting pose on bed, behind-subject camera position, centered cabin-door/ocean composition and cruise-cabin balcony setting
    must_not_define: owner identity, face, body shape, hair, clothing, hosiery material, exact decor, light or color grade
  - asset_id: OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg
    sha256: e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f
    responsibility: approved Hairstyle B updo construction with claw clip
    must_not_define: face generation/identity, body, clothing, pose, lighting or environment
  - asset_id: OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE.png
    sha256: a5e35b77fc25ba5ae80d6097c1138eaeba6bd3341360733912d8598f53d119c7
    responsibility: approved summer outfit design (white lace-trim top, blue denim shorts, light-nude hosiery)
    must_not_define: identity, face, body, skin, hair, pose, lighting or background
qa_comparison_only:
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: owner neck-below proportion comparison only
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_01/candidates/SOC_TRAVEL_002_IMG_01_CAND_02/SOC_TRAVEL_002_IMG_01_CAND_02.jpg
output_sha256: 0cacc94728b0f03419ca6e18d2e8690771a707a1bf53c3a00292e60d757042e3
qa_status: USER_APPROVED — explicit user review on 2026-09-30
approval_status: APPROVED
```
