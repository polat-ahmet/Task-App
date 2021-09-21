import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CategoriesServService } from 'src/app/services/categories-serv.service';

@Component({
  selector: 'app-category-add',
  templateUrl: './category-add.component.html',
  styleUrls: ['./category-add.component.css'],
  providers:[CategoriesServService]
})
export class CategoryAddComponent implements OnInit {

  constructor(private categoryService:CategoriesServService, private formBuilder:FormBuilder) { }

  category_name!: string;
  categoryAddForm!: FormGroup;

  ngOnInit() {
    this.createCategoryForm();
  }
  
  createCategoryForm(){
    this.categoryAddForm = this.formBuilder.group({
      name:["",Validators.required]
    })
  }

  add(){
    if(this.categoryAddForm.valid){
      this.category_name = this.categoryAddForm.value.name
      this.categoryService.addCategory(this.category_name);
      window.location.reload();
    }
  }

}
