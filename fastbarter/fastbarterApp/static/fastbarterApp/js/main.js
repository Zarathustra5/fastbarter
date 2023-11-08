let popupAuth = document.querySelector(".popup-auth");
let closePopupBtn = document.querySelector(".popup__close");
closePopupBtn.onclick = () => {
    popupAuth.classList.remove("popup_active");
}

let popupAuthRadioBtn = document.querySelector(".popup-auth .popup-auth__header input#auth");
let popupAuthForm = document.querySelector(".popup-auth .popup-auth__form_auth");
let popupRegisterRadioBtn = document.querySelector(".popup-auth .popup-auth__header input#register");
let popupRegisterForm = document.querySelector(".popup-auth .popup-auth__form_register");
popupAuthRadioBtn.onclick = () => {
    popupAuthForm.classList.add("popup-auth__form_active");
    popupRegisterForm.classList.remove("popup-auth__form_active");
}
popupRegisterRadioBtn.onclick = () => {
    popupAuthForm.classList.remove("popup-auth__form_active");
    popupRegisterForm.classList.add("popup-auth__form_active");
}

let exitAccountBtn = document.querySelector(".account-user__exit");
exitAccountBtn.onclick = () => {
    popupAuth.classList.add("popup_active");
}