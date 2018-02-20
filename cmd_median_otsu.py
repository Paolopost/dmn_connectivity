#!/usr/bin/env python

import sys
import argparse
import numpy as np
import nibabel as nib
from dipy.segment.mask import median_otsu


def cmd_median_otsu(b0_src, diff_out, mask_out):

    b0_img = nib.load(b0_src)
    b0_data = b0_img.get_data()
    b0_aff = b0_img.affine

    b0_diff, nodiff_mask = median_otsu(b0_data, 2, 1)

    b0_diff_img = nib.Nifti1Image(b0_diff.astype(np.float32), b0_aff)
    nodiff_mask_img = nib.Nifti1Image(nodiff_mask.astype(np.int16), b0_aff)
    nib.save(b0_diff_img, diff_out)
    nib.save(nodiff_mask_img, mask_out)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('b0_src', nargs='?',default='',
                        help='The source dwi file')
    parser.add_argument('diff_out', nargs='?', default='',
                        help='The output masked diffusion file')
    parser.add_argument('mask_out', nargs='?', default='',
                        help='The output dwi mask file')
    
    args = parser.parse_args()

    cmd_median_otsu(args.b0_src, args.diff_out, args.mask_out)

    sys.exit()

