# Generation Record — SOC_TRAVEL_002_IMG_02_CAND_08

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_02
candidate_id: SOC_TRAVEL_002_IMG_02_CAND_08
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: APPROVED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from approved sources; no generated shot input
reference_set_ids:
  - SOC_TRAVEL_002_REF_002_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_HOS_07_INTERTOE_NAIL_DETAIL_CANON_L1
  - OWNER_CASUAL_SUMMER_01_TEXT_AUTHORITY
reference_budget: 5 image inputs; shoes use approved outfit text authority
aspect_ratio: 4:5 vertical
resolution: native ImageGen output retained without forced resize
user_approved_composition_direction: subject and lounger on the right, sea fills the left, low table with simple food and drink in the foreground, shoes on deck; CAND_06 is not a generation input
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
  - asset_id: OWNER_HOS_07_INTERTOE_NAIL_DETAIL_CANON_L1
    path: characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png
    sha256: 29833b2de7a2c91b822a542e42843b5902d80ce9597123dce481a9b1bb462df3
    responsibility: intertoe fabric tension and softened burgundy toenails under sheer textile only
    must_not_define: gray hosiery color, owner identity/body/foot anatomy, pose, footwear, lighting or environment
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
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_02/candidates/SOC_TRAVEL_002_IMG_02_CAND_08/SOC_TRAVEL_002_IMG_02_CAND_08.png
seed_settings: seed/sampler not returned; native 4:5 output
qa_status: USER_APPROVED — explicit user review on 2026-09-30
approval_status: APPROVED
```

## Prompt assembly

Use case: photorealistic-natural. Asset type: one vertical L3 candid social photograph, shot 02 of the same cruise-day series. Input 1 defines only the deck-chair pose, both feet on the rail, arm/leg placement, side/rear camera and sea/deck composition; do not copy that person. Input 2 defines owner neck-below proportions only. Inputs 3–4 define Hairstyle B only. Input 5 defines only sheer intertoe textile tension and softly diffused burgundy nails; ignore its gray color. The white suede shoe shape/material is specified by the approved OWNER_CASUAL_SUMMER_01 outfit contract.

Create a fresh candid daytime cruise photo. Compose the reclined woman and chair on the right half, with open ocean filling the left and a low round deck table in the left foreground. Match input 1's chair recline, side/rear camera and both feet resting on the rail. Keep the face turned away/obscured. The adult owner wears the approved white floral lace-trim camisole, light-blue high-waisted denim shorts, continuous sheer light-nude pantyhose, and approved earrings. She wears no shoes. Place exactly the approved pair of white suede one-band open-toe low mule heels on the deck near the chair, casually/messily arranged, both clearly visible, separated and slightly askew. Shoe construction: one tapered, non-uniform white suede vamp strap per shoe, open toe, low slim heel; no ankle strap, slingback, multiple bands, platform, wedge, block heel, buckle or ornament.

Hosiery is one continuous fine sheer textile from hips to every toe, with light-nude color and restrained micro-sheen. Show the hosiery layer on each whole leg and foot; natural relaxed feet, anatomically normal ankles, heel, instep and toe lengths, five distinct toes per foot, toes gently aligned rather than twisted, merged, pinched or unnaturally splayed. Show subtle fabric tension bridging the spaces between toes. Burgundy-red toenails show softly beneath the cloth, never as sharp bare nail plates or polish painted on top. Match the user's liked cruise composition: a simple small plate of fruit/pastry and one clear drink on the foreground table, no other clutter. Same bright late-morning/midday ship/daylight, neutral white balance, exposure, moderate contrast, color and sharpness as the series; modern phone main camera around 26 mm equivalent, natural perspective, no ultra-wide distortion or portrait-mode blur. Vertical 4:5 medium-wide framing. Background can vary slightly while remaining a plausible passenger deck and ocean rail. No logos, text, watermark, extra people, anatomy errors, collage or multiple images. Do not use any generated candidate as an input. L3 candidate, REVIEW_REQUIRED, not Canon.
