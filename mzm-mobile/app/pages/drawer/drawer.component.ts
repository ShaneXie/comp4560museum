import { Component, ElementRef, ViewChild, Injectable, OnInit, ChangeDetectorRef } from "@angular/core";
import { View } from "ui/core/view";
import dialogs = require("ui/dialogs");
import { RadSideDrawer } from "nativescript-telerik-ui-pro/sidedrawer";
import { Page } from "ui/page";
import { ActionItem } from "ui/action-bar";
import sideDrawerModule = require('nativescript-telerik-ui-pro/sidedrawer');
import { Observable } from "data/observable";
import { RadSideDrawerComponent, SideDrawerType } from "nativescript-telerik-ui-pro/sidedrawer/angular";



@Component({
    selector: "drawer",
    templateUrl: "pages/drawer/drawer.component.html",
    styleUrls:['pages/drawer/drawer.component.css']
})
export class DrawerComponent extends Observable implements OnInit {
    constructor(private page: Page, private _changeDetectionRef: ChangeDetectorRef) {
        super();
    }

    @ViewChild(RadSideDrawerComponent) public drawerComponent: RadSideDrawerComponent;
    private drawer: SideDrawerType;

    ngAfterViewInit() {
        this.drawer = this.drawerComponent.sideDrawer;
        this._changeDetectionRef.detectChanges();
    }

    ngOnInit() {
        this.set("mainContentTexts", "SideDrawer for NativeScript can be easily setup in the XML definition of your page by defining main- and drawer-content. The component"
            + " has a default transition and position and also exposes notifications related to changes in its state. Swipe from left to open side drawer.");
        this.set("aText", "GetLocation")
    } 

    public openDrawer() {
        this.drawer.showDrawer();
    }
}
