
from pydantic import BaseModel

class CastIn(BaseModel):
    name: str
    nationality: str

class CastOut(CastIn):
    id: int

class CastUpdate(CastIn):
    name: str | None = None 
