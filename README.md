https://roadmap.sh/projects/task-tracker

#  Task Tracker CLI

This is a simple tool to help you track your daily to-do lists straight from your terminal. It saves everything locally into a `tasks.json` file. 

I wrote this from scratch in Python without using any external frameworks, focusing on clean code layout and solid file handling.

##  How the Code is Split Up
Instead of dumping everything into one huge file, I broke it down into separate pieces so it is easy to read and update:
- `models.py`: Tells Python what a Task looks like (ID, text, status, and timestamps).
- `storage.py`: Handles saving and loading the JSON file. It keeps the app safe from crashing if the database file gets missing or deleted.
- `manager.py`: The core engine. It manages tasks in memory and calculates new unique IDs automatically.
- `task_cli.py`: The interface. It reads what you type into your keyboard and triggers the right code.

---

##  How to Run It

This project uses **`uv`** to keep the environment fast and clean. 

1. **Clone the repo and enter the folder:**
   ```bash
   git clone https://github.com
   cd projects/task_manager
   ```

2. **See how to use it:**
   Run the file without any words to see the usage rules:
   ```bash
   uv run task_cli.py
   ```

3. **Add a task:**
   Type `add` followed by your task inside quotes:
   ```bash
   uv run task_cli.py add "Finish my LeetCode goals"
   ```
   **Output on screen:**
   ```text
   Task added successfully (ID: 1)
   ```

---

## 💾 What the saved file looks like
When you add a task, it automatically creates or updates a `tasks.json` file right in your directory:

```json
[
    {
        "id": 1,
        "description": "Finish my LeetCode goals",
        "status": "todo",
        "createdAt": "2026-08-08T16:30:00",
        "updatedAt": "2026-08-08T16:30:00"
    }
]
```
