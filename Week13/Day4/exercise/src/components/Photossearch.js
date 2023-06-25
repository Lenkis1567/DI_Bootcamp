
import React from 'react';


function Photossearch(props) {
  

return (
    <> 
    <h2> Pictures </h2>
    <div className="photo-container">
      <div className="photo-wrapper">
        {props.searched.map((photo, index) => (
          <img
            key={index}
            src={photo.src.small}
            alt={photo.alt}
            className="photo"
          />
        ))}
      </div>
    </div>
    </>
  );
}

export default Photossearch;

