class Alumno ():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def isPassed (self):
        if self.nota >= 5:
            return "aprobado"
        return "suspendido"

    
    def __str__ (self):
        return f"El alumno {self.nombre} ha sacado un {self.nota}. {self.nombre} ha {self.isPassed()}"

Juan = Alumno ("Juan", 4)
print(Juan)