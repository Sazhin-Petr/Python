function Info(props){
    let {albumName, artistName, releaseYear} = props
    return(
        <div>
        <h1 style={{background: 'red', padding: '20px 0', fontSize: '20px', color: 'black'}}>Наименование альбома : {albumName}</h1>
        <h1 style={{background: 'pink', padding: '20px 0', fontSize: '20px', color: 'black'}}>Исполнитель: {artistName}</h1>
        <h1 style={{background: 'black', padding: '20px 0', fontSize: '20px', color: 'white'}}>Год выпуска: {releaseYear}</h1>
        </div>
    )
}

export default Info