const buttonX = document.querySelector('.choice button.x');
const buttonY = document.querySelector('.choice button.y');
let playerChoice = null;
let YT=0;
stepsComp=[]

const winCombos = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 1]
]
//x

buttonX.addEventListener('click', () => {
    if (playerChoice === null) {
          console.log('Выбран X');
          playerChoice = 'X';
          YT=1; console.log ("YT in button x", YT)
    }
  });

  //y
buttonY.addEventListener('click', () => {
    if (playerChoice === null) {
        console.log('Выбран Y');
        playerChoice = 'Y';
  }
});

const squares = document.querySelectorAll('.square');
let steps = [];


squares.forEach((square, index) => {
    square.addEventListener('click', function(event) {
      if (YT % 2 === 1) {
        const position = index + 1; // Get the position based on the div's index
        if (steps.length === 0 && !steps.includes(position) && steps.length<8) {
          console.log(YT);
          console.log(position);
          steps.push(position);
          square.textContent = "X";
          YT = YT + 1;
          console.log("YT in div x", YT);
          computerPlay(steps, winCombos);
          console.log(computerPlay(steps, winCombos));
        }
      }
          });
     
  });
  
  // Function to calculate position based on index
  function getPosition(index) {
    const row = Math.floor(index / 3) + 1;
    const column = (index % 3) + 1;
    return [row, column];
  }

  //computer step
   function computerPlay(steps, winCombos) {
    if (YT % 2 === 0) {
      YT = YT + 1;
      if (findMatchingArray(steps, winCombos) !== false) {
        stepsComp.push(findMatchingArray(steps, winCombos).arr - findMatchingArray(steps, winCombos).matchingValues);
      } else {
        if (!steps.includes(5) && !stepsComp.includes(5)) {
          stepsComp.push(5);
        } else {
          if (!steps.includes(1) && !stepsComp.includes(1)) {
            stepsComp.push(1);
          } else {
            if (!steps.includes(3) && !stepsComp.includes(3)) {
              stepsComp.push(3);
            } else {
              if (!steps.includes(7) && !stepsComp.includes(7)) {
                stepsComp.push(7);
              } else {
                if (!steps.includes(9) && !stepsComp.includes(9)) {
                  stepsComp.push(9);
                } else {
                  if (!steps.includes(2) && !stepsComp.includes(2)) {
                    stepsComp.push(2);
                  } else {
                    if (!steps.includes(4) && !stepsComp.includes(4)) {
                      stepsComp.push(4);
                    } else {
                      if (!steps.includes(6) && !stepsComp.includes(6)) {
                        stepsComp.push(6);
                      } else {
                        if (!steps.includes(8) && !stepsComp.includes(8)) {
                          stepsComp.push(8);
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    let text = `div${stepsComp[stepsComp.length - 1]}`;
    const square_comp = document.querySelector(`#${text}`);;
    square_comp.textContent = "Y";
    return stepsComp[stepsComp.length - 1];

  }





//check on danger posttions
   function findMatchingArray(steps, winCombos) {
    for (const arr of winCombos) {
      const matchingValues = steps.filter(value => arr.includes(value));
      if (matchingValues.length >= 2) {
        return {
          array: arr,
          matchingValues: matchingValues.slice(0, 2)
        };
      }
    }
  
    return false;
  }
