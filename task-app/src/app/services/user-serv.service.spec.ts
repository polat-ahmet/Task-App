/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { UserServService } from './user-serv.service';

describe('Service: UserServ', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [UserServService]
    });
  });

  it('should ...', inject([UserServService], (service: UserServService) => {
    expect(service).toBeTruthy();
  }));
});
