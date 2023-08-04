from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile
from starlette.middleware.cors import CORSMiddleware
from posts.router import router as posts_router 
from users.router import router as users_router
from database import database
from typing import List

import cloudinary
from cloudinary.uploader import upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post('/images')
def upload_files(files: List[UploadFile]):
    urls = []
    for file in files:
        result = upload(file.file.read())
        urls.append(result['secure_url'])

    return {
        'urls': urls
    }


app.include_router(posts_router, prefix="/posts", tags=["Posts"])
app.include_router(users_router, prefix="/users", tags=["Users"])

