import { RouterModule } from "@angular/router";
import { NgModule } from "@angular/core";
import { ShoppingCartComponent } from "./shopping-cart/shopping-cart.component";
import { AppComponent } from "./app.component";
import { NotFoundComponent } from "./not-found/not-found.component";
import { ItemComponent } from "./item/item.component";
import { LoginComponent } from "./login/login.component";
import { AuthGuard } from "./login-help/auth.guard";

@NgModule({
  imports: [
    RouterModule.forRoot([
      { path: "shoppingCart", component: ShoppingCartComponent },
      { path: "home", component: AppComponent },
      { path: "items/:id", component: ItemComponent },
      { path: "login", component: LoginComponent },
      {
        path: "",
        redirectTo: "home",
        pathMatch: "full",
        canActivate: [AuthGuard]
      },
      { path: "**", component: NotFoundComponent }
    ])
  ],
  exports: [RouterModule],
  providers: []
})
export class AppRoutingModule {}
