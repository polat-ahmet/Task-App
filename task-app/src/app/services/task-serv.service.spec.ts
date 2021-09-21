/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { TaskServService } from './task-serv.service';

describe('Service: TaskServ', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TaskServService]
    });
  });

  it('should ...', inject([TaskServService], (service: TaskServService) => {
    expect(service).toBeTruthy();
  }));
});
