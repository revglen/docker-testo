import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv() 
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.get("/config")
def config():
    return {"app_name": os.getenv("APP_NAME", "not set")}