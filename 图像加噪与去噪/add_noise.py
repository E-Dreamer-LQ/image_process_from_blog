# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:00:30 2019

@author: Administrator
"""

'''
图像添加噪声
'''
import matplotlib.pyplot as plt 
import numpy as np
from skimage.util import random_noise
from PIL import Image 

img = plt.imread('F:/python编程/自己的博客园代码/picture_process/example.jpg')

fig = plt.figure(figsize = (8.0,6.0))
ax1 = fig.add_subplot(2,3,1)
##  show the original picture
ax1.imshow(img)
plt.title('original_picture')

##　gray_picture
gravity= np.array([0.299,0.587,0.114])
#red*0.299+green*0.587+blue*0.114
img_gravity=np.dot(img,gravity)
ax2 = fig.add_subplot(2,3,2)
##  show the gray_picture
ax2.imshow(img_gravity,cmap='gray')
plt.title('gray_picture')


img_gaussian =  random_noise(img, mode='gaussian', seed=100, clip=True)
ax3 = fig.add_subplot(2,3,3)
ax3.imshow(img_gaussian)
plt.title('add_gaussian')


img_salt =  random_noise(img, mode='salt', seed=100, clip=True)
ax4 = fig.add_subplot(2,3,4)
ax4.imshow(img_salt)
plt.title('add_salt')


img_pepper =  random_noise(img, mode='pepper', seed=100, clip=True)
ax4 = fig.add_subplot(2,3,5)
ax4.imshow(img_pepper)
plt.title('add_pepper')


img_sp =  random_noise(img, mode='s&p', seed=100, clip=True)
ax4 = fig.add_subplot(2,3,6)
ax4.imshow(img_sp)
plt.title('add_sp')


















