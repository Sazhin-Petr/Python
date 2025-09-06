"use strict";

class Head {
  constructor(img, h3) {
    this.img = img;
    this.h3 = h3;
  }
  render(id) {
    let show = `
        <img src='${this.img}' alt=''>
        <h3>${this.h3}</h3>`;
    document.querySelector(`#${id}`).innerHTML = show;
  }
}

let img = "https://img.icons8.com/?size=80&id=gmGctCdTEI8a&format=png";

let head = new Head(
  img,
  "Работа 24 часа в сутки, 7 дней <br> в неделю, 365 дней в году"
);
head.render("head");

let img2 = "https://img.icons8.com/?size=80&id=pjcq35k2cwfi&format=png";

let head2 = new Head(img2, "Нет географических границ");
head2.render("head2");

let img3 = "https://img.icons8.com/?size=80&id=9LYMW17xyVmc&format=png";

let head3 = new Head(img3, "Нет географических границ");
head3.render("head3");

let img4 = "https://img.icons8.com/?size=80&id=NLqXgKZ561DD&format=png";

let head4 = new Head(img4, "Безопасность");
head4.render("head4");

let img5 = "https://img.icons8.com/?size=80&id=xXV7sfjta9gx&format=png";

let head5 = new Head(img5, "Сокращение расходов на аренду и персонал");
head5.render("head5");

let img6 = "https://img.icons8.com/?size=80&id=qkEdVpshnkGA&format=png";

let head6 = new Head(img6, "Партнерские отношения");
head6.render("head6");

let img7 = "https://img.icons8.com/?size=48&id=wacnMI8aYlii&format=png";

let head7 = new Head(img7, "Покупатель всегда на связи");
head7.render("head7");

let img8 = "https://img.icons8.com/?size=48&id=rGzqchvfQdtg&format=png";

let head8 = new Head(img8, "Комфортный выбор");
head8.render("head8");

let img9 = "https://img.icons8.com/?size=48&id=18749&format=png";

let head9 = new Head(img9, "Удобство оплаты");
head9.render("head9");
