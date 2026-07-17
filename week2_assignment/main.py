from fastapi import FastAPI, HTTPException

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
    