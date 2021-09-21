import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Category } from 'src/app/models/category';
import { CategoriesServService } from 'src/app/services/categories-serv.service';
import { TaskServService } from 'src/app/services/task-serv.service';

@Component({
  selector: 'app-category-detail',
  templateUrl: './category-detail.component.html',
  styleUrls: ['./category-detail.component.css'],
  providers:[CategoriesServService, TaskServService]
})
export class CategoryDetailComponent implements OnInit {

  constructor(private activatedRoute: ActivatedRoute, 
    private categoryService:CategoriesServService,
    private taskService:TaskServService) { }

  category!: Category;

  ngOnInit() {
    this.activatedRoute.params.subscribe(params=>{
      this.getCategoryByCategoryId(params["categoryId"])
    })
  }

  getCategoryByCategoryId(id:number){
    this.categoryService.getCategoryByCategoryId(id).subscribe(data=>{
      this.category = data;
    })
  }
  deleteTask(taskId:number){
    this.taskService.deleteTask(taskId);
    window.location.reload();
  }

}
