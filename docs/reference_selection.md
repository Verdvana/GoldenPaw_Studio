# Reference Selection and Budget

## Principle

Select references by responsibility, not by visual similarity alone. Every selected reference must answer a declared need in the shot and must have approved provenance.

Start from `registries/reference_sets.yaml` and the nearest asset `REFERENCE_GUIDE.md`. They contain the already-reviewed filename choices. Do not re-analyze complete L0 folders unless the shot needs a view or property not covered by a named set.

## Default budget

The default maximum is **8 images total** for one shot generation. Prefer fewer. A suggested allocation is:

| Slot | Default | Hard max | Responsibility |
|---|---:|---:|---|
| Character identity/Canon | 1 per visible character | 2 per character | who the character is |
| Body/pose Canon | 0–1 | 1 per character | stable proportions under relevant framing |
| Outfit | 0–1 | 1 | garment design only |
| Hosiery material | 0–1 | 1 | textile, denier, finish, continuous foot coverage |
| Fixed/temporary prop | 0–1 per important prop | 2 total | geometry, scale, use mode |
| Environment | 0–1 | 1 | location and layout |
| Previous shot | 0–1 | 1 | continuity only |

Exceeding 8 requires a written exception in `REFERENCE_PLAN.md`: why each image is indispensable and which lower-priority reference was considered.

## Selection procedure

1. Parse visible characters, framing, outfit, material, prop, environment, action, and continuity needs from `SHOT.md`.
2. Pin exact approved/locked versions.
3. Select the strongest view match for each need. Do not add redundant angles that are outside the frame.
4. Record responsibility and `must_not_define` for every image.
5. Reject references that failed QA, lack provenance, are unapproved generated outputs, or conflict with the pinned Canon.
6. Resolve conflicts by authority order: scoped L1 Canon > scoped L0 source > approved L2 design > continuity reference. A previous shot never wins an identity/material conflict.

## Framing-aware examples

- Owner close-up: face anchor + chosen hairstyle; no feet/material reference.
- Owner full body, barefoot in 15D: face + body + hairstyle + outfit + hosiery material; continuity/environment only if needed.
- Cat at laptop: cat face/body anchor + locked laptop + environment; previous shot only for paw and camera continuity.
