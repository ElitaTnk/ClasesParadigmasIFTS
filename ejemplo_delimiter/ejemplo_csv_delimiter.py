import csv

def leer_cumples(archivo):
    "Abre un archivo de texto o separado por comas e imprime sus columnas, y datos del cumpleañero"
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")

        line = next(csv_reader, None)
        print(f'Los nombres de las columnas son {", ".join(line)}')

        for row in csv_reader:
            print(f'\t{row[0]} trabaja en el area de {row[1]} y nació en {row[2]}.')

def guardar_cumples(cumples):
    "Guarda en un archivo CSV los cumples indicados"
    with open('empleados_delimiter.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=";")
        # realmente no hace falta iterar aca pero queria usar writerow
        for employee in cumples:
            employee_writer.writerow(employee)


leer_cumples("empleados_delimiter.csv")
#guardar_cumples([['nombre', 'area', 'cumpleaños'],['Juan Carlos', 'Contabilidad', 'Noviembre, 5 de'], ['Roberto Carlos', 'Deportes', 'Enero, 7 de']])

# cuando importen el archivo en excel van a tener que abrirlo solo por semicolon
