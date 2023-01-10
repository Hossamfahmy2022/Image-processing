import cv2 as cv
import numpy as np


def contrast(_2Dlist_local_old_im, _int_local_low_contrast, _int_local_high_contrast):
    row, column, channal = _2Dlist_local_old_im.shape

    _2Dlist_local_new_im = np.zeros((row, column, channal), np.uint8)
    for chh in range(0, channal):
        _int_local_minum_value = 255
        _int_local_maxum_value = 0
        for row in range(0, row):
            for colum in range(0, column):
                if _2Dlist_local_old_im[row, colum, chh] < _int_local_minum_value:
                    _int_local_minum_value = _2Dlist_local_old_im[row, colum, chh]
                if _2Dlist_local_old_im[row, colum, chh] > _int_local_maxum_value:
                    _int_local_maxum_value = _2Dlist_local_old_im[row, colum, chh]

        for row in range(0, row):
            for colum in range(0, column):
                _2Dlist_local_new_im[row, colum, chh] = (_2Dlist_local_old_im[
                                                             row, colum, chh] - _int_local_minum_value) / (
                                                                    _int_local_maxum_value - _int_local_minum_value) * (
                                                                    _int_local_high_contrast - _int_local_low_contrast) + _int_local_low_contrast

    cv.imshow("old image", _2Dlist_local_old_im)
    cv.imshow("new image", _2Dlist_local_new_im)
    cv.waitKey(0)


_2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
contrast(_2Dlist_global_old_im, 0, 200)