from math import floor
import cv2 as cv
import numpy as np


def Contrast_stretch(_2Dlist_local_old_image, _int_local_low_value, _int_local_high_value):
    row, column, channal = _2Dlist_local_old_image.shape
    _2Dlist_local_new_image = np.zeros((row, column, channal))
    _int_local_old_max_value = 0
    _int_local_old_min_value = 0
    _int_local_new_max_value = _int_local_high_value
    _int_local_new_min_value = _int_local_low_value
    for chh in range(0, channal):
        _int_local_old_max_value = 0
        _int_local_old_min_value = _2Dlist_local_old_image[0, 0, chh]
        for r in range(0, row):
            for c in range(0, column):
                if _int_local_old_max_value < _2Dlist_local_old_image[r, c, chh]:
                    _int_local_old_max_value = _2Dlist_local_old_image[r, c, chh]
                if _int_local_old_min_value > _2Dlist_local_old_image[r, c, chh]:
                    _int_local_old_min_value = _2Dlist_local_old_image[r, c, chh]
        _int_local_new_pixel = 0
        for r in range(0, row):
            for c in range(0, column):
                _int_local_new_pixel = ((_2Dlist_local_old_image[r, c, chh] - _int_local_old_min_value) / (
                            _int_local_old_max_value - _int_local_old_min_value)) * (
                                                   _int_local_new_max_value - _int_local_new_min_value) + _int_local_new_min_value
                if _int_local_new_pixel > 255:
                    _2Dlist_local_new_image[r, c, chh] = 255
                elif _int_local_new_pixel < 0:
                    _2Dlist_local_new_image[r, c, chh] = 0
                else:
                    _2Dlist_local_new_image[r, c, chh] = round(_int_local_new_pixel)

    _2Dlist_local_new_image = np.uint8(_2Dlist_local_new_image)
    return _2Dlist_local_new_image


def addimage(_2Dlist_local_first_image, _2Dlist_local_second_image):
    row1, column1, channal = _2Dlist_local_first_image.shape
    _2Dlist_local_new_image = np.zeros((row1, column1, channal))
    _int_local_new_pixel = 0
    for ch in range(0, channal):
        for row in range(0, row1):
            for column in range(0, column1):
                _int_local_new_pixel = _2Dlist_local_first_image[row, column, ch] + _2Dlist_local_second_image[
                    row, column, ch]
                _2Dlist_local_new_image[row, column, ch] = _int_local_new_pixel

    _2Dlist_local_new_image = Contrast_stretch(_2Dlist_local_new_image, 0, 255)
    _2Dlist_local_new_image = np.uint8(_2Dlist_local_new_image)
    cv.imshow("old image", _2Dlist_local_first_image)
    cv.imshow("new image", _2Dlist_local_new_image)
    cv.waitKey(0)


_2Dlist_global_first_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet2\image-4.png.webp')
_2Dlist_global_second_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet2\image-5.png.webp')

addimage(_2Dlist_global_first_image, _2Dlist_global_second_image)





