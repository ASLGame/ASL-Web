import { FormEvent, useState } from "react";
import { useAppSelector } from "../../../../../../app/hooks";
import { selectUser } from "../../../../../signin/signinSlice";
import styles from "./editProfile.module.css";
import { ButtonProfile } from "../../../../../../components/Button.styled"

export function EditProfile() {
  const user = useAppSelector(selectUser);
  const username = user?.account_username;
  const email = user?.account_email;
  const [firstname, setFirstname] = useState(user!.account_firstname);
  const [lastname, setLastname] = useState(user!.account_lastname);
  const [dob, setDob] = useState(new Date(user?.account_dob!).toISOString().split('T')[0]);
  
  const onSubmit = (e: FormEvent) => {
      e.preventDefault();
  }

  return (
    <div className={styles.container}>
      <form className={styles.form} onSubmit={onSubmit}>
        <label className={styles.label}>First Name</label>
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
          type="date"
          id="dob"
          name="dob"
          value={dob}
          onChange={(e) => setDob(e.target.value)}
        />
        <label className={styles.label}>Username</label>
        <input
          className={styles.input}
          type="text"
          id="username"
          name="username"
          value={username}
          disabled
        />
        <label className={styles.label}>Email</label>
        <input
          className={styles.input}
          type="email"
          id="email"
          name="email"
            value={email}
          disabled
        />
        <ButtonProfile onClick={() => console.log("Submit")}>Save Changes</ButtonProfile>
      </form>
      <ButtonProfile onClick={() => console.log("Submit")}>Change Password</ButtonProfile>
    </div>
  );
}
