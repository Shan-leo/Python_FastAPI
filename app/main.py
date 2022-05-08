from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


class PostSchema(BaseModel):
    title: str
    content: str
    published: bool = True


try:
    conn = psycopg2.connect(host = 'localhost', database='fastapi', user='postgres', password='Coolipso2022', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successfully")

except Exception as error:
    print(f"Connection failed"
          f"Error was {error}")


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/posts")
def get_posts():
    return {"data": "Those are your posts"}


@app.post("/posts")
def create_posts(post: PostSchema):
    print(post)
    print(post.dict())
    return {"message": "Post created successfully", "pp": post}
