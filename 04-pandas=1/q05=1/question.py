##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima la suma de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    37
##  B    36
##  C    27
##  D    23
##  E    67
##  Name: _c2, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas
import os
import re
import string
os.chdir("/app/Laboratorios/04-pandas=1/")
datos = pandas.read_csv("./q05=1/tbl0.tsv", sep="\t")
letras_sum = datos.groupby([datos["_c1"]]).sum()
del letras_sum["_c0"]
print(letras_sum.iloc[:,0])