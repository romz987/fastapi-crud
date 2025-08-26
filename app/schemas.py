from enum import Enum
from pydantic import BaseModel


# Диапазон значений для Status 
class StatusEnum(str, Enum):
    created = "created"
    in_process = "in progress"
    done = "done"


# Базовая схема
class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: StatusEnum | None = None


# Схема для создания задачи
class TaskCreate(TaskBase):
    pass


# Схема для отображения задачи
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


# Схема для изменения статуса задачи
class ChangeStatus(BaseModel):
    status: StatusEnum


# Схема для обновления данных задачи
class UpdateTask(BaseModel):
    title: str | None = None
    description: str | None = None
