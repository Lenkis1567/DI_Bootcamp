// import { connect } from 'react-redux';
// import { incrementCounter, decrementCounter } from '../redux/actions';

// const Counter = (props) => {
//   const { num, handleIncrement, handleDecrement } = props;

//   return (
//     <>
//       <button onClick={handleDecrement}> - </button>
//       {num}
//       <button onClick={handleIncrement}> + </button>
      
    
//     </>
//   );
// };

// const mapStateToProps = (state) => {
//   return {
//     num: state.count,
//   };
// };

// const mapDispatchToProps = (dispatch) => {
//   return {
//     handleIncrement: () => dispatch(incrementCounter()),
//     handleDecrement: () => dispatch(decrementCounter()),
//   };
// };

// export default connect(mapStateToProps, mapDispatchToProps)(Counter);


// ==============another way========================
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { incrementCounter, decrementCounter } from '../redux/actions';

const Counter = () => {
  const num = useSelector((state) => state.count); //like mapStateToProps
  const dispatch = useDispatch(); //like mapDispatchToProps

  const handleIncrement = () => {
    dispatch(incrementCounter());
  };

  const handleDecrement = () => {
    dispatch(decrementCounter());
  };

  return (
    <>
      <button onClick={handleIncrement}> + </button>
      {num}
      <button onClick={handleDecrement}> - </button>
    </>
  );
};

export default Counter;



