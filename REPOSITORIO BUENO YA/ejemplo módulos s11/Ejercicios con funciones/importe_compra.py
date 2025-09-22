#Programa que recibe el importe de una compra y devuelva la cantidad final a pagar

#Tener en cuenta que
#Si el importe es mayor a 300, se aplica 5%
#Si el importe es mayor a 500, se aplica 10%


#Se hace la funcion de con el parametro 'a' como el importe que sera digitado por el usuario
def importe_a_pagar(a):
    #Se hace una lista de las condiciones entre los rangos de los descuentos.
    if a<=300:
        return print(f'No se aplicaron descuentos.\nmonto total={a:.2f}')
    elif a >= 600:
        return print(a-(a*0.12))
    elif a >= 500:
        return print(a-(a*0.1))
    elif a > 300:
        return print(a-(a*0.05))
    
#Se hace ciclo while para digitar correctamente el importe y que aplique descuento
    
while True:
    try:
        importe=int(input("ingresar el monto de la compra:\n"))
        if importe<=0:
            print('monto no valido')
        #Se llama a la funcion la cual retorna el total a pagar con el descuento aplicado de acuerdo a la condicion y muestra su retorno.
        else:
            print(f"El total a pagar es:", importe_a_pagar(importe))
        

    except ValueError:
        ("Dato no valido")


