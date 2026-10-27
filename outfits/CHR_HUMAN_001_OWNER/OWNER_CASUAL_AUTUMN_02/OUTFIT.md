# Outfit Design

- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- display_name: 秋季休闲穿搭02
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- episode/scene scope: reusable owner casualwear / autumn
- character_outfit_root: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02`
- status: `DESIGN_REFERENCE_AND_WORN_FRONT_APPROVED`
- approval_status: `DESIGN_REFERENCE_AND_WORN_FRONT_APPROVED`
- design_reference_status: `APPROVED`
- worn_validation_status: `APPROVED_BY_USER`
- approved_design_reference: `approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`
- prior_worn_views: [`approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT.png`] (earlier approved presentation; retained as historical version)
- approved_worn_front: `approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v015.png` (`APPROVED`; user approved likeness, hosiery/toe surface and outfit)
- prior_approved_worn_front: `approved/worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012.png` (retained historical version)
- current_worn_front_candidate: `none` (v015 promoted after explicit user approval)
- prior_worn_front_candidates: `v001` (superseded by skirt refinement), `v002` (rejected: 2:3 framing and head angle), `v003` (rejected: pantyhose absent), `v005`–`v008` (rejected: hosiery/toe coverage not visibly continuous), `v009` (superseded after user face/hair/hosiery/sole feedback), `v010` (calf gap), `v011` (superseded for more exact neutral-face source routing; review status retained), `v013` (visible garment texture), `v014` (face likeness rejected), `v015` (approved), `v016` (superseded by approved v015)
- prior_worn_front_candidate: `candidates/v001_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v001.png` (superseded by requested skirt silhouette refinement)
- current_design_reference: `approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png` (v005)
- prior_design_reference_candidates: `v001` (REJECTED), `v002` (REJECTED), `v003` (superseded), `v004` (previously approved; superseded by v005)

## Approved worn-front reference restriction

The approved v015 worn-front image may define only outfit appearance/fit, matte white
pantyhose textile including the toe surface, toe-opening interaction, and plush
mule/sole design. Its depicted face/likeness may be used only for post-generation QA
comparison and must never be a future face-generation input. Hairstyle, body
proportions, skin and identity lineage are excluded. Follow the applicable source
method for future face generation. The approved v012 image remains a historical
version under its own narrower reference restrictions.

## Design direction

Autumn outfit in dark chocolate brown and ivory. A classic tailored dark-brown blazer
with notched lapels and long sleeves layers over a fitted ivory fine-ribbed high-neck
knit top. Pair it with a dark-brown high-waisted pleated mini skirt, medium-thick
matte white pantyhose, and cream ivory plush open-toe mule slippers with an approximately 3 cm thick platform sole. Garments
are unbranded and free of graphics. Keep the skirt pleats distinct and even; the
hosiery is textile, never latex or plastic. Keep the outfit visually distinct from
`OWNER_CASUAL_AUTUMN_01` (white lace top, black ruffled skirt, silver hosiery and
silver Mary Jane shoes).

## Asset package contract

The approved v005 is a clothing-only `design_reference`, arranged as a clear,
photorealistic apparel presentation on a neutral light-gray studio background. It
contains no person, mannequin, face, hands, body, or identity cues. The previous
worn-front view predates this outfit redesign and must be revalidated before use as
the current worn view.

Candidate `v005` passed clothing-only design review and was approved by the user on
2026-10-17. It supersedes previously approved v004. Attempts `v001` and `v002` were rejected because the pantyhose was
rendered as a human-shaped leg form; `v003` was superseded by the requested color and
hosiery refinement.

Worn-front candidate `v001` was generated from source-derived face inputs, a
face-excluded body derivative, the approved outfit reference, and an L0 hair-only
derivative. Initial fit and contamination QA passed; user approval is pending.

| Layer | Asset/material ID | Construction | Color | Coverage |
|---|---|---|---|---|
| Outer layer | `OWNER_CASUAL_AUTUMN_02_BLAZER` | Tailored blazer, classic notched lapels, long sleeves | Dark chocolate brown | Torso and arms |
| Top | `OWNER_CASUAL_AUTUMN_02_KNIT_TOP` | Fitted fine-ribbed high-neck knit | Ivory | Torso and neck |
| Bottom | `OWNER_CASUAL_AUTUMN_02_SKIRT` | High-waisted mini skirt with crisp narrow pleats | Dark chocolate brown | Upper thigh |
| Hosiery | `OWNER_CASUAL_AUTUMN_02_TIGHTS` | Continuous medium-thick matte pantyhose with visible textile tension; closed toe | Soft white | Waist through hips, legs, heels, insteps and toes; only toe tips may show slight translucency |
| Footwear | `OWNER_CASUAL_AUTUMN_02_SLIPPERS` | Plush fuzzy open-toe mule slippers, approximately 3 cm thick platform sole | Cream ivory | Hosiery remains continuous through visible toe opening |

## Silhouette and fit

- shoulder/neckline fit: blazer shoulder line sits naturally; ribbed high neck lies flat.
- garment length and hem position: blazer layers over skirt; skirt hem sits at upper thigh.
- waist/hip/chest tension: knit top fits close without distortion; skirt sits securely at natural waist.
- layering and coverage: knit top remains beneath blazer; no exposed midriff.
- drape/fold behavior: soft cardigan folds, structured skirt body, no stiff or plastic surfaces.
- footwear and hosiery relationship: medium-thick matte white pantyhose remains continuous beneath both open-toe slippers, with only toe tips showing slight translucency through the opening and visible textile tension over the feet; platform sole is approximately 3 cm thick.
- worn-front leg stance: feet together and parallel; knees and calves naturally close and may touch. Preserve natural registered leg volume and alignment; do not render bowed/O-shaped legs or a stance-induced calf gap.

## Hosiery and footwear contract

- hosiery_material_id: `OWNER_CASUAL_AUTUMN_02_TIGHTS`
- denier/color/finish: medium-thick soft-white matte hosiery; exact denier not specified
- toe construction: closed and continuously covered textile toes; only toe tips may show slight skin tone through fabric, never a material break or bare toe; visible smooth fabric tension across calves, ankles, insteps and toes
- footwear: cream ivory fuzzy open-toe mule slippers with approximately 3 cm thick platform sole
- continuous coverage required: yes

## Must not redefine

Owner face identity, body geometry, skin, hairstyle, or Character Canon. The design
reference must not contain a person or imply body proportions.
