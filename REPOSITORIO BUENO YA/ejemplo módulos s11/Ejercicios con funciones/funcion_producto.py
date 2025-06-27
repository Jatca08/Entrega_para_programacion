#Programa que haga que el usuario digite un numero de entre el 1 al 10 y muestre la tabla de multiplicar de dicho nunmero
print("Programa para mostrar la tabla de multiplicar de un numero")

def fun_prod():
    while True:
        try:
            a=int(input("Ingrese un numero del 1 al 10:\n"))
            if not a in range(1,11):
                print("El numero debe estar entre el 1 y el 10.\n")
            else:
                break
        except ValueError:
            ("Ingrese un numero.")
    
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")

while True:
    fun_prod()

            
