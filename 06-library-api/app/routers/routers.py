from fastapi import APIRouter, HTTPException, Depends
from app.models.models import Book, BookCreate, BookUpdate
from app.services.services import BookService

router = APIRouter()

service = BookService()
def get_service() -> BookService:
    return service

@router.get("/")
def root():
    return {"message": "Hello World!"}

@router.get("/books", response_model=list[Book])
def list_books(service: BookService = Depends(get_service)):
    return service.get_all_books()

@router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: str, service: BookService = Depends(get_service)):
    book = service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book

@router.post("/books", response_model=Book)
def create_book(data: BookCreate, service: BookService = Depends(get_service)):
    return service.create_book(data)

@router.delete("/books/{book_id}")
def delete_book(book_id: str, service: BookService = Depends(get_service)):
    ok = service.delete_book(book_id)
    if not ok:
        raise HTTPException(404, "Book not found")
    return {"message": "Book deleted"}

@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: str, data: BookUpdate, service: BookService = Depends(get_service)):
    updated = service.update_book(book_id, data)
    if not updated:
        raise HTTPException(404, "Book not found")
    return updated

def get_router() -> APIRouter:
    return router