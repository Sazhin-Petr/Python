"use strict";

document.getElementById("btn").addEventListener("click", function () {
  let firstInput = document.getElementById("input1").value - 1;
  let secondInput = document.getElementById("input2").value - 1;
  let images = document.querySelectorAll(".image");

  let swapInput = images[firstInput].src;
  images[firstInput].src = images[secondInput].src;
  images[secondInput].src = swapInput;
});
