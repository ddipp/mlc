import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import {environment} from "@environments/environment";

import { StatusService } from '@app/s/status.service';

@Component({
  selector: 'app-tests',
  templateUrl: './tests.component.html',
  styleUrls: ['./tests.component.scss']
})
export class TestsComponent {
  getdata: string = 'init getdata';

  serverUrl = environment.apiUrl;

  constructor(
    private http: HttpClient,
    private statusService: StatusService,
  ){}

  ngOnInit(){
    this.http.get(this.serverUrl + 'test').subscribe({next:(data:any) => this.getdata=data.name});
    this.statusService.setStatus('ngOnInit from Tests page');
  }
}
