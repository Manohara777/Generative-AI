from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()

#Mongodb connection
client = AsyncIOMotorClient("mongodb://mongodb:27017")
db = client.demo_db
collection = db.users

class User(BaseModel):
    name: str
    email: str
    age: int