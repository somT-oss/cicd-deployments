from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Book
from .schemas import BookRead

router = APIRouter(prefix="/api/books", tags=["Books"])

# Create DB tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def create_book(book: dict, db: Session = Depends(get_db)):
    new_book = Book(**book)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"msg": "New book has been added"}

@router.get("/", response_model=list[BookRead])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.get("/{book_id}", response_model=dict)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book.id, "title": book.title, "author": book.author, "year": book.year}

@router.delete("/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
