import { useAppDispatch } from "../../app/hooks";
import styles from "./profile.module.css";
import { ProfilePicture } from "./components/profilePicture/ProfilePicture";

export function Profile() {
    const dispatch = useAppDispatch();

    return (
        <section className={styles.container}>
            <div className={styles.left}>
                <ProfilePicture />
            </div>
            <div className={styles.right}>
            </div>
        </section>
    )
}
