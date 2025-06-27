#Programa que dado un monto para presupuesto anual de una fabrica
#Calcular porcentaje de dinero que le corresponde a cada departamento
import os
os.system('cls')

#Funcion para calcular el porcentaje de dinero que le corresponde a cada departamento
def calcular_presupuesto_anual():
    presupuesto = float(input("Ingrese el monto del presupuesto anual: "))
    departametos=[0.50, 0.25, 0.15, 0.10] #Porcentajes de presupuesto para cada departamento
    nombres_departamentos = ["Producción", "Ventas", "Marketing", "Administración"]
    for i in range(len(departametos)):
        porcentaje = departametos[i] * 100
        cantidad = presupuesto * departametos[i]
        print(f"El departamento de {nombres_departamentos[i]} recibe el {porcentaje:.1f}% del presupuesto anual, que equivale a ${cantidad:.2f}.")

calcular_presupuesto_anual()
