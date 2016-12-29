import { NgModule, NO_ERRORS_SCHEMA } from "@angular/core";
import { NativeScriptModule } from "nativescript-angular/platform";
import { NativeScriptRouterModule } from "nativescript-angular/router";
import { SIDEDRAWER_DIRECTIVES } from "nativescript-telerik-ui-pro/sidedrawer/angular";
import { LISTVIEW_DIRECTIVES } from 'nativescript-telerik-ui-pro/listview/angular';
import { AppComponent } from "./app.component";
import {DrawerComponent} from "./pages/drawer/drawer.component";
import {HomeComponent} from "./pages/home/home.component";

import {routes} from './app.routing';

@NgModule({
    declarations: [
        AppComponent,
        SIDEDRAWER_DIRECTIVES,
        LISTVIEW_DIRECTIVES,
        DrawerComponent,
        HomeComponent 
    ],
    bootstrap: [AppComponent],
    imports: [
        NativeScriptModule,
        NativeScriptRouterModule,
        routes,
    ],
    schemas: [NO_ERRORS_SCHEMA]
})
export class AppModule { }
