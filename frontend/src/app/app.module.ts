import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule }   from '@angular/common/http';

import { AppRoutingModule } from '@app/app-routing.module';
import { AppComponent } from '@app/app.component';
import { MenuBarComponent } from '@app/c/menu-bar/menu-bar.component';
import { HomeComponent } from '@app/c/home/home.component';
import { TestsComponent } from '@app/c/tests/tests.component';
import { StatusBarComponent } from '@app/c/status-bar/status-bar.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuBarComponent,
    HomeComponent,
    TestsComponent,
    StatusBarComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
