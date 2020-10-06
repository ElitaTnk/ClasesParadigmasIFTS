import puntajes

import puntajes_csv

import puntajes_binario

datos = [("Eliana", "103", "12:08:34"), ("Julieta", "110", "11:23:12"), ("Ana", "182", "23:11:11")]

puntajes_binario.guardar_puntajes("datos_flappyBird", datos)

datos_recuperados = puntajes_binario.recuperar_puntajes("datos_flappyBird")
#
# datos = [("Eliana", "153", "12:08:34"), ("Julieta", "140", "11:23:12"), ("Ana", "182", "23:11:11")]


print(datos_recuperados)
