import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { RegisterModel } from './register-model';


@Injectable({
  providedIn: 'root'
})
export class RegisterServiceService {

  constructor(private http: HttpClient) { }

  private handleError<RegisterModel>(operation = 'operation', result?: RegisterModel) {
    return (error: any): Observable<RegisterModel> => {
      console.error(error);
      return error;
    };
  }

  registerUser(registerModel: RegisterModel): Observable<RegisterModel> {
    return this.http.post<RegisterModel>(
      'http://localhost:8000/api-user-register/', 
      registerModel);
  }
}
