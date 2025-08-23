"use strict";

document.getElementById("btn").addEventListener("click", function () {
  let firstInput = document.getElementById("input1").value;
  let secondInput = document.getElementById("input2").value;
  let images = document.querySelectorAll(".image");

  let swapInput = images[firstInput].src;
  images[firstInput].src = images[secondInput].src;
  images[secondInput].src = swapInput;
});
