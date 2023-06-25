import React from'react'
import {connect} from 'react-redux';
import Counter from './components/Counter'
import {incrementCounter, decrementCounter, } from './redux/actions'

function App() {
  return (
    <div className="App">
    <header className="App-header">
      <Counter/>
    </header>
  </div>
);
}

const mapStateToProps = (state) => {
  console.log('state in App',state);
  return {
    count: state.count

  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    handleIncrement: () => dispatch(incrementCounter()),
    handleDecrement: () => dispatch(decrementCounter())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App)


