#Programa principal
import ejemplo1 as ej1#Importamos el módulo ejemplo1
a=int(input("Ingrese el primer número:\n"))
b=int(input("Ingrese el segundo número:\n"))
print(f"La multiplicacion es: {ej1.producto(a,b)} y la resta: {ej1.resta(a,b)}")
suma=ej1.suma(a, b)
division= ej1.division(a, b)
print(f"La suma es: {suma} y la división: {division:.2f}")
print(ej1.texto) 
#fin