"""
Strip baked checkerboard pseudo-transparency from Ludo Edit Image output.

Ludo's Edit Image "Remove background" operation visually produces a transparent
PNG (checkerboard pattern visible), but the output is RGB with the checkerboard
baked as actual pixels (drift pattern #23). This script keys out the checkerboard
to produce true RGBA, ready for Godot import.

Usage:
    python key_out_checkerboard.py input.png output.png

The keying is robust against Ludo's standard checkerboard:
  - Desaturated grays (R~=G~=B within tolerance)
  - Brightness range ~200-255
  - Saturated art (building colors, character art) is untouched

Steps:
  1. Detect background pixels: desaturated + bright
  2. Set alpha to 0 on background, 255 elsewhere
  3. Erode alpha 1px to clean up anti-aliased edge halos
  4. Crop to bounding box of opaque content

Tunables (rarely needed):
  - gray_tolerance: how close R/G/B must be to register as "gray" (default 12)
  - brightness_threshold: minimum brightness for "background" (default 200)
  - erode: alpha erosion for edge cleanup (default True)
"""

import sys
from PIL import Image, ImageFilter
import numpy as np


def key_out_checkerboard(input_path, output_path,
                         gray_tolerance=12,
                         brightness_threshold=200,
                         erode=True):
    img = Image.open(input_path).convert('RGBA')
    arr = np.array(img)

    r = arr[..., 0].astype(int)
    g = arr[..., 1].astype(int)
    b = arr[..., 2].astype(int)

    gray = (
        (np.abs(r - g) < gray_tolerance) &
        (np.abs(g - b) < gray_tolerance) &
        (np.abs(r - b) < gray_tolerance)
    )
    bright = arr[..., 0] > brightness_threshold
    bg_mask = gray & bright

    arr[..., 3] = np.where(bg_mask, 0, 255)
    keyed = Image.fromarray(arr, 'RGBA')

    if erode:
        alpha = keyed.split()[3]
        alpha = alpha.filter(ImageFilter.MinFilter(3))
        keyed.putalpha(alpha)

    bbox = keyed.getbbox()
    if bbox:
        keyed = keyed.crop(bbox)

    keyed.save(output_path)
    print(f"Keyed: {input_path} -> {output_path} ({keyed.size})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python key_out_checkerboard.py input.png output.png")
        sys.exit(1)
    key_out_checkerboard(sys.argv[1], sys.argv[2])
