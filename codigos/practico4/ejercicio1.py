import numpy as np

N = [100, 1000, 10000, 100000]
for n in N:
    suma_exitos = 0
    suma_cuadrados = 0
    for i in range(n):
        permutacion = np.random.permutation(np.arange(100))
        exito = permutacion == np.arange(100)
        suma_exitos += np.sum(exito)
        suma_cuadrados += np.sum(exito)^2

    print(n)
    print(f"Esperanza: {suma_exitos / n}")
    print(f"Varianza: {(suma_cuadrados - suma_exitos^2) / n}")
    print('------------------------')
