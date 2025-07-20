from fastapi import FastAPI, HTTPException

app = FastAPI()

# Middleware to added later on


# test route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Core Backend!"}


# Routes to be added later on