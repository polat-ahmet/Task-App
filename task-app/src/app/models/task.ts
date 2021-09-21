import { Category } from "./category";
import { TaskPriority } from "./task-priority.enum"; 
import { TaskStateMy } from "./task-state.enum";
  
  export class Task {
    id!: number;
    header!: string;
    description!: string;
    state!: TaskStateMy;
    priority!: TaskPriority;
    due_date!: string;
    created_date!: string;
    updated_date!: string;
    categories!: Category[];
  }