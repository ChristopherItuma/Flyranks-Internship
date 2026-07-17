from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

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
    return tasks

# Endpoint to retrieve a specific task by its ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Endpoint to create a new task
@app.post("/tasks")
async def create_task(title: str):
    if not title:
        raise HTTPException(status_code=400, detail="Title is required")
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(new_task)

    return JSONResponse(status_code=201, content=new_task)


# Endpoint to update an existing task by its ID
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, title: str = None, done: bool = None):
    for task in tasks:
        if task["id"] == task_id:
            if title is not None:
                task["title"] = title
            if done is not None:
                task["done"] = done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint to delete a task by its ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return JSONResponse(status_code=204, content={})
    raise HTTPException(status_code=404, detail="Task not found")


#STEP 5: TEST IN SWAGGER UI
