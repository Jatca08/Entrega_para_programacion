#Programa que proporciona un archivo producto.csv
#Cada linea contiene el nombre de un producto, su precio y la cantidad en stock, separado por comas.
#El programa lee este archivo y muestra la información en un formato legible.

def leer_csv():
    with open("excel.csv", "r",encoding='utf-8-sig') as excel:
        for linea in excel:
            
            a=linea.strip().split(";")
            b=[dato.replace('[','').replace(']','') for dato in a]
            print("|".join(b))

leer_csv()