"Ejercicio 21 - Escribid un programa para solicitar al usuario tres números y mostrad en pantalla el menor de los tres."

valor1 = float(input('Dime un numero cualquiera como primer valor: '))
valor2 = float(input('Dime un segundo numero: '))
valor3 = float(input('Dime ahora unm tercer numero para porder hacer el minimo de los tres: '))

print('El minimo de los tres variables que haas introducido es: ', min(valor1,valor2, valor3))