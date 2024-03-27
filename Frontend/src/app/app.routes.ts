import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import {FestivalComponent} from "./festival/festival.component";

export const routes: Routes = [
  {path: "", component: HomeComponent},
  {path: "festival/:id", component: FestivalComponent}
];
