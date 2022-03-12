import { FunctionComponent } from "react";
import { useSelector } from "react-redux";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from "react-responsive-carousel";
import styles from "./gameCarousel.module.css";
import "./gameCarousel.css";
import { selectFeaturedGames } from "../../homeSlice";
import { Game } from "../../homeSlice";

interface GameCarouselProps {}

const GameCarousel: FunctionComponent<GameCarouselProps> = () => {
  const featuredGames = useSelector(selectFeaturedGames)!;

  const renderCarouselGames = (featuredGames: Array<Game>) => {
    return featuredGames.map((game) => {
      return (
        <div className={styles.imageContainer}>
          <img
            className={styles.image}
            src={game.gameAssets[0].path}
            alt="Whoops..."
          ></img>
          <div className={styles.middle}>
            <div className={styles.text}> {game.description} </div>
          </div>
        </div>
      );
    });
  };

  return (
    <div className={styles.carouselContainer}>
      <h2 className={styles.gameName}> Name of Game</h2>
      <Carousel
        className={styles.carousel && styles.carouselSlider}
        autoPlay={true}
        infiniteLoop={true}
        stopOnHover={true}
        showThumbs={false}
        showArrows={false}
      >
        {renderCarouselGames(featuredGames)}
        {/* <div className={styles.imageContainer}>
          <img
            className={styles.image}
            src="https://cdn.charlieintel.com/wp-content/uploads/2021/09/16034947/CoD-2023.jpg"
            alt="Whoops..."
          />
        </div>
        <div className={styles.imageContainer}>
          <img
            className={styles.image}
            src="https://cdn1.dotesports.com/wp-content/uploads/2020/04/02142718/GarenaWorld.png"
            alt="Whoops..."
          />
        </div>
        <div className={styles.imageContainer}>
          <img
            className={styles.image}
            src="https://images.livemint.com/img/2020/06/03/1600x900/Valorant_1591218052835_1591218061187.jpg"
            alt="Whoops..."
          />
        </div> */}
      </Carousel>
    </div>
  );
};

export default GameCarousel;
