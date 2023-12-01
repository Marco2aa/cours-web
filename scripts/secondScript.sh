

echo "Bonjour les devs"
i=1
while [ $i -lt 6 ]; do
    echo "Donnez svp la note " 
    read x
    echo " donnez le prenom"
    read y
    echo "donnez le nom"
    read z
    if [ $x -gt 20 ]; then

        echo $y $z "recommencez"

    elif [ $x -lt 0 ]; then

        echo $y $z "recommencez"

    elif [ $x -ge 14 ]; then

        echo $y $z "admis avec mention"
       
    elif [ $x -gt 9 ]; then

        echo $y $z "est admis"
       
     else
         echo $y $z "redouble"
    

    fi

    i=$((i+1))
done
