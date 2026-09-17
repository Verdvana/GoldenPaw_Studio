# Reference Routing by Production Situation

This is the high-level router. Exact files are resolved through `registries/reference_sets.yaml` and the asset-level guides.

| Situation | Required sources | Exclude by default |
|---|---|---|
| Build owner Face Canon | one matching owner L0 identity set; optional second angle-support image | body photos, hosiery, outfit, prior generated faces |
| Build owner Body Canon | source-derived Face recovery inputs + one L0 body-context set + calibration outfit/material | AI Face Canon or prior generated face |
| Build Hairstyle B angles | source-derived Face recovery inputs + B L0/approved scoped hair design | AI Face Canon as a generation input; candidate face/body/skin/background |
| Build owner Expression Canon | source-derived Face recovery inputs + one expression-specific L0 set | AI Face Canon or expression photo as new identity |
| Build cat Face/Front Canon | `TECH_CAT_L0_FRONT_IDENTITY` | generated side/back guesses |
| Build unseen cat angles | new real matching-angle L0 photos are required | previous AI cat outputs as identity lineage |
| Build hosiery Material Canon | one exact material set; optional second foot/full-leg complement | photographed person's identity/body/skin/nails |
| Ordinary owner close-up after lock | source-derived Face method inputs + selected Hairstyle Canon; AI Face Canon comparison only | AI Face Canon as generation input; unrelated L0 bundle |
| Ordinary owner full body after lock | source-derived Face method inputs + Body/Hairstyle Canon + Outfit + exact hosiery set if visible | AI Face Canon as generation input; unrelated L0 identity images |
| Foot/hosiery close-up | Body/feet Canon + exact material set + footwear design; Face only if visible | shoe-obscured material source as sole foot authority |
| Ordinary cat shot after lock | relevant Cat Canon view + props/environment needed by shot | all cat L0 images and previous shot as identity |
| Continuity shot | same pinned Canon/L2 assets + at most one passing previous shot | previous shot redefining identity/material/prop/home |

If a set is marked `REVIEW_REQUIRED` or `usable_for_generation: false`, it cannot be selected for generation. For owner face generation, source-derived L0 inputs and the Face method take priority; approved AI Face Canon is comparison-only. If source references conflict, report the conflict instead of averaging the images.
