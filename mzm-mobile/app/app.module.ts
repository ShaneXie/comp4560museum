import { NgModule, NO_ERRORS_SCHEMA } from "@angular/core";
// import {HttpModule} from '@angular/Http';

import { NativeScriptModule } from "nativescript-angular/platform";
import { NativeScriptRouterModule } from "nativescript-angular/router";
import { SIDEDRAWER_DIRECTIVES } from "nativescript-telerik-ui-pro/sidedrawer/angular";
import { LISTVIEW_DIRECTIVES } from 'nativescript-telerik-ui-pro/listview/angular';

import { AppComponent } from "./app.component";
import {HomeComponent} from "./pages/home/home.component";
import {CollectionDetailComponent} from "./pages/collectionDetail/collectionDetail.component";
import {CollectionComponent} from "./pages/collection/collection.component";
import {AboutComponent} from "./pages/about/about.component";
import {routes} from './app.routing';
import { DataService } from './pages/collection/collection.service';
import { NativeScriptHttpModule } from "nativescript-angular/http";

@NgModule({
    declarations: [
        AppComponent,
        SIDEDRAWER_DIRECTIVES,
        LISTVIEW_DIRECTIVES,
        HomeComponent,
        AboutComponent,
        CollectionComponent,
        CollectionDetailComponent
    ],
    bootstrap: [AppComponent],
    imports: [
        NativeScriptModule,
        NativeScriptRouterModule,
        routes,
        // HttpModule,
        NativeScriptHttpModule
    ],
    schemas: [NO_ERRORS_SCHEMA],
})
export class AppModule { }
