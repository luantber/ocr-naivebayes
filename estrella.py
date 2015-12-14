import numpy as np
import cv2
 
im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
#cv2.imshow("Umbral|",thresh)
image, contours, asd = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

nuevo = im[58:138,52:145]
cv2.imwrite("nuevo.jpg",nuevo)
cv2.drawContours (im, contours, - 1, (0, 255, 0), 3)

cv2.imshow("Original",im)
cv2.imshow("Gris",imgray)
cv2.imshow("Umbral",thresh)
cv2.imshow("NUevo",nuevo)

cv2.waitKey(0)
cv2.destroyAllWindows()
print contours
'''
print contours
m = cv2.moments(contours[2])
print m

x,y,w,h = cv2.boundingRect(contours[2])

print x,y,w,h
'''

cnt = contours[0]
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

print leftmost,rightmost,topmost,bottommost



