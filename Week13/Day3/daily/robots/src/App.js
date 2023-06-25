import React from 'react';
import {Component} from 'react';
import { connect } from 'react-redux';
import './App.css';
import Robotcontainer from './components/Robotscontainer'



class App extends Component {
  constructor(props) {
    console.log('props in app', props);
    super(props);
    this.state = {
      users: [],
      search: '',
    };
  }
  handleChange = (e) => {
    const searchStr = e.target.value;
    this.props.dispatch({type: 'SEARCH_ROBOT', payload: searchStr})
    console.log("searchStr", searchStr);
  };

  componentDidMount() {
    fetch('https://jsonplaceholder.typicode.com/users')
    .then((res)=>res.json())
    .then(users=>this.setState({users: users}))
    .catch(e=>console.log(e))
  }
  
  render() {

    return (
      <div className ="App">
          <h1 className="f1">RoboFriends</h1>
          <div className="pa2">
              <input className="pa3" type="search" placeholder="search robots" onChange={this.handleChange}/>
          </div>

        <Robotcontainer users={this.state.users} />
      </div>
    );
} }

const mapStateToProps = (state) => {
  return {
    search: state.search, 
  };
};

// export default connect()(App)
export default connect(mapStateToProps)(App)