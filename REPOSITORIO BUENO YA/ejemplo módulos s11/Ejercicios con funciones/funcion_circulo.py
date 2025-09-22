#Programa que devuelva el area de un circulo cuyo radio se le suministra como argumento
import math

def area_circulo(radio):
    area = math.pi * (radio ** 2)
    return print(f"{area:.2f}")

radio=int(input("Ingrese el radio del círculo: "))
resultado = area_circulo(radio)

