from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/users/{user_id}")
def read_user(user_id: int, q: str = None):
    return {"user_id": user_id, "q": q}