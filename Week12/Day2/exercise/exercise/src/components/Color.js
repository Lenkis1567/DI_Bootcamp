
import React from 'react';



class Color extends React.Component {
    constructor() {
        super();
         this.state = {favoriteColor: "red"};
        }

      componentDidMount() {
        setTimeout(() => {
        this.setState({
        favoriteColor: "yellow"
        });
        }, 5000);
        }

        changeColorToBlue = () => {
        this.setState({
        favoriteColor: "blue"
        });
        }
  render() {
    return (
    <div>
        <h2>My favorite color is {this.state.favoriteColor} </h2>
        <button type="button" onClick={this.changeColorToBlue}>Change to blue</button>
      
    </div>
 ) }
}

export default Color