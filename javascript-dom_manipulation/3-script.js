const toggle_button = document.getElementById("toggle_header");
toggle_button.addEventListener("click", () => {
    const header = document.querySelector("header");
    if (header.classList.contains("red")) {
        header.classList.remove("red");
        header.classList.add("blue");
    } else {
        header.classList.remove("blue");
        header.classList.add("red");
    }
});