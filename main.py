# todo_list.py

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[ {status} ] {self.title} - {self.description} (Due: {self.due_date}, Priority: {self.priority})"


def main():
    tasks = []

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear To-Do List")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority (Low/Medium/High): ")
            tasks.append(Task(title, description, due_date, priority))
            print("Task added successfully!")

        elif choice == "2":
            if not tasks:
                print("The to-do list is empty.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("The to-do list is empty.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                task_number = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1].mark_as_completed()
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

        elif choice == "4":
            tasks.clear()
            print("To-do list cleared!")

        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
