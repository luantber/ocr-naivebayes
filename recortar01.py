import cv2
import numpy as np


#Retorna Imagen BInaria
def binar(img,i=None,t=None):
	#cv2.imshow(""+str(i),images[0][i])

	'''
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	cl1 = clahe.apply(img)'''

	#equ = cv2.equalizeHist(img)
	#res = np.hstack((img,equ))

	#Filtro Gaussiano para eliminar ruido
	blur = cv2.GaussianBlur(img,(5,5),0)

	#Binarizacion Otsu (Valido con 2 picos en histograma)
	#ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
	#ret1,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)

	#Binarizacion Adaptativa INversa (Por areass)
	thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,10)

	#Erosion para borrar lineas delgadas (Posibles imperfecciones)
	kernel = np.ones((2,2),np.uint8)
	erosion = cv2.erode(thresh,kernel,iterations = 2 )
	#Dilata para aumentar el grososr (Mejora las caracteriticas)
	dilation = cv2.dilate(erosion,kernel,iterations = 5)

	#gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
	if i and t:
		cv2.imshow(str(t)+str(i),dilation)

	return thresh

#def contmax(contours):


#Guarda Imagenes BInarias recortadas y normalizadas
def recortar(base,stra,strb,n,show=None): #Base="caritas", stra="feliz", strb="triste" , n = cantidad de muestras (Equiprobable)
	for i in range(n):
		#Cargando imagenes tipo a,b
		a  = cv2.imread("base-"+base+"/"+stra+"-"+str(i)+".jpg")
		b = cv2.imread("base-"+base+"/"+strb+"-"+str(i)+".jpg")

		ag = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
		bg = cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)

		#temporales binarios
		at = binar(ag)
		bt = binar(bg)

		gg, contours1, gg2 = cv2.findContours(at,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		gg, contours2, gg2 = cv2.findContours(bt,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

		try:
			cv2.drawContours (ag, contours1[len(contours1)-1],  -1, 0, 3)
			x,y,w,h = cv2.boundingRect(contours1[len(contours1)-1])
			
		except :
			cv2.drawContours (ag, contours1,  -1, 0, 3)
			x,y,w,h = cv2.boundingRect(contours1[0])
			
		af = a[y:y+h,x:x+w]
		#img = cv2.rectangle(a,(x,y),(x+w,y+h),(0,255,0),2)
		#cv2.imshow(strb+str(i)+"re",img)
		cv2.imshow(strb+str(i)+"r",af)	
		
		try:
			cv2.drawContours (bg, contours2[len(contours2)-1],  -1, 0, 3)
			x,y,w,h = cv2.boundingRect(contours2[len(contours2)-1])
			
		except :
			cv2.drawContours (bg, contours2,  -1, 0, 3)
			x,y,w,h = cv2.boundingRect(contours2)
		
		
		bf = b[y:y+h,x:x+w]
		img = cv2.rectangle(bg,(x,y),(x+w,y+h),(0,255,0),2)
		#cv2.imshow(strb+str(i)+"re",img)
		#cv2.imshow(strb+str(i)+"r",bf)

		

		cv2.imwrite("listo-"+base+"/"+stra+"-"+str(i)+".jpg",af)
		cv2.imwrite("listo-"+base+"/"+strb+"-"+str(i)+".jpg",bf)	
				


recortar("caritas","feliz","triste",5,True)
cv2.waitKey(0)
cv2.destroyAllWindows()