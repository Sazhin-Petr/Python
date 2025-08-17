"use strict";

let image = document.getElementById("image");

document.addEventListener("DOMContentLoaded", function () {
  const showImage = document.getElementById("showImage");
  const hideImage = document.getElementById("hideImage");
  const image = document.getElementById("image");

  showImage.addEventListener("click", function () {
    image.style.display = "block";
  });

  hideImage.addEventListener("click", function () {
    image.style.display = "none";
  });
});
