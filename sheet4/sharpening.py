import cv2 as cv
import numpy as np


_2d_local_read_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet4\EdgeDetectors_Original.png')


r1, c1, ch1 = _2d_local_read_image.shape
_1d_list_local_new1 = np.zeros((r1, c1, ch1), np.uint8)
_1d_list_local_new2 = np.zeros((r1, c1, ch1), np.uint8)
_1d_list_local_new3 = np.zeros((r1, c1, ch1), np.uint8)
_1d_list_local_new4 = np.zeros((r1, c1, ch1), np.uint8)

_1d_list_local_filter1 =[[0,1,0], [0,1,0],[0,-1,0]]

_1d_list_local_filter2 =[[0,0,0],[1,1,-1],[0,0,0]]

_1d_list_local_filter3 =[[1,0,0],[0,1,0],[0,0,-1]]

_1d_list_local_filter4 =[[0,0,1],[0,1,0],[-1,0,0]]

_2d_local_read_image=cv.copyMakeBorder(_2d_local_read_image, 1, 1, 1,1, cv.BORDER_REFLECT)
r,c,ch=_2d_local_read_image.shape

for chh in range(0, ch1):
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            _1d_list_local_temp = _2d_local_read_image[i - 1:i + 1 + 1, j - 1:j + 1 + 1, chh]
            _1d_list_local_result1 = np.multiply(_1d_list_local_temp, _1d_list_local_filter1)
            _1d_list_local_value1 = round(np.sum(_1d_list_local_result1))
            if _1d_list_local_value1>255:
                _1d_list_local_value1=255
            if _1d_list_local_value1<0:
                  _1d_list_local_value1=0
            _1d_list_local_new1[i - 1, j - 1, chh] = _1d_list_local_value1


            _1d_list_local_result2 = np.multiply(_1d_list_local_temp, _1d_list_local_filter2)
            _1d_list_local_value2 = round(np.sum(_1d_list_local_result2))
            if _1d_list_local_value2>255:
                _1d_list_local_value2=255
            if _1d_list_local_value2<0:
                  _1d_list_local_value2=0
            _1d_list_local_new2[i - 1, j - 1, chh] = _1d_list_local_value2


            
            _1d_list_local_result3 = np.multiply(_1d_list_local_temp, _1d_list_local_filter3)
            _1d_list_local_value3 = round(np.sum(_1d_list_local_result3))
            if _1d_list_local_value3>255:
                _1d_list_local_value3=255
            if _1d_list_local_value3<0:
                  _1d_list_local_value3=0    
            _1d_list_local_new3[i - 1, j - 1, chh] = _1d_list_local_value3



            _1d_list_local_result4 = np.multiply(_1d_list_local_temp, _1d_list_local_filter4)
            _1d_list_local_value4 = round(np.sum(_1d_list_local_result4))
            if _1d_list_local_value4>255:
                _1d_list_local_value4=255
            if _1d_list_local_value4<0:
                  _1d_list_local_value4=0    
            _1d_list_local_new4[i - 1, j - 1, chh] = _1d_list_local_value4


            
cv.imshow("old image", _2d_local_read_image)
cv.imshow('new image 1', _1d_list_local_new1)
cv.imshow('new image 2', _1d_list_local_new2)
cv.imshow('new image 3', _1d_list_local_new3)
cv.imshow('new4 image ', _1d_list_local_new4)


cv.waitKey(0)

