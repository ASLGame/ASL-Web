import { FunctionComponent, useRef, useEffect } from "react";
import { Models } from "../../types";
import styles from "./Camera.module.css";
import { Hands } from "@mediapipe/hands";
import Webcam from "react-webcam";
import * as Cam from "@mediapipe/camera_utils";
// import {drawConnectors} from '@mediapipe/drawing_utils/index';
// import { NewonResults } from './model';

// // eslint-disable-next-line
// // @ts-ignore

interface CameraProps {
  models: Models;
}

const Camera: FunctionComponent<CameraProps> = (props) => {
  const { R_Model, L_Model } = props.models;
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);
  let camera = null;

  // const onResults = NewonResults;

  // const videoWidth = webcamReference.current.video.videoWidth;
  // const videoHeight = webcamReference.current.video.videoHeight;

  useEffect(() => {
    const hands: Hands = new Hands({
      locateFile: (file: string) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/hands@0.1/${file}`;
      },
    });

    hands.setOptions({
      selfieMode: true,
      maxNumHands: 1,
      minDetectionConfidence: 0.75,
      minTrackingConfidence: 0.5,
    });

    hands.onResults(() => console.log("hiya"));

    if (
      //   webcamRef !== null &&
      typeof webcamRef.current !== "undefined" &&
      webcamRef.current !== null
    ) {
      //@ts-ignore
      camera = new Cam.Camera(webcamRef.current.video, {
        onFrame: async () => {
          //@ts-ignore
          await hands.send({ image: webcamRef.current.video });
        },
        width: 1280,
        height: 720,
      });
      camera.start();
    }
  }, []);

  return (
    <div className={styles.webcamContainer}>
      <Webcam
        className={styles.webcam}
        videoConstraints={{ facingMode: "user" }}
        audio={false}
        screenshotFormat="image/jpeg"
        mirrored={true}
        ref={webcamRef}
      ></Webcam>
      <canvas className="canvas" ref={canvasRef} />
    </div>
  );
};

export default Camera;
