# Generation Record — SOC_TRAVEL_002_IMG_02_CAND_05

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_02
candidate_id: SOC_TRAVEL_002_IMG_02_CAND_05
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: QA_REJECTED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation from approved sources; no generated shot input
reference_set_ids:
  - SOC_TRAVEL_002_REF_002_POSE_COMPOSITION_ENVIRONMENT
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_HOS_07_INTERTOE_NAIL_DETAIL_CANON_L1
  - OWNER_CASUAL_SUMMER_01_TEXT_AUTHORITY
reference_budget: 5 image inputs; outfit is a text-only approved design authority
aspect_ratio: 4:5 vertical
resolution: 2160x2700 delivery target; native ImageGen output retained without forced resize
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_002
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/2.jpg
    sha256: 26befac678d5be83c12ea2109470415e4f683f41989559b1b04548cce4b22781
    responsibility: reclined deck-chair pose, both feet raised to rail, limb placement, camera angle, sea and deck composition
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
  - asset_id: OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hosiery_feet/approved/HOS_07_15D_GRAY_MATTE_FRONT/OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001.png
    sha256: 29833b2de7a2c91b822a542e42843b5902d80ce9597123dce481a9b1bb462df3
    responsibility: interdigital fabric tension curves and softened burgundy toenails beneath sheer hosiery only
    must_not_define: gray hosiery color, target light-nude color, owner identity/body/foot anatomy, pose, shoe design, outfit, lighting or environment
text_only_generation_authorities:
  - asset_id: OWNER_CASUAL_SUMMER_01
    path: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/OUTFIT.md
    approval_record: outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/approved/design_reference/APPROVAL.md
    responsibility: exact approved camisole, denim shorts, light-nude sheer hosiery, and white suede one-band open-toe mules; mules are removed from feet for shot 02 and placed on deck per user direction
    must_not_define: owner identity/face/body/hair, pose, lighting or background
qa_comparison_only:
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: owner proportions only
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: QA comparison only if any facial pixels become visible; never generation input
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_02/candidates/SOC_TRAVEL_002_IMG_02_CAND_05/SOC_TRAVEL_002_IMG_02_CAND_05.png
seed_settings: seed/sampler not returned; native 4:5 output
qa_status: QA_REJECTED — legs and toes read as bare; required hosiery continuity/tension is absent
approval_status: NOT_APPROVED
```


## Prompt assembly

Create one 4:5 vertical photorealistic candid daytime cruise photograph for shot 02. Use input 1 only for the reclining deck-chair pose, both feet resting on the rail, arm/leg placement, camera viewpoint and sea/deck composition; do not copy that person. Input 2 defines face-excluded owner neck-below proportions only. Inputs 3–4 define only the owner's Hairstyle B. Input 5 defines only fine hosiery tension between toes and softly diffused burgundy nail color beneath sheer fabric; explicitly ignore its gray hosiery color and lower-leg anatomy. The target light-nude hosiery color comes from the approved OWNER_CASUAL_SUMMER_01 text contract in OUTFIT.md and its approval record.

Pose: match the reference closely. Adult owner reclines in a deck chair beside the rail, upper body angled toward the sea, viewed from the side/rear. Both legs lift and extend toward the rail; place both hosiery-covered feet on the rail as the user specified. Preserve the reference camera angle, medium-wide vertical composition and relaxed arm support. Keep head turned toward the sea and face obscured. This is a casual travel snapshot.

Use Hairstyle B only: the owner's compact dark-brown gathered updo with approved center-part/crown and rear gathering. Do not copy the reference hair.

Wear the approved summer outfit: white floral lace-trim camisole with narrow straps, light-blue high-waisted denim shorts with rolled/frayed hems, continuous light-nude sheer pantyhose, and gold-tone floral cluster earrings with blue teardrop stones. Remove both white suede one-band mule heels. Place the pair casually and slightly messily on the deck floor near the chair, both shoes clearly visible and not worn. Shoe design follows the written approved outfit contract; no other footwear. No reference clothing, sunglasses, bag, food or drink props.

Pantyhose must be visibly worn as a single continuous light-nude sheer garment from hips through legs, ankles, heels, insteps and every toe. Keep the sheer layer perceptible as fine cloth over the entire surface: faint uniform micro-knit texture, softened toe contours and natural fabric tension bridging small spaces between adjacent toes. Color is pale light nude, never gray. The toenails are red-burgundy beneath the cloth: show a softly diffused red tint through fabric, never sharp bare nail plates or polish painted on top. No exposed skin gaps between toes, no bare-foot appearance, separate toe socks, toe seam, toe-cap line, opacity ring, plastic gloss or discontinuity.

Maintain the shared series look: same cruise ship/day, bright natural late-morning/midday light, consistent neutral white balance, exposure, moderate contrast, color and sharpness, modern smartphone main camera around 26 mm equivalent. Match the reference viewpoint and framing; adapt only outer crop to 4:5. Keep a plausible deck chair and ocean rail, modestly adapted. No logos, text, watermark, interface, extra people, anatomy errors, collage or multiple images. L3 candidate, REVIEW_REQUIRED, not Canon.
