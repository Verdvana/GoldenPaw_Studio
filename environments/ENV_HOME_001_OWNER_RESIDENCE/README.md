# Owner Residence — Fixed Environment Workspace

- environment_id: `ENV_HOME_001_OWNER_RESIDENCE`
- intended_level: L1 recurring-location Canon
- current_canon_version: none
- status: DRAFT
- lock_status: UNLOCKED

This package fixes the recognizable exterior and interior of the owner's home. Real reference images are L0 and go into the appropriate `source/*/raw/` folder. Generated candidates remain unapproved until domain QA and explicit user approval.

## Responsibility split

- `source/interior/raw/`: real interior rooms, permanent finishes, openings, built-ins, and stable landmarks.
- `source/exterior/raw/`: real facade, roofline, doors/windows, approach, fixed landscaping, and site relationship.
- `source/layout/raw/`: floor plans, sketches, measured diagrams, and room-connection evidence.
- `canon/interior/`: approved room identity and architecture.
- `canon/exterior/`: approved building identity and site-facing views.
- `canon/layout/`: approved spatial relationships and circulation.
- `canon/continuity/`: stable landmark map, screen-direction notes, room adjacency, and camera zones.
- `canon/versions/`: immutable version manifests after explicit lock.

Temporary furniture, decorations, weather, seasonal landscaping, and episode object placement belong to L2 unless explicitly promoted. A room image does not define the characters appearing in it.
