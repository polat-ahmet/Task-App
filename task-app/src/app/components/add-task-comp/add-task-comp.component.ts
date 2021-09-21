import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Task } from 'src/app/models/task';
import { TaskServService } from 'src/app/services/task-serv.service';


@Component({
  selector: 'app-add-task-comp',
  templateUrl: './add-task-comp.component.html',
  styleUrls: ['./add-task-comp.component.css'],
  providers:[TaskServService]
})
export class AddTaskCompComponent implements OnInit {

  constructor(private formBuilder:FormBuilder, private taskService:TaskServService) { }

  task!: Task;
  taskAddForm!: FormGroup;

  ngOnInit() {
    this.createTaskForm();
  }

  createTaskForm(){
    this.taskAddForm = this.formBuilder.group({
      header:["",Validators.required],
      description:["",Validators.required]
    })
  }

  add(){
    if(this.taskAddForm.valid){
      this.task = Object.assign({}, this.taskAddForm.value);
      this.taskService.addTask(this.task);
      window.location.reload();
    }
  }

}
