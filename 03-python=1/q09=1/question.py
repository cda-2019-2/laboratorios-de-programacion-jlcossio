##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
os.chdir("/app/Laboratorios/03-python=1/")
datos = pandas.read_csv("./q01=1/data.csv", sep="\t", header=None)
diccionario = datos[4].str.split(',',expand=True)
intermedio = diccionario[0].append(diccionario[1]).reset_index(drop=True)
intermedio = intermedio.to_frame()
for i in range(4):
    intermedio = intermedio[0].append(diccionario[i+2]).reset_index(drop=True)
    intermedio = intermedio.to_frame()
diccionario = intermedio
len(intermedio)
diccionario = diccionario.dropna()
diccionario = diccionario[0].str.split(':',expand=True)
clave = diccionario[0].value_counts().sort_index()
for index, value in clave.items():
    print(str(index)+","+str(value))


