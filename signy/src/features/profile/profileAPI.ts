const url = "http://localhost:8000/"
export const getLatestPlayed = async (uid: number) => {
    const response = await fetch(url + `signy/scores/users/latest/${uid}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
        if (response.ok) {
            return response.json();
        } else { 
            return response
        }
    
  }