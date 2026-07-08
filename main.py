# import FastAPI 
from fastapi import FastAPI , Depends


from sqlalchemy.orm import Session

from database import get_db

from schemas import TaskSchema


# import Base and Engine
from database import Base, engine

# import Task Table
from models import Task


# connects to Neon and check whether the "Tasks" Table exists , if not then create it

Base.metadata.create_all(bind=engine)

# here , Base conatins all database table definations
# and engine  , contains the cloud database connection

# create FastAPI Object
app = FastAPI()

# home API
@app.get("/")
def home():
    
    return {"message": "Welcome to Cloud Management API!"}

# this API tells that : FastAPI is running and the application started successfully

# now run the project using uvicorn main:app --reload


# as per day_2
# post Method
@app.post("/create_task")
def create_task(task : TaskSchema , db: Session = Depends(get_db)):
    
    # create Task Object
    new_task = Task(task_title = task.task_title , description = task.description , assigned_to = task.assigned_to , 
                    priority = task.priority , status = task.status , due_date = task.due_date ,
                    created_by = task.created_by)


    # add task 
    db.add(new_task)
    
    # commit Changes
    db.commit()
    
    #refresh Object
    db.refresh(new_task)
    

    # return Response 
    return{"message": "Task created Successfully"}

# the data sent from Postman is first validated by the TaskSchema (Pydantic schema) , if it is valid , the values
# are then copied into the Task model , which represents the datbase table , and finally store in the database

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    
    tasks = db.query(Task).all()
    
    return tasks


