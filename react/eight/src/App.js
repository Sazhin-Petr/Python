import {Routes, Route, Navigate} from 'react-router-dom' 
import { useState } from 'react';
import AboutInfo from './AboutInfo';
import Home from './Home';
import About from './About';
import Articles from './Articles';
import Layout from './components/Layout';
import './App.css';
import NotFoundPage from './NotFoundPage';




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
        <Route path='about/:id' element={<AboutInfo />}/>
        <Route path='articles' element={<Articles />}/>
        <Route path='articles-us' element={<Navigate to="/articles" replace/>}/>
        </Route>
        <Route path='*' element={<NotFoundPage />} />
      </Routes>
    </div>
  );
}

export default App;
