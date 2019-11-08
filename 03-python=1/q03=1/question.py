##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
os.chdir("/app/Laboratorios/03-python=1/")
datos = pandas.read_csv("./q01=1/data.csv", sep="\t", header=None)
letras = datos.groupby([datos[0]]).sum()
indice = list(letras.index)
letras = letras.values.tolist()
for i in range(5):
    print(str(indice[i])+","+str(letras[i])[1:3])
