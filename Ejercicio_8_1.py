# Abre/crea el archivo y lo sobreescribe
f = open('mifichero.txt', 'w')

f.write('Escrito 1\n')


f.close()

# Abre por segunda vez el archivo esta vez con permiso "append"
f = open('mifichero.txt', 'a')

f.write('Escrito 2\n')

f.close()