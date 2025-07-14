const tag_button = document.getElementById("red_header");
tag_button.addEventListener("click", () => {
    const header = document.querySelector("header");
    header.classList.add("red");
});