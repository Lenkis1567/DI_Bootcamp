import { applyMiddleware, combineReducers, createStore } from 'redux';
import thunk from 'redux-thunk';

function searchReducer(state=[], action={}){
   if (action.type==="SEARCH_ROBOT") {
    return action.payload
  }
  return state
}

const loadingReducer = (state = true, action) => {
  if (action.type==='LOADING_START') return true
  if (action.type==='LOADING_FINISH') return false
  if (action.type==="SEARCH_ROBOT") return false
  return state
}

const rootReducer = combineReducers({
  searchTerm: searchReducer,
  loading: loadingReducer
 })

 export const store = createStore(rootReducer, applyMiddleware(thunk))
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