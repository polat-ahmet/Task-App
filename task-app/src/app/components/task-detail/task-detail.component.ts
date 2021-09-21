import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Category } from 'src/app/models/category';
import { Task } from 'src/app/models/task';
import { CategoriesServService } from 'src/app/services/categories-serv.service';
import { TaskServService } from 'src/app/services/task-serv.service';

@Component({
  selector: 'app-task-detail',
  templateUrl: './task-detail.component.html',
  styleUrls: ['./task-detail.component.css'],
  providers:[TaskServService, CategoriesServService] 
})
export class TaskDetailComponent implements OnInit {

  constructor(private activatedRoute:ActivatedRoute, 
    private taskService:TaskServService,
    private categoryService:CategoriesServService,
    private formBuilder:FormBuilder) { }

  task!:Task;
  categories!:Category[];
  all_categories!:Category[];

  add_category_id!: number;
  addCategoryForm!:FormGroup;

  ngOnInit() {
    this.activatedRoute.params.subscribe(params=>{
      this.getTaskByTaskId(params["taskId"]),
      this.getAllCategories()
    });
    this.createAddCategoryForm();
  }

  createAddCategoryForm(){
    this.addCategoryForm = this.formBuilder.group({
      category_id:["",Validators.required]
    })
  }

  getTaskByTaskId(taskId:number){
    this.taskService.getTaskByTaskId(taskId).subscribe(data=>{
      this.task = data;
      this.categories=this.task.categories;
    })
  }

  getAllCategories(){
    this.categoryService.getAllCategories().subscribe(data=>{
      this.all_categories = data;
    })
  }

  removeCategoryFromTask(categoryId:number){
    this.taskService.removeCategoryFromTask(this.task.id, categoryId);
    window.location.reload();
  }

  addTaskToCategory(){
    if(this.addCategoryForm.valid){
      this.add_category_id = this.addCategoryForm.value.category_id
      this.taskService.addTaskToCategory(this.task.id, this.add_category_id);
      window.location.reload();
    }
  }

}
