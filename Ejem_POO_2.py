"""
La clase empleado contiene los datos que serán
compartidos por sus clases hijas. La clase empleado
contiene un constructor para inicializar sus atributos
Los datos utilizados son: nombre completo, cedula y
teléfono. Cada atributo de la clase cuenta con sus
respectivos get y set.

SIGUIENTE EJEMPLO ABAJO

"""

class Empleado():

    def __init__(self, nombre_completo, cedula, telefono): # Artículos protegidos
        self._nombre = nombre_completo 
        self._cedula = cedula
        self._telefono = telefono

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre
    
    def set_cedula(self, cedula):
        self._cedula = cedula

    def get_cedula(self):
        return self._cedula
    
    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono
        
# Crear un empleado
empleado1 = Empleado("Juan Pérez", "12345678", "555-1234")

# Obtener los valores con getters
print(empleado1.get_nombre())  # Juan Pérez
print(empleado1.get_cedula())  # 12345678
print(empleado1.get_telefono())  # 555-1234

# Modificar valores con setters
empleado1.set_nombre("Carlos López")
empleado1.set_telefono("555-5678")

# Ver los cambios
print(empleado1.get_nombre())  # Carlos López
print(empleado1.get_telefono())  # 555-5678

"""
Esta clase hereda de la clase empleado. Los nuevos
atributos son:
• Número de plaza
• Salario base
• Duración de contrato en meses
Además, cuenta con un método que calcula el salario
total El empleado recibe un aumento del 2% sobre su
salario base.
"""

class Empleado_asalariado(Empleado):

    def __init__(self, nombre_completo, cedula, telefono, n_plaza, salario, dur_contrato):
        super().__init__(nombre_completo, cedula, telefono)
        self.n_plaza = n_plaza
        self.salario = salario
        self.dur_contrato = dur_contrato

    def salario_total(self):
        self.salario_final = self.salario * 1.02
        return self.salario_final 
        
empleado2 = Empleado_asalariado("Juan López", "12345678", "555-1234", "34", 1800, 7)
print("El salario de", empleado2._nombre, "es de", empleado2.salario_total())