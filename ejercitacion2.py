# def cut(archivo, campos, delimitador):
#     try:
#         with open(archivo, 'r', newline='') as file:
#             linea = file.readline()
#             campos_seleccionados = []
#             while linea:
#                 lista_temp = linea.split(delimitador)
#                 for campo in campos:
#                     # try:
#                     #     campos_seleccionados.append(lista_temp[campo])
#                     # except IndexError:
#                     #     print(f"El campo {campo} no existe")
#
#                     if campo < len(lista_temp):
#                         campos_seleccionados.append(lista_temp[campo])
#                     else:
#                         print(f"El campo {campo} no existe")
#                 linea = file.readline()
#         #impresion final
#         for item in campos_seleccionados:
#             print(item)
#
#     except IOError:
#         print("Hubo un problema con el archivo")
import csv

def cut(archivo, campos, delimitador):
    try:
        with open(archivo, 'r', newline='') as file:
            lectura = csv.reader(file, delimiter=delimitador)
            linea = next(lectura, None)
            campos_seleccionados = []

            while linea:
                for campo in campos:
                    # if campo < len(linea):
                    #     campos_seleccionados.append(linea[campo])
                    # else:
                    #     print(f"El campo {campo} no existe")
                    try:
                        campos_seleccionados.append(linea[campo])
                    except IndexError:
                        print(f"El campo {campo} no existe")
                linea = next(lectura, None)
        #impresion final
        for item in campos_seleccionados:
            print(item)
    except IOError:
        print("Hubo un problema con el archivo")

# cut('cut.txt', [0, 5, 1], '-')


def wc(archivo):
    cant_lineas = 0
    cant_palabras = 0
    cant_caracteres = 0

    try:
        with open(archivo, 'r', newline='') as file:
            for linea in file:
                cant_lineas += 1
                linea = linea.rstrip('\n')
                cant_caracteres += len(linea)
                cant_palabras += len(linea.split())
    except IOError:
        print("Hubo un error al abrir el archivo")

    print(f"Lineas {cant_lineas}, total caracteres {cant_caracteres}, cantidad palabras {cant_palabras}")

# wc('cut.txt')

def guardar_datos(datos, archivo):
    try:
        with open(archivo, 'w', newline='') as file:
            for dato in datos:
                file.write(f'{dato}, {datos[dato]}\n')
            print('Se guardo correctamente')
    except IOError:
        print("Hubo un error al abrir el archivo")

def cargar_datos(archivo):
    try:
        with open(archivo, 'r', newline='') as file:
            linea = file.readline()
            diccionario = {}

            while linea:
                linea = linea.rstrip('\n')
                campos = linea.split(',')
                diccionario[campos[0]] = campos[1]
                linea = file.readline()

            return diccionario
    except IOError:
        print("Hubo un error al abrir el archivo")


datoss = {"nombre": "eliana", "apellido": "rodriguez"}
# guardar_datos(datoss, "ejercicio4.txt")
# print(cargar_datos("ejercicio4.txt"))

def pedirNumero():
    while True:
        numero = input("Ingrese un numero entre 1 y 10: ")
        try:
            numero = int(numero)
            if 0 < numero <= 10:
                return numero
            else:
                print("El numero tiene que estar entre 1 y 10")
        except ValueError:
            print(f"{numero} no es un valor entero")

def tablaN():
    numero = pedirNumero()
    try:
        with open(f'tabla-{numero}.txt', 'w', newline='') as file:
            for multiplicador in range(1,11):
                file.write(f'{multiplicador} x {numero} = {numero * multiplicador}\n')
    except IOError:
        print("Hubo un error con el archivo")

# tablaN()
#7 b
import os.path

def eje7_guardar(archivo, campos):
    guardar = "si"
    lista_vendedores = []
    while guardar == "si":
        vendedor = {}

        for campo in campos:
            vendedor[campo] = input(f"Ingrese {campo} del vendedor: ")
        lista_vendedores.append(vendedor)
        guardar = input("Desea seguir agregando vendedores? Si/No")

    try:
        archivo_existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(lista_vendedores)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

#7 c
def eje7_cargar(archivo):
    try:
        with open(archivo,'r', newline='') as file:
            lectura_csv = csv.DictReader(file)
            campos = lectura_csv.fieldnames

            for linea in lectura_csv:
                print(f"{linea[campos[1]]} {linea[campos[0]]} trabaja en la empresa desde {linea[campos[2]]} y lleva comisionado {linea[campos[4]]}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

# 7 a
def ejercicio7():
    ARCHIVO = "vendedores.csv"
    CAMPOS = ['Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Comisiones']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            eje7_guardar(ARCHIVO, CAMPOS)
        if opcion == "2":
            eje7_cargar(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")

ejercicio7()


#7 b listas
def eje7_guardar_listas(archivo, campos):
    guardar = "si"
    lista_vendedores = []
    while guardar == "si":
        vendedor = []

        for campo in campos:
            vendedor.append(input(f"Ingrese {campo} del vendedor: "))
        lista_vendedores.append(vendedor)
        guardar = input("Desea seguir agregando vendedores? Si/No")

    try:
        with open(archivo, 'w', newline='') as file:
            file_guarda = csv.writer(file)
            file_guarda.writerows(lista_vendedores)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

#7 c listas
def eje7_cargar_listas(archivo):
    try:
        with open(archivo,'r', newline='') as file:
            lectura_csv = csv.reader(file)

            for linea in lectura_csv:
                print(f"{linea[1]} {linea[0]} trabaja en la empresa desde {linea[2]} y lleva comisionado {linea[4]}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

# 7 a listas
def ejercicio7_listas():
    ARCHIVO = "vendedores_listas.csv"
    CAMPOS = ['Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Comisiones']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            eje7_guardar_listas(ARCHIVO, CAMPOS)
        if opcion == "2":
            eje7_cargar_listas(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")

# ejercicio7_listas()
