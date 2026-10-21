import numpy as np

califas = np.array([60,70,90])
print("----------- Ejemplo 1 imprimir califas -----------")
print(califas) # imprimir la lista de califas
print(type(califas)) # muestra el tipo de arreglo
print("----------- Ejemplo 0 dimensiones de un array-----------")

califas = np.array(60)
print(califas)
print("Dimensiones :", califas.ndim)
print("----------- Ejemplo 2 1 dimension de un array-----------")
califas = np.array([60,70,90])
print(califas)
print("Dimensiones :", califas.ndim)
print("----------- Ejemplo 2 2 dimension de un array-----------")
califas = np.array([
    [60,70,90],
    [50,80,98]
    ])# un arreglo de 2 dimensiones es como una tabla en exel
print(califas)
print("Dimensiones :", califas.ndim)
print("----------- Ejemplo 2 3 dimension de un array-----------")
califas = np.array([
    [
    [60,70,90],
    [50,80,98]
    ],
    [
    [60,70,90],
    [50,80,98]
    ]
    ])
print(califas)
print("Dimensiones :", califas.ndim)
