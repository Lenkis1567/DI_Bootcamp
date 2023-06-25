
import './App.css';
import Mainpage from './components/Mainpage'
import Photossearch from './components/Photossearch'
import Buttons from './components/Buttons'
import { useEffect, useState } from 'react';
import { createClient } from 'pexels';
import { Routes, Route, Link } from 'react-router-dom'

function App() {
  const [searched, setSearched] = useState([]);
  const [inputValue, setinputValue] = useState('mountain');
  const [defValue, setdefValue] = useState('mountain')
  
  useEffect(() => {
   const client = createClient('e05NhJaQJOtRcTpVwOPZ44idqZVa19I8w75N75S5NIWVsXGlUA145KKu');
   const query = inputValue;

    client.photos.search({ query, per_page: 30, size: 'small', orientation: 'square' })
    .then(data => {
        setSearched(data.photos)
        console.log(data.photos)})
    .catch(error => console.log(error));
    }, [inputValue]);


    const searchPhotos = (event) => {
      event.preventDefault()
      const search = event.target.firstElementChild.value
      console.log(search)
      setinputValue(search)
    }

    const searchDefPhotos = (event) => {
      event.preventDefault()
      const searchDef = event.target.innerHTML
      console.log(searchDef)
      const searchDefl = searchDef.toLowerCase()
      setinputValue(searchDefl)
      console.log(inputValue)
    }

  return (
    <> 
      <Routes>
        <Route path='/mountain' element={<App/>}>
        {/* <Route path='/search/{x}' element={<App/>}></Route>   */}
        </Route>
        </Routes>

        
     
      <div className="App">
          <Mainpage searchPhotos={searchPhotos}/>
          <Buttons searchDefPhotos={searchDefPhotos}/>
          <Photossearch searched={searched}/>
      </div>   
      </>
  );
}

export default App;
