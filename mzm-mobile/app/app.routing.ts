import { Router, RouterModule } from '@angular/router';

import {DrawerComponent} from "./pages/drawer/drawer.component";
import {HomeComponent} from "./pages/home/home.component";
import {AppComponent} from "./app.component";


export const routes = RouterModule.forRoot([
  { path: "", component: AppComponent },
  { path: "home", component: HomeComponent }
])