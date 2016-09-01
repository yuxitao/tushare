# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:27:53 2016

@author: yuxitao
"""

import pylab as pl
import scipy as sp
#img = sp.misc.face()
img = pl.imread('lepetitpoisson.jpg')
pl.imshow(img,cmap=pl.cm.gray)

img2 = img[:-2,1:-1]-img[2:,1:-1]+img[1:-1,:-2]
pl.figure()
pl.imshow(img2,cmap=pl.cm.gray)

pl.show()
