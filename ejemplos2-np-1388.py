import numpy as np

print("----------- llenar matriz de ceros -----------")
matriz = np.zeros([3,5])# 3 filas *orisontales* por 5 filas *berticales*
print(matriz)
print("----------- llenar matriz de unos -----------")
matriz = np.ones([3,5])
print(matriz)
print("----------- llenar matriz de vacio -----------")
matriz = np.empty([3,5])
print(matriz)
print("----------- llenar arreglo con rango -----------")
# El primer parametro es el valor inicial
# El segundo parametro es el valor final
# El tercer parametro es el incremento
lista = np.arange(0,10,2)
print(lista)
print("----------- llenar arreglo con rango No 2 -----------")
lista = np.arange(0,10,1)
print(lista)