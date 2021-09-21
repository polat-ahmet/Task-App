import { Component, OnInit } from '@angular/core';
//import { abort } from 'process';
import { Observable } from 'rxjs';
import { Task } from 'src/app/models/task';
import { TaskServService } from '../../services/task-serv.service';

@Component({
  selector: 'app-tasks-comp',
  templateUrl: './tasks-comp.component.html',
  styleUrls: ['./tasks-comp.component.css'],
  providers: [TaskServService]
})
export class TasksCompComponent implements OnInit {

  constructor(private taskService:TaskServService) {}

  tasks: Task[] = [];
  
  ngOnInit() {
    this.taskService.getAllTasks().subscribe(data =>{
      this.tasks = data;
    })
  }

  deleteTask(id:number){
    this.taskService.deleteTask(id);
    window.location.reload();
  }
  

}
