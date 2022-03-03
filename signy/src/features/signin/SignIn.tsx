import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useAppSelector, useAppDispatch } from "../../app/hooks";
import { signinAsync, setCurrentUser, selectSignIn } from "./signinSlice";
import styles from "./signin.module.css";
import {Button } from "../../components/Button.styled"

export function SignIn() {
  const auth = useAppSelector(selectSignIn);
  const dispatch = useAppDispatch();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div>
      <div className={styles.row}>
        <div className={styles.signinBox}>
          <h1 className={styles.h1}>Sign In</h1>
          <form className={styles.form}>
            <label className={styles.label}>Username</label>
            <input
              className={styles.input}
              type="text"
              id="username"
              name="username"
              onChange={(e) => setUsername(e.target.value)}
            />
            <label className={styles.label}>Password</label>
            <input
              className={styles.input}
              type="password"
              id="password"
              name="password"
              onChange={(e) => setPassword(e.target.value)}
            />
          </form>
          <div className={styles.link}>
            <a><Link to="/signup">Don't have an account? <br /> Sign Up</Link></a>
            <a><Link to="/forgotpassword">Forgot Password?</Link></a>
          </div>
          <div className={styles.button_container}>
            <Button onClick={() => console.log(username, password)}>Sign In</Button>
          </div>
        </div>
      </div>
    </div>
  );
}
