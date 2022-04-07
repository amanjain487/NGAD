arg1=$1
arg2=$2

if [ $# -eq 0 ]
  then
     arg1=25
     arg2=200
fi

python3 "create random txt files.py" $arg1

size="+"
size+=$arg2
size+="k"

cd "TXT Files" || exit

find . -name "*.txt" -type 'f' -size $size -delete


