def von_neumann(u):
    return (u**2 // 100) % 10000

def generar(x, mult, sum, mod):
    return (mult * x + sum) % mod

if __name__ == "__main__":
    print("Ejercicio a)")
    for semilla in [3792, 1004, 2100, 1234]:
        u = semilla
        print(f"Semilla: {u}")
        for _ in range(10):
            u = von_neumann(u)
            print(u)
        print("--------------------")

    print("Ejercicio b)")
    for y_0 in [4, 50]:
        print(y_0)
        for _ in range(10):
            y_0 = generar(y_0, 5, 4, 2**5)
            print(y_0)
