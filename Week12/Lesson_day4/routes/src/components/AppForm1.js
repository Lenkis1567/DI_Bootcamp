// import React from 'react'
// class AppForm  extends React.Component {
//     constructor () {
//         super();
//         this.state = {
//             firstname:'',
//             lastname: '',
//             color: '',
//             isgo: '',
//             gender: '',
//         }
//  }
// const [formData, setFormData] = userState({


// })

//     handleSubmit = (e) => {
//         e.preventDefault()
//         const {firstname, lastname, color, isgo} = this.state;
//         const go = isgo? 'I am going':'No I will not';
//         console.log(firstname, lastname, color, isgo);
//     }

//     handleChange = (e) => {
        
//         const value = (e.target.type ==="checkbox")
//         ? e.target.checked
//         : e.target.value;
//         console.log(value);
        
//         setFormData({...formData, [e.target.name]:value})
//     }

//     render () {
//        return(
//         <div>
//             <h1>My Form</h1>
//             <form onSubmit={this.handleSubmit}>
//                 First name: <input 
//                     type="text" 
//                     name = "firstname"
//                     onChange={(e)=>this.handleChange(e)}
//             /><br/>
//                 Last name: <input type="text" 
//                 name = "lastname"
//                 onChange={this.handleChange}
//                 /><br/>

//                 <select name = "color" onChange = {this.handleChange}>
//                     <option value = '1'> Red</option>
//                     <option value = '2'> Blue</option>
//                     <option value = '3'> Green</option>
//                 </select>

//                 <br/>

//             </form>
//             Is Going <input type ="checkbox" onChange = {this.handleChange} name = "isgo"/>

//             <br/>

//             <div onChange = {this.handleChange}>
//                 <input type='radio' value='male' name='gender'/> Male
//                 <input type='radio' value='female' name='gender'/> Female
//                 <input type='radio' value='other' name='gender'/> Other
//             </div>

//             <input type="submit" value = "submit"/>
//         </div>
//     )}

// }

// export default AppForm