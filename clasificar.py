import numpy as np
import decimal
import recortar01
import cv2
import os
import pickle
import ctypes
#recortar01.binarf("images/origen/origen-triste/triste-0.jpg","triste",8)

def cargar():
	lista = []
	tipos = []
	p = os.listdir("images/binar")
	#print p
	for d in p:
		tipos.append(d)
		print "#",d
		temp = []
		for f in os.listdir("images/binar/"+d):
			temp.append("images/binar/"+d+"/"+f)
		lista.append(temp)
	archivo = open('tipos', "w")
	pickle.dump(tipos, archivo)
	return lista


def entrenar():
	lista = []
	for i in cargar():
		temp = []
		for j in i:
			temp.append(cv2.imread(j,0)/255)
		lista.append(temp)
	
		'''
	for i in lista:
		for j in i:
			print j
			print "***"
		'''

	entrenado = train(lista)

	archivo = open('base', "w")
	pickle.dump(entrenado, archivo)
	archivo.close()
	return entrenado


def contar1(xs):
	#print xs
	a = np.zeros((100,100),dtype=np.uint8)
	for n in xs:
		a = a + n
	return a

def contar0(xs):
	a=np.ones((100,100),dtype=np.uint8)
	a = a*len(xs)
	return a - contar1(xs)

def laplace(xl):
	return xl + np.ones((100,100),dtype=np.uint8)

def normalizar(xn,n):
	#print "n es", n
	n += 2.0
	return 1/n * xn
	#return xn

def train(lst):
	rt = []
	#print len(lst)
	for i in lst:
		rt.append([normalizar(laplace(contar1(i)),len(i)),normalizar(laplace(contar0(i)),len(i))])
		#print "--------------------------"
	'''
	for i in rt:
		for j in i:
			print j
			print "______________"
	''' 
	return rt

def evals(img,en,n):
	temp = np.zeros((100,100))
	t , f = 0,0
	for i in range(0,len(img)):
		for j in range(0,len(img)):
			if img[i][j] == 1:
				temp[i][j] = en[n][0][i][j]
				t +=1
			else:
				temp[i][j] = en[n][1][i][j]	
				f +=1
	print "n: ", n , "t: " , t,"f: ",f
	return temp

def fin(ev):
	x=decimal.Decimal('1')
	ctypes.c_ulong(x)
	for i in ev:
		for j in i:
			x*=decimal.Decimal(j)
			#k+=1
			#print x , " --",  i , "  . " , j
			#if x==0:
			#		return x
	#print x
	return  x

def evaluar(img):
	img = recortar01.recortar2(img)
	imgb = (img/255)
	en = pickle.load(open("base","r"))
		
	temp = []
	for i in range( len(en)):
		temp.append(evals(imgb,en,i))

	res = []
	for i in temp:
		res.append(fin(i))

	m = res[0]
	j = 0

	tipos = pickle.load(open("tipos","r"))

	print res
	for i in range(len(res)):
		if res[i]>m:
			m=res[i]
			j = i
			print j

	print m, " pertenece ",tipos[j]

	try:
		os.makedirs("results/"+tipos[j])
	except:
		pass

	ruta = "results/"+tipos[j]+"/nuevo.jpg"
	cv2.imwrite(ruta,img)
	return ruta
#evaluar("C:/Users/Luis Antonio/Pictures/as/aTeKk5oyc.jpeg")
#cv2.waitKey(0)
#cv2.destroyAllWindows()