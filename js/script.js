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
console.log(res);   */// OK=> string, Отмена =>null

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


let m = +prompt('Введите номер месяца');
let n;
switch(m){
    case 1: n='Январь'; break
    case 2: n='Февраль'; break
    case 3: n='Март'; break
    case 4: n='Апрель'; break
    case 5: n='Май'; break
    case 6: n='Июнь'; break
    case 7: n='Июль'; break
    case 8: n='август'; break
    case 9: n='Сентябрь'; break
    case 10: n='Октябрь'; break
    case 11: n='Ноябрь'; break
    case 12: n='Декабрь'; break
    default: n='Неправильный номер месяца'
}
alert('Вы ввели: ' + n)