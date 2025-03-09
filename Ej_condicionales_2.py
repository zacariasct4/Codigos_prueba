# Solicita dos números al usuario y determina cuál de los dos es mayor o si son iguales.

num_1 = int(input("Indícame tu primer número: "))
num_2 =int(input("Y ahora el segundo: "))

if num_1 > num_2:
    print(f"{num_1} es mayor que {num_2}")
elif num_1 < num_2:
    print(f"{num_2} es mayor que {num_1}")
else:
    print("Ambos números son iguales")