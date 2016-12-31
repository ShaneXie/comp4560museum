import { Component, ElementRef, ViewChild, Injectable, OnInit, ChangeDetectorRef } from "@angular/core";
import { View } from "ui/core/view";
import dialogs = require("ui/dialogs");
import { RadSideDrawer } from "nativescript-telerik-ui-pro/sidedrawer";
import { Page } from "ui/page";
import { ActionItem } from "ui/action-bar";
import sideDrawerModule = require('nativescript-telerik-ui-pro/sidedrawer');
import { FadeTransition, DrawerTransitionBase, PushTransition, RevealTransition, ReverseSlideOutTransition, ScaleDownPusherTransition, ScaleUpTransition, SlideAlongTransition, SlideInOnTopTransition } from 'nativescript-telerik-ui-pro/sidedrawer';
import { Observable } from "data/observable";
import { RadSideDrawerComponent, SideDrawerType } from "nativescript-telerik-ui-pro/sidedrawer/angular";
import { RouterExtensions } from "nativescript-angular/router";
import { Router } from "@angular/router";

@Component({
    selector: "my-app",
    templateUrl: "app.component.html",
    styleUrls:['app.component.css']
})
export class AppComponent implements OnInit {
   constructor(private page: Page, private _changeDetectionRef: ChangeDetectorRef,private routerExtensions: RouterExtensions,private router: Router) {
        // super();
        this.sideDrawerTransition =  new ReverseSlideOutTransition();
        // this.page.on("loaded", this.onLoaded, this);
    }

    @ViewChild(RadSideDrawerComponent) public drawerComponent: RadSideDrawerComponent;
    // public sideDrawerTransition: DrawerTransitionBase;
    private drawer: SideDrawerType;
    private sideDrawerTransition: DrawerTransitionBase;

    ngAfterViewInit() {
        this.drawer = this.drawerComponent.sideDrawer;
        this._changeDetectionRef.detectChanges();
        this.drawer.gesturesEnabled=true;
        this.drawer.showOverNavigation=false;
    }


    public onLoaded(args) {
    }

    ngOnInit() {
    } 

    public openDrawer() {
        this.drawer.showDrawer();
    } 
    
    private toHome()
    {
        this.router.navigate(["/home"]);
        this.drawer.closeDrawer();
    }
    private toFish()
    {
        this.router.navigate(["/collection/fish"]);
        this.drawer.closeDrawer();
    }
    private toBird()
    {
        this.router.navigate(["/collection/bird"]);
        this.drawer.closeDrawer();
    }
    private toCollection()
    {
        this.router.navigate(["/collection/fish"]);
        this.drawer.closeDrawer();
    }
    private toAbout()
    {
        this.router.navigate(["/about"]);
        this.drawer.closeDrawer();
    }
}
