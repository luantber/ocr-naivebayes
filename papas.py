import cv2
import numpy as np

img = cv2.imread("papas/05.jpg",0)

rows, cols = img.shape
img = cv2.resize(img, (cols/8,rows/8),interpolation = cv2.INTER_AREA) 

median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)

ret, th1 = cv2.threshold ( img, 160,255 , cv2.THRESH_BINARY_INV)
#ret, otsu = cv2.threshold ( median	, 0,255 , cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
##th2 = cv2.adaptiveThreshold(median,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(median,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,4)

kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(th1,kernel,iterations=20)
fth1 = cv2.medianBlur(erosion,5)

cv2.imshow("gg",img)
#cv2.imshow	("media",median	)
#cv2.imshow	("bilateral	",bilateral)
cv2.imshow("Th1",th1)
cv2.imshow("eros",erosion)
cv2.imshow("filter gauss",fth1)
#cv2.imshow("otsu",otsu)
'''
cv2.imshow("th1",th1)

cv2.imshow("mean",th2)
cv2.imshow("gauss",th3)'''


cv2.waitKey(0)
cv2.destroyAllWindows()