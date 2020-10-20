import csv

def leer_cumples(archivo):
    "Abre un archivo de texto o separado por comas e imprime sus columnas, y datos del cumpleañero"
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file)

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Los nombres de las columnas son {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} trabaja en el area de {row[1]} , y nació en {row[2]}.')
                line_count += 1
        print(f'{line_count} lineas procesadas.')

def guardar_cumples(cumples):
    "Guarda en un archivo CSV los cumples indicados"
    with open('empleados.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file)
        # realmente no hace falta iterar aca pero queria usar writerow
        for employee in cumples:
            employee_writer.writerow(employee)


leer_cumples("cumples.txt")
guardar_cumples([['Juan Carlos', 'Contabilidad', 'Noviembre'], ['Roberto Carlos', 'Deportes', 'Enero']])
