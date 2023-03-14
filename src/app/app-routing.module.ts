import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { UserLoginComponent } from './user-login/user-login.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { EditUserProfileComponent } from './edit-user-profile/edit-user-profile.component';
import { UserRegisterComponent } from './user-register/user-register.component';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  {
    path:"",
    redirectTo: "/login",
    pathMatch: "full"
  },
  {
    path:"login",
    component: UserLoginComponent,
  },
  {
    path:"user-profile/:id", 
    component: UserProfileComponent,
    canActivate: [AuthGuard]
  },
  {
    path:"edit-user-profile/:id",
    component: EditUserProfileComponent,
    canActivate: [AuthGuard]
  },
  {
    path:"register",
    component: UserRegisterComponent,
  },
  {
    path:"**",
    component: PagenotfoundComponent,
  },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
