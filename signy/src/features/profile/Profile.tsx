import { useAppDispatch, useAppSelector } from "../../app/hooks";
import styles from "./profile.module.css";
import { ProfilePicture } from "./components/profilePicture/ProfilePicture";
import { LastPlayed } from "./components/lastPlayed/LastPlayed";
import { useEffect, useState } from "react";
import { selectUser } from "../signin/signinSlice";
import { lastestPlayedAsync, selectLatestPlayed } from "./profileSlice";

export function Profile() {
  const dispatch = useAppDispatch();
  const user = useAppSelector(selectUser)!;
  const [profileImage, setProfileImage] = useState<string>("");
  const [imageActive, setImageActive] = useState<boolean>(false);

  useEffect(() => {
    dispatch(lastestPlayedAsync(user.account_id!))
}, [])

  return (
    <section className={styles.container}>
      <div className={styles.left}>
        <ProfilePicture
          profileImage={profileImage}
          setProfileImage={setProfileImage}
          imageActive={imageActive}
          setImageActive={setImageActive}
        />
        <div className={styles.user_info}>
          <p>{user.account_username}</p>
          <p>{user.account_email}</p>
          <p>Joined: {user.account_created}</p>
        </div>
        <p className={styles.last_played}>Last Played</p>
        <LastPlayed />
      </div>
      <div className={styles.right}></div>
    </section>
  );
}
