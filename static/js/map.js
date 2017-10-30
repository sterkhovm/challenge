$( document ).ready(function() {
ymaps.ready(init); // карта соберется после загрузки скрипта и элементов
var myMap; // заглобалим переменную карты чтобы можно было ею вертеть из любого места
function init () { // функция - собиралка карты и фигни
   myMap = new ymaps.Map("map", { // создаем и присваиваем глобальной переменной карту и суем её в див с id="map"
		// center: [55.755, 37.60], // ну тут центр
		center: [55.771651, 37.637434], // ну тут центр
		behaviors: ['default', 'scrollZoom'], // скроллинг колесом
		zoom: 15 // тут масштаб
   });
// myMap.behaviors.disable('drag');
myMap.behaviors.disable("scrollZoom");


// myPlacemark3 = new ymaps.Placemark([0.0,0.0], {//
// balloonContent: '<a href="#map1" class="underline">CHALLENGE на Маяковской</a>' }, {
// iconLayout: 'default#image',
//iconImageHref: '../img/icon2.png',
// iconImageSize: [91, 83],
// iconImageOffset: [-33, -80],
// });
// /* Добавляем метки на карту */
// myMap.geoObjects.add(myPlacemark3);


var myPlacemark5 = new ymaps.Placemark([55.771651, 37.637434], {
balloonContent: '' }, {
iconLayout: 'default#image',
iconImageHref: 'static/static/img/icon2.png',
iconImageSize: [91, 83],
iconImageOffset: [-33, -80]
});

/* Добавляем метки на карту */
myMap.geoObjects.add(myPlacemark5);


// myPlacemark1 = new ymaps.Placemark([55.76879028, 37.64888750], {
// balloonContent: '<a href="#map2" class="underline">CHALLENGE Красных воротах</a>' }, {
// iconLayout: 'default#image',
// iconImageHref: 'images/icon.png',
// iconImageSize: [91, 83],
// iconImageOffset: [-33, -80],
// });
// /* Добавляем метки на карту */
// myMap.geoObjects.add(myPlacemark1);


// myPlacemark4 = new ymaps.Placemark([55.73125728, 37.61276650], {
// balloonContent: '<a href="#map3" class="underline">CHALLENGE на Октябрьской</a>' }, {
// iconLayout: 'default#image',
// iconImageHref: 'images/icon.png',
// iconImageSize: [91, 83],
// iconImageOffset: [-33, -80],
// });
// /* Добавляем метки на карту */
// myMap.geoObjects.add(myPlacemark4);

// myPlacemark2 = new ymaps.Placemark([55.74243278, 37.65314550], {
// balloonContent: '<a href="#map4" class="underline">CHALLENGE на Таганской</a>' }, {
// iconLayout: 'default#image',
// iconImageHref: 'images/icon.png',
// iconImageSize: [91, 83],
// iconImageOffset: [-33, -80],
// });
// /* Добавляем метки на карту */
// myMap.geoObjects.add(myPlacemark2);

// myPlacemark3 = new ymaps.Placemark([59.93142676, 30.35517850], {
// balloonContent: 'м. Маяковская' }, {
// iconLayout: 'default#image',
// iconImageHref: 'images/icon.png',
// iconImageSize: [91, 83],
// iconImageOffset: [-45, -83],
// });
// /* Добавляем метки на карту */
// myMap.geoObjects.add(myPlacemark3);


myMap.controls // добавим всяких кнопок, в скобках их позиции в блоке
.add('zoomControl', { left: 5, top: 5 }) //Масштаб
.add('typeSelector'); //Список типов карты

}

});
