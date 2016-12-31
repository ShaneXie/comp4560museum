import { Router, RouterModule } from '@angular/router';

import {DrawerComponent} from "./pages/drawer/drawer.component";
import {HomeComponent} from "./pages/home/home.component";
import {AboutComponent} from "./pages/about/about.component";
import {AppComponent} from "./app.component";


export const routes = RouterModule.forRoot([
  { path: "", component: HomeComponent },
  { path: "home", component: HomeComponent },
  { path: "about", component: AboutComponent }
])