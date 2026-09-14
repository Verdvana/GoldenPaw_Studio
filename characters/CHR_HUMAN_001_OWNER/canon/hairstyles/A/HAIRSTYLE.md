# HAIRSTYLE_A — Partial Approval

Primary L0 real reference: `L0_OWNER_017` — `source/identity/raw/DSC00847.jpg`.

It is authoritative for the A design's long, straight, loose-hair direction: near-center parting, natural low-to-moderate crown volume, long face-framing front panels, length extending below the chest in the source view, straight texture with subtle natural irregularity, and tapered ends. Outdoor color cast and highlights must be neutralized when building Canon.

It must not define face identity, body, skin, pink jacket, outdoor lighting, or background. The source lacks side/back coverage, so those angles are generated from the L0 reference + approved Face Canon + written A definition, never from an AI A→A chain.

Use `templates/character/HAIRSTYLE.md` to define and approve six views: front, 3/4, side, back, high-camera/subject-looking-up, and low-camera/subject-looking-down. The two high/low-camera assets are perspective-calibration views and must not redefine face identity. Component status is `PARTIAL_APPROVED`: only the explicitly listed approved front component is Canon; the remaining five views are still pending, and folder location alone grants no Canon authority.

## HAIR_A_01 execution status

`HAIR_A_01_FRONT_v001` was generated from the approved front-neutral Face Master plus the deterministic face-masked derivative of `L0_OWNER_017`. No previous Hair candidate, Body image or Hairstyle-B image was supplied. The near-center part, controlled crown volume, long straight front panels, dark-brown tone and natural strand irregularity are present, but the longest tips are clipped by the bottom frame. Technical QA therefore fails the complete-hair-edge contract. The candidate remains `REVIEW_REQUIRED` and is not Canon; any v002 must return to the same two scoped references rather than using v001 pixels.

The user confirmed that v001 was otherwise acceptable but found the nose slightly too large. This is treated as face drift inside a Hair candidate, not as a new facial-design instruction. v002 must return the visible nose to the approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` proportions, preserve the accepted hairstyle attributes only through written constraints, and widen/lower the crop enough to show all tapered hair ends with clear space beneath them. v001 pixels remain prohibited.

`HAIR_A_01_FRONT_v002` was independently generated from the same two scoped references. Technical precheck found the nose presentation more restrained and broadly returned toward the approved Face Master; all Hairstyle-A front design checks passed, and every longest tapered tip is fully visible with lower breathing room. The user explicitly approved it on 2026-09-12, and its sole raster was moved to `approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` as an attribute-scoped L1 component. Its authority is limited to the standard eye-level front Hairstyle-A appearance; it does not define face or nose identity, body, outfit, other Hairstyle-A angles, Hairstyle B, lighting or background. Five Hairstyle-A views remain pending, and neither Hairstyle A as a complete set nor `owner_v1.0` is locked.

## HAIR_A_02 execution status

`HAIR_A_02_3Q_v001` was independently generated from the approved left-three-quarter Face Master and the deterministic face-masked L0 Hairstyle-A derivative. No approved HAIR_A_01 raster or generated Hair candidate was supplied. Technical precheck passes the left-3/4 direction, near-center part, controlled crown, near/far face-side panels, long straight loose fall, complete below-chest length and unclipped tapered ends. Lower clearance beneath the longest near-side tips is slightly narrower than the prompted ideal but remains fully inspectable. The candidate is `REVIEW_REQUIRED`, has no Canon authority and cannot be used downstream before explicit user approval.

The user explicitly approved this candidate on 2026-09-14 with “不错，合格”. Its sole raster was moved to `approved/HAIR_A_02_3Q/OWNER_HAIR_A_02_3Q_CANON_001.png`. Approval is limited to the visible left-three-quarter Hairstyle-A attributes; contextual face, skin, expression, body and outfit remain outside Hair authority. Four Hairstyle-A views remain pending.

## HAIR_A_03 execution status

`HAIR_A_03_SIDE_v001` was independently generated from the approved anatomical-left profile Face Master and the deterministic face-masked L0 Hairstyle-A derivative. No approved HAIR_A_01/02 raster or generated Hair candidate was supplied. Technical precheck passes the anatomical-left true-profile direction with the nose pointing image-right, readable forehead hairline and near-ear relation, controlled crown/rear-head contour, unobscured facial profile, distinct front/rear long straight fall, restrained dark-brown highlights, complete below-chest length and unclipped tapered ends. The candidate remains `REVIEW_REQUIRED`, has no Canon authority and cannot be used downstream before explicit user approval.

The user explicitly approved this candidate on 2026-09-14 with “批准”. Its sole raster was moved to `approved/HAIR_A_03_SIDE/OWNER_HAIR_A_03_SIDE_CANON_001.png`. Approval is limited to the visible anatomical-left standard-side Hairstyle-A attributes; contextual face, skin, expression, body and outfit remain outside Hair authority. The profile Face evidence limitation remains disclosed. Three Hairstyle-A views remain pending.

## HAIR_A_04 execution status

`HAIR_A_04_BACK_v001` was independently generated from the approved rear Body Master and the deterministic face-masked L0 Hairstyle-A derivative. No approved HAIR_A_01/02/03 raster, generated Hair candidate, Face, Expression, Pose or Shot was supplied. The first ImageGen call returned no image after output moderation; one targeted neutral technical-archive retry succeeded. Technical precheck passes the centered exact rear direction with no facial edge, complete crown/rear contour, natural top flow, controlled rear mass, long predominantly straight loose dark-brown fall, lower-back projected length, tapered irregular ends, full edge visibility, pink Calibration Outfit and neutral studio presentation. The candidate remains `REVIEW_REQUIRED`, has no Canon authority and cannot be used downstream before explicit user approval. Three Hairstyle-A views remain pending until this candidate is approved.

The user explicitly approved it on 2026-09-14 with “批准，下一项”. Its sole raster was moved to `approved/HAIR_A_04_BACK/OWNER_HAIR_A_04_BACK_CANON_001.png`. Approval is limited to the exact rear Hairstyle-A crown flow, rear contour/mass, shoulder-neck fall, complete silhouette, length, density, tonal response and tapered ends; contextual body, skin, clothing and lighting remain outside Hair authority. Two Hairstyle-A views remain pending.

## HAIR_A_05 execution status

`HAIR_A_05_HIGH_CAMERA_LOOK_UP_v001` was independently generated from the approved front-neutral Face Master and the deterministic face-masked L0 Hairstyle-A derivative. No approved HAIR_A_01/02/03/04 raster or generated Hair candidate was supplied. Technical precheck confirms a clearly elevated/downward camera with the whole head raised toward the lens, near-frontal identity context, readable upper-forehead hairline, complete crown surface and near-center part path, controlled crown, backward/outward displacement of both long straight dark-brown panels, full outer silhouette and unclipped tapered ends. The candidate remains `REVIEW_REQUIRED` and cannot define neutral eye-level face geometry, body, clothing, other Hair views or Canon status.

The user explicitly approved it on 2026-09-14 with “批准 下一个”. Its sole raster was moved to `approved/HAIR_A_05_HIGH_CAMERA_LOOK_UP/OWNER_HAIR_A_05_HIGH_CAMERA_LOOK_UP_CANON_001.png`. Approval is limited to Hairstyle-A projection under the high-camera/subject-looking-up relationship; high-angle face foreshortening, body posture, clothing and lighting remain outside Hair authority. One Hairstyle-A view remains pending.

## HAIR_A_06 execution status

`HAIR_A_06_LOW_CAMERA_LOOK_DOWN_v001` was independently generated from the approved front-neutral Face Master and deterministic face-masked L0 Hairstyle-A derivative, without approved HAIR_A_01–05 or generated Hair pixels. Attempt 1 failed because the camera still read near eye level and was not saved to the project. A targeted retry establishes a clear below-chin upward view with readable chin underside, reduced crown surface, near-center frontal part, low-angle jaw/ear-side panels and complete tapered ends. Whole-head downward flexion and forward panel swing are restrained user-review points. The candidate remains `REVIEW_REQUIRED`.

The user rejected v001 because its facial relief is too pronounced and because too much crown surface/part remains visible for a low-camera view. v001 is `USER_REJECTED` and cannot be supplied to v002. The independent v002 correction requires softer/flatter approved facial relief, clearer whole-head downward flexion, no visible crown surface and at most a very short frontal part trace.

The user found v002's face close but rejected its hairstyle root-flow origin as clearly image-right. The fixed Hairstyle-A part/root-flow origin reads slightly image-left of center, approximately 47–48% of image width in a centered front projection. v003 must preserve the low-camera no-crown/no-scalp presentation while placing the hidden-part-derived frontal flow apex at that location. A01 is measurement-only and is not a v003 pixel input; v002 is prohibited.

The user explicitly approved v003 with “批准，下一项”. Its sole raster was moved to `approved/HAIR_A_06_LOW_CAMERA_LOOK_DOWN/OWNER_HAIR_A_06_LOW_CAMERA_LOOK_DOWN_CANON_001.png`. All six Hairstyle-A view components are now approved, while the full `owner_v1.0` remains unlocked.
