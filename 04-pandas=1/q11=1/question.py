##
##  Programación con Pandas
##  ===========================================================================
##
##  Si la columna _c0 es la clave en los archivos `tbl0.tsv`
##  y `tbl2.tsv`, compute la suma de tbl2._c5b por cada
##  valor en tbl0._c1.
## 
##  Rta/
##  _c1
##  A    146
##  B    134
##  C     81
##  D    112
##  E    275
##  Name: _c5b, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
import string
os.chdir("/app/Laboratorios/04-pandas=1/")
datos_0 = pandas.read_csv("./q11=1/tbl0.tsv", sep="\t")
datos_2 = pandas.read_csv("./q11=1/tbl2.tsv", sep="\t")
datos_2 = datos_2.groupby([datos_2["_c0"]]).sum()
datos = datos_0
datos["_c5b"] = datos_2["_c5b"]
tabla = datos.groupby([datos["_c1"]]).sum()
del tabla["_c0"]
del tabla["_c2"]
print(tabla.iloc[:,0])

