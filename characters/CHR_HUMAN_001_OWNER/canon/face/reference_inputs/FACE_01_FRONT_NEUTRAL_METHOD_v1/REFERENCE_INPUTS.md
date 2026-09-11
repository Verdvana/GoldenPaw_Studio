# FACE_01 Front Neutral — Stable Recovery Inputs v1

These files exist only to reproduce or recover the L1 front-neutral master from approved/L0 sources without an AI-to-AI chain.

They are the only physical copies of these derivatives. Candidate records refer here by path and checksum and do not store local input copies.

## B_FACE_SKIN_CROP.png

- source: `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001`
- operation: crop `620x680+230+380`, no scaling, retouching or color adjustment
- checksum: `760bb537c1062390d2334c0bf8b138f279ed776a1fc04c382e7ae2ca6c53a12c`
- responsibility: face identity and B-anchor skin tone only
- must not define: crown, full hairstyle, camera geometry, body, outfit, lighting or background

## B_FACE_SKIN_CROP_2X.png

- source derivative: `B_FACE_SKIN_CROP.png`
- operation: deterministic Lanczos resize from `620x680` to `1240x1360`; no AI upscaling, sharpening, restoration or color adjustment
- checksum: `c966a30809db371216973b259fd20152ba165ca5ef43d36748d2ca45b35b507e`
- responsibility: face identity and B-anchor skin tone only
- must not define: crown, full hairstyle, camera geometry, body, outfit, lighting or background

## B_FACE_SKIN_CONTEXT_NO_CROWN.png

- source: `OWNER_HAIRSTYLE_B_APPEARANCE_CANON_001`
- operation: crop `900x1000+93+350`, no scaling, retouching or color adjustment
- checksum: `d98019128bfa974a102813da52b4a2905ec4aa7c95eb5222a163e419f287e74d`
- responsibility: exact face, facial-feature relationships, natural face shape, apparent age and skin tone
- must not define: crown, Hairstyle B, source camera angle, outfit, lighting or background

## DSC00847_HAIR_ONLY_MASKED.png

- source: `L0_OWNER_017` / `DSC00847.jpg`
- operation: original-size PNG with neutral-gray ellipse masking the face; hair pixels unchanged
- checksum: `6eb98bb5c0ac728d66fd551b249fa2002e08aa60b52633a081717c4534c3a2cd`
- responsibility: Hairstyle A front design only
- must not define: gray mask, identity, face, skin, body, clothes, camera, outdoor light or background

These derivatives have no independent Canon authority. Their originals are unchanged.
