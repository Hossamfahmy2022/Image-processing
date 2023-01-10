import cv2 as cv
import numpy as np

def Guassian_function(_2d_list_local_old_image,_int_local_sigma):
    _int_local_n = round(3.7*_int_local_sigma-0.5)
    _int_local_mask_size = 2*_int_local_n+1

    _2d_list_local_old_image = cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n, _int_local_n, cv.BORDER_REFLECT)
    _int_local_t = round(_int_local_mask_size/2)
    _int_local_x= range(-_int_local_t, _int_local_t)
    _2d_list_local_filter = np.zeros([_int_local_mask_size, _int_local_mask_size], dtype=float)
    _2d_list_local_coef=(1/(2*np.pi*(_int_local_sigma**2)))
    for i in range(_int_local_mask_size):
        for j in range(_int_local_mask_size):
            _int_local_power=-((_int_local_x[i]**2)+(_int_local_x[j]**2))/(2*(_int_local_sigma**2))
            _2d_list_local_temp=float(_2d_list_local_coef*np.exp(_int_local_power))
            _2d_list_local_filter[i,j]=_2d_list_local_temp
    return _2d_list_local_filter,_int_local_n



_2d_local_read_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet4\EdgeDetectors_Original.png')
sigma=float(input("enter the sigma :"))

r1, c1, ch1 = _2d_local_read_image.shape

_2d_local_new_image = np.zeros((r1, c1, ch1))

_2d_list_local_filter,_int_local_n = Guassian_function(_2d_local_read_image,sigma)

_2d_local_read_image=cv.copyMakeBorder(_2d_local_read_image, _int_local_n, _int_local_n, _int_local_n,_int_local_n, cv.BORDER_REFLECT)
r,c,ch=_2d_local_read_image.shape


for chh in range(0, ch):
    for i in range(_int_local_n, r - _int_local_n):
        for j in range(_int_local_n, c - _int_local_n):
            _1d_list_local_temp = _2d_local_read_image[i - _int_local_n:i + _int_local_n + 1, j - _int_local_n:j + _int_local_n + 1, chh]
            _1d_list_local_result = np.multiply(_1d_list_local_temp, _2d_list_local_filter)
            _1d_list_local_value = round(np.sum(_1d_list_local_result))
            _2d_local_new_image[i - _int_local_n, j - _int_local_n, chh] = _1d_list_local_value


for chh in range(0, ch):
    for i in range(_int_local_n, r - _int_local_n):
        for j in range(_int_local_n, c - _int_local_n):
            _2d_local_new_image[i - _int_local_n, j - _int_local_n, chh] = _2d_local_read_image [i,j,chh] -_2d_local_new_image[i - _int_local_n, j - _int_local_n, chh] 
            if _2d_local_new_image[i - _int_local_n, j - _int_local_n, chh]<0 :
                _2d_local_new_image[i - _int_local_n, j - _int_local_n, chh]=0
            _2d_local_new_image[i - _int_local_n, j - _int_local_n, chh] = _2d_local_read_image [i,j,chh] +_2d_local_new_image[i - _int_local_n, j - _int_local_n, chh] 
            if _2d_local_new_image[i - _int_local_n, j - _int_local_n, chh]>255 :
               _2d_local_new_image[i - _int_local_n, j - _int_local_n, chh]=255
      
_2d_local_new_image=np.uint8(_2d_local_new_image)      
cv.imshow("old image", _2d_local_read_image)
cv.imshow("new image ", _2d_local_new_image)
cv.waitKey(0)

