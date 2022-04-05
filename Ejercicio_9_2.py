from functools import reduce

lista = [1,2,3,4,5,6,7,8,9]

def impares (x):
    if x % 2 != 0:
        return True
    return False

def suma (a, b):
    return a + b

lstImpares = list(filter(impares, lista))
print(lstImpares)

resultado = reduce(suma, lstImpares)
print(resultado)