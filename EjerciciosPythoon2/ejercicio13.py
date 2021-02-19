"Ejercicio 13 - Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. "
" Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. "
" Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. "
" Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. "

print('Introduce la cantidad inicial')
cantidad = float(input())

a = cantidad*0.96
b = a*0.96
c = b*0.96

print('El primer año te quedarias con: \t',a, ' de lo que depositaste')
print('En el segundo año te quedarias con: \t',b, ' de lo que depositaste')
print('Y al tercer año te quedarias con: \t',round(c,2), ' de lo que depositaste')





