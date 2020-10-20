# # leyendo todo el contenido
# def head(archivo, numero):
#     # file = open(archivo) otra manera
#     with open(archivo, 'r') as file:
#         # nos devuelve una lista
#         lectura = file.readlines()
#
#         # recorremos la lista
#         for linea in range(len(lectura)):
#             if linea <= numero:
#                 print(lectura[linea])
#
#
#
# # leyendo linea x linea
# def head(archivo, numero):
#     contador = 0
#     with open(archivo, 'r') as file:
#         # mientras se cumpla la condicion leemos de a 1 linea
#         while contador <= numero:
#             print(file.readline())
#             contador += 1
#
#
# head('README.md', 3)


def cp(archivo):
    with open(archivo, 'r') as file:
        lectura = file.readlines()

    with open('copiaReadme.md', 'w') as file2:
        file2.writelines(lectura)



def cp(archivo):
    with open(archivo, 'r') as file:
        with open('copiaDeALinea.md', 'w') as file2:
            linea = file.readline()
            while linea != '':
                file2.write(linea)
                linea = file.readline()

cp('README.md')
