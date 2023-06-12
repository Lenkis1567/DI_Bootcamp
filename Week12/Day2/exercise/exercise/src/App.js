import './App.css';
import Car from './components/Car.js';
import Events from './components/Events.js';
import Phone from './components/Phone.js';
import Color from './components/Color.js';

const carinfo = {
  name: "Ford",
  model: "Mustang"
};

function App() {
  
  return (
    <div style={{ marginLeft: "20px" }}>
      <h1>Car Information</h1>
      <Car info={carinfo} />  {/*в кавычках - переменная, без - то, что уйдет как пропс */ }
    <Events/>
    <Phone/>
    <Color/>
    </div>
  );
}

export default App;
