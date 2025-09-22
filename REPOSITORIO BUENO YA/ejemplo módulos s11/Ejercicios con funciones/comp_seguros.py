#2.	Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a la semana. Su política de pagos es que un vendedor recibe un sueldo base, y un 10% extra por comisiones de sus ventas. El gerente de su compañía desea saber cuánto dinero obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas realizadas, y cuanto tomando en cuenta su sueldo base y sus comisiones. Utilice una función para calcular la comisión por las tres ventas realizadas.

def calcular_comision():
    print("Programa para calcular comisiones de vendedores\n","="*60)
    vendedores=int(input("Ingrese la canditdad de vendedores:\n"))
    sueldo_base=float(input("Ingrese el sueldo base de los vendedores:\n"))
    comision=0.10 #10% de comision por venta
    for i in range(vendedores):
        ventas = []
        for j in range(3):
            while True:
                try:
                    venta = float(input(f"Ingrese el monto de la venta {j+1} del vendedor {i+1}:\n"))
                    if venta >= 0:
                        ventas.append(venta)
                        break
                    else:
                        print("El monto de la venta no puede ser negativo. Intente nuevamente.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        comision_total = sum(ventas) * comision
        total_semana = sueldo_base + comision_total
        print(f"El vendedor {i+1} obtuvo una comisión total de: ${comision_total:.2f} y un total semanal de: ${total_semana:.2f}.")

# Llamada a la función para calcular las comisiones
calcular_comision()
