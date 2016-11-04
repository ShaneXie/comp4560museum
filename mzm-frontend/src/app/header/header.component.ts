import { Component } from '@angular/core';

@Component({
  // The selector is what angular internally uses
  // for `document.querySelectorAll(selector)` in our index.html
  // where, in this case, selector is the string 'home'
  selector: 'mzm-header',  
  // We need to tell Angular's Dependency Injection which providers are in our app.
  providers: [
  ],
  // Our list of styles in our component. We may add more to compose many styles together
  styles: [ require('./header.style.scss') ],
  // Every Angular template is first compiled by the browser before Angular runs it's compiler
  templateUrl: './header.template.html'
})
export class MzmHeader {
  umLogo = 'assets/img/umlogo.gif';
  umsciLogo = 'assets/img/uofm_sci_logo.png';
  // TypeScript public modifiers
  constructor() {

  }

  ngOnInit() {
    // this.title.getData().subscribe(data => this.data = data);
  }
}
