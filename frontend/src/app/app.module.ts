import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { APP_INITIALIZER } from '@angular/core';
import { AuthModule, LogLevel, OidcConfigService } from 'angular-auth-oidc-client';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { BooksComponent } from './books/books.component';


export function configureAuth(oidcConfigService: OidcConfigService) {
  return () =>
      oidcConfigService.withConfig({
        stsServer: 'https://accounts.google.com',
        redirectUrl: window.location.origin + '/books',
        clientId: '490837879365-hfe0lg1gv8ddbbsavf0vjiil259rskgf.apps.googleusercontent.com',
        responseType: 'id_token token',
        scope: 'openid email profile',
        triggerAuthorizationResultEvent: true,
        postLogoutRedirectUri: window.location.origin + '/login',
        startCheckSession: false,
        silentRenew: false,
        // silentRenewUrl: window.location.origin + '/silent-renew.html',
        postLoginRoute: '/books',
        // forbiddenRoute: '/forbidden',
        unauthorizedRoute: '/login',
        logLevel: LogLevel.None,
        historyCleanupOff: true,
      }); 
}


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    BooksComponent
  ], 
  imports: [
    BrowserModule,
    AppRoutingModule,
    AuthModule.forRoot(), 
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    OidcConfigService,
    {
        provide: APP_INITIALIZER,
        useFactory: configureAuth,
        deps: [OidcConfigService],
        multi: true,
        
    },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
