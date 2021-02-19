"Ejercicio 4  Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."

nombre_user4 = input('Introduce tu nombre: ')
repetit = input('Introduce el numero de veces que quieres repetir tu nombre: ')

for x in range (int(repetit)):
    print(nombre_user4)
