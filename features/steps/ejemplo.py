# ejemplo.py

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "Ladra"

class Gato(Animal):
    def hablar(self):
        return "Maulla"

# Encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # atributo privado

    def mostrar_edad(self):
        return self.__edad

    def cumplir_anios(self):
        self.__edad += 1

# Probar herencia y polimorfismo
animales = [Perro("Fido"), Gato("Michi")]

for animal in animales:
    print(f"{animal.nombre} dice: {animal.hablar()}")

# Probar encapsulamiento
persona = Persona("Ana", 30)
print(f"{persona.nombre} tiene {persona.mostrar_edad()} años.")
persona.cumplir_anios()
print(f"{persona.nombre} ahora tiene {persona.mostrar_edad()} años.")