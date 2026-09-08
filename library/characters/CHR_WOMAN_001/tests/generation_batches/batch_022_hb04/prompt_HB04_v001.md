# HB04 v001 实际成功生成规格

## 输入职责

- `source_photos/DSC01276.JPG`：发型 B 的近中分、头顶体积、向后收发和碎发。
- `source_photos/DSC01595.JPG`：发型 B 与真人身份补充。
- `IMG_8108_input_working.png`：授权原照 `IMG_8108.jpg` 的无损首帧格式转换，只提供真人面部几何和轻度高机位参考；不使用其发型、服装、道具或环境。
- `source_photos/DSC01015.JPG`：真人身份、头肩比例和深棕发色。
- 没有向生成器输入任何 AI 生成图；HB03 仅作生成后的人工对照。

## 实际成功提示词

```text
Use case: photorealistic-natural
Asset type: production character continuity candidate, CHR_WOMAN_001 hair structure HB04
Primary request: Generate a new light high-angle frontal studio portrait of the same authorized 26-year-old Chinese woman to inspect hairstyle B's front hairline, narrow near-center part, crown volume and backward root direction. This is a fresh generation from authorized real photos only, not an edit of any generated image.
Input images: Image 1 is the main real hairstyle-B source for the near-center separation, modest crown lift, upward/backward gathering and sparse asymmetric temple strands. Image 2 is supplementary real hairstyle-B and identity evidence. Image 3 is a lossless format conversion of an authorized real photo, used only for the same person's facial geometry and a mild elevated-camera perspective cue; do not copy its loose hair, clothes, props or room. Image 4 is primary real-person identity and head/shoulder proportion evidence; do not copy its loose hair, smile, sports jacket or outdoor scene.
Subject: same real woman, centered and upright, head level, shoulders level, closed-mouth neutral expression. Eyes look naturally toward the slightly elevated camera without lifting the chin or bowing the head. Preserve her real broad cheeks, eye shape and spacing, nose, lips, jaw, age and natural asymmetry. Restrained natural makeup. Plain smooth pink sleeveless studio test garment, not ribbed knit, no jewelry.
Hairstyle B: dark brown-black hair, soft narrow near-center part beginning at the front hairline and continuing naturally across the crown, slightly off perfect geometric center. Natural scalp is visible only within this narrow line. Roots sweep outward and then smoothly backward; crown volume is modest and rounded, not radial, teased, bouffant or a cowlick swirl. Both sides gather cleanly behind the ears with only one or two fine asymmetric face-framing strands. No bangs and no long loose hair on shoulders or chest.
Textual continuity target from the approved rear design: the gathered lengths continue to one compact vertical folded/twisted updo at the middle back of the head, with tucked ends, secured by one medium dark translucent tortoiseshell-brown acetate claw clip at mid-occiput. In this frontal light high-angle view, the clip must remain behind the crown and should be completely hidden or show only a tiny anatomically plausible upper edge. It must never rise above the crown silhouette, sit on top of the head, or resemble a topknot. Do not invent a second clip.
Composition/framing: vertical portrait with a centered natural portrait lens. Camera only 12–15 degrees above eye level, much milder than a steep top-down shot. Show the complete front hairline, narrow part and enough crown surface to read backward flow while keeping the full face undistorted. Frame from clean space above crown through shoulders and upper torso. The camera is elevated; the woman does not lean forward or look upward sharply.
Scene and light: warm-neutral seamless studio, large soft cinematic key and gentle fill, stable white balance, realistic grouped hair strands and clean skin/fabric fields.
Constraints: use only the supplied authorized real photos as generator inputs. Preserve real identity without further eye enlargement, face narrowing, jaw sharpening, nose/lip changes, plastic skin or heavy beautification. The hairstyle design is specified textually and will be checked manually against approved continuity assets afterward.
Avoid: steep bird's-eye angle, bowed head, hunched/leaning torso, upward-staring eyes, facial foreshortening, visible claw clip above crown, clip on top of head, topknot, round bun, ponytail, braid, hair stick, scrunchie, long loose hair, wide scalp gap, radial cowlick, bald spot, oily helmet hair, crushed blacks, excessive flyaways, ribbed tank fabric, text, watermark, border, collage or multiple views.
```
