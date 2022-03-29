import { Dictionary } from "@reduxjs/toolkit";

const url = "http://localhost:8000/"

export const getscores = async () =>  {
    const response = await fetch(url + `signy/scores/highscores`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
    if (response.ok) {
        return response.json();
    } else { 
        return response;
    }
}