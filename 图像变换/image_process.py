# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:15:16 2019

@author: Administrator
"""

####  图像的灰度变换
import matplotlib.pyplot as plt 
import numpy as np
from skimage.util import random_noise
from PIL import Image 

img = plt.imread('F:/python编程/自己的博客园代码/图像变换/example_gray.jpg')
fig = plt.figure(figsize = (8.0,6.0))
ax1 = fig.add_subplot(1,2,1)
##  show the original picture
ax1.imshow(img)
plt.title('original_picture')

'''
二值化
'''
#img.flags.writeable = True   ### 必须加这句不然会报错，因为图像开始只是只读模式
#threshold = 128
#H,W,X = img.shape  
#for i in range(X-1):
#    for j in range(H-1):
#        for k in range(W-1):
#            if img[j,k,i] > threshold:
#                img[j,k,i] = 255
#            else:
#                img[j,k,i] = 0
#img_twovalues = img
#ax3 = fig.add_subplot(1,2,2)
###  show the original picture
#ax3.imshow(img_twovalues)
#plt.title('twovalues_picture')




'''
图像的log变换
'''
#img_log = np.log(1 + np.abs(img/255))   #### (0,1)的输入
#ax3 = fig.add_subplot(1,2,2)
###  show the original picture
#ax3.imshow(img_log)
#plt.title('log_picture')

'''
 图像反转
'''
#img_reversal = 255- img
#ax2 = fig.add_subplot(1,2,2)
#ax2.imshow(img_reversal)
#plt.title('reversal_picture')



'''
直方图均衡
'''
#from skimage import data,exposure
#import matplotlib.pyplot as plt
#
#img = plt.imread('F:/python编程/自己的博客园代码/图像变换/example_gray.jpg')
#plt.figure("hist",figsize=(8,8))
#
#arr=img.flatten()
#plt.subplot(221)
#plt.imshow(img,plt.cm.gray) #原始图像
#plt.subplot(222)
#plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red') #原始图像直方图
#
#img1=exposure.equalize_hist(img)
#arr1=img1.flatten()
#plt.subplot(223)
#plt.imshow(img1,plt.cm.gray) #均衡化图像
#plt.subplot(224)
#plt.hist(arr1, bins=256, normed=1,edgecolor='None',facecolor='red') #均衡化直方图



















