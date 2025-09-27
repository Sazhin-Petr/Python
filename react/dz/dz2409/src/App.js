import './App.css';
import Range from './Range';
import Header from './Header';


let head = 'Выберите размер квадрата:'

function App() {
  return (
    <div className="App">
    <Header head={head}/>
    <Range />
    </div>
  );
}

export default App;
