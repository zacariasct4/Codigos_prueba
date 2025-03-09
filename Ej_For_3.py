# Escribe un programa que solicite al usuario una cadena de texto y luego imprima cada 
# carácter de la cadena junto con su frecuencia (cuántas veces aparece en la cadena). 
# Utiliza un diccionario para almacenar las frecuencias.

frase = input("Dame una frase cualquiera:")

caracteres = sorted(frase)
dict_carac = {}

for i in range(len(caracteres)):
    if caracteres[i] != caracteres[i-1]:
        dict_carac[caracteres[i]] = frase.count(caracteres[i])
    else:
        continue

print(dict_carac)