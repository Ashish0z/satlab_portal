import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { LoggedInUser } from './auth';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  setLoggedInUser(userData: LoggedInUser): void {
    if (localStorage.getItem('userData') !== JSON.stringify(userData)) {
      localStorage.setItem('userData', JSON.stringify(userData));
    }
   }

  constructor(private http: HttpClient) { }

  logIn(username: string, password: string): Observable<LoggedInUser>{
    return this.http.post(
      'http://localhost:8000/api-user-login/', 
      {username, password}) as Observable<LoggedInUser>;
  }

  isLoggedIn(): boolean {
    return localStorage.getItem('userData') !== null;
  }

  getLoggedInUser(): LoggedInUser|null {
    let data = localStorage.getItem('userData');
    if (data !== null) {
      return JSON.parse(data) as LoggedInUser;
    }
    return null;
  }
}
