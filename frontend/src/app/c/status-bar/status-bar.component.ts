import { Component } from '@angular/core';

import { StatusService } from '@app/s/status.service';

@Component({
  selector: 'app-status-bar',
  templateUrl: './status-bar.component.html',
  styleUrls: ['./status-bar.component.scss']
})
export class StatusBarComponent {
  constructor(
    public statusService: StatusService,
  ){}
}
