# ejemplo 1
# lista = []
# for numero in range(0,11):
#     lista.append(numero ** 2)
# print(lista)
#
# lista_c = [numero **2 for numero in range(0,11)]
# print(lista_c)


# ejemplo 2
lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero ** 2)
print(lista)


lista_c = [numero **2 for numero in range(0,11) if numero % 2 == 0]
print(lista_c)
