export interface Product {
  id: number;
  name: string;
  description: string;
  rating: number;
  link: string;
  img: string;
}

export interface Category {
  id: number;
  title: string;
}

export interface Manager {
  id: number;
  dep: string;
  name: string;
  salary: number;
  rating: number;
}

export class User {
  id: number;
  username: string;
  password: string;
  firstName: string;
  lastName: string;
  token?: string;
}
