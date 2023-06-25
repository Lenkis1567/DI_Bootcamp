import { Link } from 'react-router-dom';

const Buttons = (props) => {

    return(
        <nav className="main-nav">
        <ul>
            <li ><p onClick={props.searchDefPhotos} name="mountain" Link to='/mountain'>Mountain</p>
            </li>
            <li><p onClick={props.searchDefPhotos} name="birds">Beaches</p>
            </li>
            <li><p aria-current="page" className="active" name="birds" onClick={props.searchDefPhotos}>Birds</p>
            </li>
            <li><p  name="food" onClick={props.searchDefPhotos}>Food</p>
            </li>
        </ul>
    </nav>)
}

export default Buttons