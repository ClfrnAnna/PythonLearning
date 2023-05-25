from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: str
    status: str
    difficulty_level: int
    student_id: int
    lesson_id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class TasksSchema(BaseModel):
    tasks: list[TaskSchema]


class TaskCreationSchema(BaseModel):
    status: str
    difficulty_level: int
    student_id: int
    lesson_id: int


class TaskChangeSchema(BaseModel):
    status: str | None
    difficulty_level: int | None
