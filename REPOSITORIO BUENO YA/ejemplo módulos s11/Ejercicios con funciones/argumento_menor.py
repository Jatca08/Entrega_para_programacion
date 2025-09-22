#Programa para pasar tres argumentos y retornar el menor de ellos
def menor_de_tres(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
    
# Solicitar al usuario tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
# Llamar a la función y mostrar el resultado
resultado = menor_de_tres(numero1, numero2, numero3)
print(f"El menor de los tres números es: {resultado}")