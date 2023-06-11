// import logo from './logo.svg';
import './App.css';
import UserFavoriteColors from './components/UserFavoriteColors';
import Exercise4 from './components/Exercise4';

function App() {
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals : ['Horse','Turtle','Elephant','Monkey']
  };
  return (
    <div>
      <h3>First Name: {user.firstName}</h3>
      <h3>Last Name: {user.lastName}</h3>
      <UserFavoriteColors favAnimals={user.favAnimals} name={user.firstName} />
      <Exercise4 />
    </div>
  );
};



export default App;
