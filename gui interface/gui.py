from math import floor
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math
from turtle import color
from skimage.util import random_noise
import tkinter.messagebox
import tkinter.font as font
from tkinter import *
win=Tk() #creating the main window and storing the window object in 'win'
win.title('gui') #setting title of the window
win['bg']='black'
win.geometry('200x200') #setting the size of the window
buttonFont = font.Font(family='Helvetica', size=12, weight='bold') ## set button font

def add_two_images_button():
    
    def Contrast_stretch(_2Dlist_local_old_image, _int_local_low_value, _int_local_high_value):
        row, column, channal = _2Dlist_local_old_image.shape
        _2Dlist_local_new_image = np.zeros((row, column, channal))
        _int_local_old_max_value = 0
        _int_local_old_min_value = 0
        _int_local_new_max_value = _int_local_high_value
        _int_local_new_min_value = _int_local_low_value
        for chh in range(0, channal):
            _int_local_old_max_value = 0
            _int_local_old_min_value = _2Dlist_local_old_image[0, 0, chh]
            for r in range(0, row):
                for c in range(0, column):
                    if _int_local_old_max_value < _2Dlist_local_old_image[r, c, chh]:
                        _int_local_old_max_value = _2Dlist_local_old_image[r, c, chh]
                    if _int_local_old_min_value > _2Dlist_local_old_image[r, c, chh]:
                        _int_local_old_min_value = _2Dlist_local_old_image[r, c, chh]
            _int_local_new_pixel = 0
            for r in range(0, row):
                for c in range(0, column):
                    _int_local_new_pixel = ((_2Dlist_local_old_image[r, c, chh] - _int_local_old_min_value) / (
                                _int_local_old_max_value - _int_local_old_min_value)) * (
                                                    _int_local_new_max_value - _int_local_new_min_value) + _int_local_new_min_value
                    if _int_local_new_pixel > 255:
                        _2Dlist_local_new_image[r, c, chh] = 255
                    elif _int_local_new_pixel < 0:
                        _2Dlist_local_new_image[r, c, chh] = 0
                    else:
                        _2Dlist_local_new_image[r, c, chh] = round(_int_local_new_pixel)

        _2Dlist_local_new_image = np.uint8(_2Dlist_local_new_image)
        return _2Dlist_local_new_image


    def addimage(_2Dlist_local_first_image, _2Dlist_local_second_image):
        row1, column1, channal = _2Dlist_local_first_image.shape
        _2Dlist_local_new_image = np.zeros((row1, column1, channal))
        _int_local_new_pixel = 0
        for ch in range(0, channal):
            for row in range(0, row1):
                for column in range(0, column1):
                    _int_local_new_pixel = _2Dlist_local_first_image[row, column, ch] + _2Dlist_local_second_image[
                        row, column, ch]
                    _2Dlist_local_new_image[row, column, ch] = _int_local_new_pixel

        _2Dlist_local_new_image = Contrast_stretch(_2Dlist_local_new_image, 0, 255)
        _2Dlist_local_new_image = np.uint8(_2Dlist_local_new_image)
        cv.imshow("old image", _2Dlist_local_first_image)
        cv.imshow("new image", _2Dlist_local_new_image)
        cv.waitKey(0)


    _2Dlist_global_first_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet2\image-4.png.webp')
    _2Dlist_global_second_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet2\image-5.png.webp')


    addimage(_2Dlist_global_first_image, _2Dlist_global_second_image)
def Brightness_button():
    _2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
    def  Brightness(_2Dlist_local_old_im, _int_local_offset):
        row, column, channal = _2Dlist_local_old_im.shape

        _2Dlist_local_new_im = np.zeros((row, column, channal))
        for ch in range(0, channal):
            for r in range(0, row):
                for c in range(0, column):
                    _2Dlist_local_new_im[r, c, ch] = round(_2Dlist_local_old_im[r, c, ch] + _int_local_offset)
                    if _2Dlist_local_new_im[r, c, ch] > 255:
                        _2Dlist_local_new_im[r, c, ch] = 255

        _2Dlist_local_new_im = np.uint8(_2Dlist_local_new_im)
        cv.imshow("old image", _2Dlist_local_old_im)
        cv.imshow("new image", _2Dlist_local_new_im)
        cv.waitKey(0)   
    Brightness(_2Dlist_global_old_im, 50) 
def contrast_button():
    def contrast(_2Dlist_local_old_im, _int_local_low_contrast, _int_local_high_contrast):
        row, column, channal = _2Dlist_local_old_im.shape

        _2Dlist_local_new_im = np.zeros((row, column, channal), np.uint8)
        for chh in range(0, channal):
            _int_local_minum_value = 255
            _int_local_maxum_value = 0
            for row in range(0, row):
                for colum in range(0, column):
                    if _2Dlist_local_old_im[row, colum, chh] < _int_local_minum_value:
                        _int_local_minum_value = _2Dlist_local_old_im[row, colum, chh]
                    if _2Dlist_local_old_im[row, colum, chh] > _int_local_maxum_value:
                        _int_local_maxum_value = _2Dlist_local_old_im[row, colum, chh]

            for row in range(0, row):
                for colum in range(0, column):
                    _2Dlist_local_new_im[row, colum, chh] = (_2Dlist_local_old_im[
                                                                row, colum, chh] - _int_local_minum_value) / (
                                                                        _int_local_maxum_value - _int_local_minum_value) * (
                                                                        _int_local_high_contrast - _int_local_low_contrast) + _int_local_low_contrast

        cv.imshow("old image", _2Dlist_local_old_im)
        cv.imshow("new image", _2Dlist_local_new_im)
        cv.waitKey(0)


    _2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
    contrast(_2Dlist_global_old_im, 0, 200)

def convert_gray_button():
   
    def convert_gray(old_im):
        row, column, channal = old_im.shape
        New_im = np.zeros((row, column, 1), np.uint8)
        New_im[:, :, 0] = old_im[:, :, 1]
        cv.imshow("RGB image", old_im)
        cv.imshow('Gray image', New_im)
        cv.waitKey(0)


    old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
    convert_gray(old_im)

def histogram_button():
    
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
  


def Histogram_equalization_button():
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

    plt.show()

def Histogram_matching_button():

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
    _2Dlist_global_first_image = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
    _2Dlist_global_second_image = cv.imread(r'D:\new phone\pictures\26fc3d109c518c78475a3e95ef0de0c7.jpg')
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

    plt.show()

def image_negative_button():
    
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
def power_low_button():
        
    def Contrast_stretch(_2Dlist_local_old_new_im, _int_local_low_value, _int_local_high_value):
        row, column, channal = _2Dlist_local_old_new_im.shape
        _2Dlist_local_new_new_im = np.zeros((row, column, channal))
        new_max = _int_local_high_value
        new_min = _int_local_low_value
        for chh in range(0, channal):
            _int_local_old_max = 0
            _int_local_old_min = _2Dlist_local_old_new_im[0, 0, chh]
            for r in range(0, row):
                for c in range(0, column):
                    if _int_local_old_max < _2Dlist_local_old_new_im[r, c, chh]:
                        _int_local_old_max = _2Dlist_local_old_new_im[r, c, chh]
                    if _int_local_old_min > _2Dlist_local_old_new_im[r, c, chh]:
                        _int_local_old_min = _2Dlist_local_old_new_im[r, c, chh]
            _int_local_new_pixel = 0
            for r in range(0, row):
                for c in range(0, column):
                    _int_local_new_pixel = ((_2Dlist_local_old_new_im[r, c, chh] - _int_local_old_min) / (
                                _int_local_old_max - _int_local_old_min)) * (new_max - new_min) + new_min
                    if _int_local_new_pixel > 255:
                        _2Dlist_local_new_new_im[r, c, chh] = 255
                    elif _int_local_new_pixel < 0:
                        _2Dlist_local_new_new_im[r, c, chh] = 0
                    else:
                        _2Dlist_local_new_new_im[r, c, chh] = round(_int_local_new_pixel)

        _2Dlist_local_new_new_im = np.uint8(_2Dlist_local_new_new_im)
        return _2Dlist_local_new_new_im


    def power_low(_2Dlist_local_old_im, _int_local_gamma):
        row, column, channal = _2Dlist_local_old_im.shape
        _2Dlist_local_new_im = np.zeros((row, column, channal))
        _int_local_new_pixel = 0
        for chh in range(0, channal):
            for r in range(0, row):
                for c in range(0, column):
                    _int_local_new_pixel = 255 * (_2Dlist_local_old_im[r, c, chh] / 255) ** _int_local_gamma
                    _2Dlist_local_new_im[r, c, chh] = round(_int_local_new_pixel)

        _2Dlist_local_new_im = Contrast_stretch(_2Dlist_local_new_im, 0, 255)
        _2Dlist_local_new_im = np.uint8(_2Dlist_local_new_im)
        cv.imshow("old image", _2Dlist_local_old_im)
        cv.imshow("new image", _2Dlist_local_new_im)
        cv.waitKey(0)


    _2Dlist_global_old_im = cv.imread(r'D:\new phone\pictures\6a5fbf99.jpg')
    power_low(_2Dlist_global_old_im, 3)
def subtract_two_images_button():
    
    def Contrast_stretch(_2Dlist_local_old_image, _int_local_low_value, _int_local_high_value):
        row, column, channal = _2Dlist_local_old_image.shape
        _2Dlist_local_new_image = np.zeros((row, column, channal))
        _int_local_old_max_value = 0
        _int_local_old_min_value = 0
        _int_local_new_max_value = _int_local_high_value
        _int_local_new_min_value = _int_local_low_value
        for chh in range(0, channal):
            _int_local_old_max_value = 0
            _int_local_old_min_value = _2Dlist_local_old_image[0, 0, chh]
            for r in range(0, row):
                for c in range(0, column):
                    if _int_local_old_max_value < _2Dlist_local_old_image[r, c, chh]:
                        _int_local_old_max_value = _2Dlist_local_old_image[r, c, chh]
                    if _int_local_old_min_value > _2Dlist_local_old_image[r, c, chh]:
                        _int_local_old_min_value = _2Dlist_local_old_image[r, c, chh]
            _int_local_new_pixel = 0
            for r in range(0, row):
                for c in range(0, column):
                    _int_local_new_pixel = ((_2Dlist_local_old_image[r, c, chh] - _int_local_old_min_value) / (
                                _int_local_old_max_value - _int_local_old_min_value)) * (
                                                    _int_local_new_max_value - _int_local_new_min_value) + _int_local_new_min_value
                    if _int_local_new_pixel > 255:
                        _2Dlist_local_new_image[r, c, chh] = 255
                    elif _int_local_new_pixel < 0:
                        _2Dlist_local_new_image[r, c, chh] = 0
                    else:
                        _2Dlist_local_new_image[r, c, chh] = round(_int_local_new_pixel)

        _2Dlist_local_new_image = np.uint8(_2Dlist_local_new_image)
        return _2Dlist_local_new_image


    def subimage(_2Dlist_local_first_image, _2Dlist_local_second_image):
        row1, column1, channal = _2Dlist_local_first_image.shape
        _2Dlist_local_new_image = np.zeros((row1, column1, channal))
        _int_local_new_pixel = 0
        for ch in range(0, channal):
            for row in range(0, row1):
                for column in range(0, column1):
                    _int_local_new_pixel = _2Dlist_local_first_image[row, column, ch] - _2Dlist_local_second_image[
                        row, column, ch]
                    _2Dlist_local_new_image[row, column, ch] = _int_local_new_pixel

        _2Dlist_local_new_image = Contrast_stretch(_2Dlist_local_new_image, 0, 255)
        _2Dlist_local_new_image = np.uint8(_2Dlist_local_new_image)
        cv.imshow("old image", _2Dlist_local_first_image)
        cv.imshow("new image", _2Dlist_local_new_image)
        cv.waitKey(0)


    _2Dlist_global_first_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet2\image-4.png.webp')
    _2Dlist_global_second_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet2\image-5.png.webp')

    subimage(_2Dlist_global_first_image, _2Dlist_global_second_image)


    




def Quanntization_button():
    
   
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

def smothing_with_max_filter_button():
    def smothing_with_max_filter(_2d_list_local_old_image,_int_local_n):
        _int_local_row_number,_int_local_column_number,_int_local_chanal_number=_2d_list_local_old_image.shape
        _2d_list_local_New_image = np.zeros((_int_local_row_number,_int_local_column_number,_int_local_chanal_number), np.uint8)
        _2d_list_local_old_image=cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n,_int_local_n, cv.BORDER_REFLECT)
        for chh in range(0,_int_local_chanal_number):
            for i in range(_int_local_n,_int_local_row_number-_int_local_n):
             for j in range(_int_local_n,_int_local_column_number-_int_local_n):
                _2d_list_local_temp=_2d_list_local_old_image[i-_int_local_n:i+_int_local_n+1,j-_int_local_n:j+_int_local_n+1,chh]
                _int_local_value=np.max(_2d_list_local_temp)
                _2d_list_local_New_image[i-_int_local_n,j-_int_local_n,chh]=_int_local_value
        
        cv.imshow("old image",_2d_list_local_old_image)
        cv.imshow("new image",_2d_list_local_New_image)
        cv.waitKey(0)    
    _2d_local_read_image=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
    smothing_with_max_filter(_2d_local_read_image,2)
def smothing_with_medain_filter_button():
    def smothing_with_medain_filter(_2d_list_local_old_image,_int_local_n):
        _int_local_row_number,_int_local_column_number,_int_local_chanal_number=_2d_list_local_old_image.shape
        _2d_list_local_New_image = np.zeros((_int_local_row_number,_int_local_column_number,_int_local_chanal_number), np.uint8)
        _2d_list_local_old_image=cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n,_int_local_n, cv.BORDER_REFLECT)
        for chh in range(0,_int_local_chanal_number):
            for i in range(_int_local_n,_int_local_row_number-_int_local_n):
             for j in range(_int_local_n,_int_local_column_number-_int_local_n):
                _2d_list_local_temp=_2d_list_local_old_image[i-_int_local_n:i+_int_local_n+1,j-_int_local_n:j+_int_local_n+1,chh]
                _int_local_value=np.median(_2d_list_local_temp)
                _2d_list_local_New_image[i-_int_local_n,j-_int_local_n,chh]=_int_local_value
        
        cv.imshow("old image",_2d_list_local_old_image)
        cv.imshow("new image",_2d_list_local_New_image)
        cv.waitKey(0)    
    _2d_local_read_image=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
    smothing_with_medain_filter(_2d_local_read_image,2)
def smothing_with_min_filter_button():
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
def Smoothing_with_Weighted_Filter_button():
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


def smothing_with_mean_filter_button():

    def smothing_with_mean_filter(_2d_list_local_old_image,_int_local_n):
        _int_local_row_number,_int_local_column_number,_int_local_chanal_number=_2d_list_local_old_image.shape
        _2d_list_local_New_image = np.zeros((_int_local_row_number,_int_local_column_number,_int_local_chanal_number), np.uint8)
        _2d_list_local_old_image=cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n,_int_local_n, cv.BORDER_REFLECT)
        _int_local_mask_size=2*_int_local_n+1
        _2d_list_local_mask= np.ones([_int_local_mask_size, _int_local_mask_size], dtype = int)
        _2d_list_local_mask=(_2d_list_local_mask/(_int_local_mask_size**2))
        
        for chh in range(0,_int_local_chanal_number):
            for i in range(_int_local_n,_int_local_row_number-_int_local_n):
             for j in range(_int_local_n,_int_local_column_number-_int_local_n):
                _1d_list_local_temp=_2d_list_local_old_image[i-_int_local_n:i+_int_local_n+1,j-_int_local_n:j+_int_local_n+1,chh]
                _1d_list_local_result = np.multiply(_1d_list_local_temp,_2d_list_local_mask)
                _1d_list_local_value=np.sum(_1d_list_local_result)
                _2d_list_local_New_image[i-_int_local_n,j-_int_local_n,chh]=_1d_list_local_value
        
        cv.imshow("old image",_2d_list_local_old_image)
        cv.imshow("new image",_2d_list_local_New_image)
        cv.waitKey(0)    
    _2d_local_read_image=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
    smothing_with_mean_filter(_2d_local_read_image,1)
def Edge_detection_button():
    _2d_local_read_image = cv.imread(r'D:\3 faculty\second term\Image   Processing\ass\lab_ass\sheet4\EdgeDetectors_Original.png')
    r1, c1, ch1 = _2d_local_read_image.shape
    _1d_list_local_new1 = np.zeros((r1, c1, 1), np.uint8)
    _1d_list_local_new2 = np.zeros((r1, c1, 1), np.uint8)
    _1d_list_local_new3 = np.zeros((r1, c1, 1), np.uint8)
    _1d_list_local_new4 = np.zeros((r1, c1, 1), np.uint8)

    _1d_list_local_filter1 =[[1,2,1],[0,0,0], [-1,-2,-1]]

    _1d_list_local_filter2 =[[1,0,-1],[2,0,-2],[1,0,-1]]

    _1d_list_local_filter3 =[[0,1,2],[-1,0,1],[-2,-1,0]]

    _1d_list_local_filter4 =[[2,1,0],[1,0,-1],[0,-1,-2]]

    _2d_local_read_image=cv.copyMakeBorder(_2d_local_read_image, 1, 1, 1,1, cv.BORDER_REFLECT)
    r,c,ch=_2d_local_read_image.shape

    for chh in range(0, 1):
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                _1d_list_local_temp = _2d_local_read_image[i - 1:i + 1 + 1, j - 1:j + 1 + 1, chh]
                _1d_list_local_result1 = np.multiply(_1d_list_local_temp, _1d_list_local_filter1)
                _1d_list_local_value1 = round(np.sum(_1d_list_local_result1))
                _1d_list_local_new1[i - 1, j - 1, chh] = _1d_list_local_value1


                _1d_list_local_result2 = np.multiply(_1d_list_local_temp, _1d_list_local_filter2)
                _1d_list_local_value2 = round(np.sum(_1d_list_local_result2))
                _1d_list_local_new2[i - 1, j - 1, chh] = _1d_list_local_value2


                
                _1d_list_local_result3 = np.multiply(_1d_list_local_temp, _1d_list_local_filter3)
                _1d_list_local_value3 = round(np.sum(_1d_list_local_result3))
                _1d_list_local_new3[i - 1, j - 1, chh] = _1d_list_local_value3



                _1d_list_local_result4 = np.multiply(_1d_list_local_temp, _1d_list_local_filter4)
                _1d_list_local_value4 = round(np.sum(_1d_list_local_result4))
                _1d_list_local_new4[i - 1, j - 1, chh] = _1d_list_local_value4

    for chh in range(0, 1):
        _int_local_min1=255
        _int_local_max1=0
        _int_local_min2=255
        _int_local_max2=0
        _int_local_min3=255
        _int_local_max3=0
        _int_local_min4=255
        _int_local_max4=0
        for row in range(0, r1):
                for column in range(0, c1):
                    if _1d_list_local_new1[row ,column ,chh] <_int_local_min1 :
                        _int_local_min1=_1d_list_local_new1[row ,column ,chh]
                    if _1d_list_local_new1[row,column,chh] >_int_local_max1 :
                        _int_local_max1=_1d_list_local_new1[row,column,chh]



                    if _1d_list_local_new2[row ,column ,chh] <_int_local_min2 :
                        _int_local_min2=_1d_list_local_new2[row ,column ,chh]
                    if _1d_list_local_new2[row,column,chh] >_int_local_max2 :
                        _int_local_max2=_1d_list_local_new2[row,column,chh]



                    if _1d_list_local_new3[row ,column ,chh] <_int_local_min3 :
                        _int_local_min3=_1d_list_local_new3[row ,column ,chh]
                    if _1d_list_local_new3[row,column,chh] >_int_local_max3 :
                        _int_local_max3=_1d_list_local_new3[row,column,chh] 



                    if _1d_list_local_new4[row ,column ,chh] <_int_local_min4 :
                        _int_local_min4=_1d_list_local_new4[row ,column ,chh]
                    if _1d_list_local_new4[row,column,chh] >_int_local_max4 :
                        _int_local_max4=_1d_list_local_new4[row,column,chh] 

        for row in range(0, r1):
                for column in range(0, c1):
                    _1d_list_local_new1[row,column,chh] = (_1d_list_local_new1[row ,column  ,chh] - _int_local_min1)/(_int_local_max1 - _int_local_min1) * (255 - 0) + 0


                    _1d_list_local_new2[row,column,chh] = (_1d_list_local_new2[row ,column  ,chh] - _int_local_min2)/(_int_local_max2 - _int_local_min2) * (255 - 0) + 0


                    _1d_list_local_new3[row,column,chh] = (_1d_list_local_new3[row ,column  ,chh] - _int_local_min3)/(_int_local_max3 - _int_local_min3) * (255 - 0) + 0


                    _1d_list_local_new4[row,column,chh] = (_1d_list_local_new4[row ,column  ,chh] - _int_local_min4)/(_int_local_max4 - _int_local_min4) * (255 - 0) + 0

            
    cv.imshow("old image ", _2d_local_read_image)
    cv.imshow('new image 1', _1d_list_local_new1)
    cv.imshow('new image 2', _1d_list_local_new2)
    cv.imshow('new image 3', _1d_list_local_new3)
    cv.imshow('new image 4', _1d_list_local_new4)


    cv.waitKey(0)

def sharpening_button():
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
def Unsharpe_button():
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

def butter_worth_high_pass_filter_button():
    def spatial_to_frequency(_2d_local_read_image):
        _2d_local_image_after_fourier_transform = np.fft.fft2(_2d_local_read_image, axes=(0,1))
        _2d_local_image_after_shift = np.fft.fftshift(_2d_local_image_after_fourier_transform)
        return  _2d_local_image_after_shift

    def fill_mask_values(_2d_local_mask,_int_local_DO,_int_local_order):
        for chh in range(0,ch):
            for i in range(0,_int_local_r):
                for j in range(0,_int_local_c):
                    _int_local_distance_from_center=int(((((i-(_int_local_r/2))**2)+((j-(_int_local_c/2))**2)) **0.5))
                
                    
                    _int_local_value=(1/(1+((_int_local_distance_from_center/_int_local_DO))**(2*_int_local_order)))*255
                
                    _2d_local_mask[i,j,chh]=255-_int_local_value 

                


    def apply_butter_worth_high_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform):
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

    fill_mask_values(_2d_local_mask,100,4)

    _2d_local_image_after_shift=apply_butter_worth_high_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform)

    img_filtered=frequency_to_spatial(_2d_local_image_after_shift)

    cv.imshow("ORIGINAL IMAGE", _2d_local_read_image)
    cv.imshow("MASK", _2d_local_mask)
    cv.imshow("FILTERED IMAGE", img_filtered)

    cv.waitKey(0)
  
def butter_worth_low_pass_filter_button():
        
    def spatial_to_frequency(_2d_local_read_image):
        _2d_local_image_after_fourier_transform = np.fft.fft2(_2d_local_read_image, axes=(0,1))
        _2d_local_image_after_shift = np.fft.fftshift(_2d_local_image_after_fourier_transform)
        return  _2d_local_image_after_shift

    def fill_mask_values(_2d_local_mask,_int_local_DO,_int_local_order):
        for chh in range(0,ch):
            for i in range(0,_int_local_r):
                for j in range(0,_int_local_c):
                    _int_local_distance_from_center=int(((((i-(_int_local_r/2))**2)+((j-(_int_local_c/2))**2)) **0.5))
                
                    
                    _int_local_value=(1/(1+((_int_local_distance_from_center/_int_local_DO))**(2*_int_local_order)))*255
                
                    _2d_local_mask[i,j,chh]=_int_local_value 


    def apply_butter_worth_low_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform):
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

    fill_mask_values(_2d_local_mask,100,4)

    _2d_local_image_after_shift=apply_butter_worth_low_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform)

    img_filtered=frequency_to_spatial(_2d_local_image_after_shift)

    cv.imshow("ORIGINAL IMAGE", _2d_local_read_image)
    cv.imshow("MASK", _2d_local_mask)
    cv.imshow("FILTERED IMAGE", img_filtered)

    cv.waitKey(0)

def gaussian_high_pass_filter_button():
    
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

def gaussian_low_pass_filter_button():
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


                    _2d_local_mask[i,j,chh]= _2d_local_mask[i,j,chh]*255 


    def apply_gaussian_low_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform):
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

    _2d_local_image_after_shift=apply_gaussian_low_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform)

    img_filtered=frequency_to_spatial(_2d_local_image_after_shift)

    cv.imshow("ORIGINAL IMAGE", _2d_local_read_image)
    cv.imshow("MASK", _2d_local_mask)
    cv.imshow("FILTERED IMAGE", img_filtered)

    cv.waitKey(0)

def idel_high_pass_filter_button():
    def spatial_to_frequency(_2d_local_read_image):
        _2d_local_image_after_fourier_transform = np.fft.fft2(_2d_local_read_image, axes=(0,1))
        _2d_local_image_after_shift = np.fft.fftshift(_2d_local_image_after_fourier_transform)
        return  _2d_local_image_after_shift

    def fill_mask_values(_2d_local_mask,_int_local_DO):
        for chh in range(0,ch):
            for i in range(0,_int_local_r):
                for j in range(0,_int_local_c):
                    _int_local_distance_from_center=int(((((i-(_int_local_r/2))**2)+((j-(_int_local_c/2))**2)) **0.5))
                
                    if _int_local_distance_from_center >_int_local_DO :
                        _2d_local_mask[i,j,chh]=255
                    else :
                        _2d_local_mask[i,j,chh]=0

                        


    def apply_idel_high_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform):
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

    fill_mask_values(_2d_local_mask,50)

    _2d_local_image_after_shift=apply_idel_high_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform)

    img_filtered=frequency_to_spatial(_2d_local_image_after_shift)

    cv.imshow("ORIGINAL IMAGE", _2d_local_read_image)
    cv.imshow("MASK", _2d_local_mask)
    cv.imshow("FILTERED IMAGE", img_filtered)

    cv.waitKey(0)

def idel_low_pass_filter_button():
    
    def spatial_to_frequency(_2d_local_read_image):
        _2d_local_image_after_fourier_transform = np.fft.fft2(_2d_local_read_image, axes=(0,1))
        _2d_local_image_after_shift = np.fft.fftshift(_2d_local_image_after_fourier_transform)
        return  _2d_local_image_after_shift

    def fill_mask_values(_2d_local_mask,_int_local_DO):
        for chh in range(0,ch):
            for i in range(0,_int_local_r):
                for j in range(0,_int_local_c):
                    _int_local_distance_from_center=int(((((i-(_int_local_r/2))**2)+((j-(_int_local_c/2))**2)) **0.5))
                
                    if _int_local_distance_from_center >_int_local_DO :
                        _2d_local_mask[i,j,chh]=0 
                    else :
                        _2d_local_mask[i,j,chh]=255  


    def apply_idel_low_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform):
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

    fill_mask_values(_2d_local_mask,50)

    _2d_local_image_after_shift=apply_idel_low_pass_filter(_2d_local_mask,_2d_local_image_after_fourier_transform)

    img_filtered=frequency_to_spatial(_2d_local_image_after_shift)

    cv.imshow("ORIGINAL IMAGE", _2d_local_read_image)
    cv.imshow("MASK", _2d_local_mask)
    cv.imshow("FILTERED IMAGE", img_filtered)

    cv.waitKey(0)

def gaussin_button():
    def smothing_with_gemotric_mean(_2d_list_local_old_image,_int_local_n):
        _int_local_row_number,_int_local_column_number,_int_local_chanal_number=_2d_list_local_old_image.shape
        _2d_list_local_New_image = np.zeros((_int_local_row_number,_int_local_column_number,_int_local_chanal_number), np.uint8)
        _2d_list_local_old_image=cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n,_int_local_n, cv.BORDER_REFLECT)
        for chh in range(0,_int_local_chanal_number):
            for i in range(_int_local_n,_int_local_row_number-_int_local_n):
                for j in range(_int_local_n,_int_local_column_number-_int_local_n):
                    _2d_list_local_temp=_2d_list_local_old_image[i-_int_local_n:i+_int_local_n+1,j-_int_local_n:j+_int_local_n+1,chh]
                    _int_local_muilt = 1
                    for i in range(2*_int_local_n+1):
                            for j in range(2*_int_local_n+1):
                                _int_local_muilt*=_2d_list_local_temp[i,j]
                    _int_local_base=np.power(2*_int_local_n+1,2)
                    _int_local_value=int(np.power(_int_local_muilt,1//_int_local_base))
                    
                    _2d_list_local_New_image[i-_int_local_n,j-_int_local_n,chh]= _int_local_value
               
        
        cv.imshow("old image",_2d_list_local_old_image)
        cv.imshow("new image",_2d_list_local_New_image)
        cv.waitKey(0)    
    _2d_local_read_image=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
    _2d_local_read_image=random_noise(_2d_local_read_image, mode='gaussian', seed=None,clip=True,)
    _2d_local_read_image = np.array(255*_2d_local_read_image, dtype = 'uint8')
    smothing_with_gemotric_mean(_2d_local_read_image,1)

def salt_and_pepper_button():
    def smothing_with_mid_point_filter(_2d_list_local_old_image,_int_local_n):
        _int_local_row_number,_int_local_column_number,_int_local_chanal_number=_2d_list_local_old_image.shape
        _2d_list_local_New_image = np.zeros((_int_local_row_number,_int_local_column_number,_int_local_chanal_number), np.uint8)
        _2d_list_local_old_image=cv.copyMakeBorder(_2d_list_local_old_image, _int_local_n, _int_local_n, _int_local_n,_int_local_n, cv.BORDER_REFLECT)
        for chh in range(0,_int_local_chanal_number):
            for i in range(_int_local_n,_int_local_row_number-_int_local_n):
             for j in range(_int_local_n,_int_local_column_number-_int_local_n):
                _2d_list_local_temp=_2d_list_local_old_image[i-_int_local_n:i+_int_local_n+1,j-_int_local_n:j+_int_local_n+1,chh]
                _int_local_value=np.max(_2d_list_local_temp)+np.min(_2d_list_local_temp)
                #_int_local_value=np.medain(_2d_list_local_temp) ## this is work good but not there demanded in sheet 
                _2d_list_local_New_image[i-_int_local_n,j-_int_local_n,chh]=_int_local_value/2 # remove divide by 2 in case use medain
                
        
        cv.imshow("old image",_2d_list_local_old_image)
        cv.imshow("new image",_2d_list_local_New_image)
        cv.waitKey(0)    
    _2d_local_read_image=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
    _2d_local_read_image=random_noise(_2d_local_read_image, mode='s&p',amount=0.01)
    _2d_local_read_image=np.array(255*_2d_local_read_image, dtype = 'uint8')
    smothing_with_mid_point_filter(_2d_local_read_image,2)
def MAPPING_1Order_button():
    def _1order(im,fact):
        old_r,old_c,old_k=im.shape
        new_row=old_r*fact
        new_column=old_c*fact
        new_im = np.zeros((new_row,new_column,old_k))
        old_r=range(old_r)
        old_c=range(old_c)
        old_k=range(old_k)           
        for channel in old_k:           
            for row in old_r:                                    
                    for column in old_c:                         
                        new_im[fact*row,column*fact,channel]=im[row,column,channel]
        for channel in old_k:
            for row in old_r:
                    for column in old_c:
                        ii=1
                        if fact*(column+1)<new_column :   
                            if(new_im[fact*row,fact*column,channel] <= new_im[fact*row,fact*(column+1),channel]):
                                array=range(fact*column+1 ,fact*(column+1))
                                minum=new_im[fact*row,fact*column,channel]
                                maxum=new_im[fact*row,fact*(column+1),channel] 
                                for counter in array:
                                    new_im[fact*row,counter,channel]=round(((maxum - minum)/fact)*ii + minum)
                                    ii+=1
                            elif (new_im[fact*row,fact*column,channel] > new_im[fact*row,fact*(column+1),channel])  :
                                array=range(fact*column+1 ,fact*(column+1))
                                minum=new_im[fact*row,fact*column,channel]
                                maxum=new_im[fact*row,fact*(column+1),channel]
                                for counter in array:
                                    new_im[fact*row,counter,channel]=round(((maxum - minum)/fact)*ii + minum)
                                    ii+=1
                        else :
                            new_im[fact*row,fact*column+1:new_column-1,channel]=new_im[fact*row,fact*column,channel]            
                            break
        old_c=range(new_column)      
        for channel in old_k:
            for row in old_r:                
                    for column in old_c:
                        ii=1
                        if  fact*(row+1)<new_row   :
                                if(new_im[fact*row,column,channel] <= new_im[fact*(row+1),column,channel] ):  
                                    array=range(fact*row+1 ,fact*(row+1))  
                                    minum=new_im[fact*row,column,channel]
                                    maxum=new_im[fact*(row+1),column,channel]
                                    for counter in array:
                                        
                                        new_im[counter,column,channel]=np.round(((maxum - minum)/fact)*ii + minum)
                                        ii+=1
                                elif new_im[fact*row,column,channel] > new_im[fact*(row+1),column,channel] :
                                    array=range(fact*row+1 ,fact*(row+1))
                                    maxum=new_im[fact*row,column,channel]
                                    minum=new_im[fact*(row+1),column,channel]
                                    for counter in array:
                                        new_im[counter,column,channel]=np.round(((maxum - minum)/fact)*ii + minum)
                                        ii+=1
                        else :
                            new_im[fact*row+1:new_row-1,column,channel] = new_im[fact*row,column,channel]        
        new_im=np.uint8(new_im)
        cv.imshow("Old",im)
        cv.imshow("New",new_im)
        cv.waitKey(0)

        

    im=cv.imread(r'D:\new phone\pictures\1bc53796127aa3b51b651569999483eb.jpg')
    _1order(im,3)             
def water_mark_button():
    def water_mark(_2Dlist_local_image, _2Dlist_local_logo):
        row, column, channal = _2Dlist_local_image.shape
        _2Dlist_local_image_with_water_mark = np.zeros((row, column, channal), np.uint8)
        for ch in range(0, channal):
            for r in range(0, row):
                for c in range(0, column):
                    _int_local_pixel = _2Dlist_local_image[r, c, ch]
                    _int_local_mask_pixel = _int_local_pixel & 240
                    _int_local_logo_pexil = _2Dlist_local_logo[r, c, ch]
                    _int_local_logo_shift = _int_local_logo_pexil >> 4
                    _int_local_new_pexil = _int_local_mask_pixel | _int_local_logo_shift
                    _2Dlist_local_image_with_water_mark[r, c, ch] = _int_local_new_pexil
        cv.imshow(" original image", _2Dlist_local_image) # show the  original image
        cv.imshow('water mark image', _2Dlist_local_image_with_water_mark) # show the water mark image
        cv.waitKey(0)
    _2Dlist_global_image = cv.imread(r'D:\new phone\photos\Facebook\FB_IMG_1573710370163.jpg')
    _2Dlist_global_logo_image = cv.imread(r'D:\new phone\photos\Facebook\FB_IMG_1573574341055.jpg')
    water_mark(_2Dlist_global_image, _2Dlist_global_logo_image) # call the function                                                                                                              
btn1=Button(win,text="add_two_images_button", width=20,height=10,command=add_two_images_button, bg='yellow', 
                activebackground='green', font=buttonFont)
btn1.grid(row = 0, column = 0, sticky = W)
btn2=Button(win,text="Brightness_button", width=20,height=10,command=Brightness_button,bg='yellow', 
                activebackground='green', font=buttonFont)
btn2.grid(row = 1, column = 0, sticky = W)
btn3=Button(win,text="contrast_button", width=20,height=10,command=contrast_button,bg='yellow', 
                activebackground='green', font=buttonFont)
btn3.grid(row = 2, column = 0, sticky = W)
btn4=Button(win,text="convert_gray_button", width=20,height=10,command=convert_gray_button,bg='yellow', 
                activebackground='green', font=buttonFont)
btn4.grid(row = 3, column = 0, sticky = W)
btn5=Button(win,text="histogram_button", width=20,height=10,command=histogram_button,bg='yellow', 
                activebackground='green', font=buttonFont)
btn5.grid(row = 4, column = 0, sticky = W)


btn6=Button(win,text="Histogram_equalization\nbutton", width=20,height=10,command=Histogram_equalization_button,bg='orange', 
                activebackground='green', font=buttonFont)
btn6.grid(row = 0, column = 1, sticky = W)
btn7=Button(win,text="Histogram_matching\nbutton", width=20,height=10,command=Histogram_matching_button,bg='orange', 
                activebackground='green', font=buttonFont)
btn7.grid(row = 1, column = 1, sticky = W)
btn8=Button(win,text="image_negative_button", width=20,height=10,command=image_negative_button,bg='orange', 
                activebackground='green', font=buttonFont)
btn8.grid(row = 2, column = 1, sticky = W)
btn9=Button(win,text="power_low_button", width=20,height=10,command=power_low_button,bg='orange', 
                activebackground='green', font=buttonFont)
btn9.grid(row = 3, column = 1, sticky = W)
btn10=Button(win,text="subtract_two\nimages_button", width=20,height=10,command=subtract_two_images_button,bg='orange', 
                activebackground='green', font=buttonFont)
btn10.grid(row = 4, column = 1, sticky = W)


btn11=Button(win,text="Quanntization_button", width=20,height=10,command=Quanntization_button,bg='red', 
                activebackground='green', font=buttonFont)
btn11.grid(row = 0, column = 2, sticky = W)
btn12=Button(win,text="smothing_with_max\nfilter_button", width=20,height=10,command=smothing_with_max_filter_button,bg='red', 
                activebackground='green', font=buttonFont)
btn12.grid(row = 1, column = 2, sticky = W)
btn13=Button(win,text="smothing_with_medain\nfilter_button", width=20,height=10,command=smothing_with_medain_filter_button,bg='red', 
                activebackground='green', font=buttonFont)
btn13.grid(row = 2, column = 2, sticky = W)
btn14=Button(win,text="smothing_with_min\nfilter_button", width=20,height=10,command=smothing_with_min_filter_button,bg='red', 
                activebackground='green', font=buttonFont)
btn14.grid(row = 3, column = 2, sticky = W)
btn15=Button(win,text="Smoothing_with_Weighted\nFilter_button", width=20,height=10,command=Smoothing_with_Weighted_Filter_button,bg='red', 
                activebackground='green', font=buttonFont)
btn15.grid(row = 4, column = 2, sticky = W)



btn16=Button(win,text="smothing_with_mean\nfilter_button", width=20,height=10,command=smothing_with_mean_filter_button,bg='purple', 
                activebackground='green', font=buttonFont)
btn16.grid(row = 0, column = 3, sticky = W)
btn17=Button(win,text="Edge_detection_button", width=20,height=10,command=Edge_detection_button,bg='purple', 
                activebackground='green', font=buttonFont)
btn17.grid(row = 1, column = 3, sticky = W)
btn18=Button(win,text="sharpening_button", width=20,height=10,command=sharpening_button,bg='purple', 
                activebackground='green', font=buttonFont)
btn18.grid(row = 2, column = 3, sticky = W)
btn19=Button(win,text="Unsharpe_button", width=20,height=10,command=Unsharpe_button,bg='purple', 
                activebackground='green', font=buttonFont)
btn19.grid(row = 3, column = 3, sticky = W)
btn20=Button(win,text="butter_worth\nhigh_pass\nfilter_button", width=20,height=10,command=butter_worth_high_pass_filter_button,bg='purple', 
                activebackground='green', font=buttonFont)
btn20.grid(row = 4, column = 3, sticky = W)





btn21=Button(win,text="butter_worth\nlow_pass\nfilter_button", width=20,height=10,command=butter_worth_low_pass_filter_button,bg='skyblue4', 
                activebackground='green', font=buttonFont)
btn21.grid(row = 0, column = 4, sticky = W)
btn22=Button(win,text="gaussian_high\npass_filter_button", width=20,height=10,command=gaussian_high_pass_filter_button,bg='skyblue4', 
                activebackground='green', font=buttonFont)
btn22.grid(row = 1, column = 4, sticky = W)
btn23=Button(win,text="gaussian_low\npass_filter_button", width=20,height=10,command=gaussian_low_pass_filter_button,bg='skyblue4', 
                activebackground='green', font=buttonFont)
btn23.grid(row = 2, column = 4, sticky = W)
btn24=Button(win,text="idel_high_pass\nfilter_button", width=20,height=10,command=idel_high_pass_filter_button,bg='skyblue4', 
                activebackground='green', font=buttonFont)
btn24.grid(row = 3, column = 4, sticky = W)
btn25=Button(win,text="idel_low_pass\nfilter_button", width=20,height=10,command=idel_low_pass_filter_button,bg='skyblue4', 
                activebackground='green', font=buttonFont)
btn25.grid(row = 4, column = 4, sticky = W)



btn26=Button(win,text="gaussin_button", width=20,height=10,command=gaussin_button,bg='green', 
                activebackground='green', font=buttonFont)
btn26.grid(row = 0, column = 5, sticky = W)
btn27=Button(win,text="salt_and_pepper_button", width=20,height=10,command=salt_and_pepper_button,bg='green', 
                activebackground='green', font=buttonFont)
btn27.grid(row = 1, column = 5, sticky = W)
btn28=Button(win,text="MAPPING_1Order_button", width=20,height=10,command=MAPPING_1Order_button,bg='green', 
                activebackground='green', font=buttonFont)
btn28.grid(row = 2, column = 5, sticky = W)
btn29=Button(win,text="water_mark_button", width=20,height=10,command=water_mark_button,bg='green', 
                activebackground='green', font=buttonFont)
btn29.grid(row = 3, column = 5, sticky = W)



win.mainloop() #running the loop that works as a trigger                    
