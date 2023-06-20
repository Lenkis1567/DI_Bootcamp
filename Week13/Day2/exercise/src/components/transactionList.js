import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {delete_trx, update_id} from '../redux/actions'
import TransactionForm from './TransactionForm'


const TransactionList = () => {
    const list = useSelector(state => state.list);//making the list from the state available in this compomrny
    const dispatch = useDispatch(); //method tp make the dispacth functin available in this conmpnenetn

    return (
        <> 
        <TransactionForm/>
            <h2>Transaction list</h2>
            <table style={{border:'0.5px solid white'}}> 
                <tbody>
                    {
                    list.map((item, i) => {
                        return(
                        <tr key={i} style={{fontSize: '15px'}}>
                            <td style={{border: '1px solid white', padding: "5px"}}>{item.accountNumber}</td>
                            <td style={{border: '1px solid white', padding: "5px"}}>{item.FSC}</td>
                            <td style={{border: '1px solid white', padding: "5px"}}>{item.name}</td>
                            <td style={{border: '1px solid white', padding: "5px"}}>{item.amount}</td>
                            <td style={{border: '1px solid white', padding: "5px"}}>
                            <button onClick={()=> dispatch(update_id(i))}> Edit </button>
                            </td>
                            <td style={{border: '1px solid white', padding: "5px"}}>
                            <button onClick={()=> dispatch(delete_trx(i))}> Delete </button>
                            </td>
      
                        </tr>
                        )
                    })
                    }
                </tbody>
            </table>


        </>
    )

}


export default TransactionList




        // {/* {props.list_transactions.length!==0 && 
        //     props.list_transactions.map ((item, index) => 
        //     <div key={index} style={{display: 'flex'}}>
        //         <p style={{display: 'flex', padding: '10px', border: '1px solid white'}}>{item.accountNumber}</p>
        //         <p style={{display: 'flex', padding: '10px', border: '1px solid white'}} >{item.fsc}</p>
        //         <p style={{display: 'flex', padding: '10px', border: '1px solid white'}} >{item.accountHolderName}</p>
        //         <p style={{display: 'flex', padding: '10px', border: '1px solid white'}}>{item.amount}</p>
        //      <button onClick={deleteTransaction(item, index)} style={{width:'15px'}}> Delete </button>   
        //     </div>) */}
            
        // {/* } */}