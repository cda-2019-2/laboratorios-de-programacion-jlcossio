##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c1 y una lista
##  separada por ':' de los valores de la columna _c2
##  para el archivo `tbl0.tsv`.
##
##  Rta/
##    _c0                        lista
##  0   A              1:1:2:3:6:7:8:9
##  1   B                1:3:4:5:6:8:9
##  2   C                    0:5:6:7:9
##  3   D                  1:2:3:5:5:7
##  4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
import string
os.chdir("/app/Laboratorios/04-pandas=1/")
datos = pandas.read_csv("./q08=1/tbl0.tsv", sep="\t")
letras = pandas.unique(datos["_c1"].values).tolist()
letras.sort()
def asociadas(num_parametro):
    temp = []
    for i in list(range(0,len(datos["_c1"]))):
        if datos.iloc[i, 1] == num_parametro:
            temp.append(datos.iloc[i, 2])
            temp.sort()
    return(temp)
numeros = [asociadas(j) for j in letras]
tabla = [(str(letras[i]), str(numeros[i]).replace(",",":")) for i in list(range(0,len(letras)))]
tabla = pandas.DataFrame(tabla, columns=["_c0", "lista"])
tabla["lista"] = [str(tabla.iloc[i, 1]).replace("[", "") for i in list(range(0,len(tabla["lista"])))]
tabla["lista"] = [str(tabla.iloc[i, 1]).replace("]", "") for i in list(range(0,len(tabla["lista"])))]
tabla["lista"] = [str(tabla.iloc[i, 1]).replace(" ", "") for i in list(range(0,len(tabla["lista"])))]
print(tabla)