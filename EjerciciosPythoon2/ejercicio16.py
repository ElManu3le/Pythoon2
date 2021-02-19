"Ejercicio 16 - Escribid un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacenad el resultado de la suma de esos dos números y luego mostrad ese resultado en pantalla."
"A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrar en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior."

numero1 = int(input('Escribeme un numero: '))
numero2 = int(input('Escribeme otro numero: '))
suma = numero1 + numero2

print('La suma de los dos numeros introducidos es: ',suma)
numero3 = int(input('Ahora introduce un tercer numero para multiplicar: '))
multipicacion = suma * numero3

print('La multiplcacion tiene como valor final: ', multipicacion)