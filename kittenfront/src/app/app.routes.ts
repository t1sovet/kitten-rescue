import { Routes } from '@angular/router';
import { LoginPage } from './login-page/login-page';
import { KittenList } from './kitten-list/kitten-list';

export const routes: Routes = [
    { path: '', component: KittenList },
    { path: 'login', component: LoginPage }
];
