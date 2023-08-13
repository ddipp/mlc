import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import {environment} from "@app/../environments/environment";

@Component({
  selector: 'app-tests',
  templateUrl: './tests.component.html',
  styleUrls: ['./tests.component.scss']
})
export class TestsComponent {
  getdata: string | undefined;

  serverUrl = environment.apiUrl;

  constructor(private http: HttpClient){}

  ngOnInit(){
    this.http.get(this.serverUrl + 'test').subscribe({next:(data:any) => this.getdata=data.name});
  }
}
