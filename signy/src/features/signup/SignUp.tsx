import React, { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./signup.module.css";
import { BackButton, Button } from "../../components/Button.styled";

export function SignUp() {
  const [formPhase, setFormPhase] = useState(false);
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [dob, setDob] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repassword, setRepassword] = useState("");

  let content;

  if (formPhase) {
    content = (
        <div className={styles.row}>
        <div className={styles.signupBoxv2}>
          <div className={styles.heading}>
            <BackButton onClick={() => setFormPhase(false)}>&#8249;</BackButton>
            <h1 className={styles.h1}>Sign Up</h1>
          </div>
          <form className={styles.form}>
            <label className={styles.label}>Username</label>
            <input
              className={styles.input}
              type="text"
              id="username"
              name="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <label className={styles.label}>Email</label>
            <input
              className={styles.input}
              type="email"
              id="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <label className={styles.label}>Password</label>
            <input
              className={styles.input}
              type="password"
              id="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <label className={styles.label}>Re-Enter Password</label>
            <input
              className={styles.input}
              type="password"
              id="repassword"
              name="repassword"
              value={repassword}
              onChange={(e) => setRepassword(e.target.value)}
            />
          </form>
          <div className={styles.link}>
            <a>
              <Link to="/signin">
                Already have an account? <br /> Sign In
              </Link>
            </a>
          </div>
          <div className={styles.button_container}>
            <Button onClick={() => console.log(firstname, lastname, username, password, dob, email, repassword)}>
              Sign Up
            </Button>
          </div>
        </div>
      </div>
    )
  } else {
      content = (
        <div className={styles.row}>
        <div className={styles.signupBox}>
          <div className={styles.heading}>
            <h1 className={styles.h1}>Sign Up</h1>
          </div>
          <form className={styles.form}>
            <label className={styles.label}>Firstname</label>
            <input
              className={styles.input}
              type="text"
              id="firstname"
              name="firstname"
              value={firstname}
              onChange={(e) => setFirstname(e.target.value)}
            />
            <label className={styles.label}>Last Name</label>
            <input
              className={styles.input}
              type="text"
              id="lastname"
              name="lastname"
              value={lastname}
              onChange={(e) => setLastname(e.target.value)}
            />
            <label className={styles.label}>Date of Birth</label>
            <input
              className={styles.input}
              type="text"
              id="dob"
              name="dob"
              value={dob}
              onChange={(e) => setDob(e.target.value)}
            />
          </form>
          <div className={styles.link}>
            <a>
              <Link to="/signin">
                Already have an account? <br /> Sign In
              </Link>
            </a>
          </div>
          <div className={styles.button_container}>
            <Button onClick={() => setFormPhase(true)}>
              Continue
            </Button>
          </div>
        </div>
      </div>
      )
  }
  return (
    <div>
      {content}
    </div>
  );
}
