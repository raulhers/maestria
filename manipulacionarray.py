import numpy as np 
a=np.arange(12).reshape(3,4)
a
print(a)
#b=a.ravel()
#print("ravel",b)
c=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
b=c.reshape(5,3)
print(b)
#Fusion
d=np.arange(4).reshape(2,2)
e=np.arange(5,9,1).reshape(2,2)
print(np.concatenate((d,e),axis=0))
#Division por array
f=np.arange(12).reshape(3,4)
print(f)
print(np.hsplit(f,2))
print(np.vsplit(f,1))
#Asignacion y copias
g=np.array([[1,2],[3,4]])
h=g
h.reshape(1,4)
print(h)
print(g)
#vistas
i=g.view()
print(i)
print(h)
#-----------
j = np.arange(12)
print(j)
k = j
k is j
k.shape = 3,4
print(k)
print(j)