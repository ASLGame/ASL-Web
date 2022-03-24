import * as tf from "@tensorflow/tfjs";
import { Hands } from "@mediapipe/hands";
import cam from "@mediapipe/camera_utils";
import { Models } from "../../types";

const myVideoElement: HTMLVideoElement | null =
  document.querySelector(".input_video2");

const myCanvasElement: HTMLCanvasElement | null =
  document.querySelector(".output_canvas2");

const myCanvasCtx: CanvasRenderingContext2D | null | undefined =
  myCanvasElement?.getContext("2d");

//--------------------------------------

export async function loadModel() {
  let result: Models = { R_Model: undefined, L_Model: undefined };
  result.R_Model = await tf.loadGraphModel("/rightModel.json");
  result.L_Model = await tf.loadGraphModel("/leftModel.json");

  return result;
}

// let R_model: tf.GraphModel;
// let L_model: tf.GraphModel;

// loadModel().then((result) => {
//   R_model = result.R_Model;
//   L_model = result.L_Model;
// });

export function calc_landmark_list(landmarks: any, width: number, height: number) {
  // const width: number | undefined = myCanvasElement?.width;
  // const height: number | undefined = myCanvasElement?.height;

  let landmark_points: any[] = [];

  landmarks.forEach((value: { x: number; y: number }) => {
    let landmark_x = Math.min(width - 1, value.x * width);
    let landmark_y = Math.min(height - 1, value.y * height);
    landmark_points.push(landmark_x);
    landmark_points.push(landmark_y);
  });
  //console.log('Calc_landmark', landmark_points);
  return landmark_points;
}

export function pre_process_landmarks(landmark_list: any[]) {
  let base_x;
  let base_y;

  for (let i = 0; i < landmark_list.length; i += 2) {
    if (i === 0) {
      base_x = landmark_list[i];
      base_y = landmark_list[i + 1];
    }

    landmark_list[i] = landmark_list[i] - base_x;
    landmark_list[i + 1] = landmark_list[i + 1] - base_y;
  }

  const maxValue = Math.max.apply(null, landmark_list.map(Math.abs));

  //console.log('maxValue', maxValue);
  function normalize(n: number) {
    return n / maxValue;
  }

  landmark_list = landmark_list.map(function (value) {
    return normalize(value);
  });

  //console.log('pre_process', landmark_list);
  console.log("");
  return landmark_list;
}

// //--------------------------------------

// export function NewonResults(result: any) {
//   const width: number = myCanvasElement?.width ?? 0;
//   const height: number = myCanvasElement?.height ?? 0;

//   myCanvasCtx?.save();
//   myCanvasCtx?.clearRect(0, 0, width, height);
//   myCanvasCtx?.drawImage(result.image, 0, 0, width, height);
//   //console.log(result);
//   if (result.multiHandLandmarks && result.multiHandedness) {
//     for (let index = 0; index < result.multiHandLandmarks.length; index++) {
//       const classification = result.multiHandedness[index];
//       const isRightHand = classification.label === "Right";
//       const landmarks = result.multiHandLandmarks[index];

      //Preprocess Landmarks
      // let landmark_list = calc_landmark_list(landmarks);
      // landmark_list = pre_process_landmarks(landmark_list);

      // //@ts-ignore
      // landmark_list = tf.tensor2d([landmark_list]);

      // let prediction;
      // if (isRightHand) {
      //   prediction = R_model?.predict(landmark_list);
      // } else {
      //   prediction = L_model?.predict(landmark_list);
      // }

      // const scores = prediction.arraySync()[0];

      // const maxScore = prediction.max().arraySync();
      // const maxScoreIndex = scores.indexOf(maxScore);

      // console.log(maxScoreIndex);

//       // eslint-disable-next-line
//       // @ts-ignore
//       drawConnectors(myCanvasCtx, landmarks, HAND_CONNECTIONS, {
//         color: "#00CC00",
//         lineWidth: 5,
//       });

//       // eslint-disable-next-line
//       // @ts-ignore
//       drawLandmarks(myCanvasCtx, landmarks, {
//         color: "#FF0000",
//         lineWidth: 2,
//       });
//     }
//   }
//   myCanvasCtx?.restore();
// }

// // eslint-disable-next-line @typescript-eslint/ban-ts-comment
// // @ts-ignore
// const hands: any = new Hands({
//   locateFile: (file: string) => {
//     return `https://cdn.jsdelivr.net/npm/@mediapipe/hands@0.1/${file}`;
//   },
// });

// hands?.setOptions({
//   selfieMode: true,
//   maxNumHands: 1,
//   minDetectionConfidence: 0.75,
//   minTrackingConfidence: 0.5,
// });

// hands.onResults(NewonResults);
