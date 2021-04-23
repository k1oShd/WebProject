import { Component } from "@angular/core";
import { categories } from "./categories";
import { Router } from "@angular/router";
import { AuthenticationService } from "./service/authentication.service";
import { User } from "./models";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"]
})
export class AppComponent {
  title(title: any) {
    throw new Error("Method not implemented.");
  }
  currentUser: User;
  Clicked: boolean;
  isNameFull: boolean;
  searchBar: string;
  name: string;
  categories = categories;

  constructor(
    private router: Router,
    private authenticationService: AuthenticationService
  ) {
    // this.name = prompt("Enter your Name");
    // if (this.name.length != 0) {
    //   this.isNameFull = true;
    // } else {
    //   this.isNameFull = false;
    // }
    this.authenticationService.currentUser.subscribe(
      x => (this.currentUser = x)
    );
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

  logout() {
    this.authenticationService.logout();
    this.router.navigate(["/login"]);
  }
}

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
