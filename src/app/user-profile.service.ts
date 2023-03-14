import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";
import { UserProfile } from "./user-profile";

@Injectable({
  providedIn: 'root'
})
export class UserProfileService {

  constructor(private http: HttpClient) { }

  getUserProfile(userId: string|null): Observable<UserProfile> {
    return this.http.get(`http://127.0.0.1:8000/api/v1/users/${userId}/`) as Observable<UserProfile>;
  }

  logout(): void {
    localStorage.removeItem('userData');
  }

  editUserProfile(userProfile: UserProfile): Observable<UserProfile> {
    return this.http.put(`http://127.0.0.1:8000/api/v1/users/${userProfile.id}/`, userProfile) as Observable<UserProfile>;
  }

  deleteUserProfile(userId: string): Observable<UserProfile> {
    return this.http.delete(`http://127.0.0.1:8000/api/v1/users/${userId}/`) as Observable<UserProfile>;
  }
}

