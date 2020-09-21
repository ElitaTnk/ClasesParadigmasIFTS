def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
    Pre: lista debe contener elementos comparables.
    Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        #print("devuelve lista porque len < 2")
        return lista
    medio = len(lista) // 2
    #print("hola soy merge sort")
    izq = merge_sort(lista[:medio])
    #print("izq")
    der = merge_sort(lista[medio:])
    #print("derecho")

    return merge(izq, der)

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
    Pre: lista1 y lista2 deben estar ordenadas.
    Devuelve: una lista con los elementos de lista1 y lista2."""
    #print("DEBUG", "lista1", lista1, "lista2", lista2)
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):

        if (lista1[i] < lista2[j]):
            print(f"lista 1 valor {lista1[i]}  es menor a lista2  {lista2[j]}")
            resultado.append(lista1[i])
            i += 1
        else:
            print(f"lista 2 valor {lista2[j]}  es menor a lista1  {lista1[i]}")


            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta
    print("queda", resultado)
    resultado += lista1[i:]
    print("despues de agregar al resto I ", resultado)

    resultado += lista2[j:]
    print("despues de agregar al resto J", resultado)


    return resultado


print(merge_sort([6,7,-1,0,5,2,3,8,9]))
