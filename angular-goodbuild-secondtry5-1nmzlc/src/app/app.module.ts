import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { RouterModule, Routes } from "@angular/router";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { AppRoutingModule } from "./app.routing.module";

import { AppComponent } from "./app.component";
import { TopBarComponent } from "./top-bar/top-bar.component";
import { ProductListComponent } from "./product-list/product-list.component";
import { ProductIemComponent } from "./product-iem/product-iem.component";
import { ProductCategoryComponent } from "./product-category/product-category.component";
import { ShoppingCartComponent } from "./shopping-cart/shopping-cart.component";
import { ItemComponent } from "./item/item.component";
import { NotFoundComponent } from "./not-found/not-found.component";
import { ErrorInterceptor } from "./login-help/error.interceptor";
import { JwtInterceptor } from "./login-help/jwt.interceptor";
import { LoginComponent } from "./login/login.component";
import { fakeBackendProvider } from "./login-help/fake-backend";
import { HttpClientModule, HTTP_INTERCEPTORS } from "@angular/common/http";

@NgModule({
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule,
    RouterModule.forRoot([{ path: "", component: ProductListComponent }])
  ],
  declarations: [
    AppComponent,
    TopBarComponent,
    ProductListComponent,
    ProductIemComponent,
    ProductCategoryComponent,
    ShoppingCartComponent,
    ItemComponent,
    NotFoundComponent,
    LoginComponent
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

    // provider used to create fake backend
    fakeBackendProvider
  ],
  bootstrap: [AppComponent],
  exports: [RouterModule]
})
export class AppModule {}

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
