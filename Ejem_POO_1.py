"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos
Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )
Coche (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de
Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )
Bicicleta (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de
Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        print(f"Vehículo {self.color} con {self.ruedas} ruedas")
        # return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        super().__str__()
        print(f"Y va a {self.velocidad} km/h")
        # return super().__str__() + ', Velocidad (km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        super().__str__()
        print(f"Del tipo {self.tipo}")

coche1 = Coche("rojo", 4, 100)
coche1.__str__()

bici = Bicicleta("amarilla", 2, "montaña")
bici.__str__()
# print(coche1) # Para el caso cambiado de comentarios