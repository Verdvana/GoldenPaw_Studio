# Social Post Specification

- post_id: `SOC_CAMPUS_001`
- series_id: `CAMPUS`
- asset_level: `L3`
- status: `DRAFT`
- content_pillar: `OUTFIT_DETAIL`
- format: `SINGLE`
- image_count: `1`
- primary_platform: `social feed`
- primary_aspect_ratio/resolution: `4:5 / 1024x1280 target`
- requested_publish_window: null
- approval_status: `REVIEW_REQUIRED`

## Everyday moment

An adult college student takes a casual handheld phone photo while relaxing in her chair in a lived-in four-person women's dorm room at night. A clear plastic takeaway bag holding a fried chicken cutlet rests on her lap. Her legs extend forward, ankles loosely crossed, with both heels resting on the floor. She is wearing the registered campus outfit and has taken off her sneakers; the charcoal pantyhose remain on.

## Image list

| Image asset ID | Candidate ID | Intended framing/action | Aspect ratio | Status |
|---|---|---|---|---|
| `SOC_CAMPUS_001_IMG_05` | `SOC_CAMPUS_001_IMG_05_CAND_01` | Seated phone POV toward lap and crossed lower legs; takeaway chicken visible | 4:5 | `REVIEW_REQUIRED` |

## Visible asset versions

- owner source-derived Face method and L0/L0-derived inputs: not applicable; face outside frame
- owner face QA comparison only: not applicable; face outside frame
- body (face-excluded derivative only): none; body proportions are not specified by an image reference
- hairstyle: not visible
- cat: none
- outfit: text continuity from approved `SOC_CAMPUS_001_IMG_01`–`IMG_03`: relaxed light cardigan, plain light T-shirt, dark charcoal/navy plaid A-line skirt, charcoal-black matte semi-sheer pantyhose, simple white low-top canvas sneakers removed for this moment
- hosiery/material: charcoal-black matte semi-sheer continuous pantyhose, same text-defined campus styling; no material photo used
- fixed props: none
- environment: temporary generic four-person women's dorm room at night; no established fixed-location Canon
- temporary dressing: ordinary chair, four beds/bunks, desks and personal clutter; clear takeaway bag with one chicken cutlet

## Platform and crop contract

- must preserve: lap and bagged chicken in the lower-middle frame, both legs extending forward, crossed ankles, both heel contacts visible on floor, context of shared dorm
- safe areas / prohibited edge crops: keep both feet, heels, and food bag fully inside the image; crop above shoulders so face is not visible
- text, logo, UI, watermark policy: none unless explicitly specified

## Carousel-only continuity

Not applicable; standalone image.

## Acceptance criteria

Casual non-suggestive everyday dorm snapshot; adult subject; natural hand-held phone perspective; both shoes fully off and absent; heels visibly grounded; legs crossed at ankles; fried chicken and its clear plastic takeaway bag rest plausibly on the skirt-covered lap; outfit matches registered text description. Face and identifying dorm/school details stay out of frame.

## Explicit generation gate

- approved by: user
- approval date: 2026-10-16
- approval evidence: `校园主题加一张图片` followed by a specific scene, outfit, pose, props, and camera description in the user request.
