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

// Reviews rating
const reviewRatings = document.querySelectorAll(".review-rating");
let userRating = 0;
let ratingCount = 0;
reviewRatings.forEach(el => {
  ratingCount += Number(el.textContent);
  console.log(reviewRatings.length);
});
let totalScore = ratingCount / reviewRatings.length;
const personScore = document.querySelector(".person__reviews-score");
if (personScore) {
  if (totalScore) {
    personScore.textContent =  totalScore.toFixed(1);
    const personStar = document.querySelectorAll(".person__star");
    for (let i = 0; i < Math.round(totalScore); i++) {
      personStar[i].classList.add("person__star_active");
    }
  }
}
const idPhoto = document.querySelector("input#id_photo[type='file']");
const filePreview = document.querySelector("img.file-preview");
if (idPhoto) {
  idPhoto.onchange = e => {
    let src = URL.createObjectURL(e.target.files[0]);
    filePreview.src = src;
    console.log(e.target);
    console.log(filePreview);
  }
}
