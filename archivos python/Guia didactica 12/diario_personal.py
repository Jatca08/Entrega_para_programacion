#Escribir un archivo como diario que permita guardar texto 
# de manera continua, hasta que el usuario decida no guardar mas texto.

import datetime
import os
os.system("cls")

entrada= input("Ingrese el nombre del archivo de texto donde se guardara el diario:\n")

ruta = os.path.join("Guia didactica 12", entrada)
# Función para añadir una entrada al diario

def add_entry(file_path, entry):
    with open(file_path, "a") as file:
        file.write(entry + "\n")
# Bucle para permitir al usuario añadir entradas al diario
while True:
    fecha = datetime.date.today()
    texto = input("Escriba su entrada para el diario:\n")
    entry = f"{fecha}  {texto}"
    add_entry(ruta, entry)
    
    otra_entrada = input("¿Desea añadir otra entrada? (S/N): ").strip().upper()
    if otra_entrada != "S":
        print("Gracias por usar el diario.")
        break
