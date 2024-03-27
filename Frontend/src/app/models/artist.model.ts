import {Festival} from "./festival.model";

export interface Artist {
  id: number;
  name: string;
  age: number;
  festivals: Festival[];
}
