"use strict";

let purchase = +prompt('Введите стоимость покупки');
let discount = 0;
if(purchase > 500 && purchase < 1000) {
     discount = 3; 
} else if (purchase > 1000) {
    discount = 5; 
}
let total = purchase - (purchase * discount / 100)
alert('Стоимость покупки без скидки:' + purchase + 'руб' + '\nСкидка:' + discount + '%' + '\nИтоговая стоимость:' + total + 'руб' )