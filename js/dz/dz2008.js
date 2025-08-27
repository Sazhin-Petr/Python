"use strict";

document.querySelectorAll("span").forEach((span) => {
  span.addEventListener("click", function () {
    this.parentNode.remove(); // пришлось "гуглить" по другому никак не получалось
    // let removeText = document.querySelector(".remove-button").parentNode; // удаляет по очереди, а не нажатую кнопку
    // removeText.remove();
  });
});
