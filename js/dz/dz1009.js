"use strict";

let form = document.form1;

let inputName = document.querySelector("[name='name']");
let inputPhone = document.querySelector("[name='phone']");

let message = {
  loading: "Загрузка данных",
  succes: "Спасибо! Скоро с вами свяжемся",
  failure: "Что-то пошло не так",
  incorrectName: "Имя должно состоять из букв!",
  incorrectPhone: "Телефон должен содержать только цифры!",
};

form.addEventListener("submit", (event) => {
  event.preventDefault();

  let nameValue = inputName.value.trim();
  let phoneValue = inputPhone.value.trim();

  function showMessage(text, duration = 2000) {
    let window = document.createElement("div");
    window.classList.add("window");
    window.innerHTML = text;
    document.body.appendChild(window);
    setTimeout(() => {
      if (window.parentNode) {
        window.remove();
      }
    }, duration);
    return window;
  }

  if (!/^[a-zA-Zа-яА-ЯёЁ\s]{2,}$/.test(nameValue)) {
    showMessage(message.incorrectName);
    return;
  }

  if (!/^[\d\-\s]+$/.test(phoneValue)) {
    showMessage(message.incorrectPhone);
    return;
  }

  let loadWind = showMessage(message.loading, 3000);

  setTimeout(() => {
    let request = new XMLHttpRequest();
    request.open("POST", "server.php");
    
    let formData = new FormData(form);
    request.send(formData);

    request.addEventListener("load", function () {

      if (loadWind.parentNode) {
        loadWind.remove();
      }
      
      if (request.status == 200) {
        showMessage(message.succes);
      } else {
        showMessage(message.failure);
      }
      
      form.reset();
    });

    request.addEventListener("error", function () {
      if (loadWind.parentNode) {
        loadWind.remove();
      }
      showMessage(message.failure);
    });

  }, 2000); 
});
