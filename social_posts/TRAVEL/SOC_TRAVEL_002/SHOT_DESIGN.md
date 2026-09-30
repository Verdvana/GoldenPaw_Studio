# Shot Design — SOC_TRAVEL_002

Five ordered L3 stills. Each shot is generated independently from approved character/outfit/hair authorities plus only that shot's pose/composition reference and the shared look contract. A prior shot may support sequence continuity only; it cannot define identity, outfit, hair, hosiery, or environment identity.

## Shared series look

- Story time: one bright late morning through midday on the same cruise ship; keep weather, sea state, daylight direction/quality and overall exposure coherent across all five photographs.
- Camera language: candid travel photos from one modern phone main camera, consistent natural perspective (about 26 mm equivalent), no ultra-wide distortion, no portrait-mode cutout blur, no filters or fake UI. Camera position changes only to match the five references.
- Delivery: vertical 4:5 social photographs, consistent natural white balance, moderate contrast, color and sharpness; preserve reference pose and camera viewpoint while reframing minimally for 4:5.
- Shared environment: same ship and voyage, ocean visible where framing permits. Cabin balcony for shot 01; open passenger deck for shots 02–05. Keep ship finishes and rail details plausible and mutually consistent without copying incidental exact ship branding or logos.
- Backgrounds may vary in small details. No readable brands, signs, user handles, watermarks or social UI.
- Wardrobe: use `OWNER_CASUAL_SUMMER_01` in every image, including its approved white floral lace-trim camisole, light-blue denim shorts, light-nude sheer hosiery and earrings. Apply these explicit shot-level footwear instructions: image 02 removes the mules from the feet and places that pair casually on the deck floor; images 03–04 are hosiery-covered barefoot with all shoes outside the frame; image 05 wears the approved white suede open-toe mule heels and shows the complete full body including both shoes. Do not borrow any reference-image clothing or accessories.
- Hosiery/feet: maintain one continuous light-nude sheer textile from legs across ankles, heels, insteps and toes in all five shots. Show natural fabric drape/tension between toes wherever the angle permits; red-burgundy toenail polish may show softly through the sheer hosiery, never painted on top. For image 02, `OWNER_HOS_07_15D_GRAY_MATTE_FRONT_CANON_001` defines only intertoe textile tension and softened nail visibility; its gray color is excluded. Target color comes from the approved outfit contract.
- Hair: `HAIRSTYLE_B` only, from its applicable approved scoped reference. The women in the five photos do not define owner hair or identity.
- Face: when visible, source-derived L0 Face method is the sole generation authority. Use approved AI Face Canon only for post-generation QA comparison.

## Ordered shots

| Order / asset ID | Pose, expression, camera and composition authority | Environment/background | Continuity note |
|---|---|---|---|
| 1 — `SOC_TRAVEL_002_IMG_01` | `1.jpg`: prone/reclining on cabin bed, viewed from behind; centered vertical framing through open balcony doors toward ocean. Keep face out of view as in reference. | Cruise cabin with balcony doors, bed foreground, sea horizon beyond; adapt cabin details to the shared ship/day. | Opening quiet cabin moment. |
| 2 — `SOC_TRAVEL_002_IMG_02` | `2.jpg`: reclined in deck chair, torso angled toward sea, legs lifted/extended with both feet resting on the rail; side/rear view and vertical medium-wide framing. Match limb placement and camera angle closely. | Passenger deck chair, rail and open sea; show the approved white mule pair casually/slightly messily placed on deck near the chair. | No shoes worn; keep continuous hosiery and red-burgundy polish softly visible through textile. Do not reproduce the reference's clothing, face or skin treatment. |
| 3 — `SOC_TRAVEL_002_IMG_03` | `3.jpg`: low seated/crouched pose on deck, knees bent, hands near legs, friendly smile toward camera; high camera angle and close vertical framing. | Glass or reflective deck surface with ocean/rail geometry; remove watermark and all overlay text. | Hosiery-covered bare feet; no shoes visible anywhere in frame. Match smile and pose without borrowing facial features, hair or body shape. |
| 4 — `SOC_TRAVEL_002_IMG_04` | `4.jpg`: side-seated on a lounger, torso/head turned back toward camera, open-mouth laugh; preserve bent/extended leg arrangement, side angle and crop. | Cruise deck lounger and passenger-deck structures, simplified to match the same ship. | Hosiery-covered bare feet; no shoes visible anywhere in frame. Keep the expression lively; harmonize reference's stronger sunlight with the shared daylight treatment. |
| 5 — `SOC_TRAVEL_002_IMG_05` | `5.jpg`: standing at the rail with both arms extended along it, head turned toward sea; centered vertical full-body framing and camera distance. | Same open deck and sea, with consistent rail design and daylight. | Wear approved white suede mule heels; include complete head-to-toe body and both shoes with margin below feet. Preserve one-day continuity. |

## Per-shot generation gate

Before each ImageGen call, create that shot's candidate directory and complete generation record, reference plan, prompt assembly and QA template. Include separate `generation_inputs` and `qa_comparison_only` lists, checksums, asset versions, reference responsibilities/exclusions, reference budget, output path and available settings. The pose reference is permitted only for its listed pose/expression/camera/composition duties. No generated shot is a generation input to another shot.
