import React, { FunctionComponent, useEffect, useRef, useState } from "react";
import styles from "./game.module.css";
import { Button } from "../../components/Button.styled";
import ModelCamera from "../../components/ModelCamera/ModelCamera";
import { Alphabet } from "../../types/Models";

const Game: FunctionComponent = () => {
  const [time, setTime] = useState(0);
  const [isActive, setIsActive] = useState(false);
  let [isSpelledCorrectly, setIsSpelledCorrectly] = useState(false);
  const [buffer, setBuffer] = useState<String[]>([]);
  const [flag, setFlag] = useState(true);
  let [currentLetter, setCurrentLetter] = useState(
    //@ts-ignore
    Alphabet[Math.floor(Math.random() * 26)]
  );
  let [hasBufferEmptied, setHasBufferEmptied] = useState(false);
  let [blockCheckingFlag, setBlockCheckingFlag] = useState(false);
  const [lettersSpelled, setLettersSpelled] = useState<String[]>([]);

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

  const isLetterCorrect = () => {
    console.log('current letter', currentLetter);
    //console.log('isSpellcorrectly', isSpelledCorrectly);
    let appearanceOfLetter = 0;
    buffer.forEach((char) => {
      if (char === currentLetter) {
        appearanceOfLetter += 1;
      }
    });
    if (appearanceOfLetter / 20 > 0.8) {
      //setIsSpelledCorrectly(true);
      return true
    }
    //setIsSpelledCorrectly(false);
    return false;
  };

  const emptyBuffer = () => {
    setBuffer([]);
    setHasBufferEmptied(true);
  };

  const updateBuffer = (value: String) => {
    let bufferList = buffer;
    //console.log(isSpelledCorrectly);
    //console.log(blockCheckingFlag);
    if (buffer.length === 20 && !blockCheckingFlag) {
      
      // let temp = isLetterCorrect()
      // console.log(temp);
      // if(temp){
      //   setLettersSpelled([...lettersSpelled, currentLetter]);
      //   setBuffer([]);
      //   //@ts-ignore
      //   console.log('this letter', currentLetter);
        
      // }
      bufferList.shift();
      bufferList.push(value);
      setBuffer(bufferList);
      setFlag((prev)=>{return !prev})
      
    } else {
      bufferList.push(value);
      setBuffer(bufferList);
    }
    console.log(buffer);
  };

  useEffect(() => {
    console.log('useEffect ', currentLetter);
    if(isLetterCorrect()){
      setLettersSpelled([...lettersSpelled, currentLetter]);
      //@ts-ignore
      setCurrentLetter(() => {return Alphabet[Math.floor(Math.random() * 26)]});
      setBuffer((prev) => prev = []);
    }
  //   console.log('currentletter')
  //  if(isSpelledCorrectly) {
  //    //@ts-ignore
  //    setCurrentLetter(() => {return Alphabet[Math.floor(Math.random() * 26)]});
     
  //  }
  }, [flag]);

  return (
    <>
      <div className={styles.background + " " + styles.layer1}>
        <section className={styles.container}>
          <div className={styles.left}>
            <ModelCamera updateGameBuffer={updateBuffer}></ModelCamera>
            <div className={styles.word}>
              <h3>Your next letter is: {currentLetter}</h3>
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
              <button
                onClick={() => {
                  //@ts-ignore
                  setCurrentLetter(Alphabet[Math.floor(Math.random() * 26)]);
                }}
              >
                CLICK
              </button>
              <button
                onClick={() => {
                  //@ts-ignore
                  console.log(currentLetter);
                }}
              >
                CONSOLE
              </button>
            </div>
          </div>
        </section>
      </div>
    </>
  );
};
export default Game;
