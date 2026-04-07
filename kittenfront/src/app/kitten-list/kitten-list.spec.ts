import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KittenList } from './kitten-list';

describe('KittenList', () => {
  let component: KittenList;
  let fixture: ComponentFixture<KittenList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [KittenList]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KittenList);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
