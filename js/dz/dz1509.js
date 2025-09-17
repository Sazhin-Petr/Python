"use strict";

document.querySelector("#load").addEventListener("click", loadUsers);

async function loadUsers() {
  let url = "https://jsonplaceholder.typicode.com/todos/";
  let response = await fetch(url);
  let data = await response.json();
  let html = data.map(function (item) {
    if (item.completed === true) {
      return (
        "<li>" +
        "Пользователь: " +
        item.userId +
        " выполнил задачу №" +
        " " +
        item.id +
        " " +
        " (" +
        item.title +
        ")" +
        "</li>"
      );
    }
  });
  document
    .querySelector("#list")
    .insertAdjacentHTML("afterbegin", html.join(" "));
}
