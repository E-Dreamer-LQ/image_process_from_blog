# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:17:58 2019

@author: Administrator
"""

'''
图像去除噪声
'''
import matplotlib.pyplot as plt 
import numpy as np
from skimage.util import random_noise
from PIL import Image 
import cv2

img = plt.imread('F:/python编程/自己的博客园代码/picture_process/gaussian_picture.jpg')
fig = plt.figure(figsize=(8.0,6.0))
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(img)
plt.title('blur_picture')

###  中值滤波
median_filter_img = cv2.medianBlur(img, 3)
ax2 = fig.add_subplot(2,3,2)
ax2.imshow(median_filter_img)
plt.title('median_filter')

#### 高斯滤波
Gaussian_filter_img = cv2.GaussianBlur(img, (3,3), 0)
ax2 = fig.add_subplot(2,3,3)
ax2.imshow(Gaussian_filter_img)
plt.title('Gaussian_filter')

####　均值滤波
mean_vaule_filter = cv2.blur(img, (5,5))
ax2 = fig.add_subplot(2,3,4)
ax2.imshow(mean_vaule_filter)
plt.title('mean_vaule_filter')

#### 双边滤波
#9 邻域直径，两个 75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
blur = cv2.bilateralFilter(img,9,75,75)
ax2 = fig.add_subplot(2,3,5)
ax2.imshow(blur)
plt.title('bilatral-filter')


### 傅里叶滤波
##img0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gravity= np.array([0.299,0.587,0.114])
##red*0.299+green*0.587+blue*0.114
#img = np.dot(img,gravity)
#fshift = np.fft.fft2(img)
##fshift = np.fft.fftshift(f)
##fshift_log = np.log(np.abs(fshift))
#f1shift = np.fft.ifftshift(fshift)
#img_back = np.fft.ifft2(f1shift)
#img_back = np.abs(img_back)
#ax2 = fig.add_subplot(2,3,6)
#ax2.imshow(img_back)
#plt.title('fft-filter')
#










