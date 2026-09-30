# Generation Record — SOC_TRAVEL_002_IMG_02_CAND_07

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_02
candidate_id: SOC_TRAVEL_002_IMG_02_CAND_07
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: REVIEW_REQUIRED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from approved sources; no generated shot input
reference_set_ids:
  - SOC_TRAVEL_002_REF_002_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE
  - OWNER_CASUAL_SUMMER_01_TEXT_AUTHORITY
reference_budget: 5 image inputs; outfit footwear authority is scoped to shoe design; outfit text authority remains hosiery and wardrobe contract
aspect_ratio: 4:5 vertical
resolution: native ImageGen output retained without forced resize
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_002
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/2.jpg
    sha256: 26befac678d5be83c12ea2109470415e4f683f41989559b1b04548cce4b22781
    responsibility: reclined deck-chair pose, feet on rail, limb placement, side/rear camera angle, sea/deck composition
    must_not_define: owner identity/face/body shape/hair/clothing/hosiery, shoe design or placement, exact ship design, branding/text
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: owner neck-below body proportions and limb/foot scale
    must_not_define: face, hair, outfit, hosiery material, pose, lighting or environment
  - asset_id: L0_OWNER_006
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg
    sha256: 734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17
    responsibility: real-source Hairstyle B construction only
    must_not_define: face identity/expression, body, clothing, pose, lighting or environment
  - asset_id: OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg
    sha256: e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f
    responsibility: approved B design/color/exposure and surface appearance only
    must_not_define: face generation/identity, body, clothing, pose, lighting or environment
  - asset_id: OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE.png
    sha256: a5e35b77fc25ba5ae80d6097c1138eaeba6bd3341360733912d8598f53d119c7
    responsibility: exact approved white suede tapered/non-uniform single vamp strap, open toe, low slim mule heel; shoe shape and material only
    must_not_define: owner identity/face/body/skin/hair, hosiery color, pose, lighting or environment
text_only_generation_authorities:
  - asset_id: OWNER_CASUAL_SUMMER_01
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md
    approval_record: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/APPROVAL.md
    responsibility: exact approved camisole, denim shorts, light-nude sheer hosiery, earrings; shoes removed and pair casually/messily placed on deck for shot 02
    must_not_define: owner identity/face/body/hair, pose, lighting or background
qa_comparison_only:
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: owner proportions only
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: QA comparison only if facial pixels are unexpectedly visible; never generation input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_02/candidates/SOC_TRAVEL_002_IMG_02_CAND_07/SOC_TRAVEL_002_IMG_02_CAND_07.png
seed_settings: seed/sampler not returned; native 4:5 output
qa_status: REVIEW_REQUIRED — shoe form improved; hosiery intertoe tension requires user review
approval_status: REVIEW_REQUIRED
```

## Prompt assembly

Use case: photorealistic-natural. Asset type: one vertical L3 candid social photograph, shot 02 of the same cruise-day series. Input 1 defines only the deck-chair pose, both feet on the rail, arm/leg placement, side/rear camera and sea/deck composition; do not copy that person. Input 2 defines owner neck-below proportions only. Inputs 3–4 define Hairstyle B only. Input 5 defines only the exact approved white suede mule silhouette and finish: open toe; one tapered, non-uniform vamp band; low, slim heel; no ankle strap, slingback, platform, wedge, block heel, multiple straps, buckle or ornament. Follow outfit text for all garments and light-nude hosiery.

Create a fresh candid daytime cruise photo. Adult owner reclines in a deck chair beside the rail, upper body angled toward the sea, side/rear view. Both hosiery-covered feet rest on the rail, following input 1 closely. Keep the face turned away/obscured. She wears the approved white floral lace-trim camisole, light-blue high-waisted denim shorts, continuous sheer light-nude pantyhose, and approved earrings. She wears no shoes. Place exactly the approved pair of white suede one-band open-toe low mule heels on the deck near the chair, casually and slightly messily, both clearly visible, separated and slightly askew rather than neatly paired. The two shoes must match each other and the approved shoe reference exactly in the single tapered/non-uniform vamp band, open toe, low slim heel and matte white suede. Do not invent an alternate shoe silhouette.

Hosiery is one continuous fine sheer textile from hips to every toe, with light-nude color, restrained micro-sheen, visible soft textile coverage over feet and natural tension bridging the small spaces between toes. The sheer layer must be visibly present across the full legs and every toe, not bare skin; toenails are burgundy/red beneath the cloth, softly diffused; no bare nail plates or polish painted on top. Same bright late-morning/midday ship/daylight, neutral white balance, exposure, moderate contrast, color and sharpness as the series; modern phone main camera around 26 mm equivalent, natural perspective, no ultra-wide distortion or portrait-mode blur. Vertical 4:5 medium-wide framing, preserve the pose/camera viewpoint. Background can vary slightly while remaining a plausible passenger deck and ocean rail. Deck is empty except for the chair and the two shoes: no food, drinks, cups, bottles, dishes, fruit, bags or loose props. No logos, text, watermark, extra people, anatomy errors, collage or multiple images. Do not use any generated candidate as an input. L3 candidate, REVIEW_REQUIRED, not Canon.
