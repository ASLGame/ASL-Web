import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState, AppThunk } from '../../app/store';
import { login } from "./authorizationAPI";

export interface AuthorizationState {
    user: object;
    isAuth: true | false
}

const initialState: AuthorizationState = {
    user: {},
    isAuth: false,
}

export const loginAsync = createAsyncThunk(
    'authorization/login',
    async (user: object) => {
        const response = await login(user);
        return response;
    }
)

export const authorizationSlice = createSlice({
    name: 'authorization',
    initialState,
    reducers: {
        setCurrentUser: (state, action: PayloadAction<object>) => {
            state.user = action.payload
        }
    },
    extraReducers: (builder) => {
        builder.addCase(loginAsync.fulfilled, (state) => {
            state.isAuth = !state.isAuth;
        })
    }
})

//Export actions
export const { setCurrentUser } = authorizationSlice.actions;

//Selecter allows us to select a value of the state
export const selectAuth = (state: RootState) => state.authorization.isAuth;

export default authorizationSlice.reducer;