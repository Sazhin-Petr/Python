import "./App.css";
import { useState } from "react";
import Task from "./Task";

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

  let acceptTask = (index) => {
    let newTask = [...tasks];
    newTask[index].done = false;
    setTasks(newTask);
  };

  let doneTask = (index) => {
    let newTask = [...tasks];
    newTask[index].done = true;
    setTasks(newTask);
  };

  //Второй вариант
  //  let doneTask = (index) => {
  //   let newTask = [...tasks];
  //   newTask[index].done = !newTask[index].done;
  //   setTasks(newTask);
  // };

  let deleteTask = (index) => {
    let newTask = [...tasks];
    newTask.splice(index, 1);
    setTasks(newTask);
  };

  return (
    <div className="App">
      <div className="task-list">
        {tasks.map((task, index) => (
          <Task
            key={index}
            task={task}
            acceptTask={acceptTask}
            doneTask={doneTask}
            index={index}
            deleteTask={deleteTask}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
