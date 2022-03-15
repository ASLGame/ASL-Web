const url = "http://localhost:8000/"
export const signin = async (user: object): Promise<object> => {
    let errorMessage;
    let userSignin = {};
    await fetch(url + "signy/accounts/signin", {
        method: "POST",
        body: JSON.stringify(user),
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((res) => res.json())
        .then((res) => {
            if (res.reason) {
                errorMessage = res.reason;
                throw new Error(errorMessage); //{reason: "error"}
            }
            userSignin = res;
            
        })
    return userSignin;
  }