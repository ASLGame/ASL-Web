import React, { useState } from 'react';
import { useAppSelector, useAppDispatch } from '../../app/hooks';
import {
  loginAsync,
  setCurrentUser,
  selectAuth
} from "./authorizationSlice";

export function Authorization() {
  const auth = useAppSelector(selectAuth)
  const dispatch = useAppDispatch();

  return (
    <div>
      <div>
        <button
          onClick={() => dispatch(loginAsync({}))}
        >
          Set Auth
        </button>
      </div>
    </div>
  );
}
