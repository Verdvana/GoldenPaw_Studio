# Shared L0 Hosiery Material Library

Drop your pre-organized reference folders into:

`materials/hosiery/source_library/raw/`

Use lowercase ASCII names in this order:

`<denier>d_<material-or-finish>_<color>`

Examples:

- `8d_ultra_sheer_nude`
- `15d_velvet_nude`
- `15d_high_gloss_black`
- `30d_matte_black`
- `40d_soft_sheen_gray`
- `80d_opaque_burgundy`

If more distinction is needed, append a construction qualifier such as `_reinforced_toe` or `_open_toe`. Keep original photos unchanged inside those folders.

Every folder is an L0 material source set, not a Canon asset by itself. Later Material Canon records select specific files and authorize only textile properties such as denier, color, finish, weave, opacity, stretch, highlights, and coverage behavior. They must not inherit identity, body, skin pigmentation, or anatomy from the photographed person.

Current `15d_nude_matte` routing is intentionally minimal: `IMG_2562.jpg` for sole/underside-foot coverage, `IMG_2579.jpg` and `IMG_2580.jpg` for crouching, and `IMG_2581.jpg` for standing. Do not restore deleted files as implicit fallbacks.

After adding folders, register files in `SOURCE_MANIFEST.md`. Do not move them into the 15D calibration package; that package references chosen L0 IDs from this shared library.
