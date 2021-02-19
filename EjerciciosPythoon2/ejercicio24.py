"Ejercicio 24  - Escribid un programa que, dado un número entero positivo, calcule y muestre su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1."

numerofac = int(input('Dime un numero con el que poder hacer el factorial: '))

for i in range(1, numerofac+1):
    print('En valor',i , 'es:',numerofac*i)