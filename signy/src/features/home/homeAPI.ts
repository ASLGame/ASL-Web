const url = "http://localhost:8000/signy/";

export async function newestGame() {
  const response = await fetch(url + "game/newest-game", {
    method: "GET",
  });
  if (response.ok) {
    return response.json();
  } else {
    return response;
  }
}

export async function featuredGames() {
  const response = await fetch(url + "game/featured-games", {
    method: "GET",
  });
  if (response.ok) {
    return response.json();
  } else {
    return response;
  }
}
