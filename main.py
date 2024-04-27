from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/posts")
def get_posts():
    return {"data": "array of posts"}

# @app.post("/create")
# def create_posts(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post)
    return {""}