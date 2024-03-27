import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Festival } from '../models/festival.model';
import { lastValueFrom } from 'rxjs';
import {Artist} from "../models/artist.model";

@Injectable({
  providedIn: 'root'
})
export class FestivalService {

  private baseUrl = "http://localhost:5187"

  constructor(private http: HttpClient) { }

  getAllFestivals(): Promise<Festival[]> {
    const res = this.http.get<Festival[]>(`${this.baseUrl}/festival`)
    return lastValueFrom(res)
  }

  getFestivalById(id: string): Promise<{ "festival": Festival, "artists": Artist[] }> {
    const res = this.http.get<{ "festival": Festival, "artists": Artist[] }>(`${this.baseUrl}/festival/${id}`)
    return lastValueFrom(res);
  }

}
