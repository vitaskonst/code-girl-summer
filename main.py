from fastapi import FastAPI
from posts.router import router as posts_router 

app = FastAPI()

app.include_router(posts_router, prefix="/posts")

