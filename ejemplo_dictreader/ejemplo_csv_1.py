import csv

def leer_cumples(archivo):
    "Abre un archivo de texto o separado por comas e imprime sus columnas, y datos del cumpleañero"
    with open(archivo) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        claves = csv_reader.fieldnames
        print(f'Los nombres de las columnas son {", ".join(csv_reader.fieldnames)}')

        for row in csv_reader:
            print(f'\t{row[claves[0]]} trabaja en el area de {row[claves[1]]} , y nació en {row[claves[2]]}.')

#
def guardar_cumples(cumples):
    "Guarda en un archivo CSV los cumples indicados"
    with open('empleados_dict.csv', mode='w') as employee_file:
        employee_writer = csv.DictWriter(employee_file, fieldnames=['nombre', 'area', 'mes de cumpleaños'])
        employee_writer.writeheader()
        employee_writer.writerows(cumples)

leer_cumples("empleados_dict.csv")
guardar_cumples([{'nombre': 'Juan Carlos', 'area':'Contabilidad', 'mes de cumpleaños':'Noviembre'}, {'nombre': 'Eliana Martinez', 'area':'Sistemas', 'mes de cumpleaños':'Octubre'}])
