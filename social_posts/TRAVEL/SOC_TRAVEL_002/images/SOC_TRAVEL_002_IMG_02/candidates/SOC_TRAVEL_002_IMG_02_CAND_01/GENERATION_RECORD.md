# Generation Record — SOC_TRAVEL_002_IMG_02_CAND_01

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_02
candidate_id: SOC_TRAVEL_002_IMG_02_CAND_01
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: QA_REJECTED
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation; no generated shot input
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01
  - SOC_TRAVEL_002_REF_002_POSE_COMPOSITION_ENVIRONMENT
reference_budget: 5 images
aspect_ratio: 4:5 vertical
resolution: 2160x2700 delivery target; native ImageGen output retained without forced resize
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_002
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/2.jpg
    sha256: 26befac678d5be83c12ea2109470415e4f683f41989559b1b04548cce4b22781
    responsibility: reclined deck-chair pose, visible limb placement, side/rear camera position, ocean and rail composition, broad cruise-deck setting
    must_not_define: owner identity/face/body shape/hair/clothing/hosiery, exact ship design, food/drink branding, text/watermark
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: owner neck-below proportions and limb/foot scale
    must_not_define: face, hair, clothing, hosiery material, pose, lighting or environment
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
    responsibility: approved summer outfit design and material/color intent
    must_not_define: identity, face, body, skin, hair, pose, lighting or background
qa_comparison_only:
  - asset_id: OWNER_BODY_01_FRONT_CANON_007
    path: characters/CHR_HUMAN_001_OWNER/canon/body/approved/BODY_01_FRONT/OWNER_BODY_01_FRONT_CANON_007.png
    purpose: owner neck-below proportion comparison only
  - asset_id: OWNER_FACE_01_FRONT_NEUTRAL_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/face/approved/FACE_01_FRONT_NEUTRAL/OWNER_FACE_01_FRONT_NEUTRAL_CANON_001.jpg
    purpose: post-generation identity/contamination QA comparison only if facial pixels become visible; never a generation input
original_candidate_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_02/candidates/SOC_TRAVEL_002_IMG_02_CAND_01/SOC_TRAVEL_002_IMG_02_CAND_01.png
output_path: social_posts/TRAVEL/SOC_TRAVEL_002/images/SOC_TRAVEL_002_IMG_02/candidates/SOC_TRAVEL_002_IMG_02_CAND_01/SOC_TRAVEL_002_IMG_02_CAND_01.png
output_checksum_sha256: 335d1be95c444b0764e894935a2971c6728f0d042559e6f141d498e1d00eb9ce
output_dimensions: 1122x1402
seed_settings: seed/sampler not returned; native 4:5 output
qa_status: QA_REJECTED — hosiery/toe textile continuity is not visibly supported; do not use this candidate as a downstream reference
approval_status: REJECTED_BY_QA
```

## Prompt assembly

Create exactly one 4:5 vertical, photorealistic candid vacation photograph for shot 02 of `SOC_TRAVEL_002`. Use these inputs only within their listed roles: Image 1 defines reclining pose, limb placement, camera angle/framing and broad cruise-deck/ocean composition; Image 2 defines face-excluded owner neck-below proportions; Images 3–4 define Hairstyle B only; Image 5 defines the approved summer outfit only. The person in Image 1 is not the owner and must not define identity, face, body proportions, hair, clothing or hosiery.

Pose and composition: match Image 1 closely. The adult owner reclines naturally in a deck chair beside the rail, upper body turned toward the sea and away from camera; preserve the reference's raised/extended leg arrangement, bent-leg relationship, arm support, side/rear orientation and medium-wide vertical camera angle. Keep the face turned away and obscured by the rear/side view, with no distinct facial features. Do not emphasize any body area; this is an ordinary relaxed travel snapshot.

Hair: HAIRSTYLE_B only, with the owner's approved compact gathered-updo silhouette, center-part/crown logic, dark-brown color and controlled face-framing strands appropriate to the view. Do not copy the reference model's hairstyle.

Wardrobe: use `OWNER_CASUAL_SUMMER_01` exactly: white floral lace-trim narrow-strap camisole, high-waisted light-blue denim shorts with rolled/frayed hems, continuous light-nude sheer pantyhose with restrained micro-sheen, white suede one-band open-toe low mule heels, and gold-tone floral cluster earrings with blue teardrop stones. Keep the same shoes and hosiery even though the pose reference shows bare feet. Hosiery remains one continuous textile through feet and toes; no plastic/rubber finish. Copy no reference clothing, sunglasses, handbag, food, drinks or accessories.

Setting and light: same passenger deck and ocean on the same bright late-morning/midday cruise day as the rest of this carousel. Keep a plausible deck chair and coherent rail/ocean layout; ship details may differ modestly. Maintain the shared modern smartphone main-camera look around 26 mm equivalent, natural daylight, neutral white balance, moderate contrast, consistent color and sharpness. Match Image 1's camera position and framing, adapt only outer crop for 4:5. No ultra-wide distortion, filters, portrait cutout blur, logos, readable labels, text, watermark, social UI, extra people, collage or multiple frames.

Output one candidate only. `REVIEW_REQUIRED`; L3 shot, not Canon.
