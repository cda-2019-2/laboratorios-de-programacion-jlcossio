##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el promedio de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    4.625000
##  B    5.142857
##  C    5.400000
##  D    3.833333
##  E    4.785714
##  Name: _c2, dtype: float64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
import string
os.chdir("/app/Laboratorios/04-pandas=1/")
datos = pandas.read_csv("./q02=1/tbl0.tsv", sep="\t")
group = datos.groupby([datos["_c1"]]).mean()
del group["_c0"]
print(group.iloc[:,0])