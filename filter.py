numeros = [2, 5, 10, 23, 50, 33]
#
# def multiple(numeros):
#     if numeros % 5 == 0:
#         return True

# resultado = list(filter(multiple, numeros))

resultado2 = list(filter(lambda numero: numero % 5 == 0, numeros))


print(resultado, resultado2)
