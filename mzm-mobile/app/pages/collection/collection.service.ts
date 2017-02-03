import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';
import 'rxjs/Rx';

@Injectable()
export class DataService {

  // private headers = new Headers({'Content-Type': 'application/json'});
  private baseUrl = 'http://192.168.66.88:8080';  // URL to web api
  // private baseUrl = 'http://ebony.cs.umanitoba.ca';

  constructor(private http: Http) { }

  getCollections(collectionName: string, offset: number, limit: number): Promise<any> {
    let theUrl = this.baseUrl +"/collection/"+collectionName+"/?limit="+limit+"&offset="+offset;
    console.log("getcollections ===="+theUrl+ '${this.baseUrl}/collection/${collectionName}/?limit=${limit}&offset=${offset}')
    return this.http.get(theUrl)
               .toPromise()
               .then(response => response.json())
               .catch(this.handleError);
  }


  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

}
