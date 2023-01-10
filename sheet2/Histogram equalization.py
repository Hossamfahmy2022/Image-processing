import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

_1Dlist_global_color_Red = np.zeros(256)
_1Dlist_global_color_Green = np.zeros(256)
_1Dlist_global_color_Blue = np.zeros(256)
colors_rang = range(0, 256)


def histogram(im):
    row, column, channal = im.shape
    global _1Dlist_global_color_Red
    global _1Dlist_global_color_Green
    global _1Dlist_global_color_Blue

    for ch in range(0, channal):
        for r in range(0, row):
            for c in range(0, column):
                if ch == 0:
                    _1Dlist_global_color_Red[im[r, c, ch]] += 1
                elif ch == 1:
                    _1Dlist_global_color_Green[im[r, c, ch]] += 1
                elif ch == 2:
                    _1Dlist_global_color_Blue[im[r, c, ch]] += 1


_2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
r,c,ch=_2Dlist_global_old_im.shape
histogram(_2Dlist_global_old_im)

fig = plt.figure()

plt1 = fig.add_subplot(221)
plt1.plot(colors_rang, _1Dlist_global_color_Red, color='r')

plt2 = fig.add_subplot(222)
plt2.plot(colors_rang, _1Dlist_global_color_Green, color='g')

plt3 = fig.add_subplot(223)
plt3.plot(colors_rang, _1Dlist_global_color_Blue, color='b')
fig.subplots_adjust(hspace=.5, wspace=0.5)

_1Dlist_global_sum_Red_value = np.zeros(256)
_1Dlist_global_sum_Green_value = np.zeros(256)
_1Dlist_global_sum_Blue_value = np.zeros(256)

_1Dlist_global_sum_Red_value[0] = _1Dlist_global_color_Red[0]
_1Dlist_global_sum_Green_value[0] = _1Dlist_global_color_Green[0]
_1Dlist_global_sum_Blue_value[0] = _1Dlist_global_color_Blue[0]

for chh in range(0, 3):
    for index in range(1, 256):
        if chh == 0:
            _1Dlist_global_sum_Red_value[index] = _1Dlist_global_sum_Red_value[index - 1] + _1Dlist_global_color_Red[
                index]
        elif chh == 1:
            _1Dlist_global_sum_Green_value[index] = _1Dlist_global_sum_Green_value[index - 1] + \
                                                    _1Dlist_global_color_Green[index]
        elif chh == 2:
            _1Dlist_global_sum_Blue_value[index] = _1Dlist_global_sum_Blue_value[index - 1] + _1Dlist_global_color_Blue[
                index]
_1Dlist_global_sum_Red_max_value = _1Dlist_global_sum_Red_value.max()
_1Dlist_global_sum_Green_max_value = _1Dlist_global_sum_Green_value.max()
_1Dlist_global_sum_Blue_max_value = _1Dlist_global_sum_Blue_value.max()

for chh in range(0, 3):
    for index in range(0, 256):
        if chh == 0:
            _1Dlist_global_sum_Red_value[index] = round(
                (_1Dlist_global_sum_Red_value[index] / _1Dlist_global_sum_Red_max_value) * 255)
        elif chh == 1:
            _1Dlist_global_sum_Green_value[index] = round(
                (_1Dlist_global_sum_Green_value[index] / _1Dlist_global_sum_Green_max_value) * 255)
        elif chh == 2:
            _1Dlist_global_sum_Blue_value[index] = round(
                (_1Dlist_global_sum_Blue_value[index] / _1Dlist_global_sum_Blue_max_value) * 255)

fig = plt.figure()

plt1 = fig.add_subplot(221)
plt1.plot(colors_rang, _1Dlist_global_sum_Red_value, color='r')

plt2 = fig.add_subplot(222)
plt2.plot(colors_rang, _1Dlist_global_sum_Green_value, color='g')

plt3 = fig.add_subplot(223)
plt3.plot(colors_rang, _1Dlist_global_sum_Blue_value, color='b')
fig.subplots_adjust(hspace=.5, wspace=0.5)
for chh in range(0,ch):
    for row in range(0,r):
        for column in range(0,c):
            if chh==0:
                _2Dlist_global_old_im[row,column,chh]=_1Dlist_global_sum_Red_value[_2Dlist_global_old_im[row,column,chh]]
            elif  chh==1:
                 _2Dlist_global_old_im[row,column,chh]=_1Dlist_global_sum_Green_value[_2Dlist_global_old_im[row,column,chh]]
            elif  chh==2:
                 _2Dlist_global_old_im[row,column,chh]=_1Dlist_global_sum_Blue_value[_2Dlist_global_old_im[row,column,chh]]

cv.imshow('equalization image', _2Dlist_global_old_im) 
cv.waitKey(0)
plt.show()