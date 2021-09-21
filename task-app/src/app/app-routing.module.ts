import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoriesCompComponent } from './components/categories-comp/categories-comp.component';
import { CategoryDetailComponent } from './components/category-detail/category-detail.component';
import { DashboardCompComponent } from './components/dashboard-comp/dashboard-comp.component';
import { LoginCompComponent } from './components/login-comp/login-comp.component';
import { TaskDetailComponent } from './components/task-detail/task-detail.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { TasksCompComponent } from './components/tasks-comp/tasks-comp.component';

const routes: Routes = [
  {path:'tasks', component: TasksCompComponent},
  {path:'dashboard', component: DashboardCompComponent},
  {path:'tasklist', component: TaskListComponent},
  {path:'taskdetail/:taskId', component: TaskDetailComponent},
  {path:'categorydetail/:categoryId', component: CategoryDetailComponent},
  {path:'categories', component: CategoriesCompComponent},
  {path:'login', component: LoginCompComponent},
  {path: '**', redirectTo: 'dashboard', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
