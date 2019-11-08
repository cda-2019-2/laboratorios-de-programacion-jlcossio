##
##  Programación en Python
##  ===========================================================================
##
##  La columna 5 del archvio `data.csv` codifica un diccionario donde cada
##  cadena de tres letras corresponde a una clave y el valor despues del
##  caracter `:` corresponde al valor asociado a la clave. Por cada clave,
##  obtenga el valor asociado mas pequeño y el valor asociado mas grande 
##  computados sobre todo el archivo. 
##
##  Rta/
##  aaa,0,6
##  bbb,4,7
##  ccc,0,1
##  ddd,5,5
##  eee,0,0
##  fff,4,9
##  ggg,3,3
##  hhh,6,8
##  iii,2,7
##  jjj,2,5
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
letras_max = diccionario.groupby([diccionario[0]]).max()
indice = list(letras_max.index)
letras_max = letras_max.values.tolist()
letras_min = diccionario.groupby([diccionario[0]]).min()
letras_min = letras_min.values.tolist()
for i in range(10):
    print(str(indice[i])+","+str(letras_min[i])[2:3]+","+str(letras_max[i])[2:3])


