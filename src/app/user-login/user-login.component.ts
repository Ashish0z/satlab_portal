import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { UserCredentials } from '../auth';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent implements OnInit {
  logInForm;
  constructor(private formBuilder: FormBuilder, private authService: AuthService, private router: Router) {
   this.logInForm = this.formBuilder.nonNullable.group({
     username: new FormControl('', Validators.required),
     password: new FormControl<string>('', Validators.required)
   });
  }

  ngOnInit(): void {
    if (this.authService.isLoggedIn()) {
      let user = this.authService.getLoggedInUser();
      if (user !== null) {
        this.router.navigateByUrl(`/user-profile/${user.id}`);
      }
    }
  }

  logInUser(user: UserCredentials): void {
   this.authService.logIn(user.username, user.password).subscribe({
     next: (data) => {
       this.authService.setLoggedInUser(data);
       this.router.navigateByUrl(`/user-profile/${data.id}`);
     },
     error: (error) => {
       console.log(error);
     }
   }
   );
  }

  onSubmit(): void {
    if (this.logInForm.invalid) {
      console.log(this.logInForm.errors);
    } else {
      const username = this.logInForm.value.username;
      const password = this.logInForm.value.password;
      if (username != null && password != null) {
        const formData: UserCredentials = {username, password};
        this.logInUser(formData);
      }
      else {
        console.log('Username or password is null');
      }
    }
  }
}