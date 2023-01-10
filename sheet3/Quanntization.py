import math
from turtle import color
import cv2 as cv
import numpy as np


_2d_local_read_image=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
r,c,ch=_2d_local_read_image.shape
_int_local_new = np.zeros((r,c,ch), np.uint8)
_int_local_Gray_level=120

_int_local_Gap=int(256/_int_local_Gray_level)

_1d_list_local_Colors= range(0,256,_int_local_Gap)

for channal in range(0,ch):
    for row in range(0,r):
        for column in range(0,c):
            _int_local_temp=math.floor(_2d_local_read_image[row,column,channal]/_int_local_Gap)
   
            _int_local_new[row,column,channal] = _1d_list_local_Colors[_int_local_temp]

cv.imshow("old",_2d_local_read_image)
cv.imshow('new',_int_local_new)
cv.waitKey(0)    
