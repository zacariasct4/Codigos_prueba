# Un almacén da un descuento del 15% si la compra del cliente supera los 1000 Euros. 
# Escribe un programa que pida el total de la compra y calcule el descuento 
# (si aplica) y el total a pagar.


Cuenta = float(input("¿Cuál es el total a pagar? "))

if Cuenta > 1000:
    Cuenta_final = round(Cuenta * 0.85, 2)
else:
    Cuenta_final = Cuenta

print("Finalmente la cuenta es:   €", Cuenta_final)

