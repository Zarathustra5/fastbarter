//Бургер
let burger = document.querySelector(".header__burger");
let menu = document.querySelector(".menu");
if (burger) {
  burger.onclick = function(){
    burger.classList.toggle("burger_active");
    menu.classList.toggle("burger_active");
    document.body.classList.toggle("locked");
  }
}

//Swiper главной секции
const sMain = new Swiper('.main-swiper', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  spaceBetween: 20,
  centeredSlides: true,
  initialSlide: 1,
});
