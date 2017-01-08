import { Component } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import 'rxjs/add/operator/switchMap';
import { DataService } from './collection.service';

@Component({
     moduleId: module.id,
  selector: 'collection',
  providers: [DataService
  ],
  styleUrls: [ './collection.component.css' ],
  templateUrl: './collection.component.html'
})
export class CollectionComponent {
  public collectionName: string;
  public collections: Array<any>;
  public currentPage: number;
  public totalPage: number;
  private limit: number;
  private offset: number;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private dataService: DataService
  ){
    this.collectionName = "";
    this.limit = 20;
    this.offset = 0;
  }

  ngOnInit() {
    this.route.params
      .subscribe((params: Params) => {
        this.collectionName = params['collectionName'];
        this.getCollections(this.collectionName);
      });
  }

  getCollections(collectionName: string): void {
    this.dataService
        .getCollections(collectionName, this.offset, this.limit)
        .then(data => {
          this.collections = data.result;
          this.currentPage = data.current;
          this.totalPage = data.total;
        });
  }
    public onItemLoading(args) {
        if (args.itemIndex % 2 == 0) {
            args.view.backgroundColor = "#fcc126";
        }
        else {
            args.view.backgroundColor = "#e39308";
        }
            args.view._subViews[0].fontSize = "20";
            args.view._subViews[1].fontSize = "14";
    }

  setLimit(limit: number): void {
    this.limit = limit;
    this.offset = 0;
    this.getCollections(this.collectionName);
  }
  tapToDetail(items:any):void 
  {
    // console.log(JSON.stringify(items)) 
    this.router.navigate(["/collectionDetail/"+JSON.stringify(items)]);
  }
  changePage(di: number): void {
    this.offset += di*this.limit;
    if(this.offset<0){
      this.offset = 0
    } else if (this.offset/this.limit > this.totalPage) {
      this.offset = this.totalPage * this.limit;
      this.currentPage -= 1;
    }
    this.getCollections(this.collectionName);
  }
}
