let data ;

async function fetchData() {
  try {
    
    const apiKey = '3aa4dc90569f01aadcd7265fc5260df7'; 
    const apiUrl = `http://data.fixer.io/api/latest?access_key=${apiKey}`;

    // Faites une requête à l'API en utilisant fetch
    const response = await fetch(apiUrl);

    // Vérifiez si la requête a réussi (status code 200-299)
    if (!response.ok) {
      throw new Error(`Erreur HTTP! Statut: ${response.status}`);
    }

    // Convertissez la réponse en format JSON
    data = await response.json();

    // Utilisez les taux de change récupérés de l'API
    console.log('devise de reference', data.base);
    console.log('Heure actualisation' , data.date)
    console.log('Taux de change:', data.rates);
    const devises = Object.keys(data.rates);
    const devisesRef = Object.keys(data.rates);


    console.log(devises);
    let selectDeviseRef = document.getElementById('deviseRefSelect')
    let selectDevise = document.getElementById('deviseselect')

    devises.forEach(devise => {
      let optionSelect = document.createElement('option');
      optionSelect.value = devise;
      optionSelect.text = devise;
      selectDevise.add(optionSelect);

      let optionRef = document.createElement('option');
      optionRef.value = devise;
      optionRef.text = devise;
      selectDeviseRef.add(optionRef)


    // })
    });


  } catch (error) {
    // Gérez les erreurs lors de la récupération des données
    console.error('Erreur lors de la récupération des taux de change:', error);
  }

}

// Appelez la fonction fetchData
fetchData();

function conversion() {
  
  const montantInitial = document.getElementById('valeur')
  const deviseSelect = document.getElementById('deviseselect')
  const deviseRef = document.getElementById('deviseRefSelect')
  const resultat = document.getElementById('resultat')

  const montant = parseFloat(montantInitial.value)
  const deviseRefDestination = deviseRef.value
  const deviseDestination = deviseSelect.value

  if (isNaN(montant) || montant <= 0){
    resultat.textContent = 'Veuillez saisir un montant valide';
    return
  
  }

  if (deviseRef === deviseDestination){
    resultat.textContent = 'Veuillez selectionner une autre devise'
    return
  }

  const tauxDeChanges = data.rates[deviseDestination] / data.rates[deviseRefDestination]
  const resultatOp = montant * tauxDeChanges

  resultat.value = resultatOp.toFixed(2)



}

const button = document.getElementById('conversion')

button.addEventListener("click", () => {
    conversion()
})








