#Crear programa que permita crear una lista ede compras y guardarla en un archivo de texto.
import os
os.system("cls")

e="Guia didactica 12"
# Definimos la ruta del archivo donde se guardará la lista de compras
ruta = os.path.join(e, "compras.txt")
#Creamos la lista de compras en formato escritura "w"
with open(ruta, "w") as archivo:
    #la archivo se guarda en la ruta especificada
    
   

    while True:
        obj=input("Ingrese el nombre del producto:")
        if obj.lower()=="fin":
                print("Gracioas por usar el programa :)")
                break
        if obj.strip() != "":
            archivo.write(obj + "\n")
            print(f"Producto '{obj}' añadido a la lista de compras.")
            print("(Escriba 'fin' para terminar):")
            continue
      

