from fastapi import FastAPI
from posts.router import router as posts_router 
from users.router import router as users_router
from database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(posts_router, prefix="/posts", tags=["Posts"])
app.include_router(users_router, prefix="/users", tags=["Users"])

