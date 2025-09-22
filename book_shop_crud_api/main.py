from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

list_books = []

# @app.get("/{name}")
# def read_api(name: str):
#     return {"Welcome": name}

@app.get("/")
def read_api():
    return list_books

@app.post("/")
def create_book(book: Book):
    list_books.append(book)
    return book

@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    counter = 0
    for x in list_books:
        counter += 1
        if x.id == book_id:
            list_books[counter-1] = book
            return list_books[counter-1]
    raise HTTPException (
        status_code=404,
        detail=f"Id {book_id}: Does not exist !!"
    )

@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0
    for x in list_books:
        if x.id == book_id:
            del list_books[counter-1]
            return f"Id: {book_id} deleted"
    raise HTTPException (
        status_code=404,
        detail=f"Id {book_id} : Does not exist"
    )