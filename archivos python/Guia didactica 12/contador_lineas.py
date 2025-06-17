#Programa que pide al usuario nonmbre de un archivo
# y cuenta las lineas del archivo 

import os
os.system("cls")

ruta = input("Ingrese el nombre del archivo:\n")
#Incluimos la ruta en la carpeta local del programa, en este caso "Guia didactica 12"
ruta = os.path.join("Guia didactica 12", ruta)
# Función para contar las líneas del archivo
def contar_lineas(archivo):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
            return len(lineas)
    except FileNotFoundError:
        print("El archivo no existe o la ruta es incorrecta.")
        return 0

# Bucle para permitir al usuario contar líneas en el archivo
while True:
    lineas = contar_lineas(ruta)
    if lineas > 0:
        print(f"El archivo '{ruta}' tiene {lineas} líneas.")
    else:
        print("No se pudo contar las líneas del archivo.")
    
    otra = input("¿Desea contar las líneas de otro archivo? (S/N): ").strip().upper()
    if otra != "S":
        print("Gracias por usar el contador de líneas.")
        break
    ruta = input("Ingrese el nombre del nuevo archivo:\n")
# Asegurarse de que el archivo existe antes de contar las líneas
    if not os.path.exists(ruta):
        print("El archivo no existe. Por favor, ingrese un archivo válido.")
        continue
    else:
        print(f"Contando líneas en el archivo '{ruta}'...")
        continue
# Fin del programa