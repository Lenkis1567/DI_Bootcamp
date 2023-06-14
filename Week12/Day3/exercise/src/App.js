
import './App.css';
import React from 'react';
import ErrorBoundary from './ErrorBoundary.js';


class BuggyCounter extends React.Component {
  constructor() {
    super();
    this.state = {
      count: 0,
    };
  }

  add = () => {
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    if (this.state.count > 5) {
      throw new Error('Crashed');
    }
    return (
      <div>

        <p 
          onClick={this.add} 
          style={{ margin: '15px', padding: '4px', fontSize: '24px' }}
        >
          {this.state.count}
        </p>
      </div>
    );
  }
}



function App() {
return (
  <div className="App">
    <header className="App-header">
{/* 
            <BuggyCounter/>
 */}

{/* ================== */}

      <ErrorBoundary>
            <BuggyCounter/>
            <BuggyCounter/>
      </ErrorBoundary> 

{/* =========================
{/* 
            <ErrorBoundary>
            <BuggyCounter/>
            </ErrorBoundary>
            
            <ErrorBoundary>
            <BuggyCounter/>
            </ErrorBoundary> */}

      
      </header>
    </div>
  );
}

export default App;
