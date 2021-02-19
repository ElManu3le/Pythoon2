"Ejercicio 11 - Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión."

co = float(input('Dime el capital inicial a invertir: '))
interes = float(input('Ahora dime el interes dado: '))
periodo = int(input('Dime la cantidad de años: '))

for x in range(1,periodo+1):
    def cn(x):
        return(co*(1 + (periodo*interes)))


print('El capital invertido en la inversion durante estos', periodo,'años es de:', cn(x), 'euros')