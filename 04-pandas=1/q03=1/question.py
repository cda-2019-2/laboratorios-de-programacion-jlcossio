##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el maximo de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    9
##  B    9
##  C    9
##  D    7
##  E    9
##  Name: _c2, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
import string
os.chdir("/app/Laboratorios/04-pandas=1/")
datos = pandas.read_csv("./q03=1/tbl0.tsv", sep="\t")
letras_max = datos.groupby([datos["_c1"]]).max()
del letras_max["_c0"]
del letras_max["_c3"]
print(letras_max.iloc[:,0])