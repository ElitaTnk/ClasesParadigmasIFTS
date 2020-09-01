# 5! = 5 * 4! = 120
# 4! = 4 * 3! =  24
# 3! = 3 * 2! =  6
# 2! = 2 * 1! = 2
# 1! = 1 * 0! = 1
# 0! = 1 = 1

# % * 4 * 3 * 2 * 1

def factorial(numero):
    if numero == 0:
        return 1
    else:
        print(f"soy el {numero}")
        # recur = factorial(numero -1)
        # da = recur * numero
        # return da

        return factorial(numero -1) * numero


#print(factorial(5))


def sacarFibonacci(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return sacarFibonacci(numero -1) + sacarFibonacci(numero - 2)

print(sacarFibonacci(10))
