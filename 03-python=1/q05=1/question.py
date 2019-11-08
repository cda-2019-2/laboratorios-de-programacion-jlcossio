##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
os.chdir("/app/Laboratorios/03-python=1/")
datos = pandas.read_csv("./q01=1/data.csv", sep="\t", header=None)
letras_max = datos.groupby([datos[0]]).max()
indice = list(letras_max.index)
letras_max = letras_max.values.tolist()
letras_min = datos.groupby([datos[0]]).min()
letras_min = letras_min.values.tolist()
for i in range(5):
    print(str(indice[i])+","+str(letras_max[i])[1:2]+","+str(letras_min[i])[1:2])
