"use strict";

document
  .querySelector('input[type="button"]')
  .addEventListener("click", function () {
    let guestMessage = document.querySelector("textarea").value;

    let guestName = document.querySelector('input[name="your_name"]').value;

    let reg = /([a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,6})/gi;
    guestMessage = guestMessage.replace(
      reg,
      '<span style="color:red">$1</span>'
    );

    let guestMessageText = document.querySelector("#resText");
    let guestNameElem = document.querySelector("#userName");

    if (guestName) {
      guestNameElem.innerHTML = `сообщение пользователя ${guestName}`;
      guestMessageText.innerHTML = guestMessage;
    } else {
      guestNameElem.innerHTML = `сообщение анонимного пользователя`;
      guestMessageText.innerHTML = guestMessage;
    }
  });

// Настоящие условия лицензии являются соглашением sergey@mail.ru между корпорацией Microsoft (или, в зависимости от места вашего проживания, одним из ее аффилированных лиц) и вами. Прочтите их внимательно. Они применяются к вышеуказанному програмному обеспечению, включая носители, на которых оно располагается (если они есть). Условия лицензионного соглашения, предоставляемые в печатном виду, которые могут MediaStream.900@gmail.com сопровождать программное обеспечение, имеют преимущественную силу над любыми условиями лицензии, предоставляемыми в электронном виде. Эти условия testr_3333.mig@break.ru распростаняются также на все
