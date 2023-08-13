import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StatusService {
  status: string = 'status message';

  setStatus(status: string) {
    this.status = status;
  }
}
