import cv2
import numpy as np
import ctypes

r1 = np.zeros((20,20))
r2 = np.zeros((20,20))
r3 = np.zeros((20,20))
r4 = np.zeros((20,20))
r5 = np.zeros((20,20))

r1 = cv2.rectangle(r1,(5,5),(15,15),1,-1)
r2 = cv2.rectangle(r2,(5,5),(15,15),1,-1)
r3 = cv2.rectangle(r3,(5,5),(15,15),1,-1)
r4 = cv2.rectangle(r4,(5,5),(15,15),1,-1)
r5 = cv2.rectangle(r5,(5,5),(15,15),1,-1)


c1 = np.zeros((20,20))
c2 = np.zeros((20,20))
c3 = np.zeros((20,20))
c4 = np.zeros((20,20))
c5 = np.zeros((20,20))

c1 = cv2.circle(c1,(10,10), 5 , 1 , -1)
c2 = cv2.circle(c2,(10,10), 4 , 1 , -1)
c3 = cv2.circle(c3,(10,10), 7 , 1 , -1)
c4 = cv2.circle(c4,(10,10), 6 , 1 , -1)
c5 = cv2.circle(c5,(10,10), 8 , 1 , -1)

'''
cv2.imshow('r1',r1)
cv2.imshow('r2',r2)
cv2.imshow('r3',r3)
cv2.imshow('r4',r4)
cv2.imshow('r5',r5)

cv2.imshow('c1',c1)
cv2.imshow('c2',c2)
cv2.imshow('c3',c3)
cv2.imshow('c4',c4)
cv2.imshow('c5',c5)

print r1
print "__________________"
print c2
cv2.waitKey(0)
cv2.destroyAllWindows() 
'''
x1 = [r1,r2,r3,r4,r5]
x2 = [c1,c2,c3,c4,c5]


def contar1(xs):
	a = np.zeros((20,20),dtype=np.uint8)
	for n in xs:
		a = a + n
	return a

def contar0(xs):
	a=np.ones((20,20),dtype=np.uint8)
	return len(xs) - contar1(xs)

def laplace(xl):
	return xl + np.ones((20,20),dtype=np.uint8)
	
def normalizar(xn):
	return 1/7.0 * xn

#a = normalizar(laplace(contar1(x1)))
#print a
#b=  normalizar(laplace(contar0(x1)))

#print normalizar(laplace(contar0(x1)))[100][100]

def entrenar(x1,x2):
	n = contar1(x1)[0][0] + contar0(x1)[1,1]
	rec = [normalizar(laplace(contar1(x1))),normalizar(laplace(contar0(x1)))]
	cir = [normalizar(laplace(contar1(x2))),normalizar(laplace(contar0(x2)))]
	return [rec,cir]

#print entrenar(x1,x2)

def evaluarA(val,en):
	temp = np.zeros((20,20))
	for i in range(0,len(val)):
		for j in range(0,len(val)):
			if val[i][j] == 1:
				temp[i][j] = en[0][0][i][j]
			else:
				temp[i][j] = en[0][1][i][j]	
	return temp

def evaluarB(val,en):
	temp = np.zeros((20,20))
	for i in range(0,len(val)):
		for j in range(0,len(val)):
			if val[i][j] == 1:
				temp[i][j] = en[1][0][i][j]
			else:
				temp[i][j] = en[1][1][i][j]
	return temp

def fin(ev):
	x=1
	ctypes.c_ulong(x)
	k=0
	for i in ev:
		for j in i:
			x*=j
			k+=1
			#print x
			if x==0:
				return x
	#print k
	return  x


ent = entrenar(x1,x2)
print ent

p = np.zeros((20,20))
#p = cv2.rectangle(p,(5,5),(15,15),1,-1)

p = cv2.circle(p,(10,10),5,1,-1)
'''
cv2.imshow('p',p)
cv2.waitKey(0)
cv2.destroyAllWindows() 
'''
ent = entrenar(x1,x2)
print evaluarA(p,ent)
fina = fin(evaluarA(p,ent))
finb = fin(evaluarB(p,ent))

print "fina: " + str(fina)
print "finb: " + str(finb)


evidencia = fina + finb
print "Evidencia: " + str(evidencia)

pA = fina/evidencia
pB = finb/evidencia

print pA
print pB