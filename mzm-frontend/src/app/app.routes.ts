import { Routes, RouterModule } from '@angular/router';
import { Home } from './home';
import { Collection } from './collection';
import { NoContent } from './no-content';

import { DataResolver } from './app.resolver';


export const ROUTES: Routes = [
  { path: '',      component: Home },
  { path: 'home',  component: Home },
  { path: 'collection/:collectionName', component: Collection },
  { path: '**',    component: NoContent },
];
