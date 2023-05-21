const form = document.getElementById('libform');


const libButton = document.getElementById('lib-button');
libButton.addEventListener('click', collectValues);


function collectValues(event) {
        event.preventDefault(); 
        const nounInput = document.getElementById('noun');
        const adjectiveInput = document.getElementById('adjective');
        const personInput = document.getElementById('person');
        const verbInput = document.getElementById('verb');
        const placeInput = document.getElementById('place');
      
        // values 
        const noun = nounInput.value;
        const adjective = adjectiveInput.value;
        const person = personInput.value;
        const verb = verbInput.value;
        const place = placeInput.value;
      
        // array 
        const collectedValues = [noun, adjective, person, verb, place];
      
        console.log(collectedValues);
      }
    