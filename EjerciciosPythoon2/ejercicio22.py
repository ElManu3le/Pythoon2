"Ejercicio 22 - Escribid un programa que solicite ingresar un nombre de usuario y una contraseña. "
"Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrad en pantalla “Usuario y contraseña correctos." 
"Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”. "

nombreuser = input('Dime el nombre de usuario: ')
contrasenia = input('Ahpra dime la contraseña del equipo: ')

if nombreuser != "Gwenevere" and contrasenia != "excalibur":
    print('Acceso denegado')

else:
    print('Usuario y contraseña correctos. Puede ingresar en Camelot Saber')