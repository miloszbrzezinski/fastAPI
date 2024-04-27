from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    rating: int = 5

my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}

# @app.post("/create")
# def create_posts(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

@app.post("/posts")
def create_posts(new_post: Post):
    post_dict = new_post.model_dump()
    post_dict['id'] = randrange(0, 10000000)
    my_post.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}