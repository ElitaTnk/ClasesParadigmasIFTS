numeros = [2, 5, 10, 23, 50, 33]
#
# def doblar(numero):
#     return numero *2
#
#
# print(list(map(doblar, numeros)))
#

print(list(map(lambda numero: numero *2, numeros)))
