import { Routes } from '@angular/router';
import { LoginPage } from './login-page/login-page';
import { KittenList } from './kitten-list/kitten-list';
import { KittenCreation } from './kitten-creation/kitten-creation';

export const routes: Routes = [
    { path: '', component: KittenList },
    { path: 'login', component: LoginPage },
    { path: 'create', component: KittenCreation },
];
