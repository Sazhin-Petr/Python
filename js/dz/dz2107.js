"use strict";

let month = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь'];

function monthColor(){
    let r = Math.floor(Math.random()*256);
    let g = Math.floor(Math.random()*256);
    let b = Math.floor(Math.random()*256);
    let createColor = `rgb(${r}, ${g}, ${b})`
    return createColor
}

for(let i = 0; i < month.length; i++){
    document.writeln('<div>' + month[i] + '<br>');
    let id = document.querySelectorAll('div')[i];
    id.style.textAlign = 'center';
    id.style.background = monthColor();
    id.style.fontWeight = 'bold';
 }
 month[i]