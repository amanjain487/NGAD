arg1=$1

if [ $# -eq 0 ]
  then
     arg1=5
fi

python3 "create random txt files.py"

end="-"
end+=$arg1
head -n "$end" "Random File.txt" > "temp.txt"

start="+"
# shellcheck disable=SC2006
# shellcheck disable=SC2003
start+=`expr $arg1 + 1`
tail -n "$start" "temp.txt" > "Final File.txt"

rm "temp.txt"
