# Prompt Assembly / Generation Record — IMG_02 Candidate 12

- post_id: `SOC_OUTFIT_002`
- image_asset_id: `SOC_OUTFIT_002_IMG_02`
- candidate_id: `SOC_OUTFIT_002_IMG_02_CAND_12`
- model/tool: OpenAI ImageGen (via image-generator subagent)
- status: GENERATION_BLOCKED_QUOTA_EXHAUSTED
- user_direction: "广角畸变再大胆一些；发型再蓬松有空气感一点；脚趾处体现连续袜面张力而非脚趾根根分明；镜子构图打破居中死板、更自然随意倾斜；完全遮脸"
- generation_inputs:
  - `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` (neck-below body proportions, leg and arm anatomy)
  - `OWNER_HAIR_A_01_FRONT_CANON_001` (Hair A dark-brown hair, styled with softer volume and airy texture)
  - `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE` (garment design: chocolate-brown blazer, ivory ribbed knit, pleated mini skirt)
  - `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` (continuous soft-white matte hosiery with smooth fabric tension over toes, plush mule fit)
- qa_comparison_only: none (face completely occluded by phone)
- output: none (blocked by upstream API quota exhaustion)
- QA: `social_posts/OUTFIT_DETAIL/SOC_OUTFIT_002/images/SOC_OUTFIT_002_IMG_02/qa/QA_CAND_12.md`
- planned_aspect_ratio: 4:5 vertical portrait
- error_note: 429 RESOURCE_EXHAUSTED on gemini-3.1-flash-image

## Assembled Generation Prompt

```text
A spontaneous, stylish vertical 4:5 snapshot capturing a viral aesthetic street selfie taken in a round orange-framed convex road-safety traffic mirror along a winding park lane in late autumn. The overall framing is casual, dynamic, and organic: the large round convex mirror is positioned slightly off-center with a subtle natural angle, surrounded organically by golden-yellow ginkgo and red maple foliage catching warm dappled sunlight.

Inside the convex mirror reflection, there is an intense, bold, dramatic spherical fisheye wide-angle optical curvature:
- The entire reflected scene curves aggressively along the spherical mirror face: tall autumn trees with brilliant golden leaves warp into a dramatic arched dome around the mirror edges, and the curved asphalt road strewn with golden leaves curves in a massive, sweeping spherical arc across the bottom.
- Standing far below the high-mounted mirror in the lower section of the reflection, a young woman is taking a playful, spirited mirror selfie.
- Pose and Upward Angle: She leans back slightly, looking up towards the overhead mirror, raising her modern smartphone high in front of her face with both hands or one hand, cleanly and completely covering her entire face from view. Her other hand playfully flashes a cute peace sign (V-sign) beside her head. She stands with a charming, relaxed posture: one hip slightly shifted, one leg straight and the other knee playfully bent inward in a cute casual stance. Her legs are anatomically shapely, slender, and natural.
- Hair (Airy & Voluminous): Long straight dark-brown hair (Hair A) styled with natural volume and soft airy crown texture, flowing fluffily over her shoulders and blazer rather than flat or plastered down.
- Outfit (Autumn 02): Tailored dark chocolate-brown wool blazer with clean lapels, worn open over a fitted ivory fine-ribbed high-neck knit sweater, paired with a high-waisted dark chocolate-brown pleated mini skirt with crisp vertical pleats.
- Hosiery & Footwear (CRITICAL - Smooth Fabric Tension): Continuous, medium-thick soft-white matte opaque pantyhose covers her legs smoothly from under the skirt down through the ankles, heels, insteps, and all the way over her toes. On her feet are cream-ivory fuzzy plush open-toe platform mule slippers. Crucially, at the open front of the slippers, her toes are cleanly encased inside the taut, smooth white matte fabric—showing gentle, continuous fabric surface tension across all toes together with a soft rounded outline, NOT glove-like individually separated toes, absolutely zero bare skin, no exposed toes, no breaks or seams.

Vibrant autumn daylight with rich golden tones, bold fisheye convex mirror optics, candid lifestyle travel snapshot aesthetic. No text, logos, watermark, fake UI overlays, or anatomical artifacts.
```
