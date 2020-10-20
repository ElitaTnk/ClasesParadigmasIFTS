import csv

def imprimir_notas_alumnos(alumnos, notas):
    """ Abre los archivos de alumnos y notas, y por cada alumno imprime
        todas las notas que le corresponden. """
    notas_a = open(notas)
    alumnos_a = open(alumnos)
    notas_csv = csv.reader(notas_a)
    alumnos_csv = csv.reader(alumnos_a)

    # Saltea los encabezados
    next(notas_csv)
    next(alumnos_csv)

    # Empieza a leer
    alumno = next(alumnos_csv, None)
    nota = next(notas_csv, None)
    while (alumno):
        print("{}, {} ({})".format(alumno[1], alumno[2], alumno[0]))
        if (not nota or nota[0] != alumno[0]):
            print("\tNo se registran notas")
        while (nota and nota[0] == alumno[0]):
            print("\t{}: {}".format(nota[1], nota[2]))
            nota = next(notas_csv, None)
        alumno = next(alumnos_csv, None)

    # Cierro los archivos
    notas_a.close()
    alumnos_a.close()

imprimir_notas_alumnos("alumnos.csv", "notas.csv")
