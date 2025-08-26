from sqlalchemy.orm import Session
from db import models
import schemas


# Функция для создания новой задачи
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title, description=task.description, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Функция для получения задачи по ID
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# Функция для получения списка задач с возможностью пагинации
def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()

# Функция для удаления задачи по ID
def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None

# Изменить статус задачи
def change_status(db: Session, task_id: int, status: schemas.ChangeStatus):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.status = status.status # pyright: ignore
        db.commit()
        db.refresh(db_task)
        return db_task
    return None
