#Programa que usando funciones, permita convvertir entre diferentes unidades de longitud.
#El usuario selecciona la conversion deseada.

import os
os.system('cls')

#Realizamos las funciones de conversion.
def km_to_miles(km):
    """Convierte kilómetros a millas."""
    return km * 0.621371
def miles_to_km(miles):
    """Convierte millas a kilómetros."""
    return miles / 0.621371
def meters_to_feet(meters):
    """Convierte metros a pies."""
    return meters * 3.28084
def feet_to_meters(feet):
    """Convierte pies a metros."""
    return feet / 3.28084

#Iniciamos un menu para elegir como queremos convertir.

def menu_conversion():
    print("Seleccione la conversión que desea realizar:")
    print("1. Kilómetros a Millas")
    print("2. Millas a Kilómetros")
    print("3. Metros a Pies")
    print("4. Pies a Metros")
    print("5. Salir")
    
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción deseada: "))
            if 1 <= opcion <= 5:
                return opcion
            if opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
        except ValueError:
            print("Entrada no válida, por favor ingrese un número.")


#Hacemos una funcion que reciba la entrada y active el comando de conversion correspondiente a la opcion elegida por el usuario.

def conversion(a):
    if a ==1:
        km = float(input("Ingrese la distancia en kilómetros: "))
        print(f"{km} kilómetros son {km_to_miles(km):.2f} millas.")
    elif a == 2:
        miles = float(input("Ingrese la distancia en millas: "))
        print(f"{miles} millas son {miles_to_km(miles):.2f} kilómetros.")
    elif a == 3:
        meters = float(input("Ingrese la distancia en metros: "))
        print(f"{meters} metros son {meters_to_feet(meters):.2f} pies.")
    elif a == 4:
        feet = float(input("Ingrese la distancia en pies: "))
        print(f"{feet} pies son {feet_to_meters(feet):.2f} metros.")

#Hacemos un bucle para tener el menu activo hasta que el usuario decida salir.
while True:
    opcion = menu_conversion()
    if opcion == 5:
        break
    conversion(opcion)
    print("="*60)  # Espacio en blanco para mejor legibilidad entre conversiones

