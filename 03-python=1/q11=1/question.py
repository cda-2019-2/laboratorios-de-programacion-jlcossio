##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
os.chdir("/app/Laboratorios/03-python=1/")
datos = pandas.read_csv("./q01=1/data.csv", sep="\t", header=None)
letras = pandas.DataFrame(datos[3].str.split(',').tolist(),index=datos[1]).stack()
letras = letras.reset_index([0, 1])
resumen = letras.groupby([letras[0]]).sum()
indice = list(resumen.index)
for i in list(range(0,len(indice))):
    print(str(indice[i])+","+str(resumen.iloc[i,0]))