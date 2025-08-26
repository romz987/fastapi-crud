from sqlalchemy.orm import Session
from app.db import models
from app import schemas
from app.db.models import Task


# Функция для создания новой задачи
def create_task(db: Session, task: schemas.TaskCreate) -> Task:
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# Изменить данные задачи
def update_task(
    db: Session,
    task_id: int,
    data: schemas.UpdateTask,
) -> Task | None:
    db_task = get_task(db, task_id)
    if db_task:
        db_task.title = data.title # pyright: ignore
        db_task.description = data.description # pyright: ignore
        db.commit()
        db.refresh(db_task)
        return db_task
    return None


# Функция для получения задачи по ID
def get_task(db: Session, task_id: int) -> Task | None:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


# Функция для получения списка задач
def get_tasks(db: Session) -> list[Task]:
    return db.query(models.Task).all()


# Функция для удаления задачи по ID
def delete_task(db: Session, task_id: int) -> Task | None:
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None


# Изменить статус задачи
def change_status(
    db: Session,
    task_id: int,
    status: schemas.ChangeStatus,
) -> Task | None:
    db_task = get_task(db, task_id)
    if db_task:
        db_task.status = status.status  # pyright: ignore
        db.commit()
        db.refresh(db_task)
        return db_task
    return None
