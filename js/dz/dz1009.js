"use strict";

let form = document.form1;

let inputName = document.querySelector("[name='name']");
let inputPhone = document.querySelector("[name='phone']");

let message = {
  loading: "Загрузка",
  succes: "Спасибо! Скоро с вами свяжемся",
  failure: "Что-то пошло не так",
};

form.addEventListener("submit", (event) => {
  event.preventDefault();

  let nameValue = inputName.value.trim();
  let phoneValue = inputPhone.value.trim();

  if (!(/^[a-zA-Zа-яА-ЯёЁ\s]{2,}$/.test(nameValue))) {
    alert("Имя должно состоять из букв");
    return;
  }

  if (!(/^[\d\-\s]+$/.test(phoneValue))) {
    alert("Телефон должен содержать только цифры");
  }

  let msg = document.createElement("div");
  msg.textContent = message.loading;
  form.append(msg);

  let request = new XMLHttpRequest();
  request.open("POST", "server.php");

  let formData = new FormData(form);
  request.send(formData);

  request.addEventListener("load", function () {
    if (request.status == 200) {
      request.response;
      alert(message.succes);
    } else {
      msg.textContent = message.failure;
    }
    form.reset();
    setTimeout(() => msg.remove(), 500);
  });
});
