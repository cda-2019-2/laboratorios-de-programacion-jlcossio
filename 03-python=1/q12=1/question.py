##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
os.chdir("/app/Laboratorios/03-python=1/")
datos = pandas.read_csv("./q01=1/data.csv", sep="\t", header=None)
datos['diccionario'] = datos[4].str.split(',')
dumi = datos['diccionario'].apply(lambda x: sum([int(re.sub(r'.+:', '', i)) for i in x]))
for i in list(range(0,len(datos[0]))):
    print(str(datos.iloc[i,0])+","+str(dumi[i]))

