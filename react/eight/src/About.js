import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function About(){
    let [posts, setPosts] = useState([]);

    useEffect(() =>{
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then(response => response.json())
            .then(data => setPosts(data))
    }, [])

    return(
        <div className='content'>
            <h2>About</h2>
            <ul style={{display: "block"}}>
                {
                    posts.map(post => (
                        <li key={post.id}>
                            <Link to={`/about/${post.id}`}>{post.title}</Link>
                                
                        </li>
                    ))
                }
            </ul>
        </div>
    )
}

export default About;