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
        const collectedVal = [noun, adjective, person, verb, place];
 
        let story= `In the bustling city of ${collectedVal[4]}, a  playful ${collectedVal[1]} ${collectedVal[0]} named 
${collectedVal[2]} roamed the streets with a mischievous twinkle in his emerald eyes. Known for his acrobatic 
leaps and quirky antics, Milo brought laughter and joy to everyone he ${collectValues[3]}. One day, while exploring
  an old bookstore, he stumbled upon a magical ${collectedVal[0]} that whisked him away to the whimsical land
   of Whiskerland. 
  In this enchanting place filled with dancing mice and talking birds, Milo discovered a hidden talent for singing, 
  captivating audiences with his melodious meows.`

  // adding content
  let spa=document.querySelector('#story')
  let p_st = document.createElement('p');
  p_st.textContent = story
  spa.appendChild(p_st)
   
      }
