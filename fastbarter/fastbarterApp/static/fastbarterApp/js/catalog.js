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