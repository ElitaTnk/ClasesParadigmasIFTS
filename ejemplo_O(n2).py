"""
Una empresa de autopistas tiene instalada una camara en el peaje que cuenta el numero de vehiculos que pasa, y unas gomas en el piso que cuentan el numero de ruedas de esos vehiculos.

Se pide elaborar un algoritmo que a partir del numero de vehiculos y el numero de ruedas extraiga la cantidad de coches y motos que pasan por allí
"""

# vehiculos = coches + motos
# ruedas =  coches * 4 + motos * 2

# O(n2) cuadratica
def cochesYmotosN2(vehiculos, ruedas):
    for coche in range(vehiculos + 1): # N
        for moto in range(vehiculos + 1): # N
            print(f"cantidad coches {coche} y motos {moto} y de vehiculos { vehiculos}")

            if ((coche + moto == vehiculos) and (coche * 4 + moto * 2 == ruedas)):
                #print(f"{coche * 4} + {moto*2} = {ruedas}")
                return coche, moto


# vehiculos = coches + motos
# motos = vehiculos - coches
# ruedas =  coches * 4 + motos * 2

# O(n) lineal
def cochesYmotosLineal(vehiculos, ruedas):
    for coche in range(vehiculos + 1): # N
        moto = vehiculos - coche
        print(f"cantidad coches {coche} y motos {moto} y de vehiculos { vehiculos}")

        if ((coche + moto == vehiculos) and (coche * 4 + moto * 2 == ruedas)):
            print(f"{coche * 4} + {moto*2} = {ruedas}")
            return coche, moto

# cochesYmotosN2(6, 20)
# print("------------------------")
# cochesYmotosLineal(6, 20)

# motos = vehiculos - coches
# ruedas =  coches * 4 + motos * 2
# ruedas = coches * 4 + (vehiculos - coches) * 2 =>  ruedas/2 = coches * 4/2 + (vehiculos - coches) *2/2
# ruedas/2 = coches * 2 + vehiculos - coches
# coches * 2 + vehiculos - coches = ruedas/2
# coches = ruedas/2 - vehiculos

# O(1) constante
def cochesYmotos(vehiculos, ruedas):
    coche = ruedas/2 - vehiculos #1
    moto = vehiculos - coche #1
    print(f"cantidad coches {coche} y motos {moto} y de vehiculos { vehiculos}")

    if (int(coche) + int(moto) == vehiculos): #1
        print(f"{int(coche) * 4} + {int(moto)*2} = {ruedas}")
        return int(coche), int(moto)

cochesYmotosN2(6, 20)
print("------------------------")
cochesYmotosLineal(6, 20)
print("------------------------")
cochesYmotos(6, 20)
