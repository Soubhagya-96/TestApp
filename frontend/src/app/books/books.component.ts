 import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { OidcSecurityService } from 'angular-auth-oidc-client';
import { environment } from "../../environments/environment";


@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {

  isLoggedIn: string;
  baseUrl = environment.baseUrl;
  bookdata: any;
  user: any;

  constructor(
    private router: Router,
    private oidc: OidcSecurityService,
    private http: HttpClient
  ) { }

  ngOnInit() {

    if (localStorage.getItem('usertype') == 'normal') {
      if(localStorage.getItem('loggedIn') == 'true') {
        this.user = localStorage.getItem('user');
        this.http.get(this.baseUrl + '/book/getBooks').subscribe((data) => {
          console.log("response is", data);
          this.bookdata = data;
        });
      }
      else {
        this.router.navigateByUrl('/login');
      }
    }

    else {
      this.oidc.checkAuth().subscribe((auth) => {

        if(!auth) {
          console.log("not authorized");
          this.router.navigateByUrl('/login');
        }
        else {
          this.oidc.userData$.subscribe((userinfo) => {
  
            console.log("username", userinfo.email);
            localStorage.setItem('verified','true');
  
          });
        }
  
      });
  
    }

  }

  logout() {
    this.oidc.logoff();
    localStorage.clear();
    this.router.navigateByUrl('/login');
  }

}
