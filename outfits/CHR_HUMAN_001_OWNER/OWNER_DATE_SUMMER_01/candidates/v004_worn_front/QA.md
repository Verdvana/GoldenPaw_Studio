# Worn front v004 QA

- status: REJECTED
- reviewer: Codex, 2026-10-30
- authoritative_file: OWNER_DATE_SUMMER_01_WORN_FRONT_v004.png
- sha256: 8dba3c93b318eb744d28fbb0c0699afc47be42a96923e25f7b9be8c9f769b22e
- technical: PASS; 1086 × 1448 PNG, exact 3:4, complete head/hands/feet and floor margin

## Clothing and fit

- neckline/chest: ordinary broad round neckline and opaque white front retained; no molded cup construction. Actual worn scoop depth remains a user fit-review item.
- chiffon: full translucent long sleeves, gathered cuffs and cropped elastic hem readable.
- waist hierarchy: PASS; white tights waistband lies just below top and substantially above shorts, with a broad sheer abdominal panel covering navel region.
- shorts: regular-rise conventional denim front and cuffed legs, rather than original low-rise shallow front.
- hosiery: continuous white textile visible over abdomen, legs, ankles and insteps; no obvious ankle cutoff or plastic sheen. Toe tips have a light white veil, but nail diffusion/interdigital textile tension are not strongly resolved at full-frame scale and remain REVIEW_REQUIRED. Do not claim definitive detailed foot QA pass.
- sandals: silver toe/ankle straps and floor support visible; front projection partly obscures stiletto heel structure, so exact heel geometry/height not fully verified.
- body: roughly retains natural adult volume; stance slightly asymmetric with head/torso not perfectly square; no obvious duplicated limbs. Cannot approve exact proportion matching from this result.

## Face and identity — comparison only, after generation

Opened approved Face Canon and full Body Canon only after the tool finished. Neither was a generation input.

- face contamination / identity gate: FAIL for identity drift; no obvious muddy patches, dark/bright blotches or smudges, but candidate eye/eyelid, nose/mouth and jaw relationships do not match the approved front Face Canon closely enough. Slight head turn and smile also differ from neutral frontal QA target.
- skin: generally even, no obvious severe patch contamination; identity failure remains independent of clean rendering.
- hair: front root/side sweep is more raised/rearward than the intended flat loose Hair-A reference; needs review, no claim of Hair-A pass.

Mandatory project rule rejects identity drift. Overall candidate therefore REJECTED, even though clothing layering is useful for viewing. No promotion, fit approval, Canon registration or downstream generation-reference use. No automatic retry.
