##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
import string
os.chdir("/app/Laboratorios/04-pandas=1/")
datos = pandas.read_csv("./q10=1/tbl2.tsv", sep="\t")
numeros = pandas.unique(datos["_c0"].values).tolist()
numeros.sort()
def asociadas(num_parametro):
    temp = []
    for i in list(range(0,len(datos["_c0"]))):
        if datos.iloc[i, 0] == num_parametro:
            temp.append(datos.iloc[i, 1]+":"+str(datos.iloc[i, 2]))
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