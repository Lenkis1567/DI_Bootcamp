import{INSERT, UPDATE, DELETE, UPDATE_INDEX} from './actions';
import { addToLocalStorage, getFromLocalStorage } from '../utils/storage';

const initState = {
  list: getFromLocalStorage('transactions'),
  currentIndex: -1,
  user:[]
}
 
export const reducer = (state = initState, action={}) => {
  switch (action.type) {
    // case USERS:
    //   return {...state, users:action.payload}
    case INSERT: {
        const newList = [...state.list]
        newList.push(action.payload)
        addToLocalStorage('transactions', newList)
        console.log('Reducer INSERT');
        return {...state, list:newList, currentIndex: -1}
    }
    case UPDATE: 
      state.list[state.currentIndex] = action.payload
      addToLocalStorage('transactions', [...state.list])
      return{...state, list:[...state.list], currentIndex:-1}
  
    case DELETE: 
      state.list.splice(action.payload, 1)
      addToLocalStorage('transactions', [...state.list])
      return {...state, list:[...state.list], currentIndex:-1}

    case UPDATE_INDEX:
      console.log("index of current clicked transation REDUCER", action.idTransaction);
      return {...state, currentIndex: action.idTransaction}

    default:
       return {...state}
}
  }