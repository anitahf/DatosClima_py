print("Me llamo Anita ")


import numpy as np

x = np.zeros(5)
print(x)



#Varible de Texto 
mi_variable = "Hola mundo"
print(mi_variable)

#Lista de numeros 
mi_lista = [1,2,3,4,5]
print(mi_lista)

#Diccionario
mi_diccionario = {"clave_1" : "Valor1", "clave_2" : "Valor2"}
print(mi_diccionario)
####################
#Numerica
vector_enteros = [10]*5
print(vector_enteros)

vector_flotante =[3.14]*5
print(vector_flotante)

diccionario = {"entero" :vector_enteros, "flotante" :vector_flotante, "complejo": vector_flotante}
print(diccionario)

#Cadenas
cadena_simple = "Hola mundo"
cadena_doble = ["Python es poderoso", "Me gusta"] # Tiene dos variables de texto
print(cadena_doble)

#dataframe
import pandas as pd
#Crear un Datframe con rendimientos de juegos 

datos = {
    "nombre": ["Juan", "Maria", "Carlos", "Ana"],
    "Juego 1 (puntos)": [150, 180, 130, 200],
    "Juego 2 (puntos)": [120, 80, 110, 150],
    "Juego 3 (puntos)": [200, 160, 180, 190],
}
df = pd.DataFrame(datos)
print(df)

### Practica 1 
#librerias
import pandas as pd
#importar datos 
Tmed = pd.read_excel("data/2022Tmed.xlsx")
print(Tmed)