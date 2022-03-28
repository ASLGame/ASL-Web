import styles from "./leaderboard.module.css"
import { ByGames } from "./components/GamesTable"

export function Leaderboard(){

    return(
        <div>
            <h1>Leaderboards</h1>
            <div className={styles.tables}>
                <ByGames />
            </div>
        </div>
        
    )
}