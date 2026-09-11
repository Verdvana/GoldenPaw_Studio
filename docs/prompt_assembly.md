# Prompt Assembly Contract

Future prompts are assembled from structured blocks. Do not write one free-form prompt that silently blends responsibilities.

## Assembly order

1. **Task and shot intent** — one image, composition, action, camera, lens, lighting.
2. **Identity locks** — exact character ID/version and stable identity traits.
3. **Body/appearance locks** — exact body version, selected hairstyle, stable appearance rules.
4. **Outfit and material** — design IDs; hosiery coverage path and denier/finish behavior.
5. **Props** — exact prop Canon versions, character-relative scale, interaction.
6. **Environment** — layout and style authority.
7. **Continuity** — only permitted carry-over facts from the previous shot.
8. **Negative constraints** — asset-specific exclusions and known failure modes.
9. **Output contract** — aspect ratio, resolution, crop, intended Image-to-Video use.

## Reference map

Each prompt is accompanied by a table mapping `reference_id -> path -> responsibility -> must_not_define -> priority`. The prompt must explicitly say that identity conflicts are resolved in favor of pinned Character Canon and material conflicts in favor of pinned Material Canon.

## Owner-specific injection

When hosiery is visible, inject the full coverage chain: `waist/hips -> thighs -> knees -> calves -> ankles -> heels -> insteps -> toes`, the selected denier/finish/color, realistic textile language, and the forbidden latex/PVC/plastic/rubber/liquid/body-paint list. For 15D, burgundy polish may show naturally beneath the fabric; it is never painted on top.

## Cat-specific injection

Inject the locked face shape, golden-shaded tipping pattern, eye/nose/ear traits, body proportions, and explicit anti-drift constraints. When a fixed device is visible, pin its version and relative measurements.

Use `templates/shot/PROMPT_ASSEMBLY.md` as the generation record. The record is created before the call and completed with settings/output/QA afterward.
