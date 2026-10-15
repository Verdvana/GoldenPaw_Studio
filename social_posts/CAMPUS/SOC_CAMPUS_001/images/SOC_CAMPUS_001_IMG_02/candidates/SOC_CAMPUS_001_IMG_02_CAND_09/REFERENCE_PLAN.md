# Reference Plan — SOC_CAMPUS_001_IMG_02_CAND_09

Status: `DRAFT — REVIEW_REQUIRED`

This is a scoped corrective candidate under the user's latest IMG_02 redesign instruction. CAND_08 was checked and missed three requested details (bangs, visible hosiery, iPhone X camera layout); CAND_08 pixels are not reused. One independent attempt only.

## Generation inputs (2)

| # | Asset ID / version | Source | Responsibility | Must not define |
|---|---|---|---|---|
| 1 | `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1` | `characters/CHR_HUMAN_001_OWNER/canon/body/reference_inputs/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_v7/BODY_01_FRONT_FULL_BODY_FACE_EXCLUDED_CROP.png`; SHA-256 `59b585718760d9bd528dbc1e864b6fc9f9e271054e092933c9196a3876ae2e0b` | Neck-below adult body proportions and plausible anatomy only | Face, skin, hair, clothing, hosiery, footwear, light or room |
| 2 | `L0_HOS_15_NSS_002` | `materials/hosiery/source_library/raw/15d_nude_soft_sheen/IMG_2589.jpg`; SHA-256 `1c3ea08ea6f95fb8c4f3c189dc2a0027f0214bdf031320315a60232ddf741864` | Nude 15D sheer textile color, continuity and soft sheen only | Person, identity, body shape, face/skin, pose, outfit, shoes, light or setting |

## Prompt-authorized L2 elements

- Hair: full straight bangs with long dark-brown straight hair, user specified for this shot. This is a post-specific L2 variant under `OWNER_L1_GENERATION_SPEC.md` revision `draft_1.234`; no A/B blend, Canon status or reuse.
- Face: fully occluded by the mirror-facing back of the phone. No face or face reference in generation.
- Phone, outfit, dorm mirror room, and flats: text-only direction from user's request.

## QA comparison only

- Approved Face Canon: after-generation occlusion/contamination QA only; not a generation input.
- Approved Body Canon: optional proportions comparison only; not a generation input.

No prior generated IMG_02 or other AI candidate is an input or continuity reference.
