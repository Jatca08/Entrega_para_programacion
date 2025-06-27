# Lectura de archivo poema.txt línea por línea   
import os
os.system('cls')

#Redirigimos la localizacion del archivo, en este caso en la carpeta que estamos trabajando.
directorio_actual=os.path.dirname(os.path.abspath(__file__))
ruta_poema=os.path.join(directorio_actual, "poema.txt")
try:
        with open(ruta_poema, "r", encoding="utf-8") as archivo:
         for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print(" el archivo 'poema.txt' no se encontro.")
except Exception as e:  
    print(f"ocurrio un error: {e}") 
exit