import puntajes
valores = [("Juan Pablo", 105, "4:15"), ("Eliana", 325, "8:12"), ("Gustavo", 35, "14:15"), ("Natalia", 25, "28:12")]
puntajes.guardar_puntajes("tabla.txt", valores)
recuperado1 = puntajes.recuperar_puntajes("tabla.txt")
print(recuperado1)

# [('Juan Pablo', 105, '4:15'), ('Eliana', 325, '8:12'), ('Gustavo', 35, '14:15'), ('Natalia', 25, '28:12')]

import puntajes_csv
puntajes_csv.guardar_puntajes("tabla.csv", valores)
recuperado2 = puntajes_csv.recuperar_puntajes("tabla.csv")
print(recuperado2)
#[('Juan Pablo', 105, '4:15'), ('Eliana', 325, '8:12'), ('Gustavo', 35, '14:15'), ('Natalia', 25, '28:12')]

import puntajes_pickle
puntajes_pickle.guardar_puntajes("tabla.dat", valores)
recuperado3 = puntajes_pickle.recuperar_puntajes("tabla.dat")
print(recuperado3)
#[('Juan Pablo', 105, '4:15'), ('Eliana', 325, '8:12'), ('Gustavo', 35, '14:15'), ('Natalia', 25, '28:12')]
