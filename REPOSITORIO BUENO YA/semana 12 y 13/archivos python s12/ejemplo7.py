nombre=input("Ingrese el nombre.\n")
apellido=input("Ingrese el apellido\n")
salario=input("Ingrese el salario\n")
linea = (f"{nombre}, {apellido}, {salario}")
with open("datos_usuarios.txt","a") as archivo2:
    archivo2.write(linea)
print("Datos guardados en ruta",archivo2,".")

