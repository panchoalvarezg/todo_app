from views.task_view import TaskView
from storage.task_repo import TaskRepo
from models.task import Task

class TaskController:
    def __init__(self):
        self.view = TaskView()
        self.repo = TaskRepo()

    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Selecciona una opción: ")

            if choice == '1':
                title = input("Título: ")
                description = input("Descripción: ")
                task = Task(title, description)
                self.repo.add_task(task)
                print("\n✅ Tarea agregada con éxito.\n")

            elif choice == '2':
                tasks = self.repo.get_all_tasks()
                self.view.display_tasks(tasks)

            elif choice == '3':
                task_id = int(input("ID de la tarea a completar: "))
                if self.repo.complete_task(task_id):
                    print("\n✅ Tarea marcada como completada.\n")
                else:
                    print("\n❌ Tarea no encontrada.\n")

            elif choice == '4':
                task_id = int(input("ID de la tarea a eliminar: "))
                if self.repo.delete_task(task_id):
                    print("\n🗑️ Tarea eliminada.\n")
                else:
                    print("\n❌ Tarea no encontrada.\n")

            elif choice == '5':
                print("\n👋 Saliendo de la aplicación...")
                break

            else:
                print("\n❌ Opción no válida.\n")
