# Introduce una cadena de paises por consola
strPaises = input("Introduce una lista de paises separados por 'coma + espacio': ")

# Separa la cadena por comas y la almacena en un set
lstPaises = {pais for pais in strPaises.split(', ')}

# Muestra la lista ordenada y separada por ', '
print (", ".join(sorted(lstPaises)))