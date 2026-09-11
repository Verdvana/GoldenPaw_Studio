# Reference Routing by Production Situation

This is the high-level router. Exact files are resolved through `registries/reference_sets.yaml` and the asset-level guides.

| Situation | Required sources | Exclude by default |
|---|---|---|
| Build owner Face Canon | one matching owner L0 identity set; optional second angle-support image | body photos, hosiery, outfit, prior generated faces |
| Build owner Body Canon | approved Face candidate + one L0 body-context set + calibration outfit/material | wedding/episode outfit as body authority |
| Build Hairstyle B angles | approved owner Face Canon + `OWNER_HAIRSTYLE_B_CANDIDATE` after explicit hairstyle approval | candidate face/body/skin/background |
| Build owner Expression Canon | locked/approved Face Canon + one expression-specific L0 set | expression photo as new identity |
| Build cat Face/Front Canon | `TECH_CAT_L0_FRONT_IDENTITY` | generated side/back guesses |
| Build unseen cat angles | new real matching-angle L0 photos are required | previous AI cat outputs as identity lineage |
| Build hosiery Material Canon | one exact material set; optional second foot/full-leg complement | photographed person's identity/body/skin/nails |
| Ordinary owner close-up after lock | Face Canon + selected Hairstyle Canon; outfit only if visible | owner L0 bundle, body and hosiery references |
| Ordinary owner full body after lock | Face + Body + Hairstyle Canon + Outfit + exact hosiery set if visible | unrelated L0 identity images |
| Foot/hosiery close-up | Body/feet Canon + exact material set + footwear design; Face only if visible | shoe-obscured material source as sole foot authority |
| Ordinary cat shot after lock | relevant Cat Canon view + props/environment needed by shot | all cat L0 images and previous shot as identity |
| Continuity shot | same pinned Canon/L2 assets + at most one passing previous shot | previous shot redefining identity/material/prop/home |

If a set is marked `REVIEW_REQUIRED` or `usable_for_generation: false`, it cannot be selected until the user explicitly approves the scoped use. If two references conflict, the pinned scoped Canon wins; report the conflict instead of averaging the images.
