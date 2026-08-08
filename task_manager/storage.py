import os 
import json
from typing import List ,  Dict , Any

JSON_FILE = "tasks.json"

def load_raw_tasks() -> List[Dict[str , Any]]:
    """Reads raw dictionary items from the JSON database file safely""" 
    if not os.path.exists(JSON_FILE):
        return[]

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except(json.JSONDecodeError,PermissionError):
        return[]

def save_raw_task(tasks_data: List[Dict[str, Any]] ) -> None:
    """Writes the raw payload array back into the local system file cleanly"""
    try:
        with open(JSON_FILE, "w", encoding= "utf-8") as file:
            json.dump(tasks_data , file , indent=4)
    except IOError as e:
        print(f"Critical System Error: Failed to write data to disk. Details: {e}")
