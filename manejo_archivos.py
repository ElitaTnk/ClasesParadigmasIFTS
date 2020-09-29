# archivo = open("alumnos.txt")

#linea = archivo.readline() readlines
#
# for linea in archivo:
#     print(linea)

# lineas = archivo.readlines()
#
# print(lineas)
#
#
# archivo.close()
#
# lineas = archivo.readlines()
#
# print(lineas)
with open("alumnos.txt", 'a+') as archivo:
    i = 1
    for linea in archivo:
        linea = linea.rstrip("\n")
        print("{}: {}".format(i, linea))
        #print(f"{i}: {linea}")
        i += 1

    archivo.write("hola")
