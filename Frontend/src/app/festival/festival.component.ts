import {Component, OnInit} from '@angular/core';
import {Festival} from "../models/festival.model";
import {FestivalService} from "../services/festival.service";
import {ActivatedRoute} from "@angular/router";
import {NgForOf, NgIf} from "@angular/common";
import {Artist} from "../models/artist.model";

@Component({
  selector: 'app-festival',
  standalone: true,
  imports: [
    NgIf,
    NgForOf
  ],
  templateUrl: './festival.component.html',
  styleUrl: './festival.component.css'
})
export class FestivalComponent implements OnInit {

  festival: Festival | undefined;
  artists: Artist[] | undefined;
  date: string | undefined;

  constructor(
    private festivalService: FestivalService,
    private route: ActivatedRoute,
  ) {}

  async ngOnInit() {
    const id: string = this.route.snapshot.params["id"];
    const res = await this.festivalService.getFestivalById(id);
    this.festival = res.festival;
    this.artists = res.artists;
    console.log(this.festival)
    this.date = this.formatDate(this.festival.date)
  }

  formatCurrency(value: number): string {
    return `${value} CHF`;
  }

  formatDate(date: Date | { startDate: Date; endDate: Date }): string {
    if ( date instanceof Date) {
      return new Date(date).toDateString();
    } else {
      return `${new Date(date.startDate).toDateString()} - ${new Date(date.endDate).toDateString()}`;
    }
  }

}
