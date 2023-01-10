import cv2 as cv
import numpy as np


def  Brightness(_2Dlist_local_old_im, _int_local_offset):
    row, column, channal = _2Dlist_local_old_im.shape

    _2Dlist_local_new_im = np.zeros((row, column, channal))
    for ch in range(0, channal):
        for r in range(0, row):
            for c in range(0, column):
                _2Dlist_local_new_im[r, c, ch] = round(_2Dlist_local_old_im[r, c, ch] + _int_local_offset)
                if _2Dlist_local_new_im[r, c, ch] > 255:
                    _2Dlist_local_new_im[r, c, ch] = 255

    _2Dlist_local_new_im = np.uint8(_2Dlist_local_new_im)
    cv.imshow("old image", _2Dlist_local_old_im)
    cv.imshow("new image", _2Dlist_local_new_im)
    cv.waitKey(0)


_2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
Brightness(_2Dlist_global_old_im, 50)