# Social Post Specification

- post_id: `SOC_OUTFIT_001`
- series_id: `OUTFIT_DETAIL`
- asset_level: L3
- status: DRAFT
- content_pillar: `OUTFIT_DETAIL`
- format: `CAROUSEL`
- image_count: 3
- primary_platform: Instagram-style social feed (draft)
- primary_aspect_ratio/resolution: `4:5`, 1024×1280 target (native supported portrait if unavailable)
- requested_publish_window: null
- approval_status: REVIEW_REQUIRED

## Everyday moment

A casual autumn walk with three independent, believable selfies in temporary public places. Image 01 is an arm-length front-camera selfie by a café's street-facing window; the window gives a faint partial reflection as a visual accent. This is a one-off public setting, not a recurring location canon.

## Image list

| Image asset ID | Candidate ID | Intended framing/action | Aspect ratio | Status |
|---|---|---|---|---|
| `SOC_OUTFIT_001_IMG_01` | `SOC_OUTFIT_001_IMG_01_CAND_03` | Front-camera selfie by café street window; slight side turn; partial faint window reflection | 4:5 | APPROVED_L3 |
| `SOC_OUTFIT_001_IMG_02` | pending | Public bench overhead autumn-leaf selfie | 4:5 | DRAFT; not authorized |
| `SOC_OUTFIT_001_IMG_03` | pending | Side-crouch full-body selfie in a shop fitting-room mirror | 4:5 | DRAFT; not authorized |

## Visible asset versions

- owner source-derived Face method and L0/L0-derived inputs: `OWNER_FACE_01_FRONT_NEUTRAL_METHOD_V1`; geometry crop `OWNER_FACE_L0_OWNER_013_GEOMETRY_CROP_001`; natural skin context crop `OWNER_FACE_L0_OWNER_012_SKIN_CONTEXT_CROP_001`
- owner face QA comparison only: `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001`
- body (face-excluded derivative only): `OWNER_BODY_01_FRONT_V025_FACE_EXCLUDED_v1`
- hairstyle: `OWNER_HAIR_A_01_FRONT_CANON_001` (hair-only responsibility; Hair A required)
- cat: none
- outfit: `OWNER_CASUAL_AUTUMN_02_WORN_FRONT_v012` (outfit-only responsibility)
- hosiery/material: included only as part of the scoped outfit ref; outfit image defines matte white continuous pantyhose and toe coverage, no close foot detail in this image
- fixed props: none
- environment: temporary generic public café street window, no distinct venue identity or readable signage
- temporary dressing: autumn street tree reflections and soft, indistinct passersby outside; no legible text or brand marks

## Platform and crop contract

- must preserve: face and hair silhouette, natural front-camera framing, upper outfit details, soft reflection visibly secondary to the real subject
- safe areas / prohibited edge crops: keep face and hair away from edges; crop around upper torso; do not force legs/shoes into this selfie
- text, logo, UI, watermark policy: none

## Carousel-only continuity

Keep the same autumn outfit and same general daytime walk only. Each image is independently generated. No image in this carousel defines face, body, hair, outfit, hosiery, material, fixed props or environment for another image.

## Acceptance criteria

A believable handheld front-camera selfie, unmistakably not a mirror selfie; public café window reflection is faint and physically plausible; outfit components match approved Autumn 02; owner face is source-derived with no AI face/body generation input; natural skin without blotches or relighting contamination; no private residence cues, brands, legible text, fake interface or watermark.

## Explicit generation gate

- approved by: user
- approval date: 2026-10-17
- approval evidence: user said “ok,先产生第一张吧” after specifying image 01 as a café-window front-camera selfie with a partial reflection.
