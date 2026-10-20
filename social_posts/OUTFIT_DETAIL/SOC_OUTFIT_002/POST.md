# Social Post Specification

- post_id: `SOC_OUTFIT_002`
- series_id: `OUTFIT_DETAIL`
- asset_level: L3
- status: DRAFT
- content_pillar: `OUTFIT_DETAIL`
- format: `CAROUSEL`
- image_count: 3
- primary_platform: Instagram-style social feed draft
- primary_aspect_ratio/resolution: 4:5 portrait; native generation dimensions to be recorded per image
- requested_publish_window: null
- approval_status: REVIEW_REQUIRED
- generation_gate: AUTHORIZED_BY_USER_ON_2026-10-17

## Everyday moment

An autumn visit to a public forest park, photographed as three spontaneous front-camera moments. The setting is an episode-specific public place, not a recurring location canon. The styling uses `OWNER_CASUAL_AUTUMN_02`; soft-white matte pantyhose stays continuous through feet and toes.

## Image list

| Image asset ID | Intended framing/action | Aspect ratio | Status |
|---|---|---|---|
| `SOC_OUTFIT_002_IMG_01` | Selected image: bent side-sit; left calf tucked beneath right thigh with only left foot emerging; original white hosiery appearance. | 4:5 | CAND_04 approved by user; SELECTED |
| `SOC_OUTFIT_002_IMG_02` | Refined candidate: lively selfie pose in high-mounted convex road mirror (peace sign + phone selfie); golden ginkgo curved road; straight natural legs; continuous white matte hosiery over toes in plush mules. | 3:4 / 4:5 | CAND_11 generated per user direction; REVIEW_REQUIRED |
| `SOC_OUTFIT_002_IMG_03` | Playful selfie at the forest-park café's glass door after dusk; phone fully covers the face; visible café interior and soft overlapping glass reflections. Autumn 02 outfit, cream plush open-toe mules, white hosiery continuous across toes. | 4:5 | CAND_19 in progress; REVIEW_REQUIRED |

## Visible asset versions

- character: `CHR_HUMAN_001_OWNER`
- outfit: `OWNER_CASUAL_AUTUMN_02` dark-brown blazer and pleated skirt with ivory ribbed high-neck knit; use approved clothing-only design reference or written specification
- hosiery/material: medium-thick soft-white matte pantyhose, continuous waist-to-toe textile; visible foot coverage remains intact
- footwear: IMG_01 no shoes; IMG_02 and IMG_03 cream ivory plush open-toe mules; white matte pantyhose continues beneath both toe openings and across toes/toe gaps
- body: if a body image reference is used, use only a deterministic face-excluded derivative
- hairstyle: Hair A for IMG_02 if head is visible; IMG_01 is framed below the face
- environment: temporary forest-park café glass entrance at dusk; not a recurring location
- temporary dressing: orange picnic blanket; simple unbranded snacks/fruit and a closed thermos; no permanent fixtures implied
- fixed props: none

## Platform and crop contract

- portrait 4:5 for all frames
- IMG_01 includes grass, orange mat, food, skirt and legs; keep face and shoes outside frame
- IMG_02 shows the full figure in the lower-center of the circular convex mirror; use continuous wide-angle distortion across the whole mirror disk, including the person
- IMG_03 is a playful full-length selfie facing the glass entrance door of a generic café in the forest park at dusk. The phone fully covers the face. Make the door read as transparent reflective glass: café interior remains visible through the pane while soft, low-contrast reflections of the subject, trees and lights overlap it; avoid a clean mirror-like surface. Keep the exterior park subdued and blue-hour dark, with restrained warm light inside. Autumn 02 outfit, cream plush open-toe mules and continuous white matte hosiery over toes and toe gaps.
- no text, logo, fake UI or watermark

## Carousel-only continuity

Same autumn park outing, same Autumn 02 garments and white hosiery, with footwear selected per image. Each image is generated independently from approved masters. Neither image may define face, body, hair, clothing, hosiery material or identity for the other.

## Acceptance criteria

Credible public forest-park setting; believable phone-camera perspective; IMG_01 has no shoes and IMG_02 and IMG_03 have cream plush open-toe mules; pantyhose remains continuous beneath footwear and visibly covers toes/toe gaps; snacks rest plausibly on the blanket; convex mirror physics for IMG_02 are consistent; no private-residence cues or recurring location claims. IMG_03 is a playful glass-door selfie with visible transmitted interior and soft layered reflections, not a flat mirror.

## Explicit generation gate

- approved by: user
- approval date: 2026-10-17
- approval evidence: “好 开始生成图片吧” — authorizes one candidate each for IMG_01 and IMG_02 only
- IMG_03 generation gate: AUTHORIZED by user on 2026-10-17; later changed on 2026-10-18 to a playful selfie at the forest-park café glass door, phone fully covering the face, open-toe plush mules, continuous hosiery over toes, and visibly reflective/transmissive glass. CAND_19 is in progress under this refinement. CAND_10–CAND_18 remain unapproved earlier candidates and do not define the new shot.
