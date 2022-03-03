import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState, AppThunk } from '../../app/store';
import { signin } from "./signinAPI";

export interface SignInState {
    user: object;
    isAuth: true | false
}

const initialState: SignInState = {
    user: {},
    isAuth: false,
}

export const signinAsync = createAsyncThunk(
    'authorization/signin',
    async (user: object) => {
        const response = await signin(user);
        return response;
    }
)

export const signinSlice = createSlice({
    name: 'signin',
    initialState,
    reducers: {
        setCurrentUser: (state, action: PayloadAction<object>) => {
            state.user = action.payload
        }
    },
    extraReducers: (builder) => {
        builder.addCase(signinAsync.fulfilled, (state) => {
            state.isAuth = !state.isAuth;
        })
    }
})

//Export actions
export const { setCurrentUser } = signinSlice.actions;

//Selecter allows us to select a value of the state
export const selectSignIn = (state: RootState) => state.signin.isAuth;

export default signinSlice.reducer;