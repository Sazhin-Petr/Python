"use strict";

let start = document.querySelector("#start");
let game = document.querySelector("#game");
let score = 0;
let time = document.querySelector("#time");
let isGameStarted = false;

start.addEventListener("click", startGame);
game.addEventListener("click", handleBoxClick);

function startGame() {
  isGameStarted = true;
  start.classList.add("hide");
  game.style.background = "#FFF";

  let interval = setInterval(function () {
    let t = time.textContent;
    if (t <= 0) {
      clearInterval(interval);
      endGame();
    } else {
      time.textContent = (t - 0.1).toFixed(1);
    }
  }, 100);

  renderBox();
}

function endGame() {
  isGameStarted = false;
  game.innerHTML = "";
  start.classList.remove("hide");
  game.style.background = "#8be8fb";
}

function getRandom(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

function renderBox() {
  game.innerHTML = "";
  let box = document.createElement("div");

  let boxSize = getRandom(30, 100);

  let gameSize = game.getBoundingClientRect();
  let maxTop = gameSize.height - boxSize;
  let maxLeft = gameSize.width - boxSize;

  box.style.width = box.style.height = boxSize + "px";
  box.style.background = "#000";
  box.style.position = "absolute";
  box.style.top = getRandom(0, maxTop) + "px";
  box.style.left = getRandom(0, maxLeft) + "px";
  box.style.cursor = "pointer";
  box.setAttribute("data-box", "true");

  game.insertAdjacentElement("afterbegin", box);
}

function handleBoxClick(event) {
  if (!isGameStarted) {
    return;
  }
  if (event.target.dataset.box) {
    score++;
    renderBox();
  }
}
