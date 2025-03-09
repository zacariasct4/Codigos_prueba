# Crea un número aleatorio entre 1 y 100, y el usuario debe adivinarlo. 
# El programa le indica si el número ingresado es mayor o menor que el número secreto

import random

num = random.randint(1,100)

num_dado = int(input("¿Qué número crees que es?"))

if num_dado == num:
    print("Has acertado!! El número era", num)
else:
    while num_dado != num:
        if num_dado > num:
            num_dado = int(input("Noo!! Prueba otra vez con un número menor"))
        else:
            num_dado = int(input("Noo!! Prueba otra vez con un número mayor"))

print("Has acertado!! El número era", num)


"""
numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego de adivinar el número!")
print("He elegido un número entre 1 y 100. ¡A ver si puedes adivinarlo!")

while True:
    # Pedir al usuario que ingrese un número
    guess = input("Introduce tu intento: ")
    
    # Verificar si la entrada es un número
    if guess.isdigit():
        guess = int(guess)
        intentos += 1
    else:
        print("Por favor, introduce un número válido.")
        continue

    # Comparar el número ingresado con el número secreto
    if guess < numero_secreto:
        print("El número secreto es mayor que", guess)
    elif guess > numero_secreto:
        print("El número secreto es menor que", guess)
    else:
        print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
        break
"""