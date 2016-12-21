import { Component } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import 'rxjs/add/operator/switchMap';
import { DataService } from '../services/data.service'

@Component({
  selector: 'collection',
  providers: [
  ],
  styles: [ require('./collection.style.scss') ],
  templateUrl: './collection.template.html'
})
export class Collection {
  public collectionName: string;
  public collections: Array<any>;

  constructor(
    private route: ActivatedRoute,
    private dataService: DataService
  ){
    this.collectionName = "";
  }

  ngOnInit() {
    this.route.params
      .subscribe((params: Params) => {
        this.collectionName = params['collectionName'];
        this.getCollections(this.collectionName, 0, 20);
        console.log(this.collectionName);
      });
  }

  getCollections(collectionName: string, offset: number, limit: number): void {
    this.dataService
        .getCollections(collectionName, offset, limit)
        .then(data => {
          this.collections = data.result
          console.log(data);
        });
  }
}
