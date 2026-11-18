# Mini

A mini-console style theme for REG-Station on TV screens (640x480 to 1920x1080): the systems as
a looping row of cards (logo, the console drawn as pixel art, maker and year), console-grey bands
with the help at the top and the system's logo at the bottom, the games as a framed list beside
the selected game's box. Skins (theme option `skin`): purple, black, green, grey.

Written in REG-Station's theme v2 format (REG-Station `docs/arch/THEME-V2-FORMAT.md`); needs a
REG-Station build that loads themes written in v2. Install: copy this directory to
`/userdata/themes/Mini` and pick Mini as the theme.

| path | holds |
|---|---|
| `v2/theme.json` | the skin option, the include list |
| `v2/vars.json` | the look by name; a skin changes colours only |
| `v2/components.json` | shared nodes (background, help, list rows, buttons, task) |
| `v2/mini.json` | the console bands |
| `v2/views/` | system (cards), gamelist/basic, menu, dialog, screen (status, notifications, screensaver) |
| `v2/art/devices/` | each system's console as pixel art (generated) |
| `v2/art/logos/` | each system's logo (from Canvas) |
| `tools/gen_assets.py` | makes `v2/art` from Canvas's `_inc/systems` (Pillow) |

Regenerate the art: `python3 tools/gen_assets.py <es-theme-canvas>/_inc/systems v2/art`.

Licence and marks: see NOTICE.md.
