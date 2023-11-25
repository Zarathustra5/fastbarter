let product = document.querySelector(".product");
let favoriteBtn = product.querySelector(".product__favorite");
if (favoriteBtn.classList.contains("product__favorite_active")) {
    let id = product.getAttribute("data-id");
    let removeFavoriteInput = product.querySelector("#remove-favorite");
    removeFavoriteInput.value = id;
}