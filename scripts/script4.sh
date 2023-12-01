echo "je suis le script $0"
echo " mon premier argument est $1"
for i in $@;do
    echo $i
done
echo "je possede $# arguments en parametre"