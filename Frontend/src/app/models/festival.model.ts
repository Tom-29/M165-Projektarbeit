import {Artist} from "./artist.model";

export interface Festival {
  id: number;
  name: string;
  location: string;
  lineup: Artist[];
}
