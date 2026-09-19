# Worn-Front QA

- candidate: `OWNER_WORK_AUTUMN_01_WORN_FRONT_v001`
- status: REJECTED

## Passed

- Full-body front composition includes head, hands, shoes, and feet.
- Gray cropped straight-leg trousers and black sheer hosiery read clearly.
- Feet are fully planted, with no obvious duplicated limbs or malformed hands.

## Rejection reasons

- Face QA comparison against `OWNER_FACE_01_FRONT_NEUTRAL_CANON_001` shows identity drift; this candidate cannot be used downstream.
- Hair is rendered in a half-up arrangement rather than the required HAIRSTYLE_A long, straight, loose hair.
- The white knit top is a high crew/mock neck rather than the specified collared knit sweater.
- The shoes retain a visible red outsole, an expressly excluded property of `REF_001`.

The user rejected all current autumn-officewear generated candidates on 2026-09-19.
The candidate pixels were removed and must never be used as a generation input. No approval or promotion was made.
