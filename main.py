from fastapi import FastAPI, HTTPException
from posts.router import router as posts_router 
from users.router import router as users_router
from database import database
import requests

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


def get_dog_image_url():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["message"]
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve the dog image")

@app.get("/dogs/image")
async def get_dog_image():
    try:
        image_url = get_dog_image_url()
        return {"image_url": image_url}
    except HTTPException as e:
        raise e

app.include_router(posts_router, prefix="/posts", tags=["Posts"])
app.include_router(users_router, prefix="/users", tags=["Users"])

