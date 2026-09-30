# Generation Record — SOC_TRAVEL_002_IMG_01_CAND_01

```yaml
post_id: SOC_TRAVEL_002
asset_id: SOC_TRAVEL_002_IMG_01
candidate_id: SOC_TRAVEL_002_IMG_01_CAND_01
character_id: CHR_HUMAN_001_OWNER
asset_level: L3
status: GENERATION_BLOCKED_SAFETY
generation_mode: built-in ImageGen
source_lineage: fresh parallel generation; no generated shot input
reference_set_ids:
  - OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE
  - OWNER_HAIRSTYLE_B_L0
  - OWNER_HAIRSTYLE_B_APPEARANCE_L1
  - OWNER_CASUAL_SUMMER_01
  - SOC_TRAVEL_002_REF_001_POSE_COMPOSITION_ENVIRONMENT
reference_budget: 5 images
aspect_ratio: 4:5 vertical
resolution: 2160x2700 delivery target; native ImageGen output retained without forced resize
generation_inputs:
  - asset_id: SOC_TRAVEL_002_REF_001
    path: social_posts/TRAVEL/SOC_TRAVEL_002/references/incoming/1.jpg
    sha256: ec907c94f64d2651346107b312ded2a670672146b840e6312113d3312b222d26
    responsibility: prone/reclined pose mechanics, visible limb placement, behind-subject camera position, centered cabin-door/ocean composition and broad cruise-cabin setting
    must_not_define: owner identity, face, body shape, hair, clothing, hosiery material, exact decor, light or color grade
  - asset_id: OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1
    path: characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png
    sha256: 59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b
    responsibility: owner neck-below body proportions and limb/foot scale
    must_not_define: face, hair, clothing, hosiery material, pose, lighting or environment
  - asset_id: L0_OWNER_006
    path: characters/CHR_HUMAN_001_OWNER/source/identity/raw/8.jpg
    sha256: 734458326895b48099efa0dc58c43646d8b104823c1c36c1def8f27d08d88c17
    responsibility: real-source Hairstyle B construction only
    must_not_define: face identity/expression, body, clothing, pose, lighting or environment
  - asset_id: OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001
    path: characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/CHR_WOMAN_001_HB04_HAIR_B.jpg
    sha256: e83de80864c158a299bc3e2042b198fe76bd9452b01a7d595a1cd0d973fd613f
    responsibility: approved Hairstyle B color/exposure and surface appearance only
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
    purpose: post-generation QA comparison only, if any face pixels are visible; never a generation input
output_path: not_created
seed_settings: unavailable; no image was produced
generation_attempts:
  - attempt: 1
    result: rejected by ImageGen output safety system
    category: sexual
    request_id: 070875cb-3615-4fc2-a084-2452bd055166
  - attempt: 2
    result: rejected by ImageGen output safety system after neutral non-sexual vacation framing
    category: sexual
    request_id: d28aa68e-43d8-4298-8403-eb173a1ba70c
qa_status: not_applicable_no_output
approval_status: REVIEW_REQUIRED
```

## Generation result

Two ImageGen calls were blocked by the output safety system under category `sexual`. No candidate image file was created, no visual QA could be performed, and no generation seed/settings were returned. Do not treat this folder as containing a candidate. Resume only after the user changes the pose/background brief enough to permit generation.

## Prompt assembly

Use case: photorealistic natural social-feed travel still.

Create exactly one 4:5 vertical photo for shot 01 of `SOC_TRAVEL_002`, with native output at the highest available quality. Input 1 defines only the pose, limb placement visible in the reference, rear-view camera position, centered vertical composition, balcony-door framing, ocean beyond and broad cruise-cabin setting. Match that arrangement closely. Recreate it independently; do not copy or continue the reference person.

Subject is the same adult woman represented by the owner assets, viewed from behind so her face is entirely out of view. Use the face-excluded body asset only for owner neck-below proportions. Use the real L0 B hair source and approved B appearance reference only for the exact B updo: compact center part/crown, smooth rearward gathering, centered vertical claw clip, compact folded hair and short upward/backward tuft. Do not reproduce the reference's long loose hair.

Wear the approved `OWNER_CASUAL_SUMMER_01` exactly: white lightweight floral lace-trim camisole with narrow straps, high-waisted light-blue denim shorts with rolled/frayed hems, continuous light-nude sheer pantyhose with restrained micro-sheen, white suede tapered one-band open-toe low mule heels, and gold-tone floral cluster earrings with blue teardrop stones. Keep hosiery continuous from waist through legs and toes; no bare hosiery gaps or plastic/rubber appearance. Do not borrow any clothing, accessories or visible body styling from input 1.

Composition: photographer behind the subject at ordinary seated/standing eye level, looking toward the open cruise-cabin balcony. Subject centered in the lower middle, on the bed in the same prone/reclined posture and visible limb arrangement as input 1. Preserve the bed foreground, open balcony doors and ocean horizon axis. Keep enough room context to read as a real cruise cabin; allow only small finish/decor differences from input 1. Face stays hidden.

Shared five-photo series look: bright late morning to midday on the same cruise ship and day; natural daylight, coherent sea/sky exposure, restrained neutral white balance, realistic moderate contrast and color, consistent modern smartphone main-camera character around 26 mm equivalent, natural sharpness, no ultra-wide distortion, no portrait-mode cutout blur, no filter. Match the framing and camera position of input 1 and adapt only the outer crop to 4:5.

No text, watermark, social-media interface, logos, extra people, extra limbs, anatomy errors, long loose hair, hairstyle A, mixed A/B hairstyle, reference person's identity/face/body/clothes, new wardrobe elements, dramatic color grade, flash, cinematic night lighting, collage or multiple panels. One photograph only. This is an L3 candidate and remains `REVIEW_REQUIRED`, never Canon by default.
