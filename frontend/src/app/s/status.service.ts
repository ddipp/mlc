import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StatusService {
  private status: string = '';

  setStatus(status: string) {
    this.status = status;
  }

  getStatus(): string {
    return this.status;
  }
}
