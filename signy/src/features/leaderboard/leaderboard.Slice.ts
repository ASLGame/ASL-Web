import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { getscores } from './leaderboardAPI';



export const getscoresAsync = createAsyncThunk(
    'getscores',
    async () => {
        const response = await getscores();
        return response;
    }
)

export const latestPlayedSlice = createSlice({
    name: "latestPlayed",
    //initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(getscoresAsync.rejected, (state, action) => {
            console.log(action.error)
        })
        builder.addCase(getscoresAsync.pending, (state, action) => {
            state.newlatestPlayed = "loading"
        })
        builder.addCase(getscoresAsync.fulfilled, (state, action) => {
            state.newlatestPlayed = "idle"
            state.latestPlayed = action.payload;
        })
    }
})