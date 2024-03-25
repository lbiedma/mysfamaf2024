from random import random
from rbisec import rbisec

def apostar(c: float) -> float:
    """
    Apostar c y devolver el premio con "probabilidad = 0.01".
    random devuelve un número según distribucion uniforme U(0, 1).
    """
    premio = -c
    azar = random()
    if azar < 0.01:
        premio += 70
    
    return premio

def varios_juegos(c: float, jugadas: int) -> float:
    """
    Hacer varios juegos apostando c y devolver la ganancia total.
    """
    ganancia = 0
    for i in range(jugadas):
        ganancia += apostar(c)
    
    return ganancia

def esperanza(c: float) -> float:
    """
    Hacer muchos experimentos con una apuesta de c y devolver el promedio de la ganancia.
    Esto se parece mucho a la esperanza si hago suficientes experimentos.
    """
    pruebas = []
    for i in range(10000):
        pruebas.append(varios_juegos(c, 10000))
    
    return sum(pruebas) / 100000000

if __name__ == "__main__":
    print(f"Aproximación ejercicio a): {esperanza(1)}")
    hx, hf = rbisec(esperanza, [0.1, 1], 20, 1e-4)

    print(f"Para tener esperanza 0 debería apostar aproximadamente {hx[-1]}")
