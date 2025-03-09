# Escribe un programa que pida al usuario que ingrese números. 
# Si el número ingresado es negativo, el programa debe ignorarlo y pedir otro número. 
# Si el número es positivo, el programa debe sumarlo. 
# El programa debe detenerse cuando el usuario ingrese 0 y mostrar la suma de todos 
# los números positivos ingresados.

num = int(input("Ingresa el número que quieras (positivo):"))
sum = 0

while True:
    if num < 0:
        num = int(input("El número es negativo. Ingresa otro:"))
        continue
    elif num > 0:
        sum += num
        num = int(input("Ingresa el número que quieras (positivo):"))
        continue
    else:
        break
print(sum)