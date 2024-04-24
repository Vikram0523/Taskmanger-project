class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return "ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, status):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description, priority, status)
        self.tasks.append(task)
        print("Task added successfully.")

    def edit_task(self, task_id, new_title, new_description, new_priority, new_status):
        task = self.get_task_by_id(task_id)
        if task:
            task.title = new_title
            task.description = new_description
            task.priority = new_priority
            task.status = new_status
            print("Task updated successfully.")
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print("Task deleted successfully.")
        else:
            print("Invalid task ID.")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print("No tasks found.")

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if filtered_tasks:
            for task in filtered_tasks:
                print(task)
        else:
            print(f"No tasks found with priority '{priority}'.")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")

        choice = input("Enter your choice(1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            status = input("Enter task status (Pending/In Progress/Completed): ")
            task_manager.add_task(title, description, priority, status)
        elif choice == "2":
            task_id = int(input("Enter task ID to edit: "))
            new_title = input("Enter new task title: ")
            new_description = input("Enter new task description: ")
            new_priority = input("Enter new task priority (High/Medium/Low): ")
            new_status = input("Enter new task status (Pending/In Progress/Completed): ")
            task_manager.edit_task(task_id, new_title, new_description, new_priority, new_status)
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "4":
            task_manager.view_all_tasks()
        elif choice == "5":
            priority = input("Enter priority to filter tasks (High/Medium/Low): ")
            task_manager.filter_tasks_by_priority(priority)
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            

