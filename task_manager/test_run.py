from manager import TaskManager

manager = TaskManager()
try:
    new_id = manager.add_task("Review algorathemis complexities")
    print(f"Success task added successfully (ID: {new_id})")
except ValueError as e:
    print(f"Handled Error: {e}")
    
