import {createStore, applyMiddleware} from 'redux';
import {reducer} from './reducer.js';
import thunk from 'redux-thunk'


// const myMiddleWare = (store) => (next) =>(action) => {
//     console.log('state', store.getState());
//     console.log('action', action);
//     next(action)
// }

const logger = (store) => (next) =>(action) => {
    console.log('state', store.getState());
    console.log('action', action);
    next(action)
}
const store = createStore(reducer, applyMiddleware(logger, thunk)); 
export default store;