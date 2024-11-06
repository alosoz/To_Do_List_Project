from task import Task
from task_manager import TaskManager

class main:
    

    def main():
        manager = TaskManager()
        while True:
            print("\n1. Add Task\n2. Delete Task\n3. Update Task\n4.List of Tasks\n5. Exit")
            choice = input("Chouse an option")

            if choice == '1':
                title = input('Task Title: ')
                description = input("Task description: ")
                manager.add_task(title, description)

            elif choice == '2':
                title = input("Title of the task to be deleted:")
                manager.remove_task(title)

            elif choice == '3':
                title = input("Title of the task to be update: ")
                new_title = input("New title: ")
                description = input("New description: ")
                completed = input("Complated? (yes/no): ").strip().lower() == 'yes'
                manager.update_task(title, title=new_title or title, description=description, completed=completed)

            elif choice == '4':
                manager.list_tasks()

            elif choice == '5':
                break
            
            else:
                print('Invalid selection. Please try again.')

if __name__ == "__main__":
    main.main()