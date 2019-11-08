##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
import string
os.chdir("/app/Laboratorios/04-pandas=1/")
datos = pandas.read_csv("./q09=1/tbl1.tsv", sep="\t")
numeros = pandas.unique(datos["_c0"].values).tolist()
numeros.sort()
def asociadas(num_parametro):
    temp = []
    for i in list(range(0,len(datos["_c0"]))):
        if datos.iloc[i, 0] == num_parametro:
            temp.append(datos.iloc[i, 1])
            temp.sort()
    return(temp)
letras = [asociadas(j) for j in numeros]
tabla = [(str(numeros[i]), letras[i]) for i in list(range(0,len(numeros)))]
tabla = pandas.DataFrame(tabla, columns=["_c0", "lista"])
tabla["lista"] = [str(tabla.iloc[i, 1]).replace("[", "") for i in list(range(0,len(tabla["lista"])))]
tabla["lista"] = [str(tabla.iloc[i, 1]).replace("]", "") for i in list(range(0,len(tabla["lista"])))]
tabla["lista"] = [str(tabla.iloc[i, 1]).replace(" ", "") for i in list(range(0,len(tabla["lista"])))]
tabla["lista"] = [str(tabla.iloc[i, 1]).replace("'", "") for i in list(range(0,len(tabla["lista"])))]
print(tabla)