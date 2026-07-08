# import BaseModel
from pydantic import BaseModel

# task creation schema
class TaskSchema(BaseModel):
    
    # Task Title
    task_title: str
    
    # Task Description
    description: str
    
    # Employee Assigned
    assigned_to: str
    
    # priority
    priority: str
    
    # Status
    status: str
    
    # due Date
    due_date: str
    
    # created by
    created_by : str  
    




    