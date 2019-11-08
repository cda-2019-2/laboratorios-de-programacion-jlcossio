##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
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
def uni_sort(pos_parametro):
    temp = pandas.unique(letras[pos_parametro]).tolist()
    temp.sort()
    return(temp)
letras = [uni_sort(i) for i in list(range(0,len(letras)))]
tupla = [(str(numeros[i]), letras[i]) for i in list(range(0,len(numeros)))]
for i in list(range(0,len(tupla))):
    print(tupla[i])
