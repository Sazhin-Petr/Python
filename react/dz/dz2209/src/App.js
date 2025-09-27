// import logo from './logo.png';
import './App.css';
import Header from './Header';
import Info from './Info';
import List from './List';
import Footer from './Footer';

function App(props) {
  let {albumName, artistName, releaseYear, songsList, text} = props
  return (
    <div className="App">
     <Header />
     <Info albumName={albumName} artistName={artistName} releaseYear={releaseYear} />
     <List songsList={songsList} />
     <Footer text={text} />
    </div>
  );
}

export default App;
