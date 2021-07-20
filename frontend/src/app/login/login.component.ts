import { Component, OnInit } from '@angular/core';
import { OidcSecurityService } from 'angular-auth-oidc-client';
import { FormGroup, Validators, FormControl } from "@angular/forms";
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { environment } from "../../environments/environment";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  username: string;
  password: string;
  loginGroup: any;
  userNamePattern: any;
  passWordPattern: any;
  userNameError: boolean;
  passWordError: boolean;
  user_message: string;
  password_message: string;
  baseUrl = environment.baseUrl;
  login_response: any;

  validation_messages = {
    'username': [
      { type: 'required', message: 'This field is required!' },
      { type: 'pattern', message: 'Invalid Username!' }
    ],
    'password': [
      { type: 'required', message: 'This field is required!' },
      { type: 'pattern', message: 'Invalid Password!' }
    ]
  };

  constructor(
    private oidc: OidcSecurityService,
    private router: Router,
    private http: HttpClient
  ) { }

  ngOnInit() {

    this.loginGroup = new FormGroup({
      'userName': new FormControl('', [Validators.required, Validators.pattern('^[a-zA-z]{3,32}$')]),
      'passWord': new FormControl('', [Validators.required, Validators.pattern('^[a-zA-Z][a-zA-Z0-9@#$%^&*]{7,32}$')])
    });
    this.userNamePattern = /^[a-zA-z]{3,32}$/;
    this.passWordPattern = /^[a-zA-Z][a-zA-Z0-9@#$%^&*]{7,32}$/;

  }

  googleLogin() {
    this.oidc.authorize();
  }

  login() {
    console.log("username",this.username);
    console.log("password",this.password);

    if (this.username == undefined || this.username == '') {
      this.userNameError = true;
      this.user_message = 'This field is required!';
    }

    else if (this.password == undefined || this.password == '') {
      this.passWordError = true;
      this.password_message = 'This field is required';
    }

    else if(!this.userNamePattern.test(this.username)) {
      this.userNameError = true;
      this.user_message = 'Invalid username!';
    }
    
    else if(!this.passWordPattern.test(this.password)) {
      this.passWordError = true;
      this.password_message = 'Invalid password!';
    }

    else {
      
      let body = {
        "email": "",
        "user_name": this.username,
        "password": this.password,
        "user_type": "normal"
      }

      this.http.post(this.baseUrl + '/user/checkUser', body).subscribe((response) => {
        console.log(response);
        
        if (response['status'] == 'fail') {
          alert(response['message']);
        }
        else {
          console.log(response['message']);
          localStorage.setItem('user', response['message']);
          localStorage.setItem('loggedIn', 'true');
          localStorage.setItem('usertype','normal');
          this.router.navigateByUrl('/books');
        }

      });


    }

  }

  usernameChange() {
    this.userNameError = false;
  }

  passwordChange() {
    this.passWordError = false;
  }
}
