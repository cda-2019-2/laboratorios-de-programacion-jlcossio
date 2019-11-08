##
##  Programación en Bash
##  ===========================================================================
##
##  Usando los archivos `data1.csv`, `data2.csv`, `data3.csv`, escriba en el
##  archivo `script.sh`  un programa en Bash que imprima en pantalla
##  la siguiente salida por linea:
## 
##  * El nombre del archivo.
##  * El número de la línea procesada.
##  * La letra de la primera columna del archivo.
##  * La cadena de tres letras y el valor asociado de la columna 2 del archivo original. 
##
##  Note que se genera una línea de salida por cada cadena de tres letras.
##   
##  Rta/
##
##  data1.csv,1,E,jjj:3
##  data1.csv,1,E,bbb:0
##  ...
##  data3.csv,3,B,hhh:1
##  data3.csv,3,B,ddd:2
##
##  >>> Escriba su codigo a partir de este punto <<<
##
for filename in *.csv
do
 f=$(basename $filename)
 conteo=1
 while IFS=, read -r c1 c2 c3 c4 c5 c6 c7
 do
  if [[ ! -z $c1 ]]; then
    echo "$f,$conteo,${c1:0:1},${c1#??}" | sed "s/ //g"
  fi
  if [[ ! -z $c2 ]]; then
    echo "$f,$conteo,${c1:0:1},$c2" | sed "s/ //g"
  fi
  if [[ ! -z $c3 ]]; then
    echo "$f,$conteo,${c1:0:1},$c3" | sed "s/ //g"
  fi
  if [[ ! -z $c4 ]]; then
    echo "$f,$conteo,${c1:0:1},$c4" | sed "s/ //g"
  fi
  if [[ ! -z $c5 ]]; then
    echo "$f,$conteo,${c1:0:1},$c5" | sed "s/ //g"
  fi
  if [[ ! -z $c6 ]]; then
    echo "$f,$conteo,${c1:0:1},$c6" | sed "s/ //g"
  fi
  if [[ ! -z $c7 ]]; then
    echo "$f,$conteo,${c1:0:1},$c7" | sed "s/ //g"
  fi
  if [[ $((${#c1}+${#c2}+${#c3}+${#c4}+${#c5}+${#c6}+${#c7})) > 0 ]]; then
    conteo=$((conteo + 1))
  fi
 done < <(grep '' $f)
 conteo=0
done