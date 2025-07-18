"use strict";

document.writeln('<div id="demonstration"></div>')
let div = document.querySelector('#demonstration')
div.innerHTML = 'Термсотат - прибор для поддержания постоянной температуры. Поддержание температуры обеспечивается либо за счет использования терморегуляторов, либо осуществлением фазового перехода (например, таяние льда). Для уменьшения потерь тепла или холода термостаты, как правило, теплоизолируют. Но не всегда. Широко известныавтомобильные моторы, где летом нет никакой теплоизоляции и за счет действия восковых термостатов поддерживается постоянная температура. Другиим примером термостата, широко используемого в быту, является холодильник.'
div.style.background='yellow';
div.style.color = 'black';
div.style.width = '256px';
div.style.height = '256px';
div.style.overflow = 'scroll';
div.style.outline='1px dashed red';

div.className = 'resentFont';

let res = document.querySelector('.resentFont');
res.style.fontSize = '20pt';
res.style.fontWeight = '400'
res.style.textDecoration = 'underline';