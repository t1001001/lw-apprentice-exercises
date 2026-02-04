from pydantic import BaseModel, Field

class Book(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    author: str = Field(alias="author")
    price: float = Field(alias="price")

class BookCreate(BaseModel):
    name: str = Field(alias="name")
    author: str = Field(alias="author")
    price: float = Field(alias="price")

class BookUpdate(BaseModel):
    name: str = Field(alias="name")
    author: str = Field(alias="author")
    price: float = Field(alias="price")