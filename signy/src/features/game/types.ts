import { GraphModel } from "@tensorflow/tfjs";

export interface Models {
  L_Model: GraphModel | undefined;
  R_Model: GraphModel | undefined;
}
