from pydantic import BaseModel


# Базовая схема
class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str | None = None


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
    status: str


# Схема для обновления данных задачи
class UpdateTask(BaseModel):
    title: str
    description: str
