import { Task } from "./task";

export class Category {
    id!: number;
    name!: string;
    created_date!: string;
    updated_date!: string;
    tasks!: Task[];
}
