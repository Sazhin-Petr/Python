function List(props){
    let {songsList} = props;
    return(      
        <nav>
            <ul style={{background: 'red', fontSize: '20px', color: 'yellow'}}>
                {
                 songsList.map((song, index) => {
                    return <li key = {index}>
                        {song}
                    </li>
                 })               
                }
            </ul>
        </nav>
    )
}

export default List