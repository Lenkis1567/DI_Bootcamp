import {useSelector, useDispatch} from 'react-redux';
// import {showDetails} from './redux/action';
import {DETAIL} from '../redux/reducers'


const MovieList= (props) => {

    const list = useSelector (state => state.reducer_list.movies_list);

    const dispatch = useDispatch();

    return (
        <div style={{display:'inline-block', width: '50%'}}>
            <h1> Movie list</h1>
            {
                list.map((item, index)=> {
                    return (
                        <div key={index}>
                        {item.title}
                        <button onClick={()=> dispatch ({type:DETAIL, payload:item})}>Details</button>
                        </div>
                    )
                })
            }
        </div>
    )
}

export default MovieList

// const mapDispatchToProps = dispatch => {
//     return {
//         show (item) => dispatch(showDetails(item))
//     }
// }

// export default connect(null, mapDispatchToProps)(MovieList)
// const mapStateToProps = state => {
//     return {
//         list: state.movie_list
//     }
// }
// export default connect(mapStateToProps) (MovieList)