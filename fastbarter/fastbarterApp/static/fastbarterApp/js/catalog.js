let favoriteBtns = document.querySelectorAll(".catalog-product__favorite");
favoriteBtns.forEach(el => {
    el.onclick = () => {
        el.classList.toggle("catalog-product__favorite_active");
    }
});

let productFavoriteBtn = document.querySelector(".product__favorite");
if (productFavoriteBtn) {
    productFavoriteBtn.onclick = () => {
        productFavoriteBtn.classList.toggle("product__favorite_active");
    }
}

let popupFilters = document.querySelector(".popup-filters");
let filtersBtn = document.querySelector(".catalog-filter__btn");
filtersBtn.onclick = () => {
    popupFilters.classList.add("popup_active");
}

let submitFiltersBtn = document.querySelector(".popup-filters__submit");
submitFiltersBtn.onclick = () => {
    popupFilters.classList.remove("popup_active");
}