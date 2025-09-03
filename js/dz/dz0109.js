"use strict";

function Worker(name, age, job) {
  this.name = name;
  this.age = age;
  this.job = job;

  this.who = function () {
    document.writeln(
      "Я <b>" +
        this.name +
        "</b> мне <b>" +
        this.age +
        "</b> лет. Я работаю <b>" +
        this.job +
        "ом.</b>" +
        "<br>"
    );
  };
}

let Dmitry = new Worker("Дмитрий", 26, "Дизайнер");
Dmitry.who();
let Stas = new Worker("Станислав", 29, "Программист");
Stas.who();
let Sergey = new Worker("Сергей", 35, "Менеджер");
Sergey.who();
