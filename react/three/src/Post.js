
function Post(props){
    let {name, title, id, removePost} = props;
    return(<div>
        <fieldset>
            <legend style={{fontWeight: 'bold'}}>{name}</legend>
            <p>{title}</p>
            <button onClick={() => removePost(id)}>Delete</button>
        </fieldset>
    </div>
    )  
}

export default Post;