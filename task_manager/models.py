from __future__ import annotations
from datetime import datetime
from typing import Dict, Any

class Task:
    def __init__(self,task_id:int , description:str, status:str = "todo" , created_at: str = None , updated_at:str =None):
        self.id = task_id
        self.description = description.strip()
        self.status = status
        current_time = datetime.now().isoformat()
        self.created_at = created_at if created_at else current_time
        self.updated_at = updated_at if updated_at else current_time

    def to_dict(self) -> Dict[str , Any]:
        """Serializes the object properties into a standard Python dictionary"""
        return{
            "id": self.id,
            "description":self.description,
            "status":self.status,
            "createdAt": self.created_at,
            "updatedAt":self.updated_at
        }
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Task:
        """Instantiates a Task object safely from a dictionary structure"""
        return cls(
            task_id=data["id"],
            description=data["description"],
            status=data["status"],
            created_at=data["createdAt"], 
            updated_at=data["updatedAt"]   
           )
