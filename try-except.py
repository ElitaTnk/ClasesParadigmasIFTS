archivo = None
try:
    archivo = open("miarchivo.txt")
# procesar el archivo
except IOError:
    print("Error de entrada/salida.")
# realizar procesamiento adicional
except:
    print("generico")
# procesar la excepción
finally:
# si el archivo está abierto debemos cerrarlo
    print("llego al finally")
    if archivo and not archivo.closed:
        archivo.close()
