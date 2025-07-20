from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from clerk_backend_api import Clerk
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Middleware to be added later on
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# test route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Core Backend!"}


# Routes to be added later on