import {Routes, Route} from 'react-router-dom' 
import React, { useState } from 'react';
import Home from './Home';
import About from './About';
import Articles from './Articles';
import Layout from './components/Layout';
import './App.css';




function App() {

   const [items, setItems] = useState([
        { id: 1, name: 'Apple', checked: false },
        { id: 2, name: 'Banana', checked: false },
        { id: 3, name: 'Tea', checked: false },
        { id: 4, name: 'Coffee', checked: false }
    ]);

    const handleCheckboxChange = (id) => {
        setItems(items.map(item => 
            item.id === id ? { ...item, checked: !item.checked } : item
        ));
      };

  return (
    <div >
      
      <Routes>
        <Route path='/' element={<Layout />}>
        <Route index element={<Home items={items} onCheckboxChange={handleCheckboxChange}/>}/>
        <Route path='about' element={<About />}/>
        <Route path='articles' element={<Articles />}/>
        </Route>
      </Routes>
    </div>
  );
}

export default App;
