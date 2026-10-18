# Reference Plan — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v009

- status: `APPROVED_REFERENCES_FOR_SINGLE_GENERATION`
- reference_count: `5 generation inputs; 2 QA-only comparisons`
- budget_limit: `8`
- selected_reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`, `HOS_USER_SELECTED_SHEER_PALE_AND_PLUSH_MULES`]

| Priority | Reference ID/path | Level/status/version | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|
| 1 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` | deterministic L0 face crop | face geometry/identity only | hair, skin color, body, wardrobe | maximize identity geometry fidelity |
| 2 | `OWNER_HAIRSTYLE_A_FACE_MASKED_001` | masked L0 hair derivative | Hairstyle A only | face/identity/body | user's hairstyle correction |
| 3 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | approved derivative | body proportions below neck | face/hair/wardrobe/material/pose | proportions only; user stance correction overrides reference stance |
| 4 | `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005` | approved L2 with user amendment | outfit silhouettes and colors; slipper upper | person/body/face/hair/5 cm sole | approved garments |
| 5 | `L0_HOS_USER_001` | newly catalogued user material source | pale sheer hosiery and fuzzy slipper upper only | identity, skin, anatomy, pose, sole thickness | directly addresses material fidelity request |

## Excluded references

- v005–v008 worn candidates: rejected/unreviewed generated pixels; not used for any continuity or identity responsibility.
- AI Face and Body Canon: post-generation comparison only.
- The uploaded Photo 1 fashion reference: garment design is already captured in approved v005; no need to attach it again.
