from app import schemas, crud
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status

# oth
from app.context_manager import get_db

app = FastAPI()


# Добавить задачу
@app.post(
    "/api/tasks/",
    response_model=schemas.Task,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


# Получить список задач
@app.get("/api/tasks/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks


# Получить задачу по id
@app.get("/api/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


# Обновить данные задачи
@app.put("/api/tasks/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int, data: schemas.UpdateTask, db: Session = Depends(get_db)
):
    db_task = crud.update_task(db, task_id=task_id, data=data)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


# Удалить задачу по id
@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return None


# Изменить статус задачи по id
@app.patch("/api/tasks/{task_id}", response_model=schemas.Task)
def change_status(
    task_id: int,
    status: schemas.ChangeStatus,
    db: Session = Depends(get_db),
):
    db_task = crud.change_status(db, task_id=task_id, status=status)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
