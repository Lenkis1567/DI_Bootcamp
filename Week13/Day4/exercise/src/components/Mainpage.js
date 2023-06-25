import React from 'react'

const Mainpage = (props) => {
   
    return (
        <div className='container'>
            <h1>SnapShot</h1>
            <form className="search-form" onSubmit = {props.searchPhotos}>
                <input type="text" className="search" placeholder="Search..." />
                    <button type="submit" className="search-button null" >
                        <svg height="32" width="32">
                        </svg>
                    </button>
                </form>

        </div>
    )
}

export default Mainpage
