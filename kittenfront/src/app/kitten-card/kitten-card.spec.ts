import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KittenCard } from './kitten-card';

describe('KittenCard', () => {
  let component: KittenCard;
  let fixture: ComponentFixture<KittenCard>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [KittenCard]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KittenCard);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
