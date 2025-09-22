#Programa que ingrese cantidad de horas trabajadas y que con una funcion determine y retorne el valor a pagar
#Considerando que las primeras 160 horas trabajadas seran a $6.5 y le resto de horas a $7.5

def horas_trabajadasO(horas):
    if horas <= 160:
        chamba_paga = horas * 6.5
    else:
        chamba_paga = 160 * 6.5 + (horas - 160) * 7.5
    return chamba_paga

#Ingresamos el parametro por medio del input y luego llamamos a la funcion
horas = float(input("Ingrese la cantidad de horas trabajadas: "))
pago = horas_trabajadasO(horas)
print(f"El valor a pagar es: ${pago:.2f}")
