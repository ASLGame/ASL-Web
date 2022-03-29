const url = "http://localhost:8000/signy/";

export async function allGames() {
  const response = await fetch(url + "game", {
    method: "GET",
  });
  if (response.ok) {
    return response.json();
  } else {
    return response;
  }
}
