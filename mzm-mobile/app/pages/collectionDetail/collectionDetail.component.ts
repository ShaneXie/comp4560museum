
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
            console.log(params['iteminfo'])
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
            for(var v in info[k])
            {
                var i = {}
                if(v.match(/^\d+$/))
                {
                    temp+=info[k][v]
                    console.log("====>"+temp +"  ")
                }
                else{
                    console.log("++++")
                    if(temp != "")
                    {
                        i["key"] = "Term";
                        i["val"] = temp
                        items.push(i);
                        temp=""
                        console.log("---->"+temp +"  ")
                    }

                    console.log("!!!!!!!!!");
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
    private procWord(element:any)
    {
        let word = "";
        let isNum = true;
        if(element.val != null)
        {
        // console.log("\n"+JSON.stringify(element)+"\n")
            // if(!isNaN(element.key))
            // {
            //     tempStore += element.val
            // }
            // else if(element.key )
            // else{
                word+= element.key+"  "+element.val
            // }
        }
        return word
    }
}
