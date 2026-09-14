# QA — POSE_06_BENDING_REACHING_v001

```yaml
candidate_id: POSE_06_BENDING_REACHING_v001
qa_status: FAIL_USER_REVISION_BARE_FOOT_LOOK
approval_status: REJECTED
reviewed_at: "2026-09-13"
```

## Pose and anatomy

- PASS — one 1086×1448 exact-3:4 image with full hair, reaching hand, legs and feet inside frame.
- PASS — clear forward/down reach, moderate hip hinge, naturally long spine, softly flexed knees and a lowered balancing arm.
- PASS — reaching hand and visible fingers are plausible; no obvious extra/missing limbs, fused joints or support-object artifacts.
- PASS — the rear foot is naturally plantar-flexed with forefoot support and a raised heel. Per the user's cross-type QA correction, this is biomechanically valid for a Pose asset and is not subject to the Body-turnaround requirement for both feet to lie flat.

## Identity and appearance

- PASS — approved left-three-quarter facial identity, neutral expression and clean even skin remain aligned at technical-review level.
- PASS — approved 168 cm / 60 kg body context and Hairstyle A remain broadly consistent; hair falls forward plausibly with gravity.
- PASS — pink Calibration Outfit and subtly visible burgundy toenails are present; fingernails remain natural.
- FAIL — the 15D nude matte textile veil is too weak across the feet, so the feet read close to bare skin despite no hard ankle cutoff. The user requested the scoped `HOS_15D_NUDE_MATTE_FOOT_TEXTURE_USER_001` reference for stronger fabric presence.

## Lineage and scope

Generated independently from approved left-three-quarter Face, left-three-quarter Body and Hair-A L1 Masters. No Pose image was supplied. No matching L0 bending/reaching source is registered.

## Recommendation

Do not promote v001. The user authorized v002 as an independent reconstruction from the same three approved Masters plus the scoped 15D nude matte material derivative. Preserve the accepted raised-heel pose in text only; strengthen visible textile presence without importing the material source's pose, anatomy, skin, nail color, clothing, background or floor contact. v001 must not be a pixel input or downstream reference.
