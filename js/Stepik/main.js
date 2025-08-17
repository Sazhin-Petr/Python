"use strict";

// let number = 5;

// number = 10;

// alert(number);

// const num = 100;
// console.log(num);

// const num1 = 23;
// console.log(Number.parseInt(num1)); // перевод строки в число без дробной части
// console.log(+num1); // перевод строки в число с дробной частью

// console.log(Number.MAX_VALUE);

//округление чисел

// console.log(24.23);

// console.log(Math.round(24.23));
// console.log(Math.ceil(24.23)); //округляет вверх
// console.log(Math.floor(24.23)); // округляет вниз
// console.log(Math.trunc(24.23)); // откидывает дробную часть

// const num2 = 24.2456;
// // console.log(Math.round(num2 * 100) / 100);

// console.log(num2.toFixed(2)); // переводит в строку

//  минимальные и максимальные значения

// console.log(Math.max(1, 2, -3));
// console.log(Math.min(1, 2, -3));
// console.log(Math.trunc(Math.random() * 10));
// let max = 101;
// let min = 100;
// console.log(Math.floor(Math.random() * (max - min) + min));

// строки

// const count = 5;
// console.log('У меня есть ' + count + ' яблок');
// console.log(`У меня есть ${count + 1} яблок`);

// const str = `
// привет
// пока.
// `;
// console.log(str);

// const num = 25.25;
// console.log(String(num));
// console.log(String(true));

// const str2 = "Привет, друг!";
// console.log(str2.length);

// console.log(str2[0]); // =  console.log(str.at(0));

// console.log(str2.toLocaleLowerCase());
// console.log(str2.toLocaleUpperCase());
// console.log(str2.trim());  // убираeт пробелы

// if else

// const lang = prompt("Какой у вас любимый яхык");
// if (lang === "javascript") {
//   console.log("Конечно");
// } else {
//   console.log("Вы уверены?");
// }

// const userName = prompt("Введите имя");
// if (userName === "павел") {
//   console.log("Здравствуйтеб админ");
// }

// const message = +prompt("сколько сообщений необх отправить");
// if (message) {
//   console.log(`отправляем сообщения в колве ${message}`);
// }

// const genre = prompt("Какой у вас любимый фильм");
// if (genre === "ужасы") {
//   console.log("Буу");
// } else if (genre === "комедии") {
//   console.log("Я тоже люблю смеяться");
// } else {
//   console.log("Ятаких жанров не знаю");
// }

// тернарный оператор

// const userRoll = "Админ";
// const accessAllowed = userRoll === "Админ" ? true : false;
// console.log(accessAllowed);
// if (accessAllowed) {
//   console.log("Доступ разрешен");
// } else {
//   console.log("Доступ запрещен");
// }

// const userRoll = "Админ";
// const accessAllowed = userRoll === "Админ" ? true : false;
// console.log(accessAllowed);
// accessAllowed ? console.log("Доступ разрешен") : console.log("Доступ запрещен");
