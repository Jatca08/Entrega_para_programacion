#Programa que contenga una funcion que retorne el factorial de un numero

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        #calculamos el factorial por medio de un bucle
        #Iniciamos el resultado en 1 porque vamos a multiplicar

        resultado = 1
        #Iteramos desde 2 hasta n, multiplicando cada número al resultado con paso 1

        for i in range(2, n + 1):
            #Por cada i en el rango, multiplicamos el resultado por i
            resultado *= i
    #Retornamos el resultado final del factorial
        return print(resultado)
    
numero_a_calcuar = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero_a_calcuar)