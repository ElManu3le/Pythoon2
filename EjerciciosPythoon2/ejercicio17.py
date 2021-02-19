" Ejercicio 17 - Escribird un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado."
"Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice."
"Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice."

texto = input('Dime una frase cualquiera: ')

jelle = texto[0]
print('El primer caracter de la frase es: ', jelle)

print('Ahora ingresa un numero entre 0 y ', len(texto))

indice = int(input('Introduce aqui la variable '))

textof = texto[indice -1]
print('El caracter que ahora te mostrare es: ', textof)