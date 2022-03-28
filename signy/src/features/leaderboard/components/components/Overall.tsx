import { Dictionary } from "@reduxjs/toolkit"
import { getscoresAsync } from "../../leaderboard.Slice";
import { useEffect, useState } from "react";
import { useAppDispatch } from "../../../../app/hooks"; 


export function Overall(){
    const dispatch = useAppDispatch();
    useEffect(() => {
        dispatch(getscoresAsync())
    }, [])

    return(
        <p></p>
    )
}