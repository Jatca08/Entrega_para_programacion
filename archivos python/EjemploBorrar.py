#Eliminar lineas del archivo
#Abrir el archivo y leer las lineas
with open("datos.txt","r", encoding="utf-8") as archivo:
    lineas=archivo.readlines()

lineas_filtradas=[linea for linea in lineas if linea.strip() != "Segunda linea"]

with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas_filtradas)

