from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None

class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True

class BookCreate(BookBase):
    pass
