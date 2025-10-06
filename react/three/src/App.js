import './App.css';
import React from 'react';
// import Hello from './Hello';
// import Length from './Length';
// import Form from './Form';
// import Range from './Range';
// import Posts from './Posts';
import Test from './Test';
import User from './User';

class App extends React.Component{
  
  state = {
    posts: [
      {id: '1', name: 'JS Basis', title: 'Обучение базовым конструкциям JavaScript'},
      {id: '2', name: 'JS Advanced', title: 'Обучение расширенным возможностям JavaScript'},
      {id: '3', name: 'React JS', title: 'Обучение react JS'},
    ],
    show: false
  }

  removePost = (id) => {
    this.setState({posts: this.state.posts.filter(post => post.id !== id)})
  }

  componentDidMount(){
    console.log('component Did mount');
    
  }
  componentDidUpdate(){
    console.log('component Did updait');
  }

  render(){
    let {posts} = this.state;
    return(
      <div>
        <button onClick={() => this.setState({show: !this.state.show})}>User</button>
        {this.state.show ? <User />: null}
        <Test />

        {/* <Posts posts={posts} removePost={this.removePost}/> */}
        {/* <Hello />
        <Length />
        <Form />
        <Range /> */}
    </div>
    )
  }
}
    


export default App;
