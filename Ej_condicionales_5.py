# Escribe un programa que pida al usuario un número del 1 al 7 y muestre el día 
# de la semana correspondiente. Si el número no está en ese rango, debe 
# indicar que el número es inválido.

num = int(input("Introduzca un número entre 1 y 7: "))
d_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

if 1 <= num <= 7:
    print("Hoy es", d_semana[num-1])
else:
    print("Número inválido")