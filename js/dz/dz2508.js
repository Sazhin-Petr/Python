"use strict";

let riddle = document.querySelector('input[type="button"]');

riddle.addEventListener("click", riddleAnswer);

function riddleAnswer() {
  let answer = document.form.radio;

  for (let i = 0; i < answer.length; i++) {
    if (answer[i].checked) {
      alert(answer[i].value);
    }
  }
}
