
try:
    with open("miarchivo.txt") as f:
        pass
        # procesar el archivo
except IOError:
    print("Error de entrada/salida.")
# realizar procesamiento adicional
except:
    print("generico")
# procesar la excepción
