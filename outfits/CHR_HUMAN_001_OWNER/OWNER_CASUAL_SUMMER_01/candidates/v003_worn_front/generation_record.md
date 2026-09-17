# Generation Record

- asset_id: `OWNER_CASUAL_SUMMER_01_WORN_FRONT`
- outfit_id: `OWNER_CASUAL_SUMMER_01`
- level: `L2`
- candidate_version: `v003`
- status: `REJECTED`
- output_path: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_SUMMER_01/candidates/v003_worn_front/OWNER_CASUAL_SUMMER_01_WORN_FRONT_v003.png`
- output_sha256: `5839506edd1b176ce876d8b8a8c82428deb3048a01a9255067b6420e9112c6ec`
- use_case: `identity-preserve`
- reference_budget: `4 images; same approved scoped inputs as v002`
- retry_reason: `v002 still showed exposed-looking toenails and insufficient hosiery tension curves`

## Generation inputs

- `OWNER_CASUAL_SUMMER_01_DESIGN_REFERENCE`: latest generated outfit design; outfit styling only, never face/skin/body/identity.
- `OWNER_BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v3`: approved face-excluded body proportions and stance only.
- `B_FACE_SKIN_CONTEXT_NO_CROWN`: source-derived Face method input for face identity and warm-neutral skin tone only.
- `DSC00847_HAIR_ONLY_MASKED`: masked L0 Hairstyle-A input for hair only.

## QA comparison only

- `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`: post-generation QA comparison only; forbidden as generation input.

## Prompt assembly

Use case: identity-preserve
Asset type: L2 worn-front outfit fit-validation image
Primary request: generate a fresh full-body frontal neutral standing owner in the summer casual outfit, with the face reconstructed from the source-derived Face method and a visibly closed-toe sheer hosiery layer worn under open-toe sandals.
Composition/framing: exact 3:4 portrait, eye-level frontal camera, full body, both feet completely visible; slightly larger lower-foot rendering while retaining full-body composition.
Materials/textures: critical hosiery construction — a continuous light-nude sheer micro-sheen stocking membrane lies over the top and front edge of every toe, including the nail area, inside the open-toe sandals. The sandal straps sit on top of the fabric membrane and frame it; the opening reveals fabric-covered toes, never bare skin. Burgundy polish appears only as muted blurred wine-red shapes diffused through the nude textile. Draw several fine curved hosiery tension lines over each toe and shallow V-shaped/converging valleys between adjacent toes; the valleys are fabric folds and remain filled by translucent fabric. Every toe tip is visibly covered. No bare nail plate, no sharp toenail edge, no gap between toes, no white ring, no toe-cap seam.
Constraints: preserve outfit, Hairstyle A, face-method identity, warm-neutral skin tone, body proportions, natural adult anatomy, and metallic sandals. The open-toe sandal opening changes only the shoe, not the hosiery construction; hosiery is closed-toe and continuous.
Avoid: uncovered toes, exposed nail plates, naked toe gaps, skin directly visible at toe tips, opaque tights, plastic/latex/PVC/rubber/liquid hosiery, white bands, hard seams, missing interdigital textile, face drift, AI Face Canon/Body Canon as input, extra toes/fingers, distorted footwear, logos, text, watermark.

## QA status

- v001 hosiery QA: FAIL
- v002 hosiery QA: FAIL — toes still looked exposed
- v003 fit/garment QA: pending
- v003 Face method compliance: pending
- v003 hosiery continuity/toe coverage: pending
- v003 interdigital tension curves: pending

## Final QA disposition

- `REJECTED` — the rendered toes still read as exposed at the open-toe shoe opening; the required continuous hosiery membrane, diffused burgundy polish, and clear interdigital fabric tension curves are not sufficiently reliable.
