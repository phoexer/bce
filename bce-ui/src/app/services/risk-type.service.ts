import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class RiskTypeService {
  constructor(private http: HttpClient) { }

  findAllRiskTypes() {
    return this.http
      .get(`${config.apiUrl}/risk-types/`);
  }

  createRiskTypes(data) {
    return this.http
      .post(`${config.apiUrl}/risk-types/`, data, {
        headers: new HttpHeaders({
          'Content-Type': 'application/json'
        })
      });
  }

  createRisk(data) {
    return this.http
      .post(`${config.apiUrl}/risks/`, data, {
        headers: new HttpHeaders({
          'Content-Type': 'application/json'
        })
      });
  }
}



