// #1
// function funcOne() {
//     const a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }
// funcOne()
// #1.1 - run in the console:
// funcOne() - will give `inside the funcOne function 3`
// #1.2 What will happen if the variable is declared - will give error
// with const instead of let ?

//#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // // // #2.1 - run in the console:
// funcThree() -0
// funcTwo() -5
// funcThree()
// // #2.2 What will happen if the variable is declared funcThree() -0, funcTwo() - error
// // with const instead of let ?


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive() - hello

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix() - test
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ? - test

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console - 5 and 2
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?  5 and 2
// ==============2============

// const winBattle = () => {
//      true;
//  
  
//   const experiencePoints = winBattle() ? 10 : 1;
//   console.log(experiencePoints);
// ====================================3=======
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"]

// let viol=colors.some((item)=> item ==="Violet");
// if (viol) {
//     console.log ("yeah")} 




// if (colors.includes("Violet")) {
//     console.log("Yeah");
//   } else {
//     console.log("No...");
//   }
