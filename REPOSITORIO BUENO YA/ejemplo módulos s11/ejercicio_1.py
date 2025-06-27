#Presupuesto anual de una fabrica.
import os
os.system("cls")
def presupuesto(a):
    reparto=[0.5, 0.25, 0.15, 0.1]
    repartido=[]
    for i in reparto:
        eh=a*i
        repartido.append(eh)
    return repartido
monto=int(input("Ingrese el monto anual:\n"))
print(presupuesto(monto))
presupuesto(monto)


