/*
signinSlice.ts encompasses every action and reducer with respect to authorization. 
This means that both signin and signup methods will be found here.
*/
import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { RootState, AppThunk } from '../../app/store';
import { signup } from '../signup/signupAPI';
import { signin } from "./signinAPI";

interface User {
    access_token?: string,
    account_email?: string,
    account_firstname?: string,
    account_id?: number,
    account_role?: string,
    account_username?: string,
    account_created?: string
}

export interface SignInState {
    user: User | undefined; //object
    isAuth: true | false
}

export interface AuthError {
    message: string
}

const initialState: SignInState = {
    user: undefined,
    isAuth: false,
}

export const signinAsync = createAsyncThunk(
    'authorization/signin',
    async (user: object) => {
        const response = await signin(user);
        return response;
    }
)

export const signupAsync = createAsyncThunk(
    'authorization/signup',
    async (user: object) => {
        const response = await signup(user);
        return response;
    }
)

export const signinSlice = createSlice({
    name: 'signin',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(signinAsync.rejected, (state, action) => {
            console.log(action.error);
        })
        builder.addCase(signinAsync.fulfilled, (state, action) => {
            state.user = action.payload;
            state.isAuth = true;
        })
        builder.addCase(signupAsync.rejected, (state, action) => {
            console.log(action.error);
        })
        builder.addCase(signupAsync.fulfilled, (state, action) => {
            state.user = action.payload;
            state.isAuth = true;
        })
    }
})

//Export actions
// export const { setCurrentUser } = signinSlice.actions;

//Selecter allows us to select a value of the state
export const selectSignIn = (state: RootState) => state.signin.isAuth;
export const selectUser = (state: RootState) => state.signin.user;

export default signinSlice.reducer;