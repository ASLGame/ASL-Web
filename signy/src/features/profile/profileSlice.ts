import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { RootState } from '../../app/store';
import { getLatestPlayed } from './profileAPI';

export interface GameScore {
    date_achieved: string,
    name: string,
    score: number
}

export interface LastPlayed {
    latestPlayed: Array<GameScore> | undefined
    newlatestPlayed: string,
}

const initialState: LastPlayed = {
    latestPlayed: undefined,
    newlatestPlayed: "loading"
}

export const lastestPlayedAsync = createAsyncThunk(
    'latestPlayed',
    async (uid: number) => {
        const response = await getLatestPlayed(uid);
        return response;
    }
)

export const latestPlayedSlice = createSlice({
    name: "latestPlayed",
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(lastestPlayedAsync.rejected, (state, action) => {
            console.log(action.error)
        })
        builder.addCase(lastestPlayedAsync.pending, (state, action) => {
            state.newlatestPlayed = "loading"
        })
        builder.addCase(lastestPlayedAsync.fulfilled, (state, action) => {
            state.newlatestPlayed = "idle"
            state.latestPlayed = action.payload;
        })
    }
})

export const selectLatestPlayed = (state: RootState) => state.latestPlayed.latestPlayed;
export const selectNewLatestPlayed = (state: RootState) => state.latestPlayed.newlatestPlayed;
export default latestPlayedSlice.reducer;