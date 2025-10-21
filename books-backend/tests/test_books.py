from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_books():
    # Create a new book
    response = client.post("/api/books/", json={"title": "1984", "author": "Orwell", "year": 1949})
    assert response.status_code == 200
    data = response.json()
    assert data["msg"] == "New book has been added"

    # Retrieve all books
    response = client.get("/api/books/")
    assert response.status_code == 200
    books = response.json()
    assert len(books) >= 1

def test_book_not_found():
    response = client.get("/api/books/999")
    assert response.status_code == 404
