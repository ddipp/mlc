import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from '@app/c/home/home.component';
import { TestsComponent } from '@app/c/tests/tests.component';

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'tests', component: TestsComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
