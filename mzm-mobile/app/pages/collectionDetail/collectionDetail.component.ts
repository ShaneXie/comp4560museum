
import {Component,Input} from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import 'rxjs/add/operator/switchMap';

@Component({
    selector:"collectionDetail",
    templateUrl:"./pages/collectionDetail/collectionDetail.component.html",
    styleUrls:[
        './pages/collectionDetail/collectionDetail.component.css'
    ]
})
export class CollectionDetailComponent{
    @Input() iteminfo:string="emp"
  constructor(private route: ActivatedRoute)
  {
  }

  ngOnInit() {
    this.route.params
      .subscribe((params: Params) => {
          this.iteminfo = params['iteminfo'];
          console.log(this.iteminfo)
      });
  }
 public onNavBtnTap(){
        // This code will be called only in Android.
        console.log("Navigation button tapped!");
    }
}