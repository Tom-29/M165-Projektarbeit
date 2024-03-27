import {Component, OnInit} from '@angular/core';
import {Festival} from '../models/festival.model';
import {FestivalService} from '../services/festival.service';
import {NgForOf} from "@angular/common";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    NgForOf,
    RouterLink
  ],
  templateUrl: './home.component.html',
  styleUrls: ['home.component.css']
})
export class HomeComponent implements OnInit{

  festivals: Festival[] | undefined;

  constructor(private festivalService: FestivalService) {}

   async ngOnInit() {
    this.festivals = await this.festivalService.getAllFestivals();
  }

}
