import cv2 as cv
import numpy as np


def image_negative(_1Dlist_local_old_image):
    row, column, channal = _1Dlist_local_old_image.shape

    _1Dlist_local_new_image = np.zeros((row, column, channal), np.uint8)

    for ch in range(0, channal):
        for r in range(0, row):
            for c in range(0, column):
                _1Dlist_local_new_image[r, c, ch] = 255 - _1Dlist_local_old_image[r, c, ch]
                if _1Dlist_local_new_image[r, c, ch] < 0:
                    _1Dlist_local_new_image[r, c, ch] = 0

    cv.imshow("old image", _1Dlist_local_old_image)
    cv.imshow('new image', _1Dlist_local_new_image)
    cv.waitKey(0)


_1Dlist_global_old_image = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
image_negative(_1Dlist_global_old_image)