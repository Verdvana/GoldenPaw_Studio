# HAIRSTYLE_A — Partial Approval

Primary L0 real reference: `L0_OWNER_017` — `source/identity/raw/DSC00847.jpg`.

It is authoritative for the A design's long, straight, loose-hair direction: near-center parting, natural low-to-moderate crown volume, long face-framing front panels, length extending below the chest in the source view, straight texture with subtle natural irregularity, and tapered ends. Outdoor color cast and highlights must be neutralized when building Canon.

It must not define face identity, body, skin, pink jacket, outdoor lighting, or background. The source lacks side/back coverage, so those angles are generated from the L0 reference + approved Face Canon + written A definition, never from an AI A→A chain.

Use `templates/character/HAIRSTYLE.md` to define and approve six views: front, 3/4, side, back, high-camera/subject-looking-up, and low-camera/subject-looking-down. The two high/low-camera assets are perspective-calibration views and must not redefine face identity. Component status is `PARTIAL_APPROVED`: only the explicitly listed approved front component is Canon; the remaining five views are still pending, and folder location alone grants no Canon authority.

## HAIR_A_01 execution status

`HAIR_A_01_FRONT_v001` was generated from the approved front-neutral Face Master plus the deterministic face-masked derivative of `L0_OWNER_017`. No previous Hair candidate, Body image or Hairstyle-B image was supplied. The near-center part, controlled crown volume, long straight front panels, dark-brown tone and natural strand irregularity are present, but the longest tips are clipped by the bottom frame. Technical QA therefore fails the complete-hair-edge contract. The candidate remains `REVIEW_REQUIRED` and is not Canon; any v002 must return to the same two scoped references rather than using v001 pixels.

The user confirmed that v001 was otherwise acceptable but found the nose slightly too large. This is treated as face drift inside a Hair candidate, not as a new facial-design instruction. v002 must return the visible nose to the approved `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` proportions, preserve the accepted hairstyle attributes only through written constraints, and widen/lower the crop enough to show all tapered hair ends with clear space beneath them. v001 pixels remain prohibited.

`HAIR_A_01_FRONT_v002` was independently generated from the same two scoped references. Technical precheck found the nose presentation more restrained and broadly returned toward the approved Face Master; all Hairstyle-A front design checks passed, and every longest tapered tip is fully visible with lower breathing room. The user explicitly approved it on 2026-09-12, and its sole raster was moved to `approved/HAIR_A_01_FRONT/OWNER_HAIR_A_01_FRONT_CANON_001.png` as an attribute-scoped L1 component. Its authority is limited to the standard eye-level front Hairstyle-A appearance; it does not define face or nose identity, body, outfit, other Hairstyle-A angles, Hairstyle B, lighting or background. Five Hairstyle-A views remain pending, and neither Hairstyle A as a complete set nor `owner_v1.0` is locked.
