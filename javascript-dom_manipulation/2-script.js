const tag_button = document.querySelector("#red_header");
tag_button.addEventListener("click", () => {
    const header = document.querySelector("header");
    header.classList.add("red");
});