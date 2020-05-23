# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:31:36 2019

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np 

img = plt.imread('F:/python编程/自己的博客园代码/图像变换/3.29图像单通道转3通道/0af6e4acd1cddf76c5378d20e3bfcb9f_b.jpg')
img_shape = img.shape
H = img_shape[0]
W = img_shape[1]
imgs = np.zeros(shape=(H,W,3),dtype=np.float32)
imgs[:,:,0] = img[:,:]
imgs[:,:,1] = img[:,:]
imgs[:,:,2] = img[:,:]
plt.figure()
plt.plot(img)
plt.savefig('F:/python编程/自己的博客园代码/图像变换/3.29图像单通道转3通道/3_channes.jpg')
