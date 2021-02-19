"Ejercicio 9 - Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros) calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales."

"peso(kg)/talla(m2)"

peso = int(input('Dime tu masa en KG: \t'))
estatura = float(input('Ahora dime tu estatura en metros (1.80m ): \t '))

imc = peso/(estatura**2)

print('Tu IMC(Indice de Masa Corporal) es de ', round(imc,2))