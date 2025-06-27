#3.	Escribir un programa que permita ingresar los salarios de una cantidad indicada de empleados, debe presentar al final el total que se debe pagar a cada empleado y el descuento de renta considerando que es del 10% sobre cada salario. Utiliza una función para el cálculo del descuento.

def calcular_descuento():
    descuento_de_renta=0.10
    while True:
        try:
            empleados = int(input("Ingrese la cantidad de empleados: "))
            break
        except ValueError:
            '='*60
            'Ingrese un input adecuado'
            '='*60
    salarios = []
    for i in range(empleados):
        salario=int(input(f"Ingrese el salario del empleado:{i+1}\n"))
        salarios.append(salario-(salario*descuento_de_renta))
    for j in range (len(salarios)):
        print(f"Salario del empleado {i+1}: {salarios[j]}")

calcular_descuento()