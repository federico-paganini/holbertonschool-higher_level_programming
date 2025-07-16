const update_header = document.querySelector("#update_header");

update_header.addEventListener("click", () => {
    const header_element = document.querySelector("header");
    header_element.textContent = "New Header!!!"
});