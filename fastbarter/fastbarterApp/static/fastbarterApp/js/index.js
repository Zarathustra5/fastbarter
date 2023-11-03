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

  /* Accordion */
  function activateAccordions() {
    $('.accordion__header').on('click', function () {
      let accordion = $(this).parent();
      accordion.find(".accordion__body").first().slideToggle();
      accordion.toggleClass("accordion_active");
    });
  }
  activateAccordions();

window.addEventListener('scroll', reveal);
function reveal() {
    const reveals = document.querySelectorAll('.reveal');
    for (let i = 0; i < reveals.length; i++) {
        const windowHeight = window.innerHeight;
        const revealTop = reveals[i].getBoundingClientRect().top;
        const revealPoint = 75;
        if (revealTop < windowHeight - revealPoint) {
            reveals[i].classList.add('reveal_active');
        } else reveals[i].classList.remove('reveal_active');
    }
}