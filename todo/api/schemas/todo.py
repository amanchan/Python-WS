from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from api.models.todo import Todo

GetTodo = pydantic_model_creator(Todo, name="Todo")


class PostTodo(BaseModel):
    task: str = Field(..., max_length=300)
    done: bool


class PutTodo(BaseModel):
    task: str | None = Field(None, max_length=300)
    done: bool = Field(default=False)
