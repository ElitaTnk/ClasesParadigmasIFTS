listaEntrada = [3,2,-1,5,0,2]

# O(n2)
def orden_seleccion(lista):
    ultimaPosicion = len(lista) - 1

    while ultimaPosicion > 0: #N
        mayorElemento = buscar_max(lista, 0, ultimaPosicion)
        lista[mayorElemento], lista[ultimaPosicion] = lista[ultimaPosicion], lista[mayorElemento]
        print(f"DEBUG: posicion mayor {mayorElemento}, ultima posicion {ultimaPosicion}, {lista}")
        ultimaPosicion = ultimaPosicion - 1


def buscar_max(lista, inicio, fin):
    pos_max = inicio
    for i in range(inicio +1, fin+1): #N

        if lista[i] > lista[pos_max]:
            print(f"posicion {i} {lista[i]} es mayor que {pos_max} {lista[pos_max]}")
            pos_max = i
            print("pos_max es ", pos_max)

    return pos_max

print(listaEntrada)
orden_seleccion(listaEntrada)
print(listaEntrada)
