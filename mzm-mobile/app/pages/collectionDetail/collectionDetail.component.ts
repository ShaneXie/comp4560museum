
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
    itemjson
    tempStore:string
    constructor(private route: ActivatedRoute)
    {
    }

    ngOnInit() {
        this.route.params
        .subscribe((params: Params) => {
            this.iteminfo = this.processItemInfo(params['iteminfo']);
        });
    }
    public onNavBtnTap()
    {
        console.log("Navigation button tapped!");
    }
    private processItemInfo(iteminfo):any
    {
        var res = [];
        var info = JSON.parse(iteminfo);
        for(var k in info)
        {
            //level 1 struct
            var item = {};
            item["table"] = k
            var temp =""
            var items = [];

            if( typeof info[k] === 'string' || typeof info[k] === 'number')
            {
                var i = {}
                i["key"] = k;
                i["val"] = info[k]
                items.push(i);
            }
            else{
                for(var v in info[k])
                {
                    var i = {}
                    i["key"] = v;
                    i["val"] = info[k][v]
                    items.push(i);
                }
            }

            item["data"]=items;
            res.push(item);
        }
        console.log(JSON.stringify(res))
        this.itemjson = res;
    }
    private procWord(element)
    {
        let word = "";
        if(element.val != null)
        {
            word+= element.key+"  "+element.val
        }
        return word
    }
}
