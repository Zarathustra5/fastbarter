let popupAuth = document.querySelector(".popup-auth");
let closePopupBtns = document.querySelectorAll(".popup__close");
closePopupBtns.forEach(el => {
    el.onclick = () => {
        el.closest(".popup").classList.remove("popup_active");
    }
});

let popupAuthRadioBtn = document.querySelector(".popup-auth .popup-auth__header input#auth");
let popupAuthForm = document.querySelector(".popup-auth .popup-auth__form_auth");
let popupRegisterForm = document.querySelector(".popup-auth .popup-auth__form_register");
if (popupAuthRadioBtn) {
    popupAuthRadioBtn.onclick = () => {
        popupAuthForm.classList.add("popup-auth__form_active");
        popupRegisterForm.classList.remove("popup-auth__form_active");
    }
}
let popupRegisterRadioBtn = document.querySelector(".popup-auth .popup-auth__header input#register");
if (popupRegisterRadioBtn) {
    popupRegisterRadioBtn.onclick = () => {
        popupAuthForm.classList.remove("popup-auth__form_active");
        popupRegisterForm.classList.add("popup-auth__form_active");
    }
}

let exitAccountBtn = document.querySelector(".account-user__exit");
if (exitAccountBtn) {
    exitAccountBtn.onclick = () => {
        popupAuth.classList.add("popup_active");
    }
}

let popupDeals = document.querySelector(".popup-deals");
let productAboutBtn = document.querySelector(".product-about__btn");
if (productAboutBtn) {
    productAboutBtn.onclick = () => {
        popupDeals.classList.add("popup_active");
    }
}
