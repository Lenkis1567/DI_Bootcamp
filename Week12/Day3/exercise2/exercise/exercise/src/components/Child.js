import React from 'react';

class Child extends React.Component {
  componentWillUnmount() {
    alert('Component is unmounted!');
  }

  render() {
    return <h2>Hello World!</h2>;
  }
}

export default Child;