import { useAppDispatch } from "../../app/hooks";
import styles from "./profile.module.css";
import { ProfilePicture } from "./components/profilePicture/ProfilePicture";
import { ChangeEvent, useState } from "react";

export function Profile() {
  const dispatch = useAppDispatch();
  const [profileImage, setProfileImage] = useState<string>("");
  const [imageActive, setImageActive] = useState<boolean>(false);

  return (
    <section className={styles.container}>
      <div className={styles.left}>
        <ProfilePicture
          profileImage={profileImage}
          setProfileImage={setProfileImage}
          imageActive={imageActive}
          setImageActive={setImageActive}
        />
      </div>
      <div className={styles.right}></div>
    </section>
  );
}
