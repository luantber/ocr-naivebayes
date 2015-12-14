import cv2
import numpy as np

#img = cv2.imread("caballo.jpg",0)
img = cv2.imread("papel.jpg",0)
rows, cols = img.shape
#res = cv2.resize(img,None,fx=0.2,fy=0.2,interpolation= cv2.INTER_AREA)

#Cambia el tamanio
img = cv2.resize(img, (cols/5,rows/5),interpolation = cv2.INTER_AREA) 

rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,2)
dst = cv2.warpAffine(img,M,(rows,cols),flags = cv2.INTER_LINEAR)


#dst = cv2.resize(dst, (rows/5,cols/5))
print rows,cols
ret, th1 = cv2.threshold ( img, 127,255 , cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow("gg",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)

#cv2.imshow("REduccion",res)
#cv2.imshow("Giro",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()