archi1=open("datos.txt","r", encoding="utf-8")
lineas=archi1.readlines()
print("El archivo tiene ", len(lineas), "lineas.")
print("El contenido ddel archivo")
for linea in lineas:
    print(linea, end="")
archi1.close()

