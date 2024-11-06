import json

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data.get("completed", False))

class TaskManager:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def update_task(self, title, updates):
        for task in self.tasks:
            if task.title == title:
                task.description = updates.get("description", task.description)
                task.completed = updates.get("completed", task.completed)
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("Henüz bir görev yok.")
        for task in self.tasks:
            status = "Tamamlandı" if task.completed else "Tamamlanmadı"
            print(f"{task.title} - {task.description} [{status}]")

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                return [Task.from_dict(task) for task in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def main():
    task_manager = TaskManager()

    while True:
        print("\n--- Görev Yönetim Uygulaması ---")
        print("1. Görev Ekle")
        print("2. Görev Sil")
        print("3. Görev Güncelle")
        print("4. Görevleri Listele")
        print("5. Çıkış")

        choice = input("Bir seçenek girin: ")

        if choice == "1":
            title = input("Görev başlığı: ")
            description = input("Görev açıklaması: ")
            task_manager.add_task(title, description)
            print("Görev eklendi.")

        elif choice == "2":
            title = input("Silmek istediğiniz görevin başlığı: ")
            task_manager.remove_task(title)
            print("Görev silindi.")

        elif choice == "3":
            title = input("Güncellemek istediğiniz görevin başlığı: ")
            description = input("Yeni açıklama (boş bırakılırsa değişmez): ")
            completed_input = input("Tamamlandı mı? (evet/hayır): ").strip().lower()
            completed = True if completed_input == "evet" else False

            updates = {}
            if description:
                updates["description"] = description
            updates["completed"] = completed

            task_manager.update_task(title, updates)
            print("Görev güncellendi.")

        elif choice == "4":
            task_manager.list_tasks()

        elif choice == "5":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()