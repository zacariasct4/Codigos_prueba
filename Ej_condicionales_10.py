# Una tienda ofrece descuentos basados en el total de compra. 
# Si la compra es mayor a $100, el descuento es del 10%. Si es mayor a $500, 
# el descuento es del 20%. Crea un programa que calcule el total a pagar 
# después del descuento.

Cuenta = float(input("Cuenta sin descuento:"))

if  100 < Cuenta <= 500:
    Cuenta_final = round(Cuenta * 0.9, 2)
elif Cuenta > 500:
    Cuenta_final = round(Cuenta * 0.8, 2)
else:
    Cuenta_final = Cuenta

print("LA cuenta final es: $", Cuenta_final)
