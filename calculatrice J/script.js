const input = document.getElementById("bouton")
const buttons = document.querySelectorAll('.button')

buttons.forEach(button =>{
    button.addEventListener("click",() =>{
        input.value += button.textContent;
    });
});

const buttondelete = document.getElementById("C")
const buttonclear = document.getElementById("AC")

buttondelete.addEventListener("click", () => {
    let currentvalue = input.value
    if (currentvalue.length > 0) {
        input.value=currentvalue.slice(0,-1)
    }

} )

buttonclear.addEventListener("click", () => {
    input.value = ''
})

buttonequal = document.getElementById("=")

buttonequal.addEventListener("click", () => {
    let expression = input.value
    if (expression.trim() !== ""){
        result = eval(expression)
        input.value = result
    }else{
        input.value = "ERR"
    }
})
    