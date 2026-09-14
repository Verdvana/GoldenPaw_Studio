# HAIR_B_03_SIDE_v001 — Generation Record

```yaml
character_id: CHR_HUMAN_001_OWNER
spec_revision: draft_1.183
identity_md_revision: draft_0.171
asset_id: HAIR_B_03_SIDE
candidate_id: HAIR_B_03_SIDE_v001
gate: "Gate 4 — Hairstyle Canon"
status: APPROVED_PROMOTION_SOURCE
approval_status: APPROVED
aspect_ratio: "3:4"
view: {anatomical_side: left, face_points: image_right, projection: true_profile}
reference_set_ids: [OWNER_FACE_LEFT_PROFILE_NEUTRAL_CANON_L1, OWNER_HAIRSTYLE_B_L0, OWNER_HAIRSTYLE_B_APPEARANCE_L1]
reference_count: 3
previous_generated_hair_inputs: []
output_path: "characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/approved/HAIR_B_03_SIDE/OWNER_HAIR_B_03_SIDE_CANON_001.png"
actual_dimensions_px: [1086, 1448]
generator: "built-in ImageGen"
checksum_sha256: "18d744d28041da41abc1a1b36c74ecf883fde81e1afeb6b02e526e9ea45be8d4"
qa_status: PASS_USER_APPROVED
```

## Reference roles

- approved left-profile Face (`b6c1d513...798c4`): identity, anatomical-left true profile, eye-level neutral head and skin only; hair excluded; retain limited matching-direction L0 evidence note.
- real B L0 (`73445832...8c17`): real hairline, backward gathering, wisps and updo direction only.
- approved B appearance (`e83de808...13f`): center part, controlled crown, smooth gathering, dark brown/highlights and fine strands only; its high camera/face/clothes/light excluded.
- Approved claw-clip design enters only as text: vertically centered occipital clip, compact fold, 4–6cm upward/backward tail. No B01/B02 pixels.

## Prompt assembly

Create one neutral eye-level anatomical-left true-profile Hair-B identity asset, with the nose pointing image-right. Preserve the approved profile identity while giving hair authority only to the real B reference plus the scoped B appearance reference. Show a controlled crown and center-part projection, smooth rearward gathering, a medium matte dark-brown claw clip centered vertically at the occiput, compact folded hair held inside it, and only a short 4–6 cm rooster-tail tuft curving upward/backward. From the side, reveal the clip's depth, hinge and near-side teeth without moving it off the rear centerline. Exclude a bun, topknot, ponytail, large fan, side clip, high-camera geometry, surprise, hands, sweater, warm garden light, and prior generated Hair pixels. Use the visible upper portion of the pink calibration one-piece on a plain neutral background.

## Generation result

- One built-in ImageGen call completed successfully on 2026-09-14.
- Output is a 1086×1448 RGB PNG at exact 3:4.
- Anatomical-left true profile, nose image-right, eye-level head and complete crown/clip/tail framing are present.
- Rear-centered claw-clip depth, hinge/near teeth and the short upward/backward tail are readable.
- The compact folded section beneath/behind the clip has a rounded volume. It remains visibly clip-held, but the user should specifically review whether it reads too close to a small bun.
- User explicitly approved the complete candidate with “登记吧”; the earlier rounded-fold review note is accepted within this side-view Hair-B component.

## User approval and promotion

- statement: “登记吧”
- decision: `APPROVED`
- promoted asset: `OWNER_HAIR_B_03_SIDE_CANON_001`
- operation: `MOVE`; candidate raster retained: `NO`
- original candidate path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/candidates/HAIR_B_03_SIDE_v001/HAIR_B_03_SIDE_v001.png`
- current path: `characters/CHR_HUMAN_001_OWNER/canon/hairstyles/B/approved/HAIR_B_03_SIDE/OWNER_HAIR_B_03_SIDE_CANON_001.png`
- full release lock: `NO`
