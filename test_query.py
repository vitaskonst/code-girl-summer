from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

import os
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/posts/generate-ad-text')
def genenerate_ad():
    token = os.environ.get("TOKEN")

    headers = {
        'Authorization': "Bearer " + token
    }

    keywords = "laptop, LENOVO, Intel Core i5, Nvidia, Windows 11"
    
    response = requests.post('https://7583-185-48-148-173.ngrok-free.app/advertisement', headers=headers, json={
        "input_text": keywords
    })

    body = response.json()
    return {
        "text": body['output']
    }
