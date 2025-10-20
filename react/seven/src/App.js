import { useEffect, useState } from 'react';
import './App.css';
import Users from './components/users/Users';
import Succes from './components/succes/Succes';

function App() {
  const [users, setUsers] = useState([]);
  const [searchValue, setSearchValue] = useState('');
  const [invites, setInvites] = useState([]);
  const [succes, setSucces] = useState(false)

  useEffect(()=> {
    fetch('https://reqres.in/api/users', {
          headers: {
            'x-api-key': 'reqres-free-v1'
          }
        })
          .then(res => res.json())
          .then(json => {
            setUsers(json.data)
          })
  }, [])

  const onChangeValue = (event) => {
    setSearchValue(event.target.value);
  }

  const onClickInvite = (id) => {
    if(invites.includes(id)){
      setInvites(prev => prev.filter(ch => ch !== id))
    }else{
      setInvites(prev => [...prev, id]);
    }
  }

  const onClickSendInvites = () => {
    setSucces(true)
  }

  return (
    <div className="main">
      {
        succes ? <Succes count={invites.length}/> : 
     <Users 
     items={users}
     searchValue={searchValue}
     onChangeValue={onChangeValue}
     invites={invites}
     onClickInvite={onClickInvite}
     onClickSendInvites={onClickSendInvites}
     />}
    </div>
  );
}

export default App;
