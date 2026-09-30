# QA — SOC_TRAVEL_002_IMG_04_CAND_01

Status: `REVIEW_REQUIRED`

After generation, inspect:

- Pose/camera: seated side pose, torso/head turned back, lively laugh, same bent/extended leg arrangement, lounger relationship, angle, crop and subject scale as reference 4.
- Owner face: compare only against approved Face Canon after generation; check feature relationships, natural skin color/texture, projection, and no blotches, muddy relighting, smudges, patches or iterative-generation artifacts.
- Hair: Hairstyle B, not the reference model's hairstyle.
- Wardrobe: approved camisole, denim shorts, earrings; no reference-image accessories or styling.
- Hosiery: one continuous light-nude textile from waist through feet/toes where visible; no gaps, bare toes, toe-cap boundary or latex/plastic appearance; natural drape/tension and softened burgundy nails beneath the hosiery where visible.
- Footwear: no shoes visible anywhere.
- Series: same cruise day, camera character, natural daylight, white balance, exposure, contrast and color as approved shot 02.
- Framing/content: 4:5 vertical, no added text, watermark, UI, readable brands or source leakage.

On a safety block, preserve the generation record, mark `GENERATION_BLOCKED_SAFETY`, leave QA as not applicable, and do not retry this shot without a changed user direction.

## First inspection

- Pose/camera: `PASS` — side-seated lounger pose, turned-back laughing expression, raised bent knee, second leg extended across the lounger, near hand braced on the cushion, and passenger-deck side framing are present and closely follow reference 4.
- Face/hair: `PASS_WITH_USER_REVIEW` — face reads as the owner and shows no obvious blotches or muddy relighting; B updo and approved earrings are present. Final identity approval remains with the user.
- Wardrobe/footwear: `PASS` — approved summer camisole and denim shorts; no shoes visible.
- Hosiery: `REVIEW_REQUIRED` — feet/toes appear veiled and the burgundy polish is softened, but the sheer textile is difficult to distinguish from bare skin across the legs in this bright exposure. Confirm whether the textile reads clearly enough; otherwise a focused material correction is needed.
- Series look: `PASS_WITH_USER_REVIEW` — same bright ship-deck daylight and natural phone-photo character; highlights/background are somewhat brighter and more detailed than shot 02.
- Framing: `REVIEW_REQUIRED` — native output is 1071×1469 (about 0.729 aspect), narrower than the post's 4:5 target. No stretching or reframing was applied.
- No visible watermark, overlay text, UI or readable brand.
