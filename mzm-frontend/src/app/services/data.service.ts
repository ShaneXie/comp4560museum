import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class DataService {

  // private headers = new Headers({'Content-Type': 'application/json'});
  private baseUrl = 'http://192.168.66.88:8000';  // URL to web api

  constructor(private http: Http) { }

  getCollections(collectionName: string, offset: number, limit: number): Promise<any> {
    return this.http.get(`${this.baseUrl}/collection/${collectionName}/?limit=${limit}&offset=${offset}`)
               .toPromise()
               .then(response => response.json())
               .catch(this.handleError);
  }


//   getHero(id: number): Promise<any> {
//     const url = `${this.baseUrl}/${id}`;
//     return this.http.get(url)
//       .toPromise()
//       .then(response => response.json().data as Hero)
//       .catch(this.handleError);
//   }

//   delete(id: number): Promise<void> {
//     const url = `${this.baseUrl}/${id}`;
//     return this.http.delete(url, {headers: this.headers})
//       .toPromise()
//       .then(() => null)
//       .catch(this.handleError);
//   }

//   create(name: string): Promise<Hero> {
//     return this.http
//       .post(this.baseUrl, JSON.stringify({name: name}), {headers: this.headers})
//       .toPromise()
//       .then(res => res.json().data)
//       .catch(this.handleError);
//   }

//   update(hero: Hero): Promise<Hero> {
//     const url = `${this.baseUrl}/${hero.id}`;
//     return this.http
//       .put(url, JSON.stringify(hero), {headers: this.headers})
//       .toPromise()
//       .then(() => hero)
//       .catch(this.handleError);
//   }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}



/*
Copyright 2016 Google Inc. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/