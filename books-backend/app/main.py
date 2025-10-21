from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Books API")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Books API!"}
