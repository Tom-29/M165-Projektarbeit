export interface Festival {
  id: string;
  name: string;
  country: string;
  genre: string;
  date: {
    startDate: Date;
    endDate: Date;
  } | Date;
  prices?: {
    name: string;
    amount: number;
  }[];
  ratings?: {
    stars: number;
    comment?: string;
    username: string;
  }[];
}
