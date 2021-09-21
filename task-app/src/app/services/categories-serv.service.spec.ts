/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { CategoriesServService } from './categories-serv.service';

describe('Service: CategoriesServ', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CategoriesServService]
    });
  });

  it('should ...', inject([CategoriesServService], (service: CategoriesServService) => {
    expect(service).toBeTruthy();
  }));
});
