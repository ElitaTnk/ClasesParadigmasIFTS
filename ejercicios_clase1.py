#Ejercicio 1
#
# Crear un programa que imprima por pantalla el mensaje “Hello World!”.
#
# Nota: se puede imprimir el dato puro o el dato almacenado en una variable, siempre es una buena práctica usar variables.

# Ejercicio 2
#
# Crear un programa que imprima por pantalla todos los números pares del 0 al 100.

# Ejercicio 3
#
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.

def exercise3():
    for number in range(0, 101):
        if number % 3 == 0:
            print(number)

exercise3()

# Ejercicio 4
# Crear un programa que pida al usuario que ingrese dos números y luego el programa imprima por pantalla: en un renglón la suma de ellos, en otro la resta y en otro el producto.

# Ejercicio 5
#
# Crear un programa que pida al usuario 10 números enteros, los almacene en una lista, ordene los números dentro de la lista y luego imprima por pantalla la lista completa y ordenada.

def excercise5():
    userValueList = []
    for number in range(10):
        userValue = int(input("Ingrese un numero entero"))
        userValueList.append(userValue)

    print(userValueList)
    userValueList.sort()
    print(userValueList)
#excercise5()

# Ejercicio 6
#
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo, retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.

def excercise6(number1, number2):
    if number1 > number2:
        return 1
    elif number1 == number2:
        return 0
    else:
        return -1

# userInput1 = int(input("Ingrese un numero entero "))
# userInput2 = int(input("Ingrese un numero entero "))

# resultado = excercise6(userInput1, userInput2)
# print(resultado)

# Ejercicio 7
#
# Crear un programa que le pida al usuario ingresar dos números enteros y devuelva el punto medio entre ellos.
#
# Ejercicio 8
#
# Crear un programa que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
#

# Ejercicio 9
#
# Crear un programa que solicite al usuario que ingrese su dirección mail. Imprimir un mensaje indicando si la dirección es válida o no. Una dirección se considerará válida si contiene el símbolo "@".

# Ejercicio 10
#
# Crear un programa que dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

# Ejercicio 11
#
# Crear un programa que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

def excercise11(userInput):
    wordList = userInput.split()
    # ultimaPalabra = wordList[-1]
    # longitud = len(ultimaPalabra)
    # return longitud

    return len(wordList[-1])

result = excercise11("Bienvenidos a paradigmas de programación")
print(result)
# Ejercicio 12
#
# En McDonald’s se pueden comprar patitas de pollo en 6, 9 o 20 unidades. Crear un programa que, a partir de un número, decida si es posible comprar esa cantidad de patitas.
#
#


class Persona():
    nombre = "nombre"

    def Comer():
        print("estoy comiendo")

class Perro():
    raza = ""

    def Ladrar():
        print("ladro ladro")


persona1 = Persona("Eliana")

persona1.Comer()


perro1 = Perro()
