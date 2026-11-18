#!/usr/bin/env python3
"""Mini's per-system art, generated from the Canvas theme's (Siddy212, CC BY-NC-SA):
  art/devices/<system>.png  the console drawn as pixel art: Canvas's device picture (else its
                            carousel icon) shrunk, cut to a few colours, enlarged without smoothing
  art/logos/<system>.svg    Canvas's logo, as is (the theme tints it)
Usage: gen_assets.py <canvas>/_inc/systems <theme>/v2/art [px=4] [colors=24]
"""
import os, shutil, sys
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
PX = int(sys.argv[3]) if len(sys.argv) > 3 else 4
COLORS = int(sys.argv[4]) if len(sys.argv) > 4 else 24
BOX = (288, 176)   # the drawing's room on a card, px at 1080p

def pixel(path):
    im = Image.open(path).convert('RGBA')
    bbox = im.getchannel('A').point(lambda v: 255 if v > 16 else 0).getbbox()
    if bbox: im = im.crop(bbox)
    im.thumbnail((BOX[0] // PX, BOX[1] // PX), Image.LANCZOS)
    alpha = im.getchannel('A').point(lambda v: 255 if v > 110 else 0)
    rgb = im.convert('RGB').quantize(COLORS, method=Image.Quantize.MEDIANCUT).convert('RGB')
    im = rgb.convert('RGBA'); im.putalpha(alpha)
    im = im.resize((im.width * PX, im.height * PX), Image.NEAREST)
    return im.quantize(COLORS + 1, method=Image.Quantize.FASTOCTREE)   # a palette PNG: small

os.makedirs(f'{out}/devices', exist_ok=True); os.makedirs(f'{out}/logos', exist_ok=True)
n = 0
for f in sorted(os.listdir(f'{src}/logos')):
    if not f.endswith('.svg'): continue
    name = f[:-4]
    shutil.copyfile(f'{src}/logos/{f}', f'{out}/logos/{f}')
    for pic in (f'{src}/devices/{name}.webp', f'{src}/carousel-icons-icons/{name}.webp'):
        if os.path.exists(pic):
            pixel(pic).save(f'{out}/devices/{name}.png', optimize=True); n += 1
            break
print(f'{n} devices, {len(os.listdir(out + "/logos"))} logos')
