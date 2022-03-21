import { User } from "../signin/signinSlice";
import { passwordChanges, userChanges } from "./components/tabMenu/components/editProfile/EditProfile";

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

export const updateUser = async (userData: userChanges) => {
    const response = await fetch(url + `signy/accounts/edit/profile/${userData.id}`, {
        method: "PUT",
        body: JSON.stringify(userData),
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

export const changePassword = async (userData: passwordChanges) => {
    const response = await fetch(url + `signy/accounts/edit/password/${userData.id}`, {
        method: "PUT",
        body: JSON.stringify(userData),
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