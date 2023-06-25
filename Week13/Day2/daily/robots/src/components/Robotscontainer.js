import React from 'react';
import { connect } from 'react-redux';

class Robotcontainer extends React.Component {
    constructor(props) {
        super(props)
        console.log('props', props);
    }
    
  render() {
    return (
        <>
            <div className="robots">
                <div>
                {this.props.users
                    .filter((user) => user.name.toLowerCase().includes(this.props.searchTerm || ''))
                    .map((user)=> (
                        <div className='onerobot' key={user.id}>
                            <img alt="robots" src={`https://robohash.org/${user.id}?size=200x200`}/>
                                <div>
                                    <h2>{user.name}</h2>
                                    <p>{user.email}</p>
                                </div>
                        </div>        
                    ))}
                    
                </div>

            </div>
        </>
    )}

}

export default connect((state)=>state)(Robotcontainer)