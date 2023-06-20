export const INSERT = 'INSERT'
export const DELETE = 'DELETE'
export const UPDATE = 'UPDATE'
export const UPDATE_INDEX = 'UPDATE_INDEX'
// export const USERS = 'USERS'


// export const getusers = () => (dispatch, getState) => {
//     console.log(getState().currentIndex);
//         fetch('https://jsonplaceholder.typicode.com/users') // тк задержка
//             .then (res =>res.json())
//             .then (data => {
//                 dispatch({type: USERS, payload:data})
//             })
//     }





export const insert_trx = (data) =>{
    return{
        type: 'INSERT',
        payload: data
    }
}

export const delete_trx = (indx) =>{
    console.log('action inserted');
    return{
        type: 'DELETE',
        payload: indx
    }
}

export const update_trx = (data) =>{
    return{
        type: 'UPDATE',
        payload: data
    }
}

export const update_id = (indx) =>{
    console.log("index of current clicked transation ACTION", indx);
    return{
        type: 'UPDATE_INDEX',
        idTransaction: indx
    }
}