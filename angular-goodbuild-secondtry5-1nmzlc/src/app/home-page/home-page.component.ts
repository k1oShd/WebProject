import { Component, OnInit } from "@angular/core";
import { categories } from "../categories";

@Component({
  selector: "app-home-page",
  templateUrl: "./home-page.component.html",
  styleUrls: ["./home-page.component.css"]
})
export class HomePageComponent implements OnInit {
  Clicked: boolean;
  isNameFull: boolean;
  searchBar: string;
  name: string;
  categories = categories;

  constructor() {
    // this.name = prompt("Enter your Name");
    // if (this.name.length != 0) {
    //   this.isNameFull = true;
    // } else {
    //   this.isNameFull = false;
    // }
  }

  swithcTheme(): void {
    this.Clicked = !this.Clicked;
    if (this.Clicked) {
      let body_ = document.getElementById("mainBody");
      body_.style.backgroundColor = "#1f1f1f";
      console.log("NIGTH MODE'S ON");
    } else {
      let body_ = document.getElementById("mainBody");
      body_.style.backgroundColor = "#ffffff";
      console.log("NIGTH MODE'S OFF");
    }
  }
  ngOnInit() {}
}
