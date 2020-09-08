import time

def suma_lineal(cant):
    suma = 0
    for numero in range(1, cant+1):
        suma += numero

    return suma

# 1 + n * 2 =>  2n

# O(n) lineal

def suma_continua(cant):
    return (cant /2 ) * (cant +1)

#1 + 1 + 1 = 3  ==>  O(1) constante


cantidad = 100000

for i in range(4):
    t_0 = time.time()

    suma1 = suma_lineal(cantidad)

    t_1 = time.time()

    suma2 = suma_continua(cantidad)

    t_2 = time.time()

    print(f"{suma1}, {t_1 - t_0}")
    print(f"{suma2}, {t_2 - t_1}")

    cantidad *= 10
