import { TestBed } from '@angular/core/testing';

import { RiskTypeService } from './risk-type.service';

describe('RiskTypeService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: RiskTypeService = TestBed.get(RiskTypeService);
    expect(service).toBeTruthy();
  });
});
