import { Component } from '@angular/core';

@Component({
  selector: 'collection',
  providers: [
  ],
  styles: [ require('./collection.style.scss') ],
  templateUrl: './collection.template.html'
})
export class Collection {
  constructor() {

  }

  ngOnInit() {
    // this.title.getData().subscribe(data => this.data = data);
  }
}
