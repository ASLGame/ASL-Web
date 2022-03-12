import { FunctionComponent } from "react";
import { useSelector } from "react-redux";
import { selectFeaturedGamesState } from "../../homeSlice";
import GameCarousel from "../GameCarousel/gameCarousel";
import styles from "./featuredGames.module.css";

interface FeaturedGamesProps {}

const FeaturedGames: FunctionComponent<FeaturedGamesProps> = () => {
  const featuredGamesState = useSelector(selectFeaturedGamesState);

  if (featuredGamesState !== "loading") {
    return (
      <div className={styles.container}>
        <h1 className={styles.title}>Featured Games</h1>
        <div className={styles.featuredGames}>
          <GameCarousel />
        </div>
      </div>
    );
  }
  return <p>Loading...</p>;
};

export default FeaturedGames;
