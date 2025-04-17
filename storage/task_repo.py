import json
import os
from models.task import Task

class TaskRepo:
    def __init__(self, filepath="storage/task.json"):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)

    def get_all_tasks(self):
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            return [Task.from_dict(d) for d in data]

    def save_all_tasks(self, tasks):
        with open(self.filepath, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=2)

    def add_task(self, task):
        tasks = self.get_all_tasks()
        tasks.append(task)
        self.save_all_tasks(tasks)

    def complete_task(self, task_id):
        tasks = self.get_all_tasks()
        if 0 <= task_id < len(tasks):
            tasks[task_id].completed = True
            self.save_all_tasks(tasks)
            return True
        return False

    def delete_task(self, task_id):
        tasks = self.get_all_tasks()
        if 0 <= task_id < len(tasks):
            del tasks[task_id]
            self.save_all_tasks(tasks)
            return True
        return False
