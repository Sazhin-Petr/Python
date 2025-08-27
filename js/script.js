"use strict";

/* let message;  // let, const, var
message = 'Hello'
console.log(message);

let a = 10;
a = 3.5;

let b, c;
let d = 5, e = 2;

let firstName = 'Irina';
console.log(firstName) */

// const week = 7;

// let str1 = "Двойные кавычки";
// let str2 = 'Одинарные кавычки'

// console.log(str1)
// console.log(str2)

// let str3 = `Обратные ${str1} и ${str2}
//  ка выч ки`;
// console.log(str3)

// let firstName = 'Ivan';
// alert(`Hello, ${firstName}`);

// let days = 365
// let planet = "Земля"
// let people = '7 млрд'
// let sun = 'Солнце'

// alert(`Мы живем на планете ${planet}, она делает один оборот вокруг ${sun} за ${days}. Население нашей планеты составляет примерно ${people} человек`)

// let res = confirm('Знаете ли вы HTML')
// console.log(res);  // ok=>  Отмена=>

// if(res){
//     alert('Пора учить JavaScript')
// } else{
//     alert('Нужно выучить')
// }

/* Типы данных 
-number
-string
-boolean
-null (object)
-underfined

-Object
*/

// let number = 13;
// console.log(number, typeof(number))

// let a = 23.56
// console.log(a, typeof(a));

// let b = 'Hello'
// console.log(b, typeof(b));

// let c = true
// console.log(c, typeof(c));

// let d = null;
// console.log(d, typeof(d));

// let e = undefined;
// console.log(d, typeof(e));

/* let res = prompt('Ваше имя:', 'Значение по умолчанию');
console.log(res);   */ // OK=> string, Отмена =>null

// let a = 12;
// let b = 8;
// console.log('+:',a + b);
// console.log('-:',a - b);
// console.log('*:', a * b);
// console.log('/:', a / b);
// console.log('%:', a % b);
// console.log('**:',a ** b);

// let a = '23';
// let b = '6';
// console.log(a + b);  // 23б

// let a = +prompt('Введите первое число', 5)
// let b = parseInt(prompt('Введите второе число', 3))
// // a = parseInt(a)
// // b = parseInt(b)
// alert('Результат:' + (a + b))

// console.log(parseInt('21.84'));  //21
// console.log(parseFloat('21.84'));  //21.84
// console.log(parseFloat('21.842354').toFixed(2));
// console.log(Number('21.84'));
// console.log(+'21.84');
// // console.log(+1*'21.84');
// console.log(+true)
// console.log(+false)

// let a = 0, b = 0;
// ++a;
// b++;
// console.log(a)
// console.log(b)

// let a = 0, b = 0;
// let c = a++ + 2;  //c = 0 + 2, a = 1
// let d = ++b + 2;  //b = 1, d = 1 + 2
// console.log(a)
// console.log(b)
// console.log(c)
// console.log(d)

// let a = 1;
// let b = a++; // b = 1, a = 2
// let c = b + 5 + a; // c = 1 + 5 + 2
// console.log(c)

// a ++ или a +=1

// let a = 1;
// let b = ++a; // a = 2, b = 2
// let c = b + 5 + a; // c = 2 + 5 + 2
// console.log(c)

// console.log(5 > 3);
// console.log(5 < 3);
// console.log(5 == '5');
// console.log(5 === '5');
// console.log(5 != '5');

// 7 < 3 ? alert('7') : alert('3')

// let ch = prompt('Угадайте число от 1 до 10');
// let num = 7;
// // (ch==num) ? alert('Угадали') : alert('Не угадали')
// (ch==num) ? alert('Угадали') :(ch<num) ? alert('Загаданное число больше') : alert('Загаданное число меньше');

// if (условие){
//     блок истина
// } else {
//     блок ложь
// }

/* 
false => 0, 0.0, '', false, null, undefined, NaN;
 */

// a = 52 - '5a'
// console.log(a);
// if (a){
//     console.log('TRUE');
// } else {
//     console.log('FALSE');
// }

// let a = +prompt('Введите первое число', 5);
// let b = +(prompt('Введите второе число', 0));

// if(b!=0)
//     alert(a/b); //infinity
// else
//     alert('На 0 делить нельзя')

// let a = 17;
// let b = 17;

// // if(a > b) {
// //     alert(a + '>' + b);
// // }
// // if(a < b) {
// //     alert(a + '<' + b);
// // }
// // if(a == b) {
// //     alert(a + ' == ' + b)
// // }

// if(a > b) {
//     alert(a + '>' + b);
// }
// else if(a < b) {
//     alert(a + '<' + b);
// }
// else {
//     alert(a + ' == ' + b)
// }

// if(a>b) {
//     alert(a + '>' + b);
// } else {
//     alert(a + '<' + b);
// }

// let login = prompt('Введите логин', 'admin');
// if(login){
//     if(login == 'admin'){
//         let psw = prompt('Введите пароль');
//         if(psw){
//             if(psw == 'password'){
//                 alert('Добро пожаловать');
//             } else {
//                 alert('Пароль неверен');
//             }
//         } else {
//             alert('Вход отменен')
//         }
//     } else {
//         alert('Я вас не знаю')
//     }

// } else{
//     alert('Вход отменен');
// }

// let a = 5;
// console.log(a);

// let a =1;
// if(a) {
//     let b = 5
// }

// console.log(b)

// if(5 == 5 && 5 > 2){
//     console.log('TRUE')
// } else {
//     console.log('FALSE')
// }

// console.log(!9); // 9 => !true => false
// console.log(!0);
// console.log(!!'Hello');
// console.log(!!'');

/* 
&& - and
|| - or */

// let age = prompt('Введите возраст');
// if (age > 17 && age < 70) {
//     alert('Вы можете получать права')
// } else {
//     alert('права не выдавать')
// }

// let age = prompt("Введите возраст");
// if (age < 18 || age > 69){
//      alert("Права не давать")
// } else{
//      alert("Вы можете получить права")
// }

// switch(условие){
//     case значение_1:
//         блок кода;
//         break;
//     case значение_n:
//         блок кода;
//         break;
//     default:
//         блок кода;
// }

// let a = +prompt('Введите число:');
// switch(a){
//     case 1:
//         alert('Код 1');
//         break;
//     case 2:
//         alert('Код 2');
//         break;
//     case 3:
//         alert('Код 3');
//         break;
//     default:
//         alert('Я таких значений не знаю');
//         break;
// }

// let a = +prompt('Введите результат "2 + 2": ');
// switch(a){
//     case 4:
//         alert('Верно');
//         break;
//     case 3:
//     case 5:
//         alert('Не верно');
//         break;
//     default:
//         alert('Я таких значений не знаю');
//         break;
// }

// let m = +prompt('Введите номер месяца');
// let n;
// switch(m){
//     case 1: n='Январь'; break
//     case 2: n='Февраль'; break
//     case 3: n='Март'; break
//     case 4: n='Апрель'; break
//     case 5: n='Май'; break
//     case 6: n='Июнь'; break
//     case 7: n='Июль'; break
//     case 8: n='август'; break
//     case 9: n='Сентябрь'; break
//     case 10: n='Октябрь'; break
//     case 11: n='Ноябрь'; break
//     case 12: n='Декабрь'; break
//     default: n='Неправильный номер месяца'
// }
// alert('Вы ввели: ' + n)

// document.writeln('тЕКСТ ВЫВЕДЕН В БРАУЗЕР');
// document.writeln('<p>тЕКСТ <b>ВЫВЕДЕН</b> В БРАУЗЕР</p>');
// document.writeln('<img src="103162_photo.jpg">')  //добавить картинку

// let i = 0
// do {
//     document.writeln('Это номер: '+ i + '<br>')
//     i++
// } while(i < 5);

// document.writeln('<br><br> Второй цикл');

// let j = 5;
// while (j <5) {
//     document.writeln('Это номер: '+ i + '<br>')
//     j++
// }

// let i = 1;
// do {
//     document.writeln('Квадрат: ' + i + 'равен' + i **2 + '<br>')
//     i++
// } while(i < 8);

// let ch, pr;
// do{
//     ch = prompt('Введите число', 10);
//     if (ch < 0){
//         break;
//     }
//     if(ch == 0){
//         continue;
//     }
//     pr *= ch
// }while(true);

// alert(pr);

// for(инициализация переменной; проверка условия; изменение счетчика){
//     тело цикла
// }

// for(let i = 1; i < 6; i++){
//     document.writeln(i + '<br>');
// }

// document.writeln('<br><br>Второй цикл: <br>');

// let j = 1;
// while (j < 6){
//     document.writeln(j + '<br>');
// }

// let i = 1;
// for(; ;){
//     if (i == 6) {
//         break;
//     }
//     document.writeln(i + '<br>');
//     i++
// }

// for(var i = 1; i < 6; i++){
//     document.writeln(i + '<br>');
// }

// document.writeln('i = ' + i +'<br>')

// for(let i = 0; i<4; i++){
//     document.writeln('+++ <br>');
//     for(let j=0; j<2;j++){s
//         document.writeln('-- <br>')
//     }
// }

// let tr = prompt('Введите колво строк');
// let td = prompt('Введите колво столбцов');
// let symbol = prompt('Введите символ');
// document.writeln('<table border="1">');
// for(let i=0; i < tr; i++){
//     document.writeln('<tr>');
//     for(let j=0; j < td; j++){
//         document.writeln('<td>' + symbol + '</td>');
//     }
//     document.writeln('</tr>');
// }
// document.writeln('</table>');

// document.writeln('<table border="1" width="260">');
// for(let i=1; i < 11; i++){
//     document.writeln('<tr align="center">');
//     for(let j=1; j < 11; j++){
//         if(i%2 == 0){
//         document.writeln('<td bgcolor="red">' + i * j + '</td>');
//         } else{
//             document.writeln('<td bgcolor="yellow">' + i * j + '</td>');
//         }
//     }
//     document.writeln('</tr>');
// }
// document.writeln('</table>');

// => Массив

// let arr1 = new Array(2,6,8);
// let arr2 = new Array(5);
// let arr3 = [1,3,7]
// let arr4 = [5]

// console.log(arr1);
// console.log(arr2);
// console.log(arr3);
// console.log(arr4);
// console.log(arr3.length);

// document.writeln(arr1);
// alert(arr1);

// let f = [1,2,3,4,5,6,7];
// console.log(f);
// console.log('Lenght: ', f.length);
// console.table(f);

// f.length = 3;
// console.log(f);
// console.log('Lenght: ', f.length);

// f.length = 7;
// console.log(f);
// console.log('Lenght: ', f.length);

// f.length = 0;
// console.log(f);
// console.log('Lenght: ', f.length);

// let arr = new Array(6);

// for(let i = 0; i < arr.length; i++){
//     arr[i] = prompt('Введите' + (i+1) + ' элемент массива:')
// }

// console.log(arr);

// for(let i = 0; i < arr.length; i++){
//     document.writeln(arr[i] + '<br>')
// }

// let arr = [2,6,7,'Игорь', 1.4, true];
// console.log(arr);

// let mas = [[2,1,1], [6,3,7], [8,5,6]];
// console.log(mas);
// console.table(mas);

// console.log(mas[1][2]);

// document.writeln(mas + '<br>');

// let question = ['На ноль делить можно?', 'Волга впадает в Каспийское море?', 'Атмосферное давление увеличивается с высотой?', '2х2 будет 8?', 'Дельфины - это рыбы?', 'Мадонна - это настоящее имя певицы?', 'Первая мировая началась 1 сент?'];

// let correct_answer = [false, true, false, false,false,false];

// let sum = 0;
// let res = new Array();

// for(let i = 0; i < question.length; i++){
//     let answer = confirm(question[i]);
//     if (answer == correct_answer[i]){
//         res[i] = 10
//         sum += res[i];
//     } else{
//         res[i] = 0;
//     }
// }

// console.log(res);
// console.log(sum);

// document.writeln('<table border="1" width="500">');

// document.writeln('<tr>')
// document.writeln('<th>Вопросы</th>')
// document.writeln('<th>Баллы</th>')
// document.writeln('</tr>')

// for(let i = 0; i < question.length; i++){
//     document.writeln('<tr>');
//     document.writeln('<td>' + question[i] + '</td>')
//     document.writeln('<td>' + res[i] + '</td>')
//     document.writeln('</tr>')
// }

// document.writeln('<tr>')
// document.writeln('<th>Итого</th>')
// document.writeln('<th>' + sum + '</th>')
// document.writeln('</tr>')

// document.writeln('</table>')

// let text1 = document.getElementById('text_1');
// console.log(text1);
// console.log(text1.textContent);

// text1.textContent = 'Новое содержимое <b>html разметкой</b';

// let text2 = document.getElementById('text_2');
// text2.innerHTML = 'Новое содержимое <b>html разметкой</b>'

// let res = +prompt('Выберите изображение', '1- собака, 2 - кот, 3 - птицаб 4 - рыба')
// document.writeln("<div id='image'></div>");
// let img = document.getElementById('image');

// switch(res){
//     case 1:
//         img.innerHTML = '<img src="">';
//         break;
//     case 2:
//         img.innerHTML = '<img src="">';
//         break;
//     case 3:
//         img.innerHTML = '<img src="">';
//         break;
//     case 4:
//         img.innerHTML = '<img src="">';
//         break;
//     default:
//         alert('Такого изображения нет')
// }

// let tag = document.getElementsByTagName('p')[2]
// console.log(tag);
// tag.innerHTML = 'Hello tag';
// tag.style.background = 'silver';
// tag.style.padding = '10px 20px';
// tag.style.color = 'blue';
// tag.style.fontWeight = 'bold';
// tag.id = 'test';
// tag.className = 'x';

// let q = document.getElementsByClassName('a');
// console.log(q);
// q[1].style.color = 'red';
// q[0].style.color = 'blue';

// document.querySelector(css);
// document.querySelectorAll(css);

// let select_class = document.querySelector('.a');
// let select_class = document.querySelectorAll('.a')[1];
// console.log(select_class);

// let select_tag = document.querySelector('p');
// let select_tag = document.querySelectorAll('p');
// console.log(select_tag);

// let select_id = document.querySelector('#text_1');
// let select_id = document.querySelectorAll('#text_1')[0];
// console.log(select_id);

// select_id.style.color = 'red'

// let el = document.querySelector('h2');
// el.style.color = 'red'

// let el1 = document.querySelectorAll('h2')[1];
// el1.style.color = 'purple'

// let lists = document.querySelectorAll('li');
// console.log(lists.length);
// for(let i=0; i <lists.length; i++){
//     lists[i].innerHTML += ' - фрукты';
// }

// let purples = document.querySelectorAll('.purple li')
// for(let i=0; i<purples.length; i++){
//     purples[i].innerHTML += ' !!!'
// }

// // let m = document.querySelectorAll('.red li')[1];
// let m = document.getElementsByClassName('red')[0].getElementsByTagName('li')[1];
// m.style.color = 'orange'

// document.writeln('<div id="divSample"></div>')
// let div = document.querySelector('#divSample')
// div.innerHTML = 'Дюбель - конструктивный элемент, который используется для укрепления винта ил предмета на стене, на потолке или на полу в помещении или под открытым небом в различных материалах (бетон, кирпич и прочее). Сам дюбель удерживается в конструкции при помощи сил трения. С некоторого времениэлементы связи'
// div.style.background='#f0f';
// div.style.color = '#99ffff';
// div.style.width = '50%';
// div.style.outline='10px dotted #000';

// div.className = 'resentFont';

// let res = document.querySelector('.resentFont');
// res.style.fontSize = '12pt';
// res.style.fontWeight = 'bold'
// res.style.textDecoration = 'line-through';

// let js = ['нужно', 'учить', 'JavaScript'];
// console.log(js);

// console.log(js.pop());  //убирает элемент с конца
// console.log(js);

// js.push('JavaScript', '!') //добавляет в конец
// console.log(js);

// console.log(js.shift());  //убирает с начала
// console.log(js);

// js.unshift('Почему', 'нужно')  //добавляет в начало
// console.log(js);

// let arr = js.slice(1,3);
// console.log(arr);
// console.log(js.slice(1));

// js.splice(0,1);
// console.log(js);

// js.splice(0, 2, 'Мы', 'изучаем');
// console.log(js);

// js.splice(2, 0, 'сложный', 'язык');
// console.log(js);

// js.splice(-2, 0, 'но','очень', 'интересный');
// console.log(js);

// let str = js.join('; ');
// console.log(str)

// let st = ['Фамилия', 'Имя', 'Отчество']
// let fio = new Array(3);

// for (let i = 0; i < fio.length; i++){
//     fio[i] = prompt('введите данные:\n' + st[i]);
// }

// alert(fio.join(' '));

// js.reverse();
// console.log(js);

// js.sort();
// console.log(js);

// let n = [1, 5, 15, 2];
// n.sort((a, b) => a - b);
// console.log(n);

//Функции
//Function Declaration

// function caption(a, b, c){
//     let res = a + b + c;
//     return res
// }

// let  test = caption(10, 20, 30);
// console.log(test);

// function showArrayContent(arrayToShow) {
//     if(arrayToShow.length == 1){
//         return arrayToShow
//     } else{
//         let last = arrayToShow.pop();
//         let str = arrayToShow.join(', ');
//         let res = str + ' и ' + last;
//         return res
//     }
// }

// let a = new Array('Текст');
// let b = new Array('день', 'ночь');
// let c = new Array('зима', 'весна', 'лето', 'осень')

// // alert(showArrayContent(a));
// alert(showArrayContent(b));
// alert(showArrayContent(c));

//Function Expression

// let sum1 = function(a, b){
//     return a + b;
// }

// alert(sum1(2, 3));

// alert(sum2(20, 30));

// function sum2 (a, b){
//     return a + b;
// }

// Immeditely Invoked Function Expression (IIFE) - самовызывающаяся функция (фнониманя)

// (function(){
//     alert('Привет мир');
// })();

// (function(n){
//     alert(n*n);
// })(4);

// function caption(a, b, c){
//     let res = a + b + c;
//     return res;
// }

// //Arrow Function

// // let test = (a, b, c) => a + b + c;
// let test = (a, b, c) => {
//     let res = a + b + c;
//     return res;
// };

// alert(test(10, 20, 30));

// let hello = () => alert('Hello');
// hello();

// let hello = (n) => alert('Hello ' + n);

// hello('Igor');

// document.writeln(Math.floor(7.9) + '<br>');
// document.writeln(Math.ceil(7.1) + '<br>');
// document.writeln(Math.round(7.1) + '<br>');

// (function(min, max){
//     document.writeln(Math.floor(Math.random() * (max - min) + min) + '<br>');
// })(0, 9);

// document.writeln(Math.floor(Math.random() * 9) + '<br>'); // от 0 до 9
// document.writeln(Math.floor(Math.random() * 7 + 2) + '<br>'); // от 2 до 9

// document.writeln(Math.floor(Math.random() * 7 + 7) + '<br>');

// let randMas = ['Цикл', 'Массив', 'Условие', 'Функция'];
// document.writeln(pickRandom(randMas));

// function pickRandom(mas){
//     return mas[Math.floor(Math.random() * mas.length)]
// };

// let j = 2;

// function ch(){
//     j = 1;
//     // console.log(j);
// }

// ch()
// console.log(j);

// document.writeln('<div id="block"></div')
// let id = document.getElementById('block');

// id.style.width = '100px';
// id.style.height = '100px';
// // id.style.background = 'rgb(255, 0, 0)';

// let createColor = () => {
//     let r = Math.floor(Math.random()*256);
//     let g = Math.floor(Math.random()*256);
//     let b = Math.floor(Math.random()*256);
//     // id.style.background = 'rgb('+ r +', '+ g +','+ b +')';
//     id.style.background = `rgb(${r}, ${g}, ${b})`
// }

// createColor();

// function test(a, b){
//     alert('a='+a+', b ='+b);
// }

// test(1);
// test(1, 2);

// function test(){
//     console.log(arguments[0]);
//     console.log(arguments[1]);
//     console.log(arguments[2]);
//     console.log(arguments[3]);
// }

// test(1, 2, 3);

// function sum(){
//     let res = 0;
//     for(let i=0; i < arguments.length; i++){
//         res += arguments[i];
//     }
//     return res;
// }

// document.writeln(sum() + '</br>')
// document.writeln(sum(1) + '</br>')
// document.writeln(sum(1,2) + '</br>')
// document.writeln(sum(1,2,3) + '</br>')
// document.writeln(sum(1,2,3,4) + '</br>')
// document.writeln(sum(1,2,3,4,5) + '</br>')

// function hello(name='незнакомец'){
//     // name = name || 'Незнакомец';
//     document.writeln('Привет, ' + name + '! <br>');
// }

// hello('Иван');
// hello();

// function squre(width=300, height=200, fon='green'){
//     document.writeln('<div id="shape"></div>')
//     let div = document.querySelector('#shape');

//     div.style.background = fon;
//     div.style.width = width + 'px';
//     div.style.height = height + 'px';
// }

// squre(50, 50, 'gold');
// squre(150, 100);
// squre();

// function hello(){
//     alert('Привет')
// }

// alert(hello)

// let str = "I\'m a JavaScript \"programmer\""
// document.writeln(str + '<br>');
// document.writeln(str.length + '<br>');
// document.writeln(str[2] + '<br>');

// // str[2] = 'y';
// str = str[2] + 'y';
// document.writeln(str + '<br>');

// let s = 'абббабввбабвбвббабвббабв'
// counterLetters(s);
// function counterLetters(str){
//     let letters = ['а', 'б', 'в'];
//     for(let i =0; i < letters.length; i++){
//         let count = 0;
//         for(let j=0; j<str.length; j++){
//             if(str[j] == letters[i]){
//                count++;
//             }
//         }
//         document.writeln('Символ "' + letters[i] + '" встретился ' + count + ' раз<br>');
//     }
// }

// let str = "I\'m a JavaScript \"programmer\""
// document.writeln(str[6] + '<br>');
// document.writeln(str.charAt(6) + '<br>');

// document.writeln(str.toLowerCase() + '<br>');
// document.writeln(str.toUpperCase() + '<br>');

// let n = prompt('Введите имя', 'никита')
// alert(first(n));

// function first(str){
//     let firsLetter = str.charAt(0).toUpperCase();
//     for(let i=1; i< str.length; i++){
//         firsLetter +=str[i].toLowerCase();
//     }
//     return firsLetter;
// }

// let str = "I\'m a Javascript \"programmer\"";
// let str1 = 'Я учу Javascript. Мне нравится Javascript';
// str = str.concat(str1);
// document.writeln(str + '<br>');

// // document.writeln(str.indexOf('Javascript', 7) + '<br');
// // document.writeln(str.lastIndexOf('Javascript') + '<br');

// // document.writeln(str.split('.') + '<br');
// // console.log(str.split('.', 2));

// document.writeln(str.slice(0,3) + '<br>');
// document.writeln(str.slice(-23,-10) + '<br>');
// document.writeln(str.substring(0,3) + '<br>');
// document.writeln(str.substring(3,0) + '<br>');
// document.writeln(str.substring(-10) + '<br>');

// let email;

// do{
//     email = prompt('Введите email:');
//     if(email.indexOf('@')==-1){
//         alert('Некорректно. Повторите операцию');
//         continue;
//     }
//     break;
// }while(true);

// alert('Спасибо за сотрудничество')

// let style = prompt('Введите свойство CSS', 'background-color');
// alert(replace(style));

// function replace(str){
//     let mas = str.split('-');
//     for(let i = 1; i < mas.length; i++){
//         mas[i] = mas[i].charAt(0).toUpperCase() + mas[i].slice(1);
//     }
//     return mas.join('');
// }

// События

// function loadStr(){
//     alert('Страница загружена');
// }

// let m = document.getElementById('mes');

// function over(){
//     m.style.color='red';
// }

// function out(){
//     m.style.color='yellow';
// }

// function change(){
//     let id = document.getElementById('title');
//     id.style.color='blue';
// }

// function randomBg(){
//     // document.body.style.background='rgb('+rand()+','+rand()+','+rand()+')';
//     document.body.style.background=`rgb(${rand()},${rand()},${rand()})`;
// }

// function rand(){
//     return Math.floor(Math.random()*256);
// }

// let image = document.getElementById('image');

// function on(){
//     image.src = 'night.png';
// }

// function off(){
//     image.src = 'day.png';
// }

// let but = document.getElementById('but');

// but.onclick = hello;

// function hello(){
//     alert('Спасибо');
// }

// function change(id){
//     id.innerHTML = 'Новый текст';
// }

// function setColor(elem){
//     document.body.style.background = elem.className;
// }

// let el = document.querySelector('#but');

// el.addEventListener('click', function(){
//     el.innerHTML='Новый текст';
// });

// el.addEventListener('contextmenu', function(){
//     el.style.color = 'green';
//     el.style.background = 'yellow';
// });

// document.addEventListener('mousemove', function
// (event){
//     let c = document.querySelector('#elem');
//     let x = event.clientX;
//     let y = event.clientY;
//     c.textContent = 'X =' + x + ', Y = ' + y;

//     c.addEventListener('dblclick', function
//     (event){
//         event.target.style.background='red';
//     })
// })

// let el = document.querySelector('#but');

// el.addEventListener('click', handler);

// function handler(){
//     alert('Спаибо');
//     el.removeEventListener('click', handler);
// }

// setTimeout(функция, задержка)

// setTimeout('alert("Текст")', 3000)

// setTimeout(hello, 1000, 'Привет', 'друг');
// setTimeout("hello('Привет', 'друг')", 4000);

// function hello(h, n){
//     alert(h + ', ' + n + '!');
// }

// document.writeln('<div id="dt">Создание анимированного текста</div>')

// let id = document.querySelector('#dt');

// let text = document.querySelector('#dt').innerHTML;

// let i = 0;

// window.addEventListener('load', animText);

// function animText(){

//     id.innerHTML = text.substring(0, i);
//     i++
//     if(i > text.length){
//         i = 0;
//     }
//     setTimeout(animText, 500);
// }

// let d = new Date();

// document.writeln(d + '<br>');
// document.writeln(d.toDateString() + '<br>');
// document.writeln(d.getFullYear() + '<br>');
// document.writeln(d.getMonth() + '<br>');
// document.writeln(d.getDate() + '<br>');
// document.writeln(d.getDay() + '<br>');

// Сегодня: 23 июля 2025 год, Среда

// let month = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']

// let day = ['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота']

// let d = new Date();
// let fullDate = 'Сегодня: ' + d.getDate() + ' ' + month[d.getMonth()] + ' ' + d.getFullYear() + '  год, ' + day[d.getDay()];

// document.writeln(fullDate);

// setInterval(функция, интервал)

// document.writeln('<input type="button" value="Start/Stop">');
// document.querySelector("input").addEventListener("click", startStop);

// let act,
//   run = false;
// function startStop() {
//   if (!run) {
//     act = setInterval(setColor, 1000);
//     run = true;
//   } else {
//     clearInterval(act);
//     run = false;
//   }
// }

// function setColor() {
//   let x = document.body;
//   x.style.background = x.style.background == "yellow" ? "orange" : "yellow";
// }

// document.writeln("<div id='text'>Здесь будет отображатсья текущее время</div>");

// window.addEventListener("load", () => setInterval(time, 1000));

// function time() {
//   let d = new Date();
//   let hour = d.getHours();
//   let min = d.getMinutes();
//   let sec = d.getSeconds();

//   if (min < 10) {
//     min = "0" + min;
//   }
//   if (sec < 10) {
//     sec = "0" + sec;
//   }

//   let times = hour + ":" + min + ":" + sec;
//   document.querySelector("#text").innerHTML = times;
// }

// let imgTime = [
//   "c0.gif",
//   "c1.gif",
//   "c2.gif",
//   "c3.gif",
//   "c4.gif",
//   "c5.gif",
//   "c6.gif",
//   "c7.gif",
//   "c8.gif",
//   "c9.gif",
// ];

// let t = document.querySelectorAll("#clock img");

// clock();

// function clock() {
//   let time = new Date();
//   let hours = time.getHours();
//   let mins = time.getMinutes();
//   let seconds = time.getSeconds();

//   getImg(hours, mins, seconds);
//   setTimeout(clock, 1000);
// }

// function getImg(h, m, s) {
//   t[0].src = imgTime[parseInt(h / 10)];
//   t[1].src = imgTime[h % 10];

//   t[3].src = imgTime[Math.floor(m / 10)];
//   t[4].src = imgTime[m % 10];

//   t[6].src = imgTime[Math.floor(s / 10)];
//   t[7].src = imgTime[s % 10];
// }

// document.writeln(`
//     <input type='text' size='4' id='timer' value='0.0'>
//     <input type='button' value='Start/Stop'>
//     <input type='button' value='Clear'>
//     `);

// document
//   .querySelector("input[value='Start/Stop']")
//   .addEventListener("click", startTimer);

// document
//   .querySelector("input[value='Clear']")
//   .addEventListener("click", resetTimer);

// let id, flag;
// function startTimer() {
//   if (!flag) {
//     id = setInterval(incTimer, 100);
//   } else {
//     clearInterval(id);
//   }
//   flag = !flag;
// }

// let tsec = 0;
// function incTimer() {
//   tsec++;
//   let t = tsec / 10.0;
//   if (tsec % 10 == 0) {
//     t += ".0";
//   }
//   document.getElementById("timer").value = t;
// }

// function resetTimer() {
//   document.getElementById("timer").value = "0.0";
//   tsec = 0;
// }

// let a = document.querySelector("#cl");
// a.addEventListener("click", myMove);

// function myMove() {
//   let elem = document.getElementById("animate");
//   let pos = 0;
//   let id = setInterval(frame, 5);

//   function frame() {
//     // a.style.display = "none";
//     // a.style.visibility = "hidden";
//     if (pos == 350) {
//       //   a.style.display = "block"
//       //   a.style.visibility = "visible";
//       a.addEventListener("click", myMove);
//       clearInterval(id);
//     } else {
//       a.removeEventListener("click", myMove);
//       pos++;
//       elem.style.top = pos + "px";
//       elem.style.left = pos + "px";
//     }
//   }
// }

// document.image.border = 1;
// document.writeln("<br>Ширина изображения: " + document.image.width + "<br>");
// document.writeln("<br>Высота изображения: " + document.image.height + "<br>");

// let array = new Array("2.jpg", "3.jpg", "4.jpg");
// document.writeln('<input type="button" value="<" name="left">');
// document.writeln("<img src='" + array[0] + "'>");
// document.writeln('<input type="button" value=">" name="right">');

// document.getElementsByName("right")[0].addEventListener("click", arrowRight);
// document.getElementsByName("left")[0].addEventListener("click", arrowLeft);

// let image = document.querySelector("img");

// let i = 0;

// function arrowRight() {
//   i++;
//   if (i == array.length) {
//     i = 0;
//   }
//   image.src = array[i];
// }

// function arrowLeft() {
//   i--;
//   if (i < 0) {
//     i = array.length - 1;
//   }
//   image.src = array[i];
// }

// для домашки
// let a = 5;
// let b = 10;
// let c;

// console.log("a=", a);
// console.log("b=", b);

// c = a; // 5
// a = b; //10
// b = c; // 5

// console.log("a=", a);
// console.log("b=", b);

// document.writeln('<input type="number" min="1" max="3">');
// document.writeln('<input type="button" class="btn" value="Кнопка">');

// let btn = document.querySelector(".btn");
// btn.addEventListener("click", function () {
//   let el = document.querySelector("input").value;
//   console.log(el);
// });

// alert(document.documentElement.innerHTML);
// alert(document.head.innerHTML);

// let myTitle = document.querySelector("h1").innerHTML;
// console.log(myTitle);

// let par = document.querySelector("p").firstChild.nodeValue;
// let par = document.querySelector("p").childNodes[0].nodeValue;
// let par = document.querySelector("p").nodeName;
// let par = document.querySelector("p").firstChild.nodeType;
// console.log(par);

// let elem = document.querySelector("#root");

// let tag = document.createElement("p"); //<p></p>
// let node = document.createTextNode("Новый текст");

// tag.append(node); //<p>Новый текст</p>

// elem.append(tag); // добавляет новый элемент последним дочерним элементом внутри родительского

// elem.prepend(tag); // добавляет новый элемент первым дочерним элементом внутри родительского

// elem.before(tag); // добавляет новый элемент до выбранного элемента

// elem.after(tag); // добавляет новый элемент после выбранного элемента

// elem.replaceWith(tag); // заменяет новым элементом выбранный элемент

// let list = document.querySelector("ul");

// let newItem = document.createElement("li");
// newItem.innerHTML = "Новый <i>элемент списка</i>";

// list.append(newItem);
//----------------------------
// document.querySelector("#move").addEventListener("click", change);
// document.querySelector("#add").addEventListener("click", add);
// let i = 1;

// function add() {
//   let elem = document.createElement("li");
//   elem.innerHTML = "Water " + i;
//   document.querySelector("#list2").append(elem);
//   // list2.append(elem);
//   i++;
// }

// function change() {
//   let elem = document.querySelector("#list2").lastChild;
//   document.querySelector("#list1").append(elem);
// }
//--------------------------------

// let div = document.querySelector("#root");
// div.insertAdjacentHTML("beforebegin", "<p>До выбранного элемента</p>");

// div.insertAdjacentHTML("afterend", "<p>После выбранного элемента</p>");
// div.insertAdjacentHTML(
//   "afterbegin",
//   "<p>Первый внутри выбранного элемента</p>"
// );
// div.insertAdjacentHTML(
//   "beforeend",
//   "<p>Последний внутри выбранного элемента</p>"
// );

// let first = document.querySelector("#p1");
// // first.remove();
// let second = document.querySelector("#p2");

// second.after(first);

//----------------------------------------

// let ul = document.querySelector("ul");
// let clone = ul.cloneNode(true);

// clone.querySelector("li").innerHTML = "Начало клонируемых элементов";

// ul.after(clone);
//-------------------------

// let list = document.querySelector(".list");

// list.insertAdjacentHTML("beforebegin", "<h2>Список </h2><hr>");

// let listInner = document.querySelector("h2");
// listInner.insertAdjacentText("beforeend", "планет");
// list.insertAdjacentHTML("afterend", "<hr>");

// let hr = document.querySelectorAll("hr")[1];
// let h4 = document.createElement("h4"); // <h4></h4>
// h4.innerHTML = "Конец списка"; // <h4>Конец списка</h4>
// hr.insertAdjacentElement("afterend", h4);

// let idRemove = setInterval(function () {
//   let li = document.querySelector(".list > li:last-child");
//   if (li === null) {
//     clearInterval(idRemove);
//     // alert("Список удален");
//     list.insertAdjacentHTML("afterbegin", "<li>Список удален</li>");
//   } else {
//     li.remove();
//   }
// }, 500);
//---------------------------------

// let div = document.querySelector("div");
// div.className = "alert";
// let activeDiv = document.querySelector(".active");
// activeDiv.classList.add("hidden"); // добавляет имя класса
// // activeDiv.classList.remove("hidden"); // удаляет имя класса
// activeDiv.classList.toggle("hidden"); //  если есть удаляет, если нет добавляет

// activeDiv.classList.replace("active", "alert"); // перезаписывает класс
//----------------------------------

// let frogImg = document.querySelector("#greenFrog");

// console.log(frogImg.id);
// console.log(frogImg.className);
// console.log(frogImg.alt);
// console.log(frogImg.title);
// console.log(frogImg.src);
// // console.log(frogImg.data-winter);

// frogImg.title = "Новый текст подсказки";
// console.log(frogImg.getAttribute("src"));
// console.log(frogImg.getAttribute("data-winter"));

// frogImg.setAttribute("src", "3.jpg");
// // frogImg.removeAttribute("src");

// console.log(frogImg.hasAttribute("src"));

//формы

// document.form1.style.background = "silver";
// document.forms[0].style.padding = "16px";
// document.forms["form1"].style.margin = "20px";
// document.forms.form1.style.border = "2px dotted gray";

// document.form1.name1.style.color = "blue";
// document.form1["name1"].style.background = "aqua";

// let but = document.querySelector("button");
// let txt = document.querySelector("#text1");

// but.addEventListener("click", content);
// function content() {
//   //   alert(txt.value);
//   console.log(txt.value);
// }

// ---------------------------------

// let input = document.querySelectorAll("input");
// let form1 = document.forms.form1;

// // console.log(input.length);
// // console.log(form1.length);

// for (let i = 0; i < form1.length; i++) {
//   input[i].addEventListener("click", checkAll);
// }

// let num;
// function checkAll() {
//   num = 0;
//   for (let i = 0; i < form1.length; i++) {
//     if (input[i].checked && input[i].type == "checkbox") {
//       num++;
//     }
//   }
//   if (num === 3) {
//     for (let i = 0; i < form1.length; i++) {
//       if (!input[i].checked && input[i].type == "checkbox") {
//         input[i].disabled = true;
//       }
//     }
//   } else {
//     for (let i = 0; i < form1.length; i++) {
//       input[i].disabled = false;
//     }
//   }
//   console.log(num);
// }

// let input = document.querySelectorAll("input[type='checkbox']");
// let form1 = document.forms.form1;

// console.log(input.length);
// console.log(form1.length);

// for (let i = 0; i < input.length; i++) {
//   input[i].addEventListener("click", checkAll);
// }

// let num;
// function checkAll() {
//   num = 0;
//   for (let i = 0; i < input.length; i++) {
//     if (input[i].checked) {
//       num++;
//     }
//   }
//   if (num === 3) {
//     for (let i = 0; i < input.length; i++) {
//       if (!input[i].checked) {
//         input[i].disabled = true;
//       }
//     }
//   } else {
//     for (let i = 0; i < input.length; i++) {
//       input[i].disabled = false;
//     }
//   }
//   console.log(num);
// }
// ---------------------------------

// let choose = document.querySelector('input[type="button"]');

// choose.addEventListener("click", chooseColor);

// function chooseColor() {
//   let f = document.form3.radio2;

//   console.log(f.length);
//   //   for (let i = 0; i < f.length; i++) {
//   //     if (f[i].checked) {
//   //       document.body.style.background = f[i].value;
//   //     }
//   //   }
//   document.body.style.background = f.value;
// }

// --------------------------

// Свойства для select

/*
select.option - коллекция из подэлементов <option> (масив)
select.value - значеие в данный момент <option>
select.selectedIndex - номер выбранного <option> (индекс)
*/

// let city = document.querySelector("#city");

// city.addEventListener("change", setImage);

// function setImage() {
//   let cities = city.selectedIndex;
//   //   console.log(cities);
//   let options = city.options;
//   //   console.log(options);
//   let code = options[cities].value;
//   //   console.log(code);
//   let div = document.querySelector("#image");
//   div.innerHTML = '<img src="img/' + code + '.png">';
// }

// -----------------------------

// let gas = document.querySelectorAll(".petrol");

// for (let i = 0; i < gas.length; i++) {
//   gas[i].addEventListener("click", function () {
//     let gallons = document.querySelector(".gallons").value;
//     let amount = gas[i].getAttribute("data-price");
//     let res = gallons * amount;
//     let sum = document.querySelector(".sum");
//     sum.innerHTML = res;
//   });
// }

// --------------------------------

let reg = document.querySelector(".register");

reg.addEventListener("submit", function () {
  let login = reg.login.value;
  let psd1 = reg.password1.value;
  let psd2 = reg.password2.value;
  if (!(login && psd1 && psd2)) {
    alert("Все поля должны быть заполнены");
  }
  if (psd1 !== psd2) {
    alert("Пароли не совпадают");
  }
  if (psd1.length < 6) {
    alert("Слишком короткий пароль");
  }
});
