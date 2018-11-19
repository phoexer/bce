import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {RiskTypeComponent} from './risk-type/risk-type.component';
import {RiskComponent} from './risk/risk.component';
import {HomeComponent} from './home/home.component';
import {AuthGuard} from './guards/auth.guard';
import {Register} from 'ts-node';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    canActivate: [AuthGuard]
    // redirectTo: 'home',
    // pathMatch: 'full'
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path: 'risks',
    component: RiskComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'risk-types',
    component: RiskTypeComponent,
    canActivate: [AuthGuard]
  },
  {
    path: '**',
    redirectTo: ''
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
