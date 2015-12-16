def contar1s(xs):
	cont = 0
	for i in xs:
		for j in i:
			if j == 1:
				cont += 1
	return cont

def contar0s(xs):
	return len(xs) * len(xs[0]) - contar1s

def ListaFil1s(xs):
	ys = []
	for i in xs:
		suma = 0
		for j in i:
			suma += j
		ys.append(suma)
	return ys

def ListaCol1s(xs):
	ys = [0]*len(xs[0])
	for i in range(len(xs[0])):
		for j in range(len(xs)):
			ys[i] += xs[j][i]
	return ys

xs = [
	[1,0,0,0,1],
	[1,1,1,1,0],
	[0,0,0,0,1]
	]
print(ListaFil1s(xs))
print(ListaCol1s(xs))