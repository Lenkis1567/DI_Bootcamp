// import React from 'react';

const UserFavoriteColors = (props) => {
    console.log(props);
  const { favAnimals } = props;

  const animalItems = favAnimals.map((animal, index) => (
    <li key={index}>{animal}</li>
  ));

  return (
    <div>
      <h3>User's Favorite Animals:</h3>
      <ul>{animalItems}</ul>
    </div>
  );
};

export default UserFavoriteColors;