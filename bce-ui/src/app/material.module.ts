// material.module.ts

import { NgModule } from '@angular/core';
import { MatDatepickerModule,
  MatNativeDateModule,
  MatFormFieldModule,
  MatInputModule,
  MatRadioModule,
  MatSelectModule,
  MatTooltipModule,
} from '@angular/material';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  imports: [
    MatDatepickerModule,
    MatFormFieldModule,
    MatNativeDateModule,
    MatInputModule,
    MatSelectModule,
    MatRadioModule,
    MatTooltipModule,
    BrowserAnimationsModule
  ],
  exports: [
    MatDatepickerModule,
    MatFormFieldModule,
    MatNativeDateModule,
    MatInputModule,
    MatRadioModule,
    MatSelectModule,
    MatTooltipModule,
    BrowserAnimationsModule
  ],
  providers: [ MatDatepickerModule ],
})

export class MaterialModule {}
