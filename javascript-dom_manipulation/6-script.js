fetch_name();

async function fetch_name() {
    const NAME_URL = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    const character_tag = document.querySelector("#character");
    try {
        const response = await fetch(NAME_URL);
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        const data = await response.json();

        character_tag.textContent = data.name;
    } catch (e) {
        console.error("Error: ", e);
    }
}