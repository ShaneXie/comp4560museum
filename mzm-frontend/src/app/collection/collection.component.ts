import { Component } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'collection',
  providers: [
  ],
  styles: [ require('./collection.style.scss') ],
  templateUrl: './collection.template.html'
})
export class Collection {
  public collectionName: string;

  constructor(
    private route: ActivatedRoute
  ){
    this.collectionName = "";
  }

  ngOnInit() {
    this.route.params
      .subscribe((params: Params) => {
        this.collectionName = params['collectionName'];
        console.log(this.collectionName);
      });

  }
}
