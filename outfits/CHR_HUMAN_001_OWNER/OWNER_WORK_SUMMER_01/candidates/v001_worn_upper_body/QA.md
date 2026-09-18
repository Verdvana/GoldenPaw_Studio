# QA — OWNER_WORK_SUMMER_01_WORN_UPPER_BODY_v001

## Technical precheck

- PNG is readable and RGB, 1086x1448 native output.
- Exact 3:4 portrait ratio; no forced upscale or resize.
- Upper-body framing includes face through mid-thigh; shoes are outside the crop.

## Visual checks

- Body01 neck, shoulder, torso and waist proportions are represented.
- Face is generated from source-derived face input and Hairstyle A from the masked source hair input.
- Black fitted short-sleeve top has a lowered rounded neckline.
- Champagne-white polka-dot skirt waistband and upper panel are visible with a tailored silhouette.

## Gate

`SUPERSEDED_SCOPE_CORRECTION`. This candidate was cropped to the upper body, which did not match the requested meaning of a worn full outfit. It is retained only as provenance and must not be used as a future generation input.
