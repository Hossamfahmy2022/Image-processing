import cv2 as cv
import numpy as np


def Contrast_stretch(_2Dlist_local_old_new_im, _int_local_low_value, _int_local_high_value):
    row, column, channal = _2Dlist_local_old_new_im.shape
    _2Dlist_local_new_new_im = np.zeros((row, column, channal))
    new_max = _int_local_high_value
    new_min = _int_local_low_value
    for chh in range(0, channal):
        _int_local_old_max = 0
        _int_local_old_min = _2Dlist_local_old_new_im[0, 0, chh]
        for r in range(0, row):
            for c in range(0, column):
                if _int_local_old_max < _2Dlist_local_old_new_im[r, c, chh]:
                    _int_local_old_max = _2Dlist_local_old_new_im[r, c, chh]
                if _int_local_old_min > _2Dlist_local_old_new_im[r, c, chh]:
                    _int_local_old_min = _2Dlist_local_old_new_im[r, c, chh]
        _int_local_new_pixel = 0
        for r in range(0, row):
            for c in range(0, column):
                _int_local_new_pixel = ((_2Dlist_local_old_new_im[r, c, chh] - _int_local_old_min) / (
                            _int_local_old_max - _int_local_old_min)) * (new_max - new_min) + new_min
                if _int_local_new_pixel > 255:
                    _2Dlist_local_new_new_im[r, c, chh] = 255
                elif _int_local_new_pixel < 0:
                    _2Dlist_local_new_new_im[r, c, chh] = 0
                else:
                    _2Dlist_local_new_new_im[r, c, chh] = round(_int_local_new_pixel)

    _2Dlist_local_new_new_im = np.uint8(_2Dlist_local_new_new_im)
    return _2Dlist_local_new_new_im


def power_low(_2Dlist_local_old_im, _int_local_gamma):
    row, column, channal = _2Dlist_local_old_im.shape
    _2Dlist_local_new_im = np.zeros((row, column, channal))
    _int_local_new_pixel = 0
    for chh in range(0, channal):
        for r in range(0, row):
            for c in range(0, column):
                _int_local_new_pixel = 255 * (_2Dlist_local_old_im[r, c, chh] / 255) ** _int_local_gamma
                _2Dlist_local_new_im[r, c, chh] = round(_int_local_new_pixel)

    _2Dlist_local_new_im = Contrast_stretch(_2Dlist_local_new_im, 0, 255)
    _2Dlist_local_new_im = np.uint8(_2Dlist_local_new_im)
    cv.imshow("old image", _2Dlist_local_old_im)
    cv.imshow("new image", _2Dlist_local_new_im)
    cv.waitKey(0)


_2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
power_low(_2Dlist_global_old_im, 3)