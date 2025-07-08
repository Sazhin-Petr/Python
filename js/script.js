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

let res = confirm('Знаете ли вы HTML')
console.log(res);  // ok=>  Отмена=>

if(res){
    alert('Пора учить JavaScript')
} else{
    alert('Нужно выучить')
}