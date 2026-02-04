import uuid
from typing import List, Optional
from app.models.models import Book, BookCreate, BookUpdate

class BookService:
    def __init__(self):
        self._books: List[Book] = []
        self._id = str(uuid.uuid4())

    def get_all_books(self):
        return self._books
    
    def get_book_by_id(self, id: str) -> Optional[Book]:
        for book in self._books:
            if id == book.id:
                return book
        return None
    
    def create_book(self, data: BookCreate) -> Book:
        book = Book(
            id=self._id,
            **data.model_dump()
        )
        self._books.append(book)
        return book
    
    def delete_book(self, id: str) -> bool:
        for book in self._books:
            if id == book.id:
                self._books.remove(book)
                return True
        return False
    
    def update_book(self, book_id: int, data: BookUpdate) -> Optional[Book]:
        for index, book in enumerate(self._books):
            if book.id == book_id:
                updated = book.model_copy(update=data.model_dump())
                self._books[index] = updated
                return updated
        return None