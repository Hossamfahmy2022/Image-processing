import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

_1Dlist_global_color_Red = np.zeros(256)
_1Dlist_global_color_Green = np.zeros(256)
_1Dlist_global_color_Blue = np.zeros(256)


def histogram(_2Dlist_local_histogram_old_image):
    row, column, channal = _2Dlist_local_histogram_old_image.shape
    global _1Dlist_global_color_Red
    global _1Dlist_global_color_Green
    global _1Dlist_global_color_Blue
    colors_rang = range(0, 256)

    for chh in range(0, channal):
        for r in range(0, row):
            for c in range(0, column):
                if chh == 0:
                    _1Dlist_global_color_Red[_2Dlist_local_histogram_old_image[r, c, chh]] += 1
                elif chh == 1:
                    _1Dlist_global_color_Green[_2Dlist_local_histogram_old_image[r, c, chh]] += 1
                elif chh == 2:
                    _1Dlist_global_color_Blue[_2Dlist_local_histogram_old_image[r, c, chh]] += 1


_1Dlist_global_sum_Red_value = np.zeros(256)
_1Dlist_global_sum_Green_value = np.zeros(256)
_1Dlist_global_sum_Blue_value = np.zeros(256)


def histogram_equ(_2Dlist_local_histogram_equlization_old_image):
    histogram(_2Dlist_local_histogram_equlization_old_image)

    global _1Dlist_global_sum_Red_value
    global _1Dlist_global_sum_Green_value
    global _1Dlist_global_sum_Blue_value
    _1Dlist_global_sum_Red_value = np.zeros(256)
    _1Dlist_global_sum_Green_value = np.zeros(256)
    _1Dlist_global_sum_Blue_value = np.zeros(256)
    _1Dlist_global_sum_Red_value[0] = _1Dlist_global_color_Red[0]
    _1Dlist_global_sum_Green_value[0] = _1Dlist_global_color_Green[0]
    _1Dlist_global_sum_Blue_value[0] = _1Dlist_global_color_Blue[0]

    for ch in range(0, 3):
        for index in range(1, 256):
            if ch == 0:
                _1Dlist_global_sum_Red_value[index] = _1Dlist_global_sum_Red_value[index - 1] + \
                                                      _1Dlist_global_color_Red[index]
            elif ch == 1:
                _1Dlist_global_sum_Green_value[index] = _1Dlist_global_sum_Green_value[index - 1] + \
                                                        _1Dlist_global_color_Green[index]
            elif ch == 2:
                _1Dlist_global_sum_Blue_value[index] = _1Dlist_global_sum_Blue_value[index - 1] + \
                                                       _1Dlist_global_color_Blue[index]
    Run_SumR_max = _1Dlist_global_sum_Red_value.max()
    Run_SumG_max = _1Dlist_global_sum_Green_value.max()
    Run_SumB_max = _1Dlist_global_sum_Blue_value.max()

    for ch in range(0, 3):
        for index in range(0, 256):
            if ch == 0:
                _1Dlist_global_sum_Red_value[index] = round((_1Dlist_global_sum_Red_value[index] / Run_SumR_max) * 255)
            elif ch == 1:
                _1Dlist_global_sum_Green_value[index] = round(
                    (_1Dlist_global_sum_Green_value[index] / Run_SumG_max) * 255)
            elif ch == 2:
                _1Dlist_global_sum_Blue_value[index] = round(
                    (_1Dlist_global_sum_Blue_value[index] / Run_SumB_max) * 255)


_1Dlist_global_matching_Red = np.zeros(256)
_1Dlist_global_matching_Green = np.zeros(256)
_1Dlist_global_matching_Blue = np.zeros(256)
_2Dlist_global_first_image = cv.imread(r'D:\new phone\photos\Facebook\FB_IMG_1573710370163.jpg')
_2Dlist_global_second_image =cv.imread(r'D:\new phone\photos\Facebook\FB_IMG_1573574341055.jpg')
r,c,ch=_2Dlist_global_first_image.shape
histogram_equ(_2Dlist_global_first_image)
_1Dlist_global_first_Red_histogram_channal = _1Dlist_global_sum_Red_value
_1Dlist_global_first_Green_histogram_channal = _1Dlist_global_sum_Green_value
_1Dlist_global_first_Blue_histogram_channal = _1Dlist_global_sum_Blue_value
histogram_equ(_2Dlist_global_second_image)
_1Dlist_global_scond_Red_histogram_channal = _1Dlist_global_sum_Red_value
_1Dlist_global_scond_Green_histogram_channal = _1Dlist_global_sum_Green_value
_1Dlist_global_scond_Blue_histogram_channal = _1Dlist_global_sum_Blue_value
_1dlist_colors_range = range(0, 256)
for chh in range(0, 3):
    for index_match in range(0, 256):
        _int_local_minum_differnt_value = _1Dlist_global_first_Red_histogram_channal.max()
        _int_local_postion_in_old_image = 0
        for index in range(0, 256):
            if chh == 0:
                if abs(_1Dlist_global_first_Red_histogram_channal[index_match] -
                       _1Dlist_global_scond_Red_histogram_channal[index]) == 0:
                    _int_local_postion_in_old_image = index
                    break
                if abs(_1Dlist_global_first_Red_histogram_channal[index_match] -
                       _1Dlist_global_scond_Red_histogram_channal[index]) < _int_local_minum_differnt_value:
                    _int_local_minum_differnt_value = abs(_1Dlist_global_first_Red_histogram_channal[index_match] -
                                                          _1Dlist_global_scond_Red_histogram_channal[index])
                    _int_local_postion_in_old_image = index

            elif chh == 1:
                if abs(_1Dlist_global_first_Green_histogram_channal[index_match] -
                       _1Dlist_global_scond_Green_histogram_channal[index]) == 0:
                    _int_local_postion_in_old_image = index
                    break
                if abs(_1Dlist_global_first_Green_histogram_channal[index_match] -
                       _1Dlist_global_scond_Green_histogram_channal[index]) < _int_local_minum_differnt_value:
                    _int_local_minum_differnt_value = abs(_1Dlist_global_first_Green_histogram_channal[index_match] -
                                                          _1Dlist_global_scond_Green_histogram_channal[index])
                    _int_local_postion_in_old_image = index
            elif chh == 2:
                if abs(_1Dlist_global_first_Blue_histogram_channal[index_match] -
                       _1Dlist_global_scond_Blue_histogram_channal[index]) == 0:
                    _int_local_postion_in_old_image = index
                    break
                if abs(_1Dlist_global_first_Blue_histogram_channal[index_match] -
                       _1Dlist_global_scond_Blue_histogram_channal[index]) < _int_local_minum_differnt_value:
                    _int_local_minum_differnt_value = abs(_1Dlist_global_first_Blue_histogram_channal[index_match] -
                                                          _1Dlist_global_scond_Blue_histogram_channal[index])
                    _int_local_postion_in_old_image = index

        if chh == 0:
            _1Dlist_global_matching_Red[index_match] = _1dlist_colors_range[_int_local_postion_in_old_image]
        elif chh == 1:
            _1Dlist_global_matching_Green[index_match] = _1dlist_colors_range[_int_local_postion_in_old_image]
        elif chh == 2:
            _1Dlist_global_matching_Blue[index_match] = _1dlist_colors_range[_int_local_postion_in_old_image]

fig = plt.figure()

colors_rang = range(0, 256)
plt1 = fig.add_subplot(221)
plt1.plot(colors_rang, _1Dlist_global_matching_Red, color='r')

plt2 = fig.add_subplot(222)
plt2.plot(colors_rang, _1Dlist_global_matching_Green, color='g')

plt3 = fig.add_subplot(223)
plt3.plot(colors_rang, _1Dlist_global_matching_Blue, color='b')
fig.subplots_adjust(hspace=.5, wspace=0.5)
for chh in range(0,ch):
    for row in range(0,r):
        for column in range(0,c):
            if chh==0:
                _2Dlist_global_first_image[row,column,chh]=_1Dlist_global_matching_Red[_2Dlist_global_first_image[row,column,chh]]
            elif  chh==1:
                _2Dlist_global_first_image[row,column,chh]=_1Dlist_global_matching_Green[_2Dlist_global_first_image[row,column,chh]]
            elif  chh==2:
                 _2Dlist_global_first_image[row,column,chh]=_1Dlist_global_matching_Blue[_2Dlist_global_first_image[row,column,chh]]


cv.imshow('matching image', _2Dlist_global_first_image) 
cv.waitKey(0)

plt.show()