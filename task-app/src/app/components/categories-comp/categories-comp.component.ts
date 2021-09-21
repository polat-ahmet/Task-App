import { Component, OnInit } from '@angular/core';
import { Category } from 'src/app/models/category';
import { CategoriesServService } from 'src/app/services/categories-serv.service';

@Component({
  selector: 'app-categories-comp',
  templateUrl: './categories-comp.component.html',
  styleUrls: ['./categories-comp.component.css'],
  providers: [CategoriesServService]
})
export class CategoriesCompComponent implements OnInit {

  constructor(private CategoriesService:CategoriesServService) { }

  categories!: Category[];

  ngOnInit() {
    this.CategoriesService.getAllCategories().subscribe(data=>{
      this.categories = data;
    })
  }

  deleteCategory(id:number){
    this.CategoriesService.deleteCategory(id);
    window.location.reload();
  }

}
