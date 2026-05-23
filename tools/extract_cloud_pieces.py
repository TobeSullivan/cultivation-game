"""
Extract individual cloud forms from a keyed clouds PNG into separate sprite files.

Input: a true-RGBA cloud-band PNG (e.g. assets/hub/clouds.png after key_out_checkerboard).
Output: one PNG per connected-component blob in the alpha channel, bbox-cropped,
        written to <output_dir>/cloud_NN.png (zero-padded, 1-indexed).

Connected components are found via 8-connectivity on the alpha>0 mask.
Tiny blobs below `min_area` pixels are skipped as keying noise.

Usage:
    python extract_cloud_pieces.py input.png output_dir [--min-area N]

Example:
    python extract_cloud_pieces.py assets/hub/clouds.png assets/hub/clouds/
"""

import argparse
import os
import sys
from PIL import Image
import numpy as np
from scipy.ndimage import label, find_objects


def extract(input_path: str, output_dir: str, min_area: int = 200) -> None:
    img = Image.open(input_path).convert("RGBA")
    arr = np.array(img)
    alpha = arr[..., 3]
    mask = alpha > 0

    # 8-connectivity (includes diagonals)
    structure = np.ones((3, 3), dtype=int)
    labeled, num_labels = label(mask, structure=structure)
    slices = find_objects(labeled)

    os.makedirs(output_dir, exist_ok=True)

    kept = 0
    skipped = 0
    for i, sl in enumerate(slices, start=1):
        if sl is None:
            continue
        component_mask = labeled[sl] == i
        area = int(component_mask.sum())
        if area < min_area:
            skipped += 1
            continue

        # Crop the RGBA image to bbox; zero out pixels belonging to other components
        crop = arr[sl].copy()
        crop[..., 3] = np.where(component_mask, crop[..., 3], 0)
        out_img = Image.fromarray(crop, "RGBA")

        kept += 1
        out_path = os.path.join(output_dir, f"cloud_{kept:02d}.png")
        out_img.save(out_path)
        h, w = component_mask.shape
        print(f"  cloud_{kept:02d}.png  bbox=({sl[1].start},{sl[0].start})-({sl[1].stop},{sl[0].stop})  size={w}x{h}  area={area}")

    print(f"\nExtracted {kept} cloud pieces (skipped {skipped} below min_area={min_area}) into {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input PNG (keyed, true RGBA)")
    parser.add_argument("output_dir", help="Output directory for cloud_NN.png files")
    parser.add_argument("--min-area", type=int, default=200,
                        help="Skip components smaller than this pixel count (default 200)")
    args = parser.parse_args()
    extract(args.input, args.output_dir, args.min_area)
