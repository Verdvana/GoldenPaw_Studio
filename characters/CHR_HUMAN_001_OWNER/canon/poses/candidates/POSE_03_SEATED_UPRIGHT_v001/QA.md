# QA — POSE_03_SEATED_UPRIGHT_v001

```yaml
candidate_id: POSE_03_SEATED_UPRIGHT_v001
qa_status: FAIL_USER_REJECTED_FACE_ITERATION_POLLUTION
approval_status: REJECTED
reviewed_at: "2026-09-13"
```

## Technical checks

- PASS — one 1086×1448 exact-3:4 image; complete hair, hands, stool contact, lower legs and both feet remain inside frame.
- PASS — centered neutral pelvis, naturally vertical spine/torso, level head and lowered shoulders produce a clear upright seated posture without slouching, leaning or back arch.
- PASS — thighs point forward at natural width, knees are separated and bent near 90°, lower legs descend near vertically, and both feet rest flat and uncrossed on one floor plane.
- PASS — both hands rest lightly on the upper thighs with ten visible plausible fingers and no object interaction.
- PASS — seated soft-tissue compression at hips/thighs is plausible and does not visibly change the approved body mass or limb scale beyond ordinary articulation.
- PASS — approved adult identity, front face, 168 cm / 60 kg body baseline and Hairstyle A remain recognizably aligned with the BODY_01 Master at technical-review level.
- PASS — pink calibration garment remains opaque; light-nude sheer legwear remains continuous over calves, ankles, heels, insteps and toes without an ankle cutoff, toe band, bare-toe break, plastic gloss or body-paint boundary.
- PASS — neutral-gray stool functions only as support; no chair back, armrests, props, text, watermark, collage or reusable environment design appears.
- PASS — no obvious duplicated/missing limbs, fused legs, broken hips/knees/ankles, duplicated heels or extra/missing digits.

## Source-coverage limitation

No registered L0 seated-articulation image exists. The seated joint relationships are a conservative generated construction from the approved standing Body Master and require user review before approval.

## Scope reminder

This candidate may define only `POSE_03` upright-seated articulation after explicit user approval. It cannot redefine permanent identity/body geometry, Hairstyle A, Calibration Outfit, reusable hosiery material, stool/environment design, other poses or the full `owner_v1.0` release.

## User decision

Rejected. The seated pose and other visible attributes may be retained as text-only guidance, but the face shows iteration pollution and obvious sensitive/blotchy patches. v001 must not be supplied to v002 or used downstream.
