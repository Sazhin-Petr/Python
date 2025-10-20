import "./Succes.css"

function Succes({count}){
    return(
        <div className="succes-block">
            <h3>Успешно</h3>
            <p>Всем <b>{count}</b> пользователям отправлено приглашение</p>
            {/* <a href="/">Назад</a> */}
            <button onClick={() => window.location.reload()} className='send-invite-btn'>Назад</button>
        </div>
    )
}

export default Succes;