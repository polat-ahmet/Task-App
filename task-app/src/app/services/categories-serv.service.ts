import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Category } from '../models/category';

@Injectable({
  providedIn: 'root'
})
export class CategoriesServService {

  constructor(private httpClient:HttpClient) { }

  path="http://127.0.0.1:5000/";

  getAllCategories():Observable<Category[]>{
    return this.httpClient.get<Category[]>(this.path+"allcategoriesinformation")
  }
  getCategoryByCategoryId(id:number):Observable<Category>{
    return this.httpClient.get<Category>(this.path+"categoryinformation/"+id)
  }

  addCategory(name:String){
    this.httpClient.post<Category>(this.path+"categoryadd?name="+name, name).subscribe();
  }

  deleteCategory(id:number){
    this.httpClient.delete<Category>(this.path+"categoryedit/"+id).subscribe();
  }

}
