import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Task } from '../models/task';

@Injectable({
  providedIn: 'root'
})
export class TaskServService {

  constructor(private httpClient:HttpClient) { }

  path="http://127.0.0.1:5000/"; 


  getAllTasks():Observable<Task[]>{
    return this.httpClient.get<Task[]>(this.path+"alltasksinformation")
  }

  getTaskByTaskId(id:number):Observable<Task>{
    return this.httpClient.get<Task>(this.path+"taskinformation/"+id)
  }

  addTask(task:Task){
    this.httpClient.post<Task>(this.path+"taskadd/1?header="+task.header+"&description"+task.description+"&priority=çok önemli&due_date=1111111", task).subscribe();
  }

  deleteTask(id:number){
    this.httpClient.delete<Task>(this.path+"taskedit/"+id).subscribe();
  }

  removeCategoryFromTask(taskId:number, categoryId:number){
    this.httpClient.delete<Task>(this.path+"removetaskfromcategory/"+categoryId+"?task_id="+taskId).subscribe();
  }

  addTaskToCategory(taskId:number, categoryId:number){
    this.httpClient.post<Task>(this.path+"addtasktocategory/"+categoryId, { task_id: taskId }).subscribe();
  }

}
