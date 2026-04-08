import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KittenCreation } from './kitten-creation';

describe('KittenCreation', () => {
  let component: KittenCreation;
  let fixture: ComponentFixture<KittenCreation>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [KittenCreation]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KittenCreation);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
