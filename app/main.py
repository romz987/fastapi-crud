from app import schemas, crud
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
# oth 
from app.context_manager import get_db

app = FastAPI()


@app.get("/")
async def root():
    return { "roman": "it works!" }

# Добавить задачу
@app.post("/tasks/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

# Получить список задач
@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

# Получить задачу по id
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# Удалить задачу по id 
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return None

# Изменить статус задачи по id 
@app.patch("/tasks/{task_id}", response_model=schemas.Task)
def change_status(task_id: int, status: schemas.ChangeStatus, db: Session = Depends(get_db)):
    db_task = crud.change_status(db, task_id=task_id, status=status)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
