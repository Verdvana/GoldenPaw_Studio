# Face Contamination QA Rules

These rules apply to every L2/L3 candidate with the owner's face visible.

## Reference isolation

1. For future owner assets, the source-derived Face generation method and its L0 inputs are the sole face-generation authority. Approved AI Face Canon images are forbidden as generation inputs.
2. Approved AI Face Canon images may be used only as post-generation QA comparison references for identity drift, geometry, projection, skin contamination and facial artifacts.
3. A Body reference must be a deterministic face-excluded derivative when used with a visible face. It may define only the declared neck-below body, proportions, limbs, feet, or pose scope.
4. Do not use a prior Outfit, Shot, or other AI-generated candidate as an identity reference.
5. Outfit, environment, material, and design references must not define face, skin, body, hair, or identity.

## Required QA check

Every candidate QA must record:

- `face_contamination_check`: `PASS`, `FAIL`, or `REVIEW_REQUIRED`;
- comparison against the approved Face Canon;
- whether the face has dark/bright blotches, muddy relighting, patches, smudges, texture amplification, duplicated features, or identity drift;
- whether any Body/reference image was allowed to define the face;
- the decision to reject, regenerate, or send for user review.

Any visible face contamination is a QA failure and the candidate must not be promoted or used downstream.
