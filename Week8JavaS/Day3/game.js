
function playTheGame() {
    if (confirm('Do you want to play the game?')) {
        function ask() {
            var a = Number(prompt('Guess the number: '));
            if (isNaN(a)) {
                alert('Sorry, Not a number, Goodbye');
            }
            else if (a < 0 || a > 10) {
                alert('Sorry, Not a valid number, Goodbye');
            }
            else {
                return a;
            }
        }

        var computerNumber = Math.round(Math.random() * 10);
        var userNumber = ask();
        compareNumbers(userNumber, computerNumber);
    } else {
        alert("No problem, Goodbye");
    }
}

function compareNumbers(userNumber, computerNumber) {
    if (userNumber < computerNumber) {
        alert("Your number is smaller than the computer’s, guess again");
        playTheGame();
    }
    else if (userNumber > computerNumber) {
        alert("Your number is bigger than the computer’s, guess again");
        playTheGame();
    }
    else {
        alert('WINNER');
    }
}

playTheGame();


// function playTheGame() {
//     var confirmed = localStorage.getItem("confirmed");
//     if (!confirmed) {
//         if (confirm('Do you want to play the game?')) {
//             localStorage.setItem("confirmed", true);
//         } else {
//             alert("No problem, Goodbye");
//             return;
//         }
//     }

//     var attempts = 0; // Track the number of attempts
//     function ask() {
//         var a = Number(prompt('Guess the number: '));
//         if (isNaN(a)) {
//             alert('Sorry, Not a number, Goodbye');
//         }
//         else if (a < 0 || a > 10) {
//             alert('Sorry, Not a valid number, Goodbye');
//         }
//         else {
//             return a;
//         }
//     }

//     var computerNumber = Math.round(Math.random() * 10);
//     var userNumber = ask();
//     while (userNumber !== undefined) {
//         attempts++; // Increment attempts after each guess
//         if (attempts > 3) {
//             alert('Out of chances');
//             return;
//         }
//         compareNumbers(userNumber, computerNumber);
//         userNumber = ask();
//     }
// }

// function compareNumbers(userNumber, computerNumber) {
//     if (userNumber < computerNumber) {
//         alert("Your number is smaller than the computer’s, guess again");
//     }
//     else if (userNumber > computerNumber) {
//         alert("Your number is bigger than the computer’s, guess again");
//     }
//     else {
//         alert('WINNER');
//     }
// }

// playTheGame();
