# Character Directory Naming

Use `CHR_<TYPE>_<NNN>_<ALIAS>` for every character folder and asset ID.

| Type | Existing example | Next example |
|---|---|---|
| Human | `CHR_HUMAN_001_OWNER` | `CHR_HUMAN_002_FRIEND` |
| Cat | `CHR_CAT_001_TECH_CAT` | `CHR_CAT_002_NEIGHBOR_CAT` |
| Dog | — | `CHR_DOG_001_<ALIAS>` |
| Other | — | `CHR_<TYPE>_001_<ALIAS>` |

Rules:

- Number independently within each type, using three digits.
- Never reuse an ID, even after a character is retired.
- Keep the ID stable after registration; change the display name in metadata rather than renaming a production folder.
- The alias is short uppercase ASCII with underscores and describes production identity, not an episode-specific costume or role.
- Add the new ID, path, and Canon status to `registries/assets.yaml`.
- Copy the generic character templates; do not clone another character's approved Canon as an identity source.
