import sys
from manager import TaskManager

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [command] [arguments]")
        print("Commands: add, update, delete, list, mark-in-progress, mark-done")
        return

    command = sys.argv[1].lower().strip()
    manager = TaskManager()

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
            print('Example: python task_cli.py add "Buy groceries"')
            return

        description = sys.argv[2]
        new_id = manager.add_task(description)
        print(f"Task added successfully (ID: {new_id})")

    else:
        print(f"Unknown command: '{command}'")

if __name__ == "__main__":
    main()
