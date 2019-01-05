import numpy as np
a = np.array([2,3,4])
print(a)
print(a.dtype)
b = np.array([[2,3,4],[5,6,7]])
print(b)
c = np.arange(1,21,1).reshape(4,5)
print(c)
d = np.array([34,12,3,4])
e = np.array([2,3,4,5])
f = d-e
print(f)
g = e*10
print(g)
h = np.linspace(2,3,10)
print(h)
j = np.empty((3,4))
print(j)
print(c.sum(axis=0))
#trabajo con listas
#h = arr[-2:]
#h[::]=0

#print(h)
#multi dimensiones
i=np.array([[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33],[40,41,42,42]])
print(i)
print(i[2,0])
print("imprime toda la columna ", i[0:5,1])
print("imprime toda la fila",i[0])
#mascaras
j=np.arange(10000)
l=mascara=(j>0)&(j<3)
l
print(l)
datos = np.array([3, 7, -2, 6, 7, -8, 11, -1, -2, 8,1,2])
datos
mask=datos>=0
print(mask)
#recorrer la matriz
for i in datos.flat:
	print(i)
#recorrer y aplanar
print("aplanar",np.ravel(c))
k=c.ravel()

m=np.arange(12).reshape(3,4)
print(m)
m.ravel()
n=shape(3,4)

print(n)