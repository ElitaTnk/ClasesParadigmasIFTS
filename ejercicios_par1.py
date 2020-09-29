# ejercicio 1 Cortar una pizza
# from fractions import Fraction
# #
# def cortadorPizza(pizza, original,  porciones):
#     for corte in range(porciones):
#         pizza = pizza/2
#         if pizza == original/porciones:
#             return pizza
#
#
# # recursivo , creditos emanuel
# def exercisePizza(pizza, original, porciones):
#     if pizza == original/porciones:
#         return pizza
#     return exercisePizza(pizza / 2, original, porciones)
#
# print(cortadorPizza(1, 1, 8))
# print (Fraction(exercisePizza(1, 1, 8)))
#
#
# def cuadrados():
#     lista = []
#     for i in range(4):
#         lista.append(int(input(f"ingrese el numero {i + 1}: ")))
#
#     return cuadrado(lista)
#
# def cuadrado(lista):
#     return [numero * numero for numero in lista]
#
# print(cuadrados())

# no funciona
# def contadorDigitos(numero, contador):
#     if numero >= contador:
#         numero //= 10
#         contador = contadorDigitos(numero, contador+1)
#     return contador
#
# print(contadorDigitos(33888, 0))


#creditos : martin
# def contador_digitos(numero, contador):
#     contador += 1
#     numero = numero /10
#     if numero <= 1:
#         return contador
#     return contador_digitos(numero, contador)
#
# print(contador_digitos(6234, 0))
#
def separadorDeListas(lista):
    sub1 = lista.copy()
    sub2 = []

    for elemento in lista:
        if isinstance(elemento, list):
            if len(sub2) > 0:
                sub2 += elemento
            else:
                sub2 = elemento.copy()


            sub1.remove(elemento)

    return sub1, sub2

print(separadorDeListas([1, ['a', 'b', 'c'], 2, 3, ['c', 'd', 'e']]))
