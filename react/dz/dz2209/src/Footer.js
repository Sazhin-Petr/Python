function Footer(props){
    let {text} = props
    return(
        <footer style={{fontSize: '20px', color: 'black'}}>
                <p>{text}</p>
            </footer>
    )
}

export default Footer