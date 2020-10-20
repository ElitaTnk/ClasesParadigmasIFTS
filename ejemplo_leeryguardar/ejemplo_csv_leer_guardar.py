import csv

def leer_cumples(archivo):
    "Abre un archivo de texto o separado por comas e imprime sus columnas, y datos del cumpleañero"
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file)
        lista_de_cumples = []
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                #guardo el encabezado en variable
                header = row
                line_count += 1
            else:
                lista_de_cumples.append(row)
                line_count += 1
        return header, lista_de_cumples

def guardar_cumples(encabezado, cumples):
    "Guarda en un archivo CSV los cumples indicados"
    with open('empleados_leeryguadar.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file)

        employee_writer.writerow(encabezado)
        employee_writer.writerows(cumples)

# deconstruyo el resultado de leer cumples en dos variables y paso a la siguiente funcion como parametros
categorias , cumpleañitos = leer_cumples("cumples.txt")
guardar_cumples(categorias, cumpleañitos)
