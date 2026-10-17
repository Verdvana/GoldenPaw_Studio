# Outfit Design

- outfit_id: `OWNER_CASUAL_AUTUMN_02`
- display_name: 秋季休闲穿搭02
- level: `L2`
- intended_character_id: `CHR_HUMAN_001_OWNER`
- episode/scene scope: reusable owner casualwear / autumn
- character_outfit_root: `outfits/CHR_HUMAN_001_OWNER/OWNER_CASUAL_AUTUMN_02`
- status: `DESIGN_REFERENCE_APPROVED_WORN_FRONT_REVIEW_REQUIRED`
- approval_status: `DESIGN_REFERENCE_APPROVED`
- design_reference_status: `APPROVED`
- worn_validation_status: `REVIEW_REQUIRED`
- approved_design_reference: `approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`
- approved_worn_views: `[]`
- current_worn_front_candidate: `candidates/v001_worn_front/OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v001.png`
- current_design_reference: `approved/design_reference/OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE.png`
- prior_design_reference_candidates: `v001` (REJECTED), `v002` (REJECTED), `v003` (superseded by user-requested refinement)

## Design direction

Cozy, relaxed autumn homewear with a warm neutral palette. The top is a cream-oatmeal
crew-neck knit cardigan with a gently relaxed fit, waist-length hem, narrow ribbed
cuffs and hem, and small matte wood-look buttons. Wear it buttoned over a plain warm
ivory crew-neck tee; keep both layers unbranded and free of graphics. Pair it with a
lighter warm medium-brown wool-blend mini skirt, thin white pantyhose with slight
natural show-through, and pale beige-tan fuzzy open-toe mule slippers.

The silhouette should feel comfortable and everyday: cardigan shoulders sit naturally,
the skirt has a simple A-line shape with a clean hem, and the slippers have a soft
plush upper and low flexible sole. Keep the outfit visually distinct from
`OWNER_CASUAL_AUTUMN_01` (white lace top, black ruffled skirt, silver hosiery and
silver Mary Jane shoes).

## Asset package contract

The first candidate is a clothing-only `design_reference`, arranged as a clear,
photorealistic apparel presentation on a neutral light-gray studio background. No
person, mannequin head, face, hands, body, or identity cues. Show the complete
cardigan, undershirt, skirt, thin white pantyhose, and both slippers as separate
products; the pantyhose is neatly folded and the slippers' openings remain visible.
The worn-front validation view checks the hosiery-to-slipper relationship and fit on
the owner.

Candidate `v004` passed clothing-only design QA and was approved by the user on
2026-10-17. Attempts `v001` and `v002` were rejected because the pantyhose was
rendered as a human-shaped leg form; `v003` was superseded by the requested color and
hosiery refinement.

Worn-front candidate `v001` was generated from source-derived face inputs, a
face-excluded body derivative, the approved outfit reference, and an L0 hair-only
derivative. Initial fit and contamination QA passed; user approval is pending.

| Layer | Asset/material ID | Construction | Color | Coverage |
|---|---|---|---|---|
| Top layer | `OWNER_CASUAL_AUTUMN_02_CARDIGAN` | Crew neck, gently relaxed long sleeves, waist-length, small matte wood-look buttons, narrow ribbed cuffs and hem | Cream oatmeal | Torso and arms |
| Base layer | `OWNER_CASUAL_AUTUMN_02_TEE` | Plain crew-neck tee, smooth cotton jersey, no print | Warm ivory | Visible at neckline and a small area below cardigan opening |
| Bottom | `OWNER_CASUAL_AUTUMN_02_SKIRT` | Simple clean A-line mini skirt, substantial wool-blend texture, no ruffles or lace | Lighter warm medium brown | Upper thigh |
| Hosiery | `OWNER_CASUAL_AUTUMN_02_TIGHTS` | Continuous thin pantyhose with slight natural show-through, matte textile finish, closed toe | White | Waist through hips, legs, heels, insteps and toes |
| Footwear | `OWNER_CASUAL_AUTUMN_02_SLIPPERS` | Low-profile mule slippers, plush fuzzy upper, open toe, soft flat sole | Pale beige-tan | Footwear leaves hosiery-covered toe area visible |

## Silhouette and fit

- shoulder/neckline fit: natural shoulder seam; crew neckline lies flat without gaping.
- garment length and hem position: cardigan hem meets the skirt waistband; skirt hem sits at upper thigh.
- waist/hip/chest tension: relaxed cardigan and tee; skirt sits securely at natural waist without pulling.
- layering and coverage: tee remains a narrow underlayer; no exposed midriff.
- drape/fold behavior: soft cardigan folds, structured skirt body, no stiff or plastic surfaces.
- footwear and hosiery relationship: thin white pantyhose remains continuous beneath both open-toe slippers, with fabric-covered toes naturally visible through the opening.

## Hosiery and footwear contract

- hosiery_material_id: `OWNER_CASUAL_AUTUMN_02_TIGHTS`
- denier/color/finish: thin white pantyhose with slight natural show-through, matte textile; exact denier to be selected during later material validation
- toe construction: closed and continuously covered textile toes; subtle skin tone may show through, but never a material break or bare toe
- footwear: pale beige-tan fuzzy open-toe mule slippers
- continuous coverage required: yes

## Must not redefine

Owner face identity, body geometry, skin, hairstyle, or Character Canon. The design
reference must not contain a person or imply body proportions.
