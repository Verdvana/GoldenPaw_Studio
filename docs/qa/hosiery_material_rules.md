# Hosiery Material System and QA

## Material definition

Pantyhose is a single continuous textile garment. Define each material with color, denier, transparency, knit/mesh visibility, finish, toe construction, waistband/panel notes, elasticity, compression, and behavior under the intended lighting.

The L1 calibration material is `15D velvet-finish sheer pantyhose`. It is realistic textile—not latex, rubber, PVC, plastic, liquid coating, or body paint—and continuously covers:

`thigh -> knee -> calf -> ankle -> heel -> instep -> toes`

## Visibility logic

- Sheer/15D: skin and burgundy toenail polish may be naturally visible through the textile. Fabric remains visibly present over toes and nails.
- Medium denier: reduce nail visibility according to opacity and lighting.
- Opaque/high denier: do not force nails or toe detail through the fabric.
- Open-toe shoes: obey the declared hosiery toe construction; shoes do not justify a material break.
- Barefoot means no shoes, not no hosiery. Use `legwear: none` only when truly bare legs/feet are intended.

## Reject conditions

Reject the asset if any applicable item is present:

- material ends or changes at ankle, instep, heel, or toes;
- bare/naked toes appear while continuous closed-toe pantyhose is specified;
- polish appears on top of hosiery or is unnaturally enhanced;
- latex/PVC/plastic/rubber/wet/liquid/body-paint surface;
- denier, color, finish, toe construction, or coverage conflicts with design;
- seam, tension, transparency, highlight, or weave changes implausibly across the foot;
- duplicated/missing toes, fused foot/shoe, broken heel, or other anatomy errors.

## Reference isolation

Real hosiery photos are L0 Material Source. They may define textile appearance, coverage, foot transition, transparency, tension, and highlights. They must not define the owner's identity, face, body, skin pigmentation, or proportions.

## Current 15D nude matte routing

- sole/underside-foot QA: `HOS_15D_NUDE_MATTE_BAREFOOT` / `IMG_2562.jpg`;
- crouching QA: `HOS_15D_NUDE_MATTE_CROUCHING` / `IMG_2579.jpg`, with `IMG_2580.jpg` for the side response when needed;
- standing QA: `HOS_15D_NUDE_MATTE_STANDING` / `IMG_2581.jpg`.

These are deliberately narrow responsibilities. Do not supplement them with deleted files; record a coverage gap instead.
