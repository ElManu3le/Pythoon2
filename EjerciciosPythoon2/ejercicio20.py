"Ejercicio 20 - Escribíd un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”."
"Verificad si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato."

vocales = ["A","E","I","O","U","a","e","i","o","u"]
letra = input('Introduceme una vocal: ')

if letra in vocales:
    print('Esta en la lista')

elif len(letra)>=1 or letra in vocales:
        print('No es una letra o no se encuentra en la lista de vocalesr')

else:
    print('No esta en la lista de vocales!!')





