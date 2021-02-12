"Ejercicio 8 - Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = n(n+1)/2 "
" suma = n(n+1)/2 "

n = int(input('Hola, introduce un numero positivo entero para hacer esta funcion: \t'))    

for x in range(1,n+1):
    def suma(x):
        return(x*(x+1)/2)

    print('Aqui el resultado con el valor de n =', x, '=>',suma(x))
    
    
    
    
    




