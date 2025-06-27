#Programa que permite ingresar las calificaciones de varios estudiantes
#Mediante funciones, calcule el promedio general, la calificacion mas alta y la calificacion mas baja
import os
os.system('cls')
"====Funciones askjfksaloifshlkdfhj====="

"""Definimos una funcion que retorne el promedio"""
def calc_prom(lista_notas):
    promedio=sum(lista_notas)/len(lista_notas)
    return promedio
"""Definimos una funcion que retorne la calificacion mas alta"""
def nota_mayor(a):
    mayor=a[0][0]
    for z in a:
        for nota in z:
            if nota > mayor:
                mayor = nota
    return mayor
"""Definimos una funcion que retorne la calificacion mas baja"""
def nota_menor(a):
    menor=a[0][0]
    for z in a:
        for nota in z:
            if nota < menor:
                menor = nota
    return menor


#Creamos una lista para almacenar las calificaciones
lista_notas=[]
#Ingrewsamos cuantos estudiantes vamos a evaluar
estudiantes=int(input("Ingrese la cantidad de estudiantes: "))
#Iteramos para ingresar las calificaciones de cada estudiante
materias = 3
#Establecemos ya el numero de materias para el rango, se puede hacer mas dinamico si se desea cambiandolo por un input

for i in range(estudiantes):
    notas=[]
    for j in range(materias):
        while True:
            try:
                nota=int(input(f"Ingrese la nota del estudiante {i+1} en la materia {j+1}:\n"))
                
                if 0 <= nota <=100:
                    notas.append(nota)
                    break
                else:
                    print("Por favor, ingrese una nota entre 0 y 100.")
                    
                
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
    lista_notas.append(notas)

print(lista_notas)

#Hacemos una lista para guardar los promedios de cada estudiante
prom_comp=[]
#calculamos el promedio de cada estudiante
for i in range(estudiantes):
    promedio_estudiante = calc_prom(lista_notas[i])
    print(f"El promedio del estudiante {i+1} es: {promedio_estudiante:.2f}")
    prom_comp.append(promedio_estudiante)

#calculamos el promedio general
promedio_general = calc_prom(prom_comp)
print(f"El promedio general de todos los estudiantes es: {promedio_general:.2f}")

#calculamoos la calificacion mas alta
mayor = nota_mayor(lista_notas)
print(f"La calificación más alta es: {mayor}")
#calculamos la calificacion mas baja
menor = nota_menor(lista_notas)
print(f"La calificación más baja es: {menor}")

#Imprimimos el promedio de cada estudiante
for i in range(estudiantes):
    print(f"El promedio del estudiante {i+1} es: {prom_comp[i]:.2f}")

print('====Fin del programa====')   
#Fin del programa