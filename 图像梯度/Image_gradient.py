# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:43:14 2020

@author: Administrator
"""

import cv2 as cv

class Image_Gradent():
    def __init__(self,image_name):
        self.img = image_name; 
    #Sobel算子
    def sobel_demo(self):
        grad_x = cv.Sobel(self.img, cv.CV_32F, 1, 0)   #对x求一阶导
        grad_y = cv.Sobel(self.img, cv.CV_32F, 0, 1)   #对y求一阶导
        gradx = cv.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式
        grady = cv.convertScaleAbs(grad_y)
        cv.imshow("gradient_x", gradx)  #x方向上的梯度
        cv.imshow("gradient_y", grady)  #y方向上的梯度
        gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0) #图片融合
        cv.imshow("gradient", gradxy)
        
    #Scharr算子
    def Scharr_demo(self):
        grad_x = cv.Scharr(self.img, cv.CV_32F, 1, 0)   #对x求一阶导
        grad_y = cv.Scharr(self.img, cv.CV_32F, 0, 1)   #对y求一阶导
        gradx = cv.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式
        grady = cv.convertScaleAbs(grad_y)
        cv.imshow("gradient_x", gradx)  #x方向上的梯度
        cv.imshow("gradient_y", grady)  #y方向上的梯度
        gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
        cv.imshow("gradient", gradxy)
    def Laplace_demo(self):
        dst = cv.Laplacian(self.img, cv.CV_32F)
        lpls = cv.convertScaleAbs(dst)
        cv.imshow("Laplace_demo", lpls)

if __name__ == "__main__":
    img = cv.imread('./d.jpg')
    cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
    cv.imshow('input_image', img)
    Solution = Image_Gradent(img)
    Solution.sobel_demo()
    cv.waitKey(0)
    cv.destroyAllWindows()



    
    