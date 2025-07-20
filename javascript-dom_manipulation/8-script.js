document.addEventListener('DOMContentLoaded', () => {
  fetchHello();
});

async function fetchHello () {
  const NAME_URL = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const moviesList = document.querySelector('#hello');
  try {
    const response = await fetch(NAME_URL);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    const data = await response.json();
    moviesList.textContent = data.hello;
  } catch (e) {
    console.error('Error: ', e);
  }
}
