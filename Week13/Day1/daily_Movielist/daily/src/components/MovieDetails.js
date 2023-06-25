import {useSelector} from 'react-redux'

const MovieDetails = (props) => {
    const details = useSelector(state=>state.reducer_detail.movie_details)
    return (
        <div style={{display:'inline-block', width: '50%'}}>
            <h1> Movie details</h1>
            <h2>Title: {details.title}</h2>
            <h2>Release date: {details.releaseDate}</h2>
            <h2>Movie detail: {details.rating}</h2>
        </div>
    )
}
export default MovieDetails