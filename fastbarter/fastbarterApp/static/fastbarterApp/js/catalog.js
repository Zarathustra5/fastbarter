/*
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
*/

let products = document.querySelectorAll(".catalog-product");
products.forEach(el => {
    let favoriteBtn = el.querySelector(".catalog-product__favorite");
    if (favoriteBtn.classList.contains("catalog-product__favorite_active")) {
        let id = el.getAttribute("data-id");
        let removeFavoriteInput = el.querySelector("#remove-favorite");
        removeFavoriteInput.value = id;
    } else {
        let options = el.querySelectorAll("#id_catalog option");
        let title = el.querySelector(".catalog-product__title");
        options.forEach(option => {
            if (option.textContent == title.textContent) {
                option.selected = true;
            }
        });
    }
});

let popupFilters = document.querySelector(".popup-filters");
let filtersBtn = document.querySelector(".catalog-filter__btn");
if (filtersBtn) {
    filtersBtn.onclick = () => {
        popupFilters.classList.add("popup_active");
    }
}

// Поиск товара
const searchForm = document.querySelector("#form-search");
const searchInput = document.querySelector("#input-search");
if (searchForm && searchInput) {
    searchForm.onsubmit = e => {
        e.preventDefault();
    }
    searchInput.oninput = e => {
        const search = e.target.value;
        searchProduct(search);
    }
    const searchVal = searchInput.value;
    if (searchVal) searchProduct(searchVal);
}

function searchProduct(search) {
    const products = document.querySelectorAll(".catalog-product");
    products.forEach(product => {
        product.classList.add("catalog-product_hidden");
        const textFields = product.querySelectorAll(".catalog-product__search-text");
        textFields.forEach(field => {
            let fieldFormatted = field.textContent.toLowerCase();
            if (fieldFormatted.includes(search.toLowerCase())) {
                product.classList.remove("catalog-product_hidden");
            }
        });
    });
    if (history.pushState) {
        const baseUrl = window.location.protocol + "//" + window.location.host + window.location.pathname;
        const newUrl = baseUrl + '?s=' + search;
        history.pushState(null, null, newUrl);
    } else {
        console.warn('History API не поддерживается');
    }
}

// Сортировка товаров
const sortBtns = document.querySelectorAll(".catalog-sort__btn");
sortBtns.forEach(btn => {
    btn.onclick = () => {
        const active = "catalog-sort__btn_active";
        if (btn.classList.contains("catalog-sort__btn_default")) {
            if (!btn.classList.contains(active)) {
                window.location.reload();
                // const sortBtnPrice = document.querySelector(".catalog-sort__btn_price");
                // sortBtnPrice.classList.remove(active);
                // sortBtnPrice.classList.remove(active+"-cheap");
                // sortBtnPrice.classList.remove(active+"-expensive");
                // btn.classList.add(active);
            }
        } else {
            const sortBtnDef = document.querySelector(".catalog-sort__btn_default");
            sortBtnDef.classList.remove(active);
            btn.classList.add(active);
            if (!btn.classList.contains(active+"-cheap")) {
                btn.classList.remove(active+"-expensive");
                btn.classList.add(active+"-cheap");
                sortProducts(true);
            } else {
                btn.classList.remove(active+"-cheap");
                btn.classList.add(active+"-expensive");
                sortProducts(false);
            }
        }
    }
});

function sortProducts(isCheap) {
    const sortedProducts = $(".catalog-product").toArray().sort(function(a, b){
        const aVal = parseInt(a.getAttribute("data-price").replace(/\s/g, '')),
            bVal = parseInt(b.getAttribute("data-price").replace(/\s/g, ''));
        if (isCheap) {
            return aVal - bVal;
        } else {
            return bVal - aVal;
        }
    })
    sortedProducts.forEach(product => {
        $(".catalog__products").append(product);
    });
}

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

let filterBtns = document.querySelectorAll(".popup-filters-categories__icon-block");
filterBtns.forEach(el => {
  el.onclick = () => {
	let categoryIcon = el.querySelector(".category-icon");
    categoryIcon.classList.toggle("category-icon_active");
	let options = document.querySelectorAll(".popup-filters__categories-select option");
	options.forEach(option => {
		if (el.getAttribute("data-id") == option.value) {
			if (categoryIcon.classList.contains("category-icon_active")) {
				option.selected = true;
			} else {
				option.selected = false;
			}
		}
	});
  }
});
