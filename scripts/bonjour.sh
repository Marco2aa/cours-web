# # echo "bonjour $1"
# # echo "bonjour $2"
# # echo "bonjour $3"



if [ $# -eq 0 ]; then
    echo "bonjour marcheur blanc"
    else
        i=2
        while [ $i -le $# ]; do
        
        echo "bonjour ${!i}"
        
        i=$((i+2))

    done
fi
    
