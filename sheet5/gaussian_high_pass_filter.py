import math
import numpy as np
import cv2 as cv

def spatial_to_frequency(_2d_local_read_image):
    _2d_local_image_after_fourier_transform = np.fft.fft2(_2d_local_read_image, axes=(0,1))
    _2d_local_image_after_shift = np.fft.fftshift(_2d_local_image_after_fourier_transform)
    return  _2d_local_image_after_shift

def fill_mask_values(_2d_local_mask,_int_local_DO):
    for chh in range(0,ch):
        for i in range(0,_int_local_r):
            for j in range(0,_int_local_c):
                _int_local_distance_from_center=int(((((i-(_int_local_r/2))**2)+((j-(_int_local_c/2))**2)) **0.5))
            
                _2d_local_mask[i,j,chh]=int((math.exp(int(-pow(_int_local_distance_from_center,2)/(2*pow(_int_local_DO,2))))))


                _2d_local_mask[i,j,chh]= 255-_2d_local_mask[i,j,chh]*255 

                
def apply_gaussian_high_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform):
    dft_shift_masked = np.multiply(_2d_local_image_after_fourier_transform,_2d_local_mask) /255 
    return dft_shift_masked


def frequency_to_spatial(dft_shift_masked):
    back_ishift_masked = np.fft.ifftshift(dft_shift_masked)
    img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0,1))
    img_filtered = np.abs(img_filtered).clip(0,255).astype(np.uint8)
    return img_filtered

_2d_local_read_image = cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
_int_local_r,_int_local_c,ch=_2d_local_read_image.shape   

_2d_local_mask = np.zeros_like(_2d_local_read_image)

_2d_local_image_after_fourier_transform=spatial_to_frequency(_2d_local_read_image)

fill_mask_values(_2d_local_mask,100)

_2d_local_image_after_shift=apply_gaussian_high_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform)

img_filtered=frequency_to_spatial(_2d_local_image_after_shift)

cv.imshow("ORIGINAL IMAGE", _2d_local_read_image)
cv.imshow("MASK", _2d_local_mask)
cv.imshow("FILTERED IMAGE", img_filtered)

cv.waitKey(0)











