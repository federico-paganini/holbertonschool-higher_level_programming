const add_item_btn = document.getElementById("add_item");
add_item_btn.addEventListener("click", () => {
    const ul_list = document.querySelector(".my_list");
    const new_element = document.createElement("li");
    new_element.innerText = "Item";
    ul_list.appendChild(new_element);
})