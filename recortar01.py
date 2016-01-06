import cv2
import numpy as np


#Retorna Imagen BInaria
def binar(img,i=None,t=None):
	#cv2.imshow(""+str(i),images[0][i])

	ag = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	equ = cv2.equalizeHist(ag)
	'''


	cv2.imshow("equ",equ)

	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	cl1 = clahe.apply(img)'''


	#Filtro Gaussiano para eliminar ruido
	blur = cv2.GaussianBlur(ag,(5,5),0)
	cv2.imshow("blur",blur)
	#Binarizacion Otsu (Valido con 2 picos en histograma)
	#ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
	#ret1,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)

	#Binarizacion Adaptativa INversa (Por areass)
	thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,10)

	#Erosion para borrar lineas delgadas (Posibles imperfecciones)
	kernel = np.ones((2,2),np.uint8)
	erosion = cv2.erode(thresh,kernel,iterations = 1 )
	#Dilata para aumentar el grososr (Mejora las caracteriticas)
	dilation = cv2.dilate(erosion,kernel,iterations = 2)

	#gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
	if i and t:
		cv2.imshow(str(t)+str(i),dilation)

	#cv2.imshow("thresh",thresh)
	return dilation

#def contmax(contours):

"""
#Guarda Imagenes BInarias recortadas y normalizadas
def recortar(base,stra,strb,n,show=None): #Base="caritas", stra="feliz", strb="triste" , n = cantidad de muestras (Equiprobable)
	for i in range(n):
		#Cargando imagenes tipo a,b
		a  = cv2.imread("base-"+base+"/"+stra+"-"+str(i)+".jpg")
		b = cv2.imread("base-"+base+"/"+strb+"-"+str(i)+".jpg")

		ag = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
		bg = cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)

		#temporales binarios
		at = binar(ag,stra,str(i))
		bt = binar(bg,strb,str(i))

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
		#cv2.imshow(strb+str(i)+"r",af)	
		
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

		af = cv2.resize(af,(100, 100), interpolation = cv2.INTER_CUBIC)
		bf = cv2.resize(bf,(100, 100), interpolation = cv2.INTER_CUBIC)

		cv2.imwrite("listo-"+base+"/"+stra+"-"+str(i)+".jpg",af)
		cv2.imwrite("listo-"+base+"/"+strb+"-"+str(i)+".jpg",bf)	
"""
def recortar2(path):
	a  = cv2.imread(path)

	#ag = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
	#equ = cv2.equalizeHist(ag)

	#cv2.imshow("equ",equ)

	#cv2.imshow("a",a)

	#temporales binarios
	at = binar(a)

	cv2.imshow("at",at)
	gg, contours1, gg2 = cv2.findContours(at,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

	try:
		#cv2.drawContours (ag, contours1[len(contours1)-1],  -1, (0,255,0), 3)
		#cv2.drawContours (ag, contours1,  -1, (0,255,0), 3)
		x,y,w,h = cv2.boundingRect(contours1[len(contours1)-1])
		print "try1 \n"
		
	except :
		#cv2.drawContours (ag, contours1,  -1, 0, 3)
		x,y,w,h = cv2.boundingRect(contours1[0])
		print "   try2   "
		
	#cv2.imshow("a",a)
	try:
		af = a[y-3:y+h+3,x-3:x+w+3]
		af = cv2.resize(af,(100, 100), interpolation = cv2.INTER_CUBIC)
		print "tryy11"

	except:
		af = a[y-0:y+h+0,x-0:x+w+0]
		af = cv2.resize(af,(100, 100), interpolation = cv2.INTER_CUBIC)
		print "tryy22"

	cv2.imshow("lml",af)
	cv2.imwrite("temp.jpg",af)
	x = binar(cv2.imread("temp.jpg"))
	cv2.imwrite("temp2.jpg",x)
	return x

def recortar(path,tipo,n):
	print path
	a  = cv2.imread(path,1)

	#temporales binarios
	at = binar(a)
	#cv2.imshow("at",at)
	gg, contours1, gg2 = cv2.findContours(at,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

	try:
		#cv2.drawContours (ag, contours1[len(contours1)-1],  -1, (0,255,0), 3)
		#cv2.drawContours (ag, contours1,  -1, (0,255,0), 3)
		x,y,w,h = cv2.boundingRect(contours1[len(contours1)-1])
		print "try1  \n"
		
	except :
		#cv2.drawContours (ag, contours1,  -1, 0, 3)
		print "try2 .."
		x,y,w,h = cv2.boundingRect(contours1[0])
		print "try2"
		
			
	try:
		print "aqui1"
		af = a[y-3:y+h+3,x-3:x+w+3]
		af = cv2.resize(af,(100, 100), interpolation = cv2.INTER_CUBIC)

	except:
		print "aqui2"
		af = a[y-0:y+h+0,x-0:x+w+0]
		af = cv2.resize(af,(100, 100), interpolation = cv2.INTER_CUBIC)

	#cv2.imshow("af",af)

	#img = cv2.rectangle(a,(x,y),(x+w,y+h),(0,255,0),2)
	#cv2.imshow("gg",img)


	#cv2.imshow(tipo+str(n),af)
	
	cv2.imwrite("images/origen/origen-"+tipo+"/"+tipo+str(n)+".jpg",af)

def binarf(path,tipo,n):
	image = cv2.imread(path)
	
	#gris = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#cv2.imshow("gr"+str(n),gris)
	af = binar(image)

	
	#cv2.imshow("af",af)
	path = "images/binar/"+tipo+"/"+tipo+str(n)+".jpg"

	cv2.imwrite(path,af)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()


#def binarf2(path,tipo,n):

#recortar("caritas","feliz","triste",5,True)
