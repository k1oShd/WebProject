import { Component, OnInit } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { Product } from "../models";
import { products } from "../products";

@Component({
  selector: "app-item",
  templateUrl: "./item.component.html",
  styleUrls: ["./item.component.css"]
})
export class ItemComponent implements OnInit {
  product: Product;

  constructor(private route: ActivatedRoute) {
    const id = +this.route.snapshot.paramMap.get("id");
    // console.log(id);
    this.product = products.find(x => x.id === id);
    // console.log(this.product);
  }

  ngOnInit() {}
}
