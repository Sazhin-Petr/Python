import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

let albumName = 'Encore'
let artistName = 'Eminem'
let releaseYear = '2004'
let songsList =   [
  '1:	«Curtains Up»',
  '2.	«Evil Deeds»',
  '3.	«Never Enough»',
  '4.	«Yellow Brick Road»',
  '5.	«Like Toy Soldiers»',
  '6.	«Mosh»',
  '7.	«Puke»',
  '8.	«My 1st Single»',
  '9.	«Paul»',
  '10.	«Rain Man»',
  '11.	«Big Weenie»',
  '12.	«Em Calls Paul»',
  '13.	«Just Lose It»',
  '14.	«Ass Like That»',
  '15.	«Spend Some Time»',
  '16.	«Mockingbird»',
  '17.	«Crazy in Love»',
  '18.	«One Shot 2 Shot»',
  '19.	«Final Thought»',
  '20.	«Encore/Curtains Down»'
]
;
let text = 'Copyright - 2025'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App albumName={albumName} artistName={artistName} releaseYear={releaseYear} songsList={songsList} text={text}/>
  </React.StrictMode>
);

