import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import{HttpClientModule} from '@angular/common/http'

import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarCompComponent } from './components/navbar-comp/navbar-comp.component';
import { TasksCompComponent } from './components/tasks-comp/tasks-comp.component';
import { DashboardCompComponent } from './components/dashboard-comp/dashboard-comp.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { TaskDetailComponent } from './components/task-detail/task-detail.component';
import { CategoriesCompComponent } from './components/categories-comp/categories-comp.component';
import { LoginCompComponent } from './components/login-comp/login-comp.component';
import { AddTaskCompComponent } from './components/add-task-comp/add-task-comp.component';
import { UserCompComponent } from './components/user-comp/user-comp.component';
import { CategoryAddComponent } from './components/category-add/category-add.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CategoryDetailComponent } from './components/category-detail/category-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [		
    AppComponent,
    NavbarCompComponent,
    TasksCompComponent,
    DashboardCompComponent,
    TaskListComponent,
    TaskDetailComponent,
    CategoriesCompComponent,
    LoginCompComponent,
    AddTaskCompComponent,
    UserCompComponent,
    CategoryAddComponent,
    CategoryDetailComponent,
   ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatIconModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
