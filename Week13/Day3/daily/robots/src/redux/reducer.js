import { combineReducers, createStore } from 'redux';

function searchReducer(state=[], action={}){
  console.log('action', action)
  if (action.type==="SEARCH_ROBOT") {
    return action.payload
  }
  return state
}

const rootReducer = combineReducers({
  searchTerm: searchReducer
 })

 export const store = createStore(rootReducer)
 store.subscribe(()=> console.log('store get state', store.getState()))

  // export const reducer = (state = initState, action={}) => {
  //   switch (action.type) {

  //     case 'INCREMENT_COUNTER':
  //       console.log('INCREMENT_COUNTER');
  //       return {...state, count: state.count + 1}
  //     case 'DECREMENT_COUNTER':
  //       console.log('DECREMENT_COUNTER');
  //       return {...state, count: state.count - 1}
  //     default:
  //       return {...state}
  //   }
  // }