import cv2 as cv
import numpy as np
def fill_mask_values_in_Weighted_Filter(_2d_list_local_old_image,_int_local_sigma):
    _int_local_n = round(3.7*_int_local_sigma-0.5)
    _int_local_mask_size = 2*_int_local_n+1
    _2d_list_local_old_image = cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n, _int_local_n, cv.BORDER_REFLECT)
    _int_local_t = round(_int_local_mask_size/2)
    _int_local_x= range(-_int_local_t, _int_local_t)
    _2d_list_local_mask = np.zeros([_int_local_mask_size, _int_local_mask_size], dtype=float)
    _2d_list_local_cofficients=(1/(2*np.pi*(_int_local_sigma**2)))

    for i in range(_int_local_mask_size):
        for j in range(_int_local_mask_size):
            _int_local_power=-((_int_local_x[i]**2)+(_int_local_x[j]**2))/(2*(_int_local_sigma**2))
            _2d_list_local_temp=float(_2d_list_local_cofficients*np.exp(_int_local_power))
            _2d_list_local_mask[i,j]=_2d_list_local_temp
    return _2d_list_local_mask,_int_local_n

def Smoothing_with_Weighted_Filter(_2d_list_local_old_image):
    _int_local_row_number, _int_local_column_number, _int_local_chanal_number = _2d_list_local_old_image.shape
    _2d_list_local_New_image = np.zeros((_int_local_row_number, _int_local_column_number, _int_local_chanal_number), np.uint8)
    _2d_list_local_mask,_int_local_n = fill_mask_values_in_Weighted_Filter(_2d_list_local_old_image,1)

    for chh in range(0, _int_local_chanal_number):
        for i in range(_int_local_n, _int_local_row_number - _int_local_n):
            for j in range(_int_local_n, _int_local_column_number - _int_local_n):
               _1d_list_local_temp=_2d_list_local_old_image[i-_int_local_n:i+_int_local_n+1,j-_int_local_n:j+_int_local_n+1,chh]
               _1d_list_local_result = np.multiply(_1d_list_local_temp,_2d_list_local_mask)
               _1d_list_local_value=np.sum(_1d_list_local_result)
               _2d_list_local_New_image[i-_int_local_n,j-_int_local_n,chh]=_1d_list_local_value
               
    cv.imshow("old image",_2d_list_local_old_image)
    cv.imshow("new image",_2d_list_local_New_image)
    cv.waitKey(0)
_2d_local_read_image = cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
Smoothing_with_Weighted_Filter(_2d_local_read_image)