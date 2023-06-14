import './App.css';
// import Car from './components/Car.js';
// import Events from './components/Events.js';
// import Phone from './components/Phone.js';
// import Color from './components/Color.js';
import Child from './components/Child.js';
import React from 'react';

// const carinfo = {
//   name: "Ford",
//   model: "Mustang"
// };

// function App() {
  
//   return (
//     <div style={{ marginLeft: "20px" }}>
//       <h1>Car Information</h1>
//       <Car info={carinfo} />  {/*в кавычках - переменная, без - то, что уйдет как пропс */ }
//     <Events/>
//     <Phone/>
//     <Color/>
//     <Child/>
//     </div>
//   );
// }
class App extends React.Component {
  constructor() {
    super();
    this.state = {
      show: true
    };
  }

  handleClick = () => {
    this.setState({ show: false });
  };

  render() {
    return (
      <div>
        {this.state.show && <Child />}
        <button onClick={this.handleClick}>Delete</button>
      </div>
    );
  }
}

export default App;
