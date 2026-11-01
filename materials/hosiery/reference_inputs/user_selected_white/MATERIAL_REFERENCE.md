# Mandatory white hosiery material reference

- material_id: `HOS_USER_SELECTED_WHITE_STRICT`
- level: L0 source + deterministic L0-derived generation input; no L1 promotion
- category: white hosiery textile appearance
- status: APPROVED (user-selected reference responsibility only)
- source_asset_id: `L0_HOS_USER_WHITE_001`
- source_path: `materials/hosiery/source_library/raw/user_selected_white/PHOTO_1.jpg`
- source_sha256: `34ccb3f3923b441768f69f2f22ef95eb5bde3f31adf74af8172365bf503528df`
- generation_input_asset_id: `HOS_USER_WHITE_001_LOWER_LEG_FOOT_CROP_001`
- generation_input_path: `materials/hosiery/reference_inputs/user_selected_white/PHOTO_1_LOWER_LEG_FOOT_MATERIAL_CROP.png`
- generation_input_sha256: `ce3b4fe1aafebe2818baae37dd3a76ca712820b1232d2ed15e06adf55002095d`

## User decision and scope

- approver: user
- date: 2026-10-31 (Asia/Shanghai)
- approval evidence, verbatim: “把这张图片里的白色丝袜作为该项目中任何一张ai生成图片需要严格参考得白色丝袜图片”
- Applies project-wide to every future AI-generated image depicting white hosiery, including L1/L2/L3. White hosiery must use this named reference set as a required material input and QA reference. This does not require white hosiery in every image or recolor nude/black calibration materials.
- This decision takes priority over earlier white-hosiery material references and earlier generated outfit images for future generation. Existing approved/locked images remain historical records and are not edited or promoted by this decision. Other sources may fill a documented missing view only; they must not override the selected white appearance. A later explicit user decision may change this requirement.

## Visual/physical contract and limits

- color: photo-observed milky white, with skin softly visible through thinner/stretched regions; do not inherit the photographed person's skin tone.
- opacity/denier: visually sheer to semi-sheer; exact D number, brand and fiber composition unverified. Do not relabel this as 15D or 30D without evidence. If a shot also specifies denier, record it separately from what this source proves.
- finish: smooth textile with visible soft directional sheen and elongated highlights under direct flash. Preserve textile translucency; do not turn highlights into latex/PVC/plastic/liquid or painted white skin.
- coverage: visible knee/calf/ankle/instep/toes remain one continuous hosiery surface, including visible toes inside open-toe sandals. Full pantyhose continuity follows project QA; hidden waist/gusset, underside foot, reinforced-toe construction and knit details are not established by this photo.
- tension: natural highlight and opacity variation over curved and stretched areas, without copying the source leg shape or pose.
- lighting: compare material response in the intended shot light; do not copy night flash, blown highlights, colored reflections or the scene's exposure as permanent material properties.
- generation input: use the deterministic lower-leg/foot crop by default (one material image). Do not attach the uncropped portrait as a material generation input. The source remains immutable ingestion evidence.
- must_not_define: person identity, face, hair, body or foot anatomy and proportions, skin pigmentation, nail color, pose, clothing, shoe design, car, background, watermark, scene lighting, unseen waistband/gusset/sole construction, exact denier.

## Required generation record and QA

1. When white hosiery is visible, declare `HOS_USER_SELECTED_WHITE_STRICT` in the reference plan, with input asset ID, version `source_v1/crop_v1`, path, SHA-256, material-only responsibilities and exclusions. Record the crop in `generation_inputs`; declare QA references separately in `qa_comparison_only` with their scoped duties.
2. Prompt must require this source's white color impression, translucency, textile sheen and continuous leg-to-toe coverage. Clothing/shot/candidate images cannot replace this material authority.
3. Compare output against this reference for white color, opacity, sheen, ankle/instep/toe continuity, and absence of naked toes, abrupt white toe bands, paint-like surfaces or plastic gloss. Reject material drift; do not treat an older approved AI outfit image as overriding this source.
4. Keep character identity, face/skin, body, hair and nails under their separately applicable project authorities. Burgundy nail visibility depends on real opacity; never force it through opaque fabric.
5. If an angle is not evidenced (for example sole, waist or gusset), record the coverage gap. A supplemental reference supplies only that gap and cannot change the white-material appearance.

## Ingestion and deterministic provenance

- attachment original name: `照片 1.jpg`
- attachment path at ingestion: `/tmp/codex-remote-attachments/01a19227-4b9d-7881-83ba-993a94494e09/40597932-B58D-4309-979F-BB1EE3CBB175/1-照片-1.jpg`
- original dimensions: 960 × 1280 pixels, JPEG
- original bytes copied unchanged once to the repository's unique raw path; attachment and raw SHA-256 verified equal.
- crop operation: Pillow `Image.open(source).crop((415, 675, 550, 1188)).save(destination)`; zero-based pixel coordinates, right/bottom exclusive; output 135 × 513 PNG.
- No AI, resize, recoloring, retouching, sharpening, compositing or geometric alteration. Crop removes face/hair/upper body and preserves observed lower-leg/foot material pixels. Residual car/shoe/background pixels have no authority.
- The crop inherits its source's scoped responsibility and has no independent Canon authority. Original and derivative each have one authoritative physical file; records contain paths/checksums only.
