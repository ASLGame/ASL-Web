import React, { FunctionComponent, useEffect, useRef, useState } from "react";
import styles from "./game.module.css";
import Webcam from "react-webcam";
import { Button } from "../../components/Button.styled";

interface GameProps {}

const Game: FunctionComponent<GameProps> = () => {
  const cameraRef = useRef(null);
  const [time, setTime] = useState(0);
  const [isActive, setIsActive] = useState(false);

  const renderLetters = (word: string) => {
    const arrLetter = word.split("");
    return (
      <>
        <table className={styles.letterTable}>
          <tbody>
            {arrLetter.map((letter) => {
              return (
                <>
                  <tr>
                    <td>{letter.toUpperCase()}</td>
                    <td className={styles.answerCell}> x</td>
                  </tr>
                </>
              );
            })}
          </tbody>
        </table>
      </>
    );
  };

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isActive) {
      interval = setInterval(() => {
        setTime((time) => parseFloat((time + 0.01).toFixed(2)));
      }, 10);
    } else if (!isActive && time !== 0) {
      clearInterval(time);
    }
    return () => clearInterval(interval);
  }, [isActive, time]);

  return (
    <>
      <div className={styles.background + " " + styles.layer1}>
        <section className={styles.container}>
          <div className={styles.left}>
            <h1 className={styles.title}> Spelling Hands</h1>
            <div className={styles.webcamContainer}>
              <p> {time} </p>
              <Webcam
                className={styles.webcam}
                videoConstraints={{ facingMode: "user" }}
                audio={false}
                screenshotFormat="image/jpeg"
                mirrored={true}
                ref={cameraRef}
              ></Webcam>
            </div>
            <div className={styles.word}>
              <h3>Your next word is: caca</h3>
            </div>
          </div>
          <div className={styles.right}>
            <div className={styles.gameboard}>
              <h1 className={styles.gameboardTitle}> Score </h1>
              <div className={styles.letters}>
                {renderLetters("wordsdsdas")}
              </div>
              <hr className={styles.divider}></hr>
              <table>
                <tbody>
                  <tr>
                    <td>Total</td>
                    <td className={styles.answerCell}> 20</td>
                  </tr>
                </tbody>
              </table>
              <Button
                style={{
                  width: "50%",
                  minWidth: "100px",
                  alignSelf: "center",
                  fontSize: "20px",
                  marginTop: "2%",
                }}
              >
                Next
              </Button>
            </div>
          </div>
        </section>
      </div>
    </>
  );
};
export default Game;
