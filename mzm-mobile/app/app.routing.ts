import { Router, RouterModule } from '@angular/router';

import {HomeComponent} from "./pages/home/home.component";
import {CollectionComponent} from "./pages/collection/collection.component";
import {CollectionDetailComponent} from "./pages/collectionDetail/collectionDetail.component";
import {AboutComponent} from "./pages/about/about.component";
import {AppComponent} from "./app.component";


export const routes = RouterModule.forRoot([
  { path: "", component: HomeComponent },
  { path: "home", component: HomeComponent },
  { path: "collection/:collectionName", component: CollectionComponent },
  { path: "collectionDetail/:iteminfo", component: CollectionDetailComponent },
  { path: "about", component: AboutComponent }
],{ useHash: true })