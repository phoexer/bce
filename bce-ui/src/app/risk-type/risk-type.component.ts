import { Component, OnInit } from '@angular/core';
import {FormArray, FormControl, FormGroup} from '@angular/forms';
import {RiskTypeService} from '../services/risk-type.service';
import {Error} from 'tslint/lib/error';
import {HttpErrorResponse} from '@angular/common/http';
import {Router} from '@angular/router';
import {AlertService} from '../services/alert.service';

@Component({
  selector: 'app-risk-type',
  templateUrl: './risk-type.component.html',
  styleUrls: ['./risk-type.component.scss']
})
export class RiskTypeComponent implements OnInit {
  riskTypeForm: FormGroup;
  submitted = false;
  index = 0;
  active = true;

  constructor(
    private riskTypeService: RiskTypeService,
    private router: Router,
    private alertService: AlertService
  ) { }

  ngOnInit() {
    this.riskTypeForm = new FormGroup({});

    this.riskTypeForm.addControl('name', new FormControl());
    this.riskTypeForm.addControl('label', new FormControl());
    this.riskTypeForm.addControl('description', new FormControl());
    this.riskTypeForm.addControl('tooltip', new FormControl());
    this.riskTypeForm.addControl('active', new FormControl());
    // this.riskTypeForm.addControl('fields', new FormArray([]));
    this.riskTypeForm.addControl('fields', new FormArray([this.createNewField()]));
    // this.optionsNeeded[0] = true;
    // this.optionsNeeded.push(false);
  }

  createNewField() {
    let field = new FormGroup({});

    field.addControl('name', new FormControl());
    field.addControl('label', new FormControl());
    field.addControl('tooltip', new FormControl());
    field.addControl('type', new FormControl());
    field.addControl('visible', new FormControl());
    field.addControl('hidden', new FormControl());
    field.addControl('required', new FormControl());
    field.addControl('options', new FormArray([]));
    this.index++;
    return field;
  }

  createNewOption() {
    let option = new FormGroup({});
    option.addControl('choice', new FormControl());
    option.addControl('label', new FormControl());
    return option;
  }
  onAddField() {
    (this.riskTypeForm.controls['fields'] as FormArray).push(this.createNewField());
  }
  onRemoveField(optionIndex) {
    (this.riskTypeForm.controls['fields'] as FormArray).removeAt(optionIndex);
  }

  onAddOption(fieldGroup: FormGroup) {
    (fieldGroup.controls.options as FormArray).push(this.createNewOption());
  }
  onRemoveOption(fieldGroup: FormGroup, j) {
    (fieldGroup.controls.options as FormArray).removeAt(j);
  }

  onChange(fieldGroup: FormGroup, value) {
    // objArray.find(obj => obj.id == 3);
    if (value === 'RADIO' || value === 'DROPDOWN') {
      (fieldGroup.controls.options as FormArray).push(this.createNewOption());
    } else {
      while ((fieldGroup.controls.options as FormArray).length) {
        (fieldGroup.controls.options as FormArray).removeAt(0);
      }
    }
  }

  onSubmit() {
    window.scroll(0,0);
    this.submitted = true;
    // console.log('Submitted');
    // console.log(this.riskTypeForm);
    // console.log(this.riskTypeForm.value);
    // console.log(JSON.stringify(this.riskTypeForm.value));
    let body; // = this.riskTypeForm.value; // JSON.stringify(this.riskTypeForm.value);

    let bodyTemp = JSON.stringify(this.riskTypeForm.value, function (key, value) {
        return value === null ? '' : value;
    });
    bodyTemp = bodyTemp.split('"active":""').join('"active":false');
    bodyTemp = bodyTemp.split('"visible":""').join('"visible":false');
    bodyTemp = bodyTemp.split('"hidden":""').join('"hidden":false');
    bodyTemp = bodyTemp.split('"required":""').join('"required":false');

    body = JSON.parse(bodyTemp);

    try{
      this.riskTypeService.createRiskTypes(body).subscribe(data => {

          this.alertService.success('Risk Type Created', true);
          this.router.navigate(['/']);
        },
        (err: HttpErrorResponse) => {

          for (let key in err.error) {
            // console.log("Field \"" + key + "\": " + err.error[key]);
            this.alertService.error(key + ": " + err.error[key], true);
          }
        });
    }catch (e) {
      // console.log(e.toString());
      this.alertService.error(e.message, true);
    }

  }
}
