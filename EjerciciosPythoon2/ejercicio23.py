" Ejercicio 23  - Escribid un programa que, dada una frase por el usuario, muestre la cantidad total de vocales (tanto mayúsculas como minúsculas) que contiene."

vocales = ["A","E","I","O","U","a","e","i","o","u"]
frase = input('Dime una frase: ')

contador = 0
for i in frase:
    
    if i in vocales:
        contador = contador + 1

print('En la frase se pueden contar con: ',contador, 'vocales')
        

