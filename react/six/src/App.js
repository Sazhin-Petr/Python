import ImageGallery from "react-image-gallery";
import './App.css'
import data from './data.json'


function App(){
    const collections = data.collections

    return(
        <div className="App">
            <h1>Моя коллекция фотографий</h1>

        <div className="image-gallery-wrapper">
            {
                collections.map((obj, index) => (
                    <div className="collection">
                        <h2>{obj.name}</h2>
                        <ImageGallery items={obj.photos}/>;
                    </div>
                ))
            }
        </div>
        </div>
    )
}

export default App;