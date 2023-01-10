import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def histogram(_2Dlist_local_old_im):
    row, column, channal = _2Dlist_local_old_im.shape

    _1Dlist_local_colors_RED = np.zeros(256)
    _1Dlist_local_colors_Green = np.zeros(256)
    _1Dlist_local_colors_Blue = np.zeros(256)

    _1Dlist_local_colors_range = range(0, 256)
    fig = plt.figure()

    for chh in range(0, channal):
        for row in range(0, row):
            for colum in range(0, column):

                if chh == 0:
                    _1Dlist_local_colors_RED[_2Dlist_local_old_im[row, colum, chh]] += 1
                if chh == 1:
                    _1Dlist_local_colors_Green[_2Dlist_local_old_im[row, colum, chh]] += 1
                if chh == 2:
                    _1Dlist_local_colors_Blue[_2Dlist_local_old_im[row, colum, chh]] += 1

        if chh == 0:
            plt1 = fig.add_subplot(221)
            plt1.plot(_1Dlist_local_colors_range, _1Dlist_local_colors_RED, color='r')
        elif chh == 1:
            plt2 = fig.add_subplot(222)
            plt2.plot(_1Dlist_local_colors_range, _1Dlist_local_colors_Green, color='g')
        elif chh == 2:
            plt3 = fig.add_subplot(223)
            plt3.plot(_1Dlist_local_colors_range, _1Dlist_local_colors_Blue, color='b')
    fig.subplots_adjust(hspace=.5, wspace=0.5)

    plt.show()


_2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
histogram(_2Dlist_global_old_im)