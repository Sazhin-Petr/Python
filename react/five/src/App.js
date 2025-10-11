import "./App.css";
import { useState } from "react";
// import Counter from './Counter';
// import Person from './Person';
// import Modal from './Modal';
// import Item from './Item';
import Task from "./Task";
import Form from "./Form";

function App() {
  let [tasks, setTasks] = useState([
    {
      text: "Выучить JavaScript",
      done: false,
    },
    {
      text: "Познакомитсья с React",
      done: false,
    },
    {
      text: "Устроится на работу",
      done: false,
    },
  ]);
  let addTask = (text) => {
    let newTask = [...tasks, { text }];
    setTasks(newTask);
  };


  let acceptTask = (index) => {
    let newTask = [...tasks];
    newTask[index].done = false;
    setTasks(newTask);
  }


  let doneTask = (index) => {
    let newTask = [...tasks];
    newTask[index].done = !newTask[index].done;
    setTasks(newTask);
  };


  //Второй вариант
  //  let doneTask = (index) => {
  //   let newTask = [...tasks];
  //   newTask[index].done = !newTask[index].done;
  //   setTasks(newTask);
  // };

  let deleteTask = index =>{
    let newTask = [...tasks];
    newTask.splice(index, 1);
    setTasks(newTask);
  }

  return (

    
    <div className="App">
      <div className="task-list">
        {/* <Counter />
     <Person /> */}
        {/* <Modal /> */}
        {/* <Item /> */}
        {tasks.map((task, index) => (
          <Task key={index} 
          task={task}
          acceptTask={acceptTask} 
          doneTask={doneTask} 
          index={index}
          deleteTask={deleteTask} 
          />
        ))}
        <Form addTask={addTask} />
      </div>
    </div>
  );
}

export default App;
