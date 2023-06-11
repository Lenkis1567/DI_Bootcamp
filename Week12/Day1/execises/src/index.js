import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));

// #1
// root.render(
//   <React.StrictMode>
//     <h1> I do not use JSX </h1>
//   </React.StrictMode>
// );

//  #2.1
// const helloMessage = <h1> Hello World!</h1>;
// root.render(helloMessage)


// #2.2
// const myelement = <h1> I Love JSX! Sometimes...</h1>;
// root.render(myelement)

// 2.3
// const sum = 5 + 5;
// const sentence = <h4>React is {sum} times better with JSX</h4>;
// root.render(sentence);

//3

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
