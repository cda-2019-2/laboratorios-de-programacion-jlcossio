##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, genera una lista de tuplas que asocien las 
##  columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una
##  lista con todas las letras asociadas (columna 1) a dicho valor de la 
##  columna 2.
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##  ('2', ['A', 'E', 'D'])
##  ('3', ['A', 'B', 'D', 'E', 'E'])
##  ('4', ['E', 'B'])
##  ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##  ('6', ['C', 'E', 'A', 'B'])
##  ('7', ['A', 'C', 'E', 'D'])
##  ('8', ['E', 'E', 'A', 'B'])
##  ('9', ['A', 'B', 'E', 'C'])
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
os.chdir("/app/Laboratorios/03-python=1/")
datos = pandas.read_csv("./q01=1/data.csv", sep="\t", header=None)
numeros = pandas.unique(datos[1].values).tolist()
numeros.sort()
def asociadas(num_parametro):
    temp = []
    for i in list(range(0,len(datos[1]))):
        if datos.iloc[i, 1] == num_parametro:
            temp.append(datos.iloc[i, 0])
    return(temp)
letras = [asociadas(j) for j in numeros]
tupla = [(str(numeros[i]), letras[i]) for i in list(range(0,len(numeros)))]
for i in list(range(0,len(tupla))):
    print(tupla[i])
