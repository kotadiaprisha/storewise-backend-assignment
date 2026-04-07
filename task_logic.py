from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,desc
from app.main import *
from app.models import *
from sqlalchemy.orm import Session,aliased
from datetime import datetime, timedelta

DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def question2(db: Session):
    tasks = db.query(Task).order_by(desc(Task.created_at)).all()
    grouped_tasks = {}

    for task in tasks:
        key = str(task.parent_id)
        if task.parent_id is not None: 
            else:"null"
        
        if key not in grouped_tasks:
            grouped_tasks[key]=[]

        grouped_tasks[key].append({
            "id" : task.id,
            "title" : task.title,
            "part_id" : task.parent_id,
            "created_at" : str(task.creted_at)
        })

    return grouped_tasks


def question3(db: Session):
    today = datetime.utcnow().date()
    tommorow = today + timedelta(days=1)

    tasks = db.query(Task).filter(
        Task.priority==1,
        Task.due_date >=today,
        Task.due_date < tommorow + timedelta(days=1)
        ).all()
    
    result = []

    for task in tasks:
        result.append({
            "id":task.id,
            "name":task.title,
            "due_date":str(task.due_date),
            "priority":task.priority
        })

        return result


def question4(db: Session):
    TaskAlias = aliased(Task)

    tasks = db.query(Task).outerjoin(TaskAlias,Task.id==TaskAlias.parent_id).filter(Task.parent_id==None, TaskAlias.id==None).all()
    
    result=[]

    for task in tasks:
        result.append({
            "id":task.id,
            "name":task.title,
            "parent_id":task.parent_id,
            "created_at":str(task.created_at)
        })

        return result


def question5(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id==task_id).first()

    if not task:
        return {"error":"Task not found"}
    else:
        print("Task_id:",task_id)
        print("Parent_id:",task.parent_id)

    if task.parent_id is None:
        return {
            "task_id":task_id,
            "siblings_count":0,
            "reason":"this task has no parent_id"
        }
    
    siblings = db.query(Task).filter(Task.parent_id==task.parent_id,Task.id !=task_id).count()

    return{
        "task_id":task_id,
        "sibling_count":len(siblings)
    }


def question6(tasks, query: str):
    pass


def question7(tasks):
    pass


def question8(tasks, criteria: dict, sort_by: str):
    
    raise HTTPException(status_code=401, detail="For this task, 8, you are expected to solve it using SQLAlchemy. Please don't use this function, and return the result directly from the ")


def question9(tasks, worker_threads: int):
    pass