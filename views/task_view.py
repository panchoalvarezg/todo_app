class TaskView:
    def display_menu(self):
        print("\n--- TODO APP ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

    def display_tasks(self, tasks):
        if not tasks:
            print("\n📭 No hay tareas.")
        else:
            print("\n📋 Lista de tareas:")
            for idx, task in enumerate(tasks):
                status = "✅" if task.completed else "⏳"
                print(f"{idx}. [{status}] {task.title} - {task.description}")

