
from pydantic import BaseModel

class MovieIn(BaseModel):
    name: str
    plot: str
    generes: list[str]
    casts_id: list[int]

class MovieOut(MovieIn):
    id: int

class MovieUpdate(MovieIn):
    name: str | None = None 
    plot: str | None = None 
    generes: list[str] | None = None 
    casts: list[int] | None = None 