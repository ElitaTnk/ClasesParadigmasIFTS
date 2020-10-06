import pickle

def guardar_puntajes(nombre_archivo, puntajes):
    """Guarda la lista de puntajes en el archivo.
    Pre: nombre_archivo corresponde a un archivo válido,
    puntajes corresponde a una lista de tuplas de 3 elementos.
    Post: se guardaron los valores en el archivo,
    separados por comas.
    """

    with open(nombre_archivo, "wb") as f:
        pickle.dump(puntajes, f)

def recuperar_puntajes(nombre_archivo):
    """Recupera los puntajes a partir del archivo provisto.
    Devuelve una lista con los valores de los puntajes.
    Pre: el archivo contiene los puntajes en el formato esperado,
    separados por comas
    Post: la lista devuelta contiene los puntajes en el formato:
    [(nombre1,puntaje1,tiempo1),(nombre2,puntaje2,tiempo2)].
    """

    with open(nombre_archivo, "rb") as f:
        return pickle.load(f)
