import cv2 as cv
import numpy as np
def smothing_with_min_filter(_2d_list_local_old_image,_int_local_n):
    _int_local_row_number,_int_local_column_number,_int_local_chanal_number=_2d_list_local_old_image.shape
    _2d_list_local_New_image = np.zeros((_int_local_row_number,_int_local_column_number,_int_local_chanal_number), np.uint8)
    _2d_list_local_old_image=cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n,_int_local_n, cv.BORDER_REFLECT)
    for chh in range(0,_int_local_chanal_number):
        for i in range(_int_local_n,_int_local_row_number-_int_local_n):
         for j in range(_int_local_n,_int_local_column_number-_int_local_n):
               _2d_list_local_temp=_2d_list_local_old_image[i-_int_local_n:i+_int_local_n+1,j-_int_local_n:j+_int_local_n+1,chh]
               _int_local_value=np.min(_2d_list_local_temp)
               _2d_list_local_New_image[i-_int_local_n,j-_int_local_n,chh]=_int_local_value
    
    cv.imshow("old image",_2d_list_local_old_image)
    cv.imshow("new image",_2d_list_local_New_image)
    cv.waitKey(0)    
_2d_local_read_image=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
smothing_with_min_filter(_2d_local_read_image,2)