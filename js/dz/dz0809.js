"use strict";

let inputRub = document.querySelector("#rub");
let inputUSD = document.querySelector("#usd");
let inputEUR = document.querySelector("#eur");

inputRub.addEventListener("input", () => {
  let request = new XMLHttpRequest();
  request.open("GET", "current.json");
  request.setRequestHeader("Content-type", "application/json; charset=utf8");
  request.send();

  request.addEventListener("load", () => {
    if (request.status == 200) {
      console.log(request.response);
      let data = JSON.parse(request.response);
      console.log(data);
      inputUSD.value = (inputRub.value / data.current.usd).toFixed(2);
      inputEUR.value = (inputRub.value / data.current.eur).toFixed(2);
    } else {
      inputUSD.value = "Что-то пошло не так";
      inputEUR.value = "Что-то пошло не так";
    }
  });
});
