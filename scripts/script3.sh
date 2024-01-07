
i=2
while [ $i -le 20 ];do
    echo $i
    i=$((i+2))
    
   

done

for i in {1..5};do
    touch f$i
done
