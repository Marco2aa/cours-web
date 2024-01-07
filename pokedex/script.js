let clickButton = document.getElementById('button')
let pokeImage = document.getElementById('image')
let pokeName = document.getElementById('name')
let pokeNumber = document.getElementById('number')

async function randomPokemon() {
    let randomNumber = Math.ceil(Math.random() * 150 ) + 1

    let requestString = `https://pokeapi.co/api/v2/pokemon/${randomNumber}`

    let data = await fetch(requestString)
    
    let response = await data.json();

    pokeImage.src = response.sprites.front_shiny;
    pokeName.textContent = response.name;
    pokeNumber.textContent = `#${response.id}`;

    console.log(response)
}

randomPokemon()
clickButton.addEventListener("click" , randomPokemon)