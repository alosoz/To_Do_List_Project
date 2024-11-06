from task import Task
import json

class TaskManager:

    def __init__ (self, file_path = "tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def add_task (self, title, description):
        self.tasks.append(Task(title, description))
        self.save_tasks()

    def remove_task (self, title):
        for task in self.tasks:
            if task.title != title:
                self.tasks.delete()
        self.save_tasks()

    def update_task (self, title, updates):
        for task in self.tasks:
            if task.title == title:
                task.title = updates.get('description', task.description)
                task.completed = updates.get('completed', task.completed)
        self.save_tasks()
    
    def list_tasks(self):
        for task in self.tasks:
            if task.completed:
                status = 'Complated'
            else:
                status = 'Not Complated'
            print(f"{task.title} - {task.description} [{status}]")

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            tasks_as_dicts = []
            for task in self.tasks:
                task_dict = task.to_dict()
                tasks_as_dicts.append(task_dict)

            json.dump(tasks_as_dicts, file, indent=4)
            #yukarudaki kodlarin bir satirda kisa yazilisi
            # json.dump([task.to_dict() for task in self.tasks], file, indent=4)


    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
                tasks_list = []
                for task_data in tasks_data:
                    task = Task.from_dict(task_data)
                    tasks_list.append(task)

            return tasks_list
        
                #yukarudaki kodlarin bir satirda kisa yazilisi
                #return[Task.from_dick(task) for task in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    