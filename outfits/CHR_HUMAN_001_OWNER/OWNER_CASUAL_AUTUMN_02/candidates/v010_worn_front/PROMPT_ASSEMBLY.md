# Prompt Assembly — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v010

- model/tool: built-in ImageGen
- status: `READY_FOR_SINGLE_GENERATION`
- generation_inputs: five scoped references listed in `generation_record.md`
- qa_comparison_only: approved Face, Hairstyle-A-front and Body Canons; post-generation only
- face_generation_rule: L0-derived face geometry + `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; no AI Canon is a generation input

## Final assembled prompt

Use case: photorealistic-natural. Create one independent L2 full-body worn-front
fashion photograph in exact 3:4 portrait framing. Show the entire head, complete hair
silhouette, both legs and both slippers, with clear space around the feet. The owner
faces the camera in a relaxed, balanced neutral standing pose against a plain neutral
light-gray studio background.

Face and hair: generate the owner's recognizable face only from the supplied L0-derived
face-geometry crop and the approved `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1` constraints.
Translate the source's slight three-quarter crop into a neutral front projection,
preserving natural face width and the exact relationships of forehead, eyelids, eye
spacing and shape, nose, cheeks, lips, jaw and rounded chin. Keep natural warm-neutral
skin and texture. No beautification, face slimming, V-line shaping, enlarged eyes,
refined/narrowed nose, sharpened jaw, pointed chin, whitening, cooling, smoothing,
blotches or relighting contamination. Do not use any AI Face/Body Canon or previous
candidate as an image input.

Reproduce Hairstyle A from the masked L0 `DSC00847` hair derivative alone: very flat
roots close to the scalp, narrow low crown, naturally imperfect near-center part with
the front flow apex slightly image-left of center, long straight loose dark-brown
lengths extending below the chest, fine separated strand groups, slim face-framing
locks, modest asymmetry and tapered slightly uneven ends. Keep the two front panels
unequal as in the source; do not make a perfectly symmetric curtain. Hair remains
loose over both blazer shoulders, not tucked behind ears, tied, clipped, pinned,
curled, waved, swept back, half-up or in a ponytail. No dome-shaped crown or thick
blowout volume. Use a neutral frontal projection with a visually level head and face.

Use the face-excluded body derivative only for accepted neck-below body proportions,
stature and natural limb volume. Preserve the registered body proportions without
slimming or reshaping. Feet together and parallel; thighs, knees and calves aligned
naturally close and touching where they meet; straight parallel shins, ankles close,
heels together, toes forward. No O-shaped bowing, no outward knee/ankle deviation and
no stance-induced calf gap.

Dress the figure in the approved autumn outfit design: dark chocolate tailored blazer
with notched lapels and long sleeves; fitted ivory fine-ribbed high-neck knit; dark
chocolate high-waisted mini skirt with distinct crisp pleats. Make the legwear
medium-thick matte white pantyhose, visibly white and opaque across the legs, with a
continuous textile surface from waist/hips over thighs, knees, calves, ankles, heels,
instep, forefoot and toes. Show realistic smooth hosiery tension stretched over both
calves, ankles, insteps and toes, with natural taut contour and fine fabric texture.
Only the very tips of the covered toes may show a faint hint of skin through the
textile; all toes remain covered and the hosiery is continuous. No bare toe, cutout,
seam gap, transparency over legs, glossy plastic, latex, rubber, wet sheen or body
paint.

Add cream ivory plush fuzzy open-toe mule slippers, guided by the user-provided Photo
2 only for the plush upper and toe-opening interface. The slippers have a restrained,
clearly visible approximately 3 cm thick light-colored sole, not a high platform.
Keep covered hosiery toes visible through the opening, with slight translucency only
at their tips. Sole thickness is specified by the latest user text; the reference
images do not define it.

Soft even neutral studio lighting, realistic natural skin and textile texture, sharp
readable clothing and footwear construction, no props, jewelry, logos, text,
watermark, extra people or extra limbs. Generate one candidate only. This is an L2
review candidate, not Canon.

## Generation settings/result

- generated_at: `2026-10-17`
- seed/settings: `not exposed by ImageGen`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02/candidates/v010_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v010.png`
- output_checksum: `345592b5cb475a21808e0524dcf126f52ded9f04ac11dc28a08c4d59286c2792`
- QA_record: `generation_record.md`
