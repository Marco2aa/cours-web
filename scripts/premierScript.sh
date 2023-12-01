# echo "Bonjour les dev" 
# read x
# echo "x=$x"

# if [ $x -ge 14 ]; then
#     echo "mention"
# elif [ $x -gt 9 ]; then
#     echo "admis"
# else
#     echo "redouble"
# fi

# for i in {1..10};do
#     echo "bonjour$i"
# done


for i in {1..5};do
    echo "Donnez svp la note" 
    read x
    if [ $x -ge 14 ]; then
        echo "mention"
       
    elif [ $x -gt 9 ]; then
        echo "admis"
       
    else
        echo "redouble"
   
    fi
done

