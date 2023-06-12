import React, { Component } from "react";

// class Events extends Component {
//   clickMe = () => {
//     alert("I was clicked"); 
       
//   };

//   render() {
//     return (
//       <div>
//         <button onClick={this.clickMe}>Click Me</button>
//       </div>
//     );
//   }
// }

// this is to catch all buttons
// class Events extends Component {
//     handleKeyDown = (event) => {
//       console.log("Key pressed: ", event.target.value);
//       alert(event.target.value);
//     };
  
//     render() {
//       return (
//         <div>
//           <input type="text" onKeyUp={this.handleKeyDown} />
//         </div>
//       );
//     }
//   }


// class Events extends Component {
//     handleKeyDown = (event) => {
//       if (event.key === "Enter") {
//         const inputText = event.target.value;
//         alert("Enter key was pressed, you text is: " + inputText);
//       }
//     };
//     render() {
//         return (
//           <div>
//             <input type="text" onKeyDown={this.handleKeyDown} />
//           </div>
//         );
//       }
//     }


class Events extends Component {
    state = {
      isToggleOn: true
    };
  
    handleClick = () => {
      this.setState((prevState) => ({
        isToggleOn: !prevState.isToggleOn
      }));
    };
  
    render() {
      return (
        <div>
          <button type="button" onClick={this.handleClick}>
            {this.state.isToggleOn ? "ON" : "OFF"}
          </button>
        </div>
      );
    }
  }

export default Events;
