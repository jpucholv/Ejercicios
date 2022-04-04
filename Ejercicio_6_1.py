class Vehiculo ():
    def __init__ (self, color = "", ruedas = 0, puertas = 0):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return f"Vehículo {self.color} de {self.ruedas} ruedas y {self.puertas} puertas."

class Coche (Vehiculo):
    def __init__ (self,color = "", ruedas = 0, puertas = 0, velocidad = 0, cilindrada = 0):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__ (self):
        return f"Coche {self.color} de {self.ruedas} ruedas y {self.puertas} puertas, viaja a {self.velocidad} y su cilidrada son {self.cilindrada} cc"
    
Peyotito = Coche ("negro", 4, 5, 0, 1200)

print(Peyotito)