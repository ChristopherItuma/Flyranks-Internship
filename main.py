from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from db import create_db_and_tables, insert_sample_tasks, get_all_tasks, get_task_by_id, create_task as create_task_in_db, update_task_in_db, delete_task_in_db


tasks = [
  {
    "id": 1,
    "title": "Complete my flyranks assignment",
    "done": False
  },
  {
    "id": 2,
    "title": "Upload the results to github",
    "done": False
  },
  {
    "id": 3,
    "title": "Submit the assignment",
    "done": False
  }
]

app = FastAPI()

create_db_and_tables()
insert_sample_tasks()

# Root endpoint that returns basic information about the API
@app.get("/")
async def read_root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

# Health check endpoint that returns a simple message indicating the API is running
@app.get("/health")
async def health_check():
    return { "status": "ok" }


# Endpoint to retrieve all tasks
@app.get("/tasks")
async def get_tasks():
    get_tasks = get_all_tasks()
    return get_tasks
# Endpoint to retrieve a specific task by its ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Endpoint to create a new task
@app.post("/tasks", status_code=201)
async def create_task(title: str):
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    new_task = await create_task_in_db(title)
    return new_task



# Endpoint to update an existing task by its ID
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, title: str = None, done: bool = None):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = await update_task_in_db(task_id, title, done)
    return updated_task

# Endpoint to delete a task by its ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    deleted_task = await delete_task_in_db(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return JSONResponse(status_code=204, content={})


#STEP 5: TEST IN SWAGGER UI
