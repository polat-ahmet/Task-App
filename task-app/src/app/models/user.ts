import { Task } from "./task";

export class User {
    id!: number;
    username!: string;
    email!: string;
    password!: string;
    created_date!: string;
    updated_date!: string;
    tasks!: Task[];
}
