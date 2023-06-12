import React, { Component } from "react";

class Phone extends Component {
    constructor(){
        super();
        this.state = {
            brand: "Samsung",
            model: "Galaxy S20",
            color: "black",
            year: 2020
        };
    }
    changeColor = () => { 
        let colors =['blue', 'red', 'green', 'yellow', 'grey', 'silver']
        let randomColor = colors[Math.floor(Math.random() * colors.length)];
        this.setState({ color: randomColor });

    }
    render()  {  
        return (
            <div>
            <h2>My phone is a {this.state.brand}</h2>
            <h4>It is a {this.state.color} {this.state.model} from {this.state.year}.</h4>
            <button type="button" onClick={this.changeColor}> Change color </button>
            </div>
        )
}
}

export default Phone;