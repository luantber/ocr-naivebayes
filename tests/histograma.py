import cv2

import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("estrella.jpg",0)
#rows, cols  = img.shape
#img = cv2.resize(img, (cols/8,rows/8),interpolation = cv2.INTER_AREA) 

equ = cv2.equalizeHist(img)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
hist2 = cv2.calcHist([equ],[0],None,[256],[0,256])

#plt.hist(img.ravel(),256,[0,256])
plt.plot(hist)
plt.plot(hist2)
cv2.imshow('original',img)
cv2.imshow('original-eq',equ)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
