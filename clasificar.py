import numpy as np
import decimal
import recortar01
import cv2
import os
import pickle
#recortar01.binarf("images/origen/origen-triste/triste-0.jpg","triste",8)

def cargar():
	lista = []
	p = os.listdir("images/binar")
	#print p
	for d in p:
		#print "#",d
		temp = []
		for f in os.listdir("images/binar/"+d):
			temp.append("images/binar/"+d+"/"+f)
		lista.append(temp)
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
			for k in j:
				print k
				'''
	entrenado = train(lista)

	archivo = open('base', "w")
	pickle.dump(entrenado, archivo)
	archivo.close()
	return entrenado


def contar1(xs):
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
	n += 2.0
	return 1/n * xn
	#return xn

def train(lst):
	rt = []
	for i in lst:
		rt.append([normalizar(laplace(contar1(i)),len(lst)),normalizar(laplace(contar0(i)),len(lst))])
	return rt

def evalfin(img,n):
	temp = np.zeros((100,100))
	for i in range(0,len()):
		for j in range(0,len(val)):
			if val[i][j] == 1:
				temp[i][j] = en[0][0][i][j]
			else:
				temp[i][j] = en[0][1][i][j]	
	return temp	

def evaluar(n):


#for i in entrenar():
#	print i
#	print "----------------"