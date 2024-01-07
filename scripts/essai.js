function calculatrice(n1, n2, operation){
    if (operation === "addition" || operation === "add" || operation === "+" ){
        addition(n1, n2)
    }else if (operation === "multiplication" || operation === "mul" || operation === "*"){
        multiplication(n1, n2)
    }else if (operation === "division" || operation === "div" || operation === "/"){
        division(n1, n2)
    }else if (operation === "soustraction" || operation === "sub" || operation ==="-"){
        soustraction(n1, n2)
    }

}

function addition(n1, n2) {
    console.log(`${n1} + ${n2} = ${n1 + n2}`);

}

function division(n1, n2) {
    if (n2 !== 0) {
        console.log(`${n1} / ${n2} = ${n1 / n2}`);
    }else {
        console.log("Le diviseur est égal à zero , veuillez rentrer un autre nombre")
    }
}

function multiplication(n1, n2) {
    console.log(`${n1} * ${n2} = ${n1 * n2}`)

}

function soustraction(n1, n2){
    if (n1 > n2) {
        console.log(`${n1} - ${n2} = ${n1 - n2}`)
    
    }else {
        console.log(`${n2} - ${n1} = ${n2 - n1}`);
    }
}

calculatrice(75, 0, "/")


function suiteFibo(longueur){
    let maListeFibo = [0 , 1];
    for(let i = 2; i < longueur ;i++){
        let nombreSuivant  = maListeFibo[ i - 1] + maListeFibo[ i - 2];
        maListeFibo.push(nombreSuivant);
    }
    

    console.log(`les ${longueur} premiers nombres de la suite de fibonnaci sont ${maListeFibo}`);
}


suiteFibo(100)

