const stars = document.querySelectorAll(".review-header__star");
stars.forEach(el => {
    el.onclick = e => {
        let count = 0;
        if (el.classList.contains("review-header__star_active")) {
            for (let star of stars) {
                star.classList.remove("review-header__star_active")
            }
        }
        for (let star of stars) {
            count++;
            star.classList.add("review-header__star_active")
            if (star == el) {
                break;
            }
        }
        const ratingInput = document.querySelector("#id_rating");
        ratingInput.value = count;
    }
});
