# Social Post Prompt Assembly / Generation Record

- post_id: SOC_DATE_001
- image_asset_id: SOC_DATE_001_IMG_01
- candidate_id: SOC_DATE_001_IMG_01_CAND_01
- model/tool: built-in image_gen
- status: GENERATED; QA FAIL; REVIEW_REQUIRED
- generation_inputs / qa_comparison_only / settings / output: candidates/SOC_DATE_001_IMG_01_CAND_01/GENERATION_RECORD.json
- reference_plan: REFERENCE_PLAN.md
- prompt constraints: applicable Face method identity/skin/hair constraints; studio pose, lighting, Calibration Outfit and lens/framing are L1-only and not inherited into L3.

## Final assembled prompt

Use case: photorealistic-natural.
Create ONE candid lifestyle photograph for a summer date social carousel, portrait 4:5. A real adult woman, same identity as reference 1, caught in a small ongoing moment outside a neighborhood cafe on a summer afternoon. Someone walking slightly ahead has just called her; she is taking a short ordinary step, head turning gently toward the photographer, lips in a very small spontaneous smile, shoulders and hands relaxed and asymmetric. Do not make her stop for a fashion pose. No hip-pop, model crossed legs, hand on waist, staged hair touching, exaggerated turn or runway stride.
Camera: handheld companion snapshot, approximately 45–50mm equivalent from conversational distance far enough to include full body, camera at upper torso height with natural perspective. Frame is actually tilted approximately 5 degrees so cafe door jambs and pavement lines are oblique, off-axis and off-center, a little extra environment on one side and uneven headroom. No perspective correction, perfectly level horizon, straight architectural elevation, symmetry or centered catalog layout. Keep both complete shoes inside frame with ground margin. Tiny natural movement in sleeve/hair, face remains readable. Ordinary moderate depth of field with recognizable lived-in surroundings, no glamour blur.
Reference duties, strict:
1 face-only real-source crop: identity and exact facial-feature relationships ONLY. Preserve forehead/eyes/eyelids/eye spacing/brows/nose/cheeks/lips/jaw/chin relationships and natural face width. No face slimming, widening, V-line, enlarged eyes, sharpened jaw, pointed chin, age change or generic beauty replacement. Exclude its makeup, retouch, hair, jewelry, light and background.
2 real-source skin crop: warm-neutral natural skin hue/depth/texture baseline ONLY; not geometry, hairstyle or camera. No whitening, pink cast, muddy patches, smudges, bright/dark facial blotches, plastic smoothing.
3 face-masked real Hairstyle A reference: hair ONLY, long straight loose dark-brown hair, near-center imperfect part, flat close-to-scalp roots and low crown, restrained density, fine strand groups, tapered wispy ends. Mask is missing information. Exclude clothing, body, face, background, source lighting/color cast. No hairstyle B or blended hairstyle.
4 neck-below face-excluded body derivative: anatomical proportions and limb scale ONLY, adult 168cm/60kg target, natural waist/hips/thigh widths. Do not inherit its static pose, swimsuit, nude hosiery, skin color, hair, lighting or backdrop. It has no face-generation authority.
5 approved clothing-only design v003: garment design, colors, layering and hosiery coverage ONLY; no identity, anatomy, skin, pose, lighting, backdrop. Match the white broad shallow round neckline, opaque fully lined chest, under-bust cropped hem, long translucent chiffon sleeves and cuffs; normal regular mid-rise light-blue washed cuffed denim shorts. White semitransparent HIGH-WAIST closed-toe pantyhose worn beneath shorts, waistband substantially above shorts, above navel near cropped blouse hem; visible abdominal region remains covered in white sheer fabric, not a bare stomach and not an opaque corset. Silver thin ankle and toe-strap OPEN-TOE STILETTO high-heeled sandals over the hosiery. Continuous same white sheer textile from abdomen/waist through hips/thighs/knees/calves/ankles/heels/insteps and every toe; toe openings of sandals still contain fully fabric-covered toes. Subtle burgundy toenails only naturally visible beneath fabric. No stockings, bare toes, latex, plastic, liquid coating or painted skin. Do not invent exact denier.
Scene: small cafe entrance, warm cream plaster, a dark wood door, a couple of casual outdoor chairs and modest green plants, ordinary sidewalk; no prominent lettering. Soft open summer daylight with coherent shadows, white clothing retains fabric detail. A believable everyday street snapshot with slightly imperfect timing and relaxed energy. No text overlay, logo, watermark, fake UI, collage, extra panels or other featured people. Generate one finished photo.


## Generation result

Built-in image_gen; seed unavailable. Actual 1122×1402 near 4:5. Output and SHA-256 in candidate GENERATION_RECORD.json; QA: qa/QA.md.
