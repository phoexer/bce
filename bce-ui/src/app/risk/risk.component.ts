import { Component, OnInit } from '@angular/core';
import {RiskTypeService} from '../services/risk-type.service';
import {Error} from 'tslint/lib/error';
import {HttpErrorResponse} from '@angular/common/http';
import {FormArray, FormControl, FormGroup, NgForm} from '@angular/forms';
import {AlertService} from '../services/alert.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-risk',
  templateUrl: './risk.component.html',
  styleUrls: ['./risk.component.scss']
})
export class RiskComponent implements OnInit {
  riskTypes: any;
  selectedRiskType: any;
  submitted = false;
  riskForm: FormGroup;

  constructor(private riskTypeService: RiskTypeService,
              private router: Router,
              private alertService: AlertService) {

  }

  ngOnInit() {
    this.riskTypeService.findAllRiskTypes().subscribe(data => {
        this.riskTypes = data;
        console.log('Here Be Data');
        console.log(data);
        // return data;
      },
      (err: HttpErrorResponse) => {
        if (err.error instanceof Error) {
          console.log('Client-side error occured.');
        } else {
          console.log('Server-side error occured.');
        }
      });
  }

  onChange(id) {
    // objArray.find(obj => obj.id == 3);
    this.selectedRiskType =  this.riskTypes.filter(x => x.id === parseInt(id))[0];
    console.log(id);
    console.log(this.selectedRiskType);
    // console.log(this.selectedRiskType.name);
    // this.selectedRiskType = newRiskType;

    this.riskForm = new FormGroup({});
    // this.riskForm = new FormArray({});

    for (let field of this.selectedRiskType.fields) {
      console.log(field.name);
      this.riskForm.addControl(field.name, new FormControl());
    }
  }

  onSubmit() {
    this.submitted = true;
    let bodyTemp = JSON.stringify(this.riskForm.value, function (key, value) {
      return value === null ? '' : value;
    });

    let body = {
      name: 'form data',
      data: btoa(bodyTemp)
    };

    this.riskTypeService.createRisk(body).subscribe(data => {

        this.alertService.success('Risk Created Successfully. ', true);
        this.router.navigate(['/']);
      },
      (err: HttpErrorResponse) => {
        if (err.error instanceof Error) {
          this.alertService.error('Client-side error occured.');
        } else {
          this.alertService.error('Server-side error occured.');
        }
      });
  }

}
