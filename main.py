from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[str]
    name: str
    last_name: str
    age: int
    date: datetime = datetime.now()

users_list = []

app = FastAPI()

@app.get("/users/")
async def get_users():
    return users_list

@app.get("/user/{id}")
async def get_user(id: str):
    for user in users_list:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/new_user/")
async def create_user(user: User):
    user.id = str(uuid())
    users_list.append(user.dict())
    return users_list[-1]
    

@app.delete("/delete_user/{id}")
async def delete_user(id: str):
    for index,user in enumerate(users_list):
        if user["id"] == id:
            users_list.pop(index)
            return {"message: DELETE"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put('/delete_user/{id}')
def update_post(post_id: str, updatedUser: User):
    for index, user in enumerate(users_list):
        if user["id"] == id:
            users_list[index]["name"]= updatedUser.dict()["name"]
            users_list[index]["last_name"]= updatedUser.dict()["last_name"]
            users_list[index]["age"]= updatedUser.dict()["age"]
            return {"message": "Post has been updated succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")