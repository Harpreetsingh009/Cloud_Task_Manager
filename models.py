# import  rerquired SQLAlchemy columns
from sqlalchemy import Column, Integer, String

# import base class
from database import Base

# create Task table
class Task(Base):
    
    # Table Name
    __tablename__ = "tasks"
    
    # primary key
    id = Column(Integer, primary_key=True)
    
    # Task Title
    task_title = Column(String , nullable=False)
    
    # Task Description
    description = Column(String)
    
    # Employee Assigned
    assigned_to = Column(String)
    
    # priority 
    priority = Column(String)
    
    # Task Status
    status = Column(String)
    
    # due Date
    due_date = Column(String)
    
    # created by
    created_by = Column(String)
    
# this file only defines the structure of the table , and think of its as a blueprint

