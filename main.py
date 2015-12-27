import cv2
import numpy as np
import ctypes
from recortar01 import *
import decimal

base = "caritas"
stra = "feliz"
strb= "triste"

x1 = []
x2 = []

for i in range(5):
	x1.append(binar(cv2.imread("listo-"+base+"/"+stra+"-"+str(i)+".jpg",0))/255)
	x2.append(binar(cv2.imread("listo-"+base+"/"+strb+"-"+str(i)+".jpg",0))/255)
"""
for i in range(100):
	for j in range(100):
		print x1[0][i][j],
	print "\n" """

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
	
def normalizar(xn):
	return 1/7.0 * xn
	#return xn
"""	
print contar0(x1)[0][0]
print contar1(x1)[0][0]	
print contar0(x1)[32][32]
print contar1(x1)[32][32]
"""
#a = normalizar(laplace(contar1(x1)))[32][32]
#b=  normalizar(laplace(contar0(x1)))[32][32]

#print a
#print b
#print normalizar(laplace(contar0(x1)))[100][100]

def entrenar(x1,x2):
	n = contar1(x1)[0][0] + contar0(x1)[1,1]
	rec = [normalizar(laplace(contar1(x1))),normalizar(laplace(contar0(x1)))]
	cir = [normalizar(laplace(contar1(x2))),normalizar(laplace(contar0(x2)))]
	return [rec,cir]

#print entrenar(x1,x2)

def evaluarA(val,en):
	temp = np.zeros((100,100))
	for i in range(0,len(val)):
		for j in range(0,len(val)):
			if val[i][j] == 1:
				temp[i][j] = en[0][0][i][j]
			else:
				temp[i][j] = en[0][1][i][j]	
	return temp

def evaluarB(val,en):
	temp = np.zeros((100,100))
	for i in range(0,len(val)):
		for j in range(0,len(val)):
			if val[i][j] == 1:
				temp[i][j] = en[1][0][i][j]
			else:
				temp[i][j] = en[1][1][i][j]
	return temp

def fin(ev):
	x=decimal.Decimal('1')
	ctypes.c_ulong(x)
	k=0
	for i in ev:
		for j in i:
			x*=decimal.Decimal(j)
			#k+=1
			#print x , " --",  j , "  . " , k
			#if x==0:
			#		return x
	print k
	return  x


#MAin
ent = entrenar(x1,x2)
#print ent

#p = binar(cv2.imread("listo-caritas/triste-4.jpg",0))
p = binar(cv2.imread("listo-caritas/triste-3.jpg",0))
p = p/255


'''for i in range(5):
	cv2.imshow("ima"+str(i),x1[i])
	cv2.imshow("imb"+str(i),x2[i])'''

#cv2.imshow("ima"+str(i),p)
#cv2.imshow("imb"+str(i),p)

cv2.imshow('p',p)
cv2.waitKey(0)
cv2.destroyAllWindows() 


ent = entrenar(x1,x2)
#print evaluarA(p,ent)
fina = fin(evaluarA(p,ent))
finb = fin(evaluarB(p,ent))

print "fina: " ,fina
print "finb: " ,finb


evidencia = fina + finb
print "Evidencia: " , evidencia , fina+finb

pA = fina/evidencia
pB = finb/evidencia

print pA
print pB

if pA>pB :
	print "Tipo A"
else:
	print "Tipo B"