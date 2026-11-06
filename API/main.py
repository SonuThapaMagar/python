from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todo_db={
    1:"Sleep",
    2:"Eat",
    3:"Repeat"
}

class Task(BaseModel):
    title:str
    
#Fast api object
@app.get('/tasks/{task_id}')
def get_task(task_id:int):
    return {"task":todo_db.get(task_id,"NotFound")}

#Post
@app.post('/tasks/{task_id}')
def add_task(task_id:int,item:Task):
    todo_db[task_id]=item.title
    return {"message":"Added","all_tasks":todo_db}

#Put
@app.put('/tasks/{task_id}')
def update_task(task_id:int,item:Task):
    todo_db[task_id]=item.title
    return {"message":"Updated","all_tasks":todo_db}

#Delete
@app.delete('/tasks/{task_id}')
def delete_task(task_id:int):
    todo_db.pop(task_id,None)
    return {"message":"Deleted","all_tasks":todo_db}