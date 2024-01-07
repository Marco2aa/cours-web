if [ $# -eq 0 ];then
    echo " rentrez au moins un seul argument"
    exit 0
elif [ ! -d $@ ];then   
    echo "Attention j'attends des repertoires"
    exit 0

else    
    x=$(ls $1)
    nb=0
    for i in $x;do
        if [ -x $1/$i ] && [ ! -d $1/$i ];then
            echo $i 
            nb=$((nb+1))
            du -h $1/$i
            mv $1/$i $1/exec/$i

        fi
    done
    echo $nb
fi