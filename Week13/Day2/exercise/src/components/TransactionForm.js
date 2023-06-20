import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {connect} from 'react-redux'
import {insert_trx, update_trx} from '../redux/actions'
import {useState, useEffect} from 'react'


const TransactionForm = (props) => {
    const [transaction, setTransaction] = useState (
        {
            accountNumber: '',
            FSC: '',
            name: '',
            amount: ''
        }
    )

    // const currentIndex = useSelector((state) => state.currrentIndex);
    const currentIndex = useSelector((state) => state.currentIndex);
    const list = useSelector(state=>state.list)
    const dispatch =  useDispatch()

    const handleInputChange = (e) => {
          setTransaction({...transaction, [e.target.name]:e.target.value})
    }
    
    // console.log ('Before useEffect', currentIndex);
    
    // when we mount the componenet
    // when we update the componenet
    useEffect(() =>{
      console.log("in use effect");
      if (currentIndex !== -1) {
        const trx = list[currentIndex];
        setTransaction({
          accountNumber: trx.accountNumber|| '',
          FSC: trx.FSC||'',
          name: trx.name||'',
          amount: trx.amount || ''
        })
      }
    }, [currentIndex])

       
    const handleSubmit = (e) => {
      e.preventDefault();
      if (currentIndex === -1) {
        dispatch(insert_trx(transaction))
      } else {
        dispatch(update_trx(transaction))
      }

    };

    return (
        <div>
            <h1>Financial Transactions:</h1>
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="accountNumber">Account Number:</label>
        <input
          type="text"
          name="accountNumber"
          className="accountNumber"
          placeholder="Enter Account Number"
          onChange={handleInputChange}
          value={transaction.accountNumber}
       
          required
        />
      </div>
      <div>
        <label htmlFor="fsc">FSC:</label>
        <input
          type="text"
          name="FSC"
          className="fsc"
          placeholder="Enter FSC"
          onChange={handleInputChange}
          value={transaction.FSC}
          required
        />
      </div>
      <div>
        <label htmlFor="accountHolderName">A/C Holder Name:</label>
        <input
          type="text"
          className="accountHolderName"
          name = "name"
          placeholder="Enter A/C Holder Name"
          onChange={handleInputChange}
          value={transaction.name}
      
          required
        />
      </div>
      <div>
        <label htmlFor="amount">Amount:</label>
        <input
          type="text"
          className="amount"
          name = "amount"
          placeholder="Enter Amount"
          onChange={handleInputChange}
          value={transaction.amount}
       
          required
        />
      </div>
      <button type="submit" value={currentIndex===-1 ? "Submit" : "Update"}>Submit</button>
    </form>    


        </div>


    )
  
}

const mapDispatchToProps = (dispatch) => {
    return {
        insert_data : (new_transaction) => dispatch (insert_trx((new_transaction)))
    }
}

export default connect(null, mapDispatchToProps) (TransactionForm)