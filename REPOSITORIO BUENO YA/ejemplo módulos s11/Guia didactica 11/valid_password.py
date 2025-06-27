#Programa que valide una contrase;a que cumpla los criterios
#minimo de caracteres, al menos una mayuscula, un numero y un caracter especial. Usar funciones para cada validacion.


#Import re sirve para trabajar expresiones regulares, en este caso, para validar caracteres especiales en la contrase;a.
import re
#funcion para validar el minimo de caracteres
def min_length(password):
    return len(password) >=8

#Funcion para validar al menos una mayuscula
def mayuscula(password):
    return any(char.isupper() for char in password)

#Funcion para validar al menos un numero
def numero(password):
    return any(char.isdigit() for char in password)

#Funcion para validar al menos un caracter especial
def caracter_especial(password):
    return bool(re.search(r'[!@#$%^&*(),.?":;{}/<>|`~\-\_+=]', password))

#Funcion para validar la contrase;a completa
def validar_password(password):
    if not min_length(password):
        return "La contraseña debe tener al menos 8 caracteres."
    if not mayuscula(password):
        return "La contraseña debe contener al menos una letra mayúscula."
    if not numero(password):
        return "La contraseña debe contener al menos un número."
    if not caracter_especial(password):
        return "La contraseña debe contener al menos un carácter especial."
    return "Contraseña válida."

#Funcion para solicitar la contrase;a al usuario
def solicitar_contrasena():
    while True:
        password = input("Ingrese una contraseña: ")
        resultado = validar_password(password)
        if resultado == "Contraseña válida.":
            print(resultado)
            print("Contraseña: ", password)
            break
        else:
            print(resultado)


# Llamada a la función para solicitar la contraseña
solicitar_contrasena()



