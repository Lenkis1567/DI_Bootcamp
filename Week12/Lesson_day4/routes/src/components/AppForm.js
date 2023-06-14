import React from 'react'
class AppForm  extends React.Component {
    constructor () {
        super();
        this.state = {
            firstname:'',
            lastname: '',
            age: '',
            color: '',
            gender: '',
            nutsFree: false,
            lactoseFree: false,
            vegan: false,
              
        }
 }


    handleSubmit = (e) => {
        e.preventDefault()
        const {firstname, lastname, color, age, gender, nutsFree, lactoseFree, vegan} = this.state;
        const alnutsFree = nutsFree? 'Yes': 'No';
        const alactoseFree = lactoseFree ? 'Yes' : 'No';
        const alvegan = vegan?  'Yes': 'No';
        console.log(firstname, lastname, color, age, gender, alnutsFree, alactoseFree, alvegan);
    }

    handleChange = (e) => {
        
        const value = (e.target.type ==="checkbox")
        ? e.target.checked
        : e.target.value;
        console.log(value);
        this.setState({[e.target.name]: value})
    }


    render () {
       return(
    <>
        <div class="input">
            <h1>My Form</h1>
            <form onSubmit={this.handleSubmit} class='inputForm'>
                First name: <input 
                    type="text" 
                    name = "firstname"
                    onChange={(e)=>this.handleChange(e)}
            /><br/>
                Last name: <input type="text" 
                    name = "lastname"
                    onChange={this.handleChange}
                /><br/>

                Age: <input type="text" 
                    name = "age"
                    onChange={this.handleChange}
                /><br/>

            <div onChange = {this.handleChange}>
                <input type='radio' value='male' name='gender'/> Male
                <input type='radio' value='female' name='gender'/> Female
            </div>
    
                <h4>Select your destination:</h4>
                <select name = "color" onChange = {this.handleChange}>
                <option value=""> Please choose your destination </option>
                    <option value = '1'> Brazil</option>
                    <option value = '2'> Thailand</option>
                    <option value = '3'> Japan</option>
                </select>

                <br/>

                <h3>Dietary restrictions:</h3>
                    <label>
                        <input
                        type="checkbox"
                        name="nutsFree"
                        checked={this.state.nutsFree}
                        onChange={this.handleChange}
                        />
                        Nuts free
                    </label>
                    <br />
                    <label>
                        <input
                        type="checkbox"
                        name="lactoseFree"
                        checked={this.state.lactoseFree}
                        onChange={this.handleChange}
                        />
                        Lactose free
                    </label>
                    <br />
                    <label>
                        <input
                        type="checkbox"
                        name="vegan"
                        checked={this.state.vegan}         
                        onChange={this.handleChange}
                        />
                        Vegan
                    </label>

            </form>
            
            <br/>

            <input type="submit" value = "submit"/>
        </div>
        <div class="output">
            <h2>Entered information</h2>
            <div>
                <p name='entered-info'>
                Your name: {this.state.firstname} {this.state.lastname}
                </p>
                <p name='entered-info'>
                    Your age: {this.state.age}
                </p>
                <p name='entered-info'>
                    Your gender: {this.state.gender}
                </p>

                <p name='entered-info'>
                Your destination: {this.state.color === '1' ? 'Brazil' : this.state.color === '2' ? 'Thailand' : 'Japan'}
                </p>
                
                <p>Your dietary restrictions:<br/>
                    <span>**Nuts free: {this.state.nutsFree ? 'Yes' : 'No'}</span>
                    <span>**Lactose free: {this.state.lactoseFree ? 'Yes' : 'No'}</span>
                    <span>Vegan meal: {this.state.vegan ? 'Yes' : 'No'}</span>
                </p>


            </div>

        </div>
       </>
    )}

}

export default AppForm