import { configureStore, ThunkAction, Action, combineReducers, getDefaultMiddleware } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';
import signinReducer from "../features/signin/signinSlice";
import latestPlayedReducer from "../features/profile/profileSlice";
import { persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage';

const reducers = combineReducers({
  counter: counterReducer,
    signin: signinReducer,
  latestPlayed: latestPlayedReducer
})


const persistConfig={
  key: "root",
  storage,
}

const persistedReducer = persistReducer(persistConfig, reducers)

export const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware({
    serializableCheck: {
      ignoreActions: true,
    }
  })
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
