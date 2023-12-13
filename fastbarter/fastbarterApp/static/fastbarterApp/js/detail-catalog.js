let product = document.querySelector(".product");
let favoriteBtn = product.querySelector(".product__favorite");
if (favoriteBtn.classList.contains("product__favorite_active")) {
    let id = product.getAttribute("data-id");
    let removeFavoriteInput = product.querySelector("#remove-favorite");
    removeFavoriteInput.value = id;
}
const selectProduct = document.querySelector(".popup-deals__select-product");
if (selectProduct) {
  selectProduct.onchange = () => {
    const myProducts = document.querySelectorAll(".my-announcement-container .my-announcement");
    myProducts.forEach(el => {
      el.style.display = "none";
      if (selectProduct.value == el.getAttribute("data-id")) {
        el.style.display = "flex";
      }
    });
  }
}
