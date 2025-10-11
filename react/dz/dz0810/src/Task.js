function Task(props){
    let {task, acceptTask, doneTask, index, deleteTask} = props;

    return(
        <div className="task" style={{textDecoration: task.done ? 'line-through' : ""}}>
            {task.text}
            <div>
                <button onClick={() => acceptTask(index)}>Accept</button>
                <button onClick={() => doneTask(index)}>Done</button>
                <button onClick={() => deleteTask(index)}>X</button>
            </div>
        </div>
    )
}

export default Task;