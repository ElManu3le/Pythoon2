"Ejercicio 10 - Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente. "

n = int(input('Introduce un numero entero com dividendo: '))
m = int(input('Introduce otro numero entero como divisior: '))

print('El cociente de esta operacion esel primer valor y el resto es el segundo.', divmod(n,m))