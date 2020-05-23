#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:39:42 2018

@author: liuqiang
"""
from astropy.io import fits
import os
#read a fits file
hud = fits.open('/home/liuqiang/my_code_test/read and save fits_test/0final.fits')
starimage = hud[0].data
starimage.dtype = 'float64'
starimage = torch.from_numpy(starimage)








##save a fits file
#path = '/home/liuqiang/sex/'
#if os.path.exists(path+'1.fits'):
#    os.remove(path+'1.fits')
#grey = fits.PrimaryHDU(img)
#greyHDU = fits.HDUList([grey])
#greyHDU.writeto(path +'1.fits')




















    