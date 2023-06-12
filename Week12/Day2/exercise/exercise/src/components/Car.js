import React from 'react';
import Garage from './Garage.js';

// function Car(props) {
//   return (
//     <div>
//       <h2>This car is {props.info.model}</h2>
//     </div>
//   );
// }

// class Car extends React.Component { 
// render() {
//   return (
//     <div>
//       <h2>This car is {this.props.info.model}</h2>
//     </div>
//         );
//     }
// }

class Car extends React.Component {
    constructor() {
        super();
         this.state = {color: "red"};
  }
  render() {
    return (
    <div>
        <h2>This car is {this.state.color} {this.props.info.model}. </h2>
        <Garage/>
    </div>
 ) }
}

export default Car;


