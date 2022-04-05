from functools import reduce

lista = []
x = int(input("Introudce el número menor del rango: "))
y = int(input("Introduce el número mayor del rango: "))

for n in range (x,y+1):
    lista.append(n)

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