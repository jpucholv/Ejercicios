import pickle

class Vehiculo ():
    def __init__ (self, marca = "", modelo = "", color = ""):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__ (self):
        return f"Vehícuolo marca {self.marca}, modelo {self.modelo} y color {self.color}"

# Creo un objeto del tipo Vehículo y guardo su estado en .bin
coche = Vehiculo('Audi', 'a4', 'gris')
print(coche)

f = open("Ejercicio_8_2.bin", "wb")
pickle.dump(coche, f)
f.close()

# Cargo el estado de coche en un nuevo objeto
f = open("Ejercicio_8_2.bin", "rb")
nuevoCoche = pickle.load(f)
f.close()

print(nuevoCoche)