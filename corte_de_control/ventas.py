import csv

def ventas_clientes_mes(archivo_ventas):
    """ Recorre un archivo csv, con la información almacenada en el
    formato: cliente,año,mes,venta """

    # Inicialización
    ventas = open(archivo_ventas)
    ventas_csv = csv.reader(ventas)

    item = next(ventas_csv, None)
    total = 0

    while item:
        # Inicialización para el bucle de cliente
        cliente = item[0]
        total_cliente = 0
        print("Cliente {}".format(cliente))

        while item and item[0] == cliente:
            # Inicialización para el bucle de año
            anyo = item[1]
            total_anyo = 0
            print("\tAño: {}".format(anyo))

            while item and item[0] == cliente and item[1] == anyo:
                mes, monto = item[2], float(item[3])
                print("\t\tVentas del mes {}: {:.2f}".format(mes, monto))
                total_anyo += monto
                # Siguiente registro
                item = next(ventas_csv, None)

            # Final del bucle de año
            print("\tTotal para el año {}: {:.2f}".format(anyo, total_anyo))
            total_cliente += total_anyo

        # Final del bucle de cliente
        print("Total para el cliente {}: {:.2f}\n".format(cliente, total_cliente))
        total += total_cliente

    # Final del bucle principal
    print("Total general: {:.2f}".format(total))

    # Cierre del archivo
    ventas.close()

ventas_clientes_mes("ventas.csv")
