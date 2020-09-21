def quick_sort(lista):
    """Ordena la lista de forma recursiva.
    Pre: los elementos de la lista deben ser comparables.
    Devuelve: una nueva lista con los elementos ordenados."""
    print("entra a quick sort")
    if len(lista) < 2:
        print("devuelve lista con 1 elemento")
        return lista
    menores, medio, mayores = _partition(lista)
    print("concatena")
    return quick_sort(menores) + medio + quick_sort(mayores)

def _partition(lista):
    """Pre: lista no vacía.
    Devuelve: tres listas: menores, medio y mayores."""
    pivote = lista[0]
    menores = []
    mayores = []
    for x in range(1, len(lista)):
        print(f"pivote: {pivote}, valor: {lista[x]}")

        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores, [pivote], mayores


print(quick_sort([7,5,3,12,9,2,10,4,15,8]))
