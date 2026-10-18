# Reference Plan — OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v005

- status: `APPROVED_REFERENCES_FOR_SINGLE_GENERATION`
- reference_count: `5 generation inputs; 3 QA-only comparisons`
- budget_limit: `8`
- selected_reference_set_ids: [`OWNER_L0_FACE_013_GEOMETRY_CROP_V1`, `OWNER_L0_FACE_012_SKIN_CONTEXT_CROP_V1`, `OWNER_HAIRSTYLE_A_L0_SCOPED_DERIVATIVE`, `OWNER_BODY_FRONT_CURRENT_V025_FACE_EXCLUDED_DERIVATIVE`, `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE`]

| Priority | Reference ID/path | Level/status/version | Responsibility | Must not define | Why needed |
|---:|---|---|---|---|---|
| 1 | `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001` | deterministic L0 derivative | face identity/feature geometry | hair, body, outfit, lighting | Source-derived face generation authority |
| 2 | `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001` | deterministic L0 derivative | natural skin tone/texture context | fine geometry, hair, body, outfit | Source-derived skin context |
| 3 | `OWNER_HAIRSTYLE_A_FACE_MASKED_001` | deterministic L0 derivative | Hairstyle A only | face/identity/body | Explicit user-selected hairstyle A |
| 4 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | approved deterministic derivative | neck-below proportions and stance | face, hair, outfit, hosiery | Registered face-excluded body reference |
| 5 | `OWNER_CASUAL_AUTUMN_02_DESIGN_REFERENCE_v005` | L2 approved | new outfit only | face, body, pose, identity | Approved outfit design |

## Conflict resolution

L0-derived face method owns face generation. The face-excluded body derivative owns neck-below proportions. The A hairstyle derivative owns hair only. The approved v005 outfit reference owns garment design only. Three listed comparison references are post-generation QA only and are not sent to ImageGen.

## Excluded references

- Prior worn candidates and prior outfit v004: excluded to avoid generated-image lineage and superseded outfit design.
- Approved Face and Body Canons: comparison-only; never generation inputs.
- User fashion photos from the preceding design task: excluded because their design responsibility is now carried by approved outfit v005; they do not define owner identity or body.
