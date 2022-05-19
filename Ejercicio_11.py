import sqlite3

conn = sqlite3.connect('Ejercicio_11.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM alumnos WHERE nombre = "Roberto"')

for row in rows:
    print(row)

cursor.close()
conn.close()